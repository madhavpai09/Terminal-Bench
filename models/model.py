from pydantic import BaseModel
from typing import Optional,Union
from enum import Enum
import pandas as pd
from datasets import load_dataset
import pdb
import uuid

class TaskCreate(BaseModel):
    name: str
    id: Optional[str] = None
    taskset_name : str
    instruction : str = "No instruction provided"
    description : Optional[str] = None
    complexity : Optional[str] = None
    priority : Optional[str] = None
    environment : Optional[str] = None
    golden_sol : Optional[Union[str, dict]] = None
    
    
class TaskSetCreate(BaseModel):
    name: str
    description : Optional[str] = None
    tasks : list[TaskCreate]

class CSVImportRequest(BaseModel):
    file_path: str

class Complexity(str, Enum):
    EASY = "easy" 
    MEDIUM = "medium"
    HARD = "hard"

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class FileSource(str, Enum):
    FILE = "file"
    HF_DATASET = "hf_dataset"

class HuggingFaceDataset(BaseModel):
    dataset_name: str
    split: Optional[str] = None
    
class FileDataset(BaseModel):
    file_path: str

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
