from pydantic import BaseModel

class AdvertCreate(BaseModel):
    title: str
    description: str
    price: int
    image_urls: str

class AdvertResponse(BaseModel):
    id: int
    title: str
    price: int
    main_image: str

    class Config:
        from_attributes = True