from typing import List, Optional

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy_utils import TSVectorType, JSONType

from dispatch.database import Base
from dispatch.models import DispatchBase


class Plugin(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    slug = Column(String, unique=True)
    description = Column(String)
    version = Column(String)
    author = Column(String)
    author_url = Column(String)
    type = Column(String)
    enabled = Column(Boolean)
    configuration = Column(JSONType)

    search_vector = Column(TSVectorType("title"))


# Pydantic models...
class PluginBase(DispatchBase):
    pass


class PluginCreate(PluginBase):
    title: str
    slug: str
    author: str
    author_url: str
    type: Optional[str]
    enabled: Optional[bool] = True
    description: Optional[str]
    configuration: Optional[dict]


class PluginUpdate(PluginBase):
    id: int
    enabled: Optional[bool] = True


class PluginRead(PluginBase):
    id: int
    title: str
    slug: str
    author: str
    author_url: str
    type: Optional[str]
    enabled: Optional[bool] = True
    description: Optional[str]
    configuration: Optional[dict]


class PluginPagination(DispatchBase):
    total: int
    items: List[PluginRead] = []
