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
    def retrieve(self, id: str) -> Optional[Record]:
        raise NotImplemented


class JSONRepository(Repository):
    _file_path: str
    
    def __init__(self, file_path: str):
        self._file_path = file_path
        with open(self._file_path, 'r') as json_file:
            if not json_file.read():
                self._initialize_database()

    def _initialize_database(self):
        with open(self._file_path, 'w') as json_file:
            json.dump({}, json_file)
    
    def _load_database(self) -> dict:
        with open(self._file_path, 'r') as json_file:
            return json.load(json_file)

    def save(self, record: Record) -> Record:
        data = self._load_database()
        data[record.id] = record.to_dict()
        with open(self._file_path, 'w') as json_file:
            json.dump(data, json_file, sort_keys=True, indent=2)
        
    def retrieve(self, id: str) -> Optional[Record]:
        data = self._load_database()
        return Record.from_dict(id, data.get(id)) if id in data else None
