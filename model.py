from typing import Dict
from enum import Enum
from enum import auto
import pendulum
from copy import deepcopy

class Status(Enum):
    WATCHED = auto()
    TO_WATCH = auto()


class Record:
    id: str
    title: str
    status: Status
    uri: Dict[str, str]
    date_watched: str
    date_added: str

    def __init__(self, id: str, title: str, status: Status, uri: Dict[str, str] = None, date_watched: str = None):
        self.id = id
        self.title = title
        self.status = status
        self.uri = uri if uri is not None else {}
        self.date_watched = date_watched
        self.date_added = pendulum.today().to_iso8601_string()
    
    @classmethod
    def from_dict(cls, id: str, raw: dict):
        return cls(id=id, title=raw.get('title'), uri=raw.get('uri'), status=raw.get('status'), date_watched=raw.get('date_watched'))
    
    def to_dict(self):
        result = deepcopy(self.__dict__)
        del(result['id'])
        for key, value in list(result.items()):
            if not value:
                del(result[key])
        return result
    
    def __repr__(self):
        string = f'Record(id="{self.id}", title="{self.title}", status="{self.status}", uri={self.uri}'
        if(self.date_watched):
            string += f', date_watched={self.date_watched}'
        return string + ')'
