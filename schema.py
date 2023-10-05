import pandas as pd
from enum import Enum
import typing
import strawberry
from strawberry.schema.config import StrawberryConfig
import operator
from index import ind_get_rec
df = pd.read_csv('comp.csv')

@strawberry.type
class Record:
  mark: float
  name: str
  type: str
  subj: str

@strawberry.type
class Query:
  @strawberry.field
  def records(self, type:str, name:str) -> typing.List[Record]:
    _df = df[df['name'] == name]
    _df = _df[_df['type'] == type]
    return _df.to_dict('records')

  @strawberry.field
  def subj_records(self, type:str, name: str, subj:str) -> typing.List[Record]:
    _df = pd.DataFrame.from_dict(ind_get_rec(type, name))
    _df = _df[_df['subj'] == subj]
    return _df.to_dict('records')

def default_resolver(root, field):
  try: return operator.getitem(root, field)
  except KeyError: return getattr(root, field)

config = StrawberryConfig(default_resolver=default_resolver)
schema = strawberry.Schema(query=Query, config=config)
