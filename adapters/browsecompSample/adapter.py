import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.core.taskset import TaskSet
import pandas as pd

from models import model
from app.core.task import Task
from gitclone import git_clone

class BrowseCompAdapter(TaskSet):
    def _map_row_to_webpages_data(self, row: pd.Series) -> model.WebpagesData:
        return model.WebpagesData(
            docid=row['docid'],
            url=row['url'],
            title=row.get('title').split("---")[0],
            content= "\n".join(row.get('title').split("---")[1:])
        )
        

    def import_webdata(self, dataset: model.Dataset):
        
        continue

if __name__ == '__main__':
    adapter = BrowseCompAdapter('browsecompSample')
    dataset = model.Dataset(
        source=model.FileSource.HF_DATASET,
        data=model.HuggingFaceDataset(
            dataset_name="Tevatron/browsecomp-plus-corpus",
            split="train"
        )
    )
    
    adapter.import_taskset(dataset)
    adapter.save_to_file()