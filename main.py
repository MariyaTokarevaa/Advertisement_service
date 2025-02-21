from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from database import Session, engine, Base
from models import Advertisement
from schemas import AdvertCreate, AdvertResponse
from typing import List

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Зависимость для получения сессии базы данных
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# Маршрут для создания новой задачи
@app.post('/ads', response_model=AdvertResponse)
def create_advert(advert: AdvertCreate, db: Session = Depends(get_db)):
    if len(advert.image_urls) > 3:
        raise HTTPException(status_code=400, detail="Не больше 3 ссылок на фото.")
    else:
    new_advert = Advertisement(**advert.dict())
    db.add(new_advert)
    db.commit()
    db.refresh(new_advert)
    return (f'Создано новое объявление {new_advert.title}')

# Маршрут для получения списка задач
@app.get('/ads', response_model=List[AdvertResponse])
def get_advert(skip: int = 0, limit: int = 10, sort_by: str = 'date', db: Session = Depends(get_db)):
    pass
# Маршрут для получения задачи по ID