import pandas as pd
import os
import sys
import requests
from git import Repo
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_path)

from adapters.SweSample import gitapi

from models import model
from app.core.taskset import TaskSet
from app.core.task import Task


class SWEBenchAdapter(TaskSet):
    def _map_row_to_task_create(self, row: pd.Series) -> model.TaskCreate:
        return model.TaskCreate(
            id = row.get("instance_id"),
            name = row.get("repo"),
            taskset_name=self.task_set_name,
            instruction=row.get("problem_statement"),
            complexity=row.get("difficulty"),

            metadata = {
                "base_commit" : row.get("base_commit"),
                "environment_setup_commit" : row.get("environment_setup_commit"),
                "patch": row.get("patch"),
                "test_patch": row.get("test_patch"),
                "hints_text": row.get("hints_text"),
                "FAIL_TO_PASS": row.get("FAIL_TO_PASS"),
                "PASS_TO_PASS": row.get("PASS_TO_PASS")      
            }
        )
    
    def import_taskset(self, dataset: model.Dataset):
        try:
            df = model.Dataset.load_dataset_in_dataframe(dataset)
        except Exception as e:
            raise ValueError(f"Error loading dataset: {e}")
        
        src_path = os.path.join(base_path, "environment", "src")
        
        unique_repos = df['repo'].unique()
        repo_paths = {}
        
        for repo_name in unique_repos:
            repo_url = f"https://github.com/{repo_name}"
            target_dir = os.path.join(src_path, repo_name)
            
            print(f"Ensuring clone for {repo_name} at {target_dir}...")
            gitapi.gitclone(repo_url, target_dir)
            repo_paths[repo_name] = target_dir

        for i, row in df.iterrows():
            instance_id = row.get("instance_id")
            repo_name = row.get("repo")
            base_commit = row.get("base_commit")
            
            repo_local_path = repo_paths.get(repo_name)
            
            task_name = instance_id 
            
            task_create = self._map_row_to_task_create(row)
            task_create.name = task_name
            task_create.metadata["local_repo_path"] = repo_local_path
            
            Task.create(task_create)
            
            new_task = Task(
                id = task_create.id,
                name=task_create.name,
                instruction=task_create.instruction,
                complexity=task_create.complexity,
                metadata=task_create.metadata
            )
            self._add_task(new_task)
            
            self._generate_agent_py(task_create.name, base_commit, repo_local_path)
            
        self.save_to_file()

    def _generate_agent_py(self, task_name, base_commit, repo_path):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        task_dir = os.path.join(project_root, 'app', 'data', 'taskset', self.task_set_name, task_name)
        agent_path = os.path.join(task_dir, 'agents', 'agent.py')
        
        agent_content = f"""import git
import os

def main():
    repo_path = "{repo_path}"
    repo = git.Repo(repo_path)
    try:
        repo.git.checkout('{base_commit}')
        print(f"Checked out {base_commit}")
    except Exception as e:
        print(f"Failed to check out {base_commit}: {{e}}")

if __name__ == "__main__":
    main()
"""
        os.makedirs(os.path.dirname(agent_path), exist_ok=True)
        with open(agent_path, 'w') as f:
            f.write(agent_content)


if __name__ == '__main__':
    adapter = SWEBenchAdapter('swe_task_set')
    dataset = model.Dataset(
        source=model.FileSource.HF_DATASET,
        data=model.HuggingFaceDataset(
            dataset_name="princeton-nlp/SWE-bench_Verified",
            split="test"
        )
    )
    
    adapter.import_taskset(dataset)
    adapter.save_to_file()

