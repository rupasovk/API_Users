from typing import Annotated, Union
from pydantic import BaseModel, Field


class User(BaseModel):
    name: Union[str, None]
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=200)]

users = []