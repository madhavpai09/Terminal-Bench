import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.core.taskset import TaskSet
import pandas as pd
import os
from models import model
from app.core.task import Task

class TestsetAdapter(TaskSet):
    def _map_row_to_task_create(self, row: pd.Series) -> model.TaskCreate:
        return model.TaskCreate(
            name=row['task_name'],
            taskset_name=self.task_set_name,
            instruction=row.get('instruction', None),
            description=row.get('description', None),
            complexity=str(row.get('complexity', None)),
            priority=str(row.get('priority', None)),
            environment=row.get('environment', None)
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
    adapter = TestsetAdapter('newtest_set')
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'new_taskset.csv')
    dataset = model.Dataset(
        source=model.FileSource.FILE,
        data=model.FileDataset(
            file_path=file_path
        )
    )
    adapter.import_taskset(dataset)