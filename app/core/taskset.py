import os
import sys 
from pathlib import Path
from task import Task

class TaskSet:
    def __init__(self, task_set_name: str):
        self.task_set_name = task_set_name
        if os.path.exists(task_set_name):
            self.load_from_file(task_set_name)
        self.tasks = []

    def _add_task(self, task: Task):
        self.tasks.append(task)
    
    def add_task(self, task: Task):
        self._add_task(task)
        self.save_to_file()

    def run(self):
        for task in self.tasks:
            task.run()

    def load_from_file(self, file_path: str):
        with open(file_path, 'r') as f:
            tasks = f.read().splitlines()
            for task in tasks:
                self._add_task(Task(task))

    def save_to_file(self, file_path: str):
        with open(file_path, 'w') as f:
            for task in self.tasks:
                f.write(task.task_name + '\n')
    
    def import_taskset(self):
        return NotImplementedError

