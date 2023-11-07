# item_routes.py
from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel

router = APIRouter()

# http://127.0.0.1:8000/items/2222?q=red


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@router.get("/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

# 其他物品相關的路由處理函數
