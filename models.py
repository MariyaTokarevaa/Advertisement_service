from sqlalchemy import Column, Integer, String, Text, Sequence
from database import Base

# Определяем модель Advertisement
class Advertisement(Base):
    __tablename__ = 'advertisements'

    id = Column(Integer, Sequence('ad_id_seq'), primary_key=True)
    title = Column(String(200), index=True)
    description = Column(Text)
    price = Column(Integer)
    image_urls = Column(Text)  # Сохраним ссылки на фото как текст

    def __repr__(self):
        return f'<Advertisement (title={self.title}, description={self.description}, price={self.price})>'