# user_routes.py
from fastapi import APIRouter

router = APIRouter()


@router.get("/{user_id}")
def read_user(user_id: int):
    # 處理用戶相關的邏輯
    pass

# 其他用戶相關的路由處理函數
