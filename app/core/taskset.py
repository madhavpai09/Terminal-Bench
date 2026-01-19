import os
import sys
from typing import Optional 
from app.core.task import Task
from client import client_user
from models import model

class TaskSet:
    def __init__(self, name: str):
        self.task_set_name = name
        self.base_dir = os.path.join(self._get_tasksets_dir(), name)
        self.tasks_file = os.path.join(self.base_dir, 'tasks.txt')
        self.tasks = []
        if os.path.exists(self.tasks_file):
            self.load_from_file(self.tasks_file)

    def _add_task(self, task: Task):
        self.tasks.append(task)
    

    def add_task(self, task: Task, notify: bool = False):
        self._add_task(task)
        self.save_to_file()
        if notify:
            client_user.add_task_request(self.task_set_name, task.task_name)


    def run(self):
        for task in self.tasks:
            task.run()

    def load_from_file(self, file_path: str):
        with open(file_path, 'r') as f:
            tasks = f.read().splitlines()
            for task in tasks:
                self._add_task(Task(task))

    def save_to_file(self, file_path: Optional[str] = None):
        if file_path is None:
            file_path = self.tasks_file
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            for task in self.tasks:
                f.write(task.task_name + '\n')
    
    def import_taskset(self, file_path: str):
        return NotImplementedError

    @staticmethod
    def create(taskset_create):
        taskset = TaskSet(taskset_create.name)
        os.makedirs(taskset.base_dir, exist_ok=True)
        taskset.save_to_file()
        return taskset

    @staticmethod
    def get(name: str):
        return TaskSet(name)

    @staticmethod
    def _get_tasksets_dir():
        app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tasksets_dir = os.path.join(app_dir, 'data', 'taskset')
        os.makedirs(tasksets_dir, exist_ok=True)
        return tasksets_dir