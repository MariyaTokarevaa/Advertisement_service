from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Указываем URL базы данных
database_url = 'postgresql://postgres:12345@localhost:5432/advertisement_db'

# Создаем движок SQLAlchemy
engine = create_engine(database_url)

# Создаем локальную сессию
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()