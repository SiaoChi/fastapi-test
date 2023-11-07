from typing import Union
from fastapi import FastAPI, HTTPException, status, File, UploadFile
from router.user_routes import router as user_router
from router.item_routes import router as item_router
import shutil
from pathlib import Path

# https://fastapi.tiangolo.com/ 官方文檔
app = FastAPI(debug=True, title="FastApi-App-Test")
# http://127.0.0.1:8000/docs 直接產出API文檔


@app.get("/", status_code=status.HTTP_201_CREATED)
def read_root():
    return {"Hello": "World"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # 確保static資料夾存在
    static_folder = Path("static")
    static_folder.mkdir(parents=True, exist_ok=True)

    # 指定檔案儲存路徑，自行定義
    file_path = static_folder / file.filename

    # 使用shutil將檔案儲存到指定路徑
    with file_path.open("wb") as f:
        shutil.copyfileobj(file.file, f)

    return {"filename": file.filename}


@app.post("/limit-uploadfile", status_code=201)
async def create_upload_file_limit(file: UploadFile = File(...)):
    # 限制檔案大小為最多 2MB
    if file.file:
        max_file_size = 2 * 1024 * 1024
        if file.file._file.__sizeof__() > max_file_size:
            raise HTTPException(status_code=400, detail="檔案大小超過上限")

    # 限制檔案格式為圖像（例如，只允許JPEG和PNG）
    allowed_image_formats = ["image/jpeg", "image/png"]
    if file.content_type not in allowed_image_formats:
        raise HTTPException(status_code=400, detail="不支持的檔案格式")

    # 將檔案保存到靜態資料夾，需要加入await因為fn是一個promise
    result = await create_upload_file(file)
    return result

# 使用router管理的寫法
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(item_router, prefix="/items", tags=["items"])


# CMD run server指令，--reload會自動更新
# uvicorn main:app --reload
