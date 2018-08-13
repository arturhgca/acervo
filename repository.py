from abc import ABC
from abc import abstractmethod
from typing import Optional
import json

from model import Record

class Repository(ABC):
    @abstractmethod
    def save(self, record: Record) -> Record:
        raise NotImplemented

    abstractmethod
    def retrieve(self, key: str) -> Optional[Record]:
        raise NotImplemented


class JSONRepository(Repository):
    _file_path: str
    
    def __init__(self, file_path: str):
        self._file_path = file_path

    def save(self, record: Record) -> Record:
        with open(self._file_path, 'r') as json_file:
            data = json.load(json_file)
        data[record.key] = record.to_dict()
        print(data)
        with open(self._file_path, 'w') as json_file:
            json.dump(data, json_file, sort_keys=True, indent=2)
        
    def retrieve(self, key: str) -> Optional[Record]:
        with open(self._file_path, 'r') as json_file:
            data = json.load(json_file)
            return Record.from_dict(key, data.get(key)) if key in data else None
