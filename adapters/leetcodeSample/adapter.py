import pandas as pd
import os
import sys
from models import model
base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_path)
from app.core.taskset import TaskSet
from app.core.task import Task
from models.model import Complexity, Priority


class LeetcodeAdapter(TaskSet):
    def _map_complexity(self, value):
        if value >= 80:
            return Complexity.EASY
        elif value >= 50:
            return Complexity.MEDIUM
        else:
            return Complexity.HARD

    def _map_complexity_to_priority(self, complexity: Complexity):
        if complexity == Complexity.EASY:
            return Priority.LOW
        elif complexity == Complexity.MEDIUM:
            return Priority.MEDIUM
        else:
            return Priority.HIGH

    def _map_row_to_task_create(self, row: pd.Series) -> model.TaskCreate:
        labels = row.get("labels")
        name = labels.get("questionTitle")

        instruction = row.get("content").split("\n\n")[0]
        description = "\n".join(row.get("content").split("\n\n")[1:])

        ac_rate = labels.get("acRate")
        percentage = float(ac_rate.strip("%")) if ac_rate else 0.0

        complexity = self._map_complexity(percentage)
        priority = self._map_complexity_to_priority(complexity)

        environment = labels.get("programming_language")

        golden_sol = row.get("test")
    

        return model.TaskCreate(
            name=name,
            taskset_name=self.task_set_name,
            instruction=instruction,
            description=description,
            complexity=complexity,
            priority=priority,
            environment=environment,
            golden_sol=golden_sol
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
                name=task_create.name,
                instruction=task_create.instruction,
                description=task_create.description,
                complexity=task_create.complexity,
                priority=task_create.priority,
                environment=task_create.environment
            )
            self._add_task(new_task)
        self.save_to_file()

if __name__ == '__main__':
    adapter = LeetcodeAdapter('new_leetcode_set')
    dataset = model.Dataset(
        source=model.FileSource.HF_DATASET,
        data=model.HuggingFaceDataset(
            dataset_name="sine/LeetCodeSample",
            split="test"
        )
    )
    adapter.import_taskset(dataset)