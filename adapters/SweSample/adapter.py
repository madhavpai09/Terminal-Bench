import pandas as pd
import os
import sys
import requests
from git import Repo
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_path)

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
        
        for i, row in df.iterrows():
            task_create = self._map_row_to_task_create(row)
            Task.create(task_create)
            
            new_task = Task(
                id = task_create.id,
                name=task_create.name,
                instruction=task_create.instruction,
                complexity=task_create.complexity,
                metadata=task_create.metadata

            )
            self._add_task(new_task)
        self.save_to_file()


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

