import pendulum

from repository import JSONRepository
from model import Record, Status


repo = JSONRepository('./database.json')

record = Record('0', 'K-19: The Widowmaker', Status.TO_WATCH.name, {'imdb': 'https://www.imdb.com/title/tt0267626/'})
print(record.__dict__)
repo.save(record)

record = Record('1', 'Finding Dory', Status.TO_WATCH.name, {'imdb': 'https://www.imdb.com/title/tt2277860/'})
print(record.__dict__)
repo.save(record)

record = Record('2', 'Memento', Status.WATCHED.name, {'imdb': 'https://www.imdb.com/title/tt0209144/'}, date_watched=pendulum.datetime(2018, 4, 26).to_iso8601_string())
print(record.__dict__)
repo.save(record)

print(repo.retrieve('na'))
