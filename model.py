from typing import Dict
from enum import Enum
from enum import auto

class Status(Enum):
    WATCHED = auto()
    TO_WATCH = auto()


class Record:
    key: str
    title: str
    status: Status
    uri: Dict[str, str]
    date_watched: str

    def __init__(self, key: str, title: str, status: Status, uri: Dict[str, str] = None, date_watched: str = None):
        self.key = key
        self.title = title
        self.status = status
        self.uri = uri if uri is not None else {}
        self.date_watched = date_watched
    
    @classmethod
    def from_dict(cls, key: str, raw: dict):
        return cls(key=key, title=raw.get('title'), uri=raw.get('uri'), status=raw.get('status'), date_watched=raw.get('date_watched'))
    
    def to_dict(self):
        result = self.__dict__
        del(result['key'])
        for key in result:
            if not key:
                del(result[key])
        return result
    
    def __repr__(self):
        string = f'Record(key="{self.key}", title="{self.title}", status="{self.status}", uri={self.uri}'
        if(self.date_watched):
            string += f', date_watched={self.date_watched}'
        return string + ')'
