from fastapi import FastAPI
from pymongo import MongoClient
# pydantic-settings 패키지에서 BaseSettings를 가져옵니다.
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from typing import List, Any

# 환경 설정 클래스 정의
class Settings(BaseSettings):
    mongo_database_url: str

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI()

# MongoDB 연결 설정
client = MongoClient(settings.mongo_database_url)
db = client.transript  # 데이터베이스 이름을 'transript'로 변경

# Pydantic 모델 정의
class Item(BaseModel):
    _id: str
    videoid: str
    processed_data: List[Any]
    status: int
    transcript: List[Any]

@app.get("/api/items", response_model=List[Item])
async def read_items():
    try:
        items = db.transript.find().limit(5)  # 'collection_name'을 실제 컬렉션 이름인 'transript'로 변경
        return list(items)
    except Exception as e:
        # 예외 로깅을 추가하는 것이 좋습니다.
        # 로그 설정이 되어있다면, 예외를 로깅합니다.
        # 예: logging.exception(e)
        return {"error": "Unable to fetch items from the database."}

@app.get("/api/index")
def hello_world():
    return {"message": "Hello World"}
