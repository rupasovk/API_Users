from pydantic import BaseModel
from typing import Union

class Order(BaseModel):
    name: str
    id: int
    description: Union[str, None] = None
    price: Union[float, None] = None
    UserId: Union[int, None] = None