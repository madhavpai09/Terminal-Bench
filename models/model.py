from pydantic import BaseModel
from typing import Optional, Union, List
from enum import Enum
import pandas as pd
from datasets import load_dataset
import pdb
import uuid
from pathlib import Path


class TaskCreate(BaseModel):
    id: Optional[str] = str(uuid.uuid4())
    name: str
    description : Optional[str] = None

    taskset_name : str
    instruction : str = "No instruction provided"
    category: Optional[str] = None
    complexity : Optional[str] = None
    priority : Optional[str] = None

    environment : Optional[str] = None
    
    golden_solution : Optional[Union[str,dict,Path]] = None
    sample_solution : Optional[Union[str,dict,Path]] = None
    data_dirs : Optional[List[Path]] = None
    metadata : Optional[dict] = None

    
class TaskSetCreate(BaseModel):
    name: str
    description : Optional[str] = None
    tasks : list[TaskCreate]



# we use these to import CSV files for tasksets
class CSVImportRequest(BaseModel):
    file_path: str


class FileDataset(BaseModel):
    file_path: str


#we use this to import hugginf face datasets
class HuggingFaceDataset(BaseModel):
    dataset_name: str
    split: Optional[str] = None

    
class FileSource(str, Enum):
    FILE = "file"
    HF_DATASET = "hf_dataset"


class Dataset(BaseModel):
    source: FileSource
    data: Union[HuggingFaceDataset, FileDataset]

    @staticmethod
    def load_dataset_in_dataframe(dataset: 'Dataset'):
        if dataset.source == FileSource.FILE:
            if not os.path.exists(dataset.data.file_path):
                raise FileNotFoundError(f"CSV file not found: {dataset.data.file_path}")
            df = pd.read_csv(dataset.data.file_path)
        elif dataset.source == FileSource.HF_DATASET:
            data = load_dataset(dataset.data.dataset_name, split=dataset.data.split)
            df = data.to_pandas()
        else:
            raise ValueError(f"Unsupported dataset source: {dataset.source}")
        return df


#incase any taskset data has any other format of complexity or priority we can use these to map
class Complexity(str, Enum):
    EASY = "easy" 
    MEDIUM = "medium"
    HARD = "hard"


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"



#using this to import webpages data for BrowseComp
class WebpagesData(BaseModel):
    docid: str
    url: str
    title: str
    content: str
