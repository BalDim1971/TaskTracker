from sqlalchemy import (create_engine)

from databases import Database

from src.config import DB_NAME, DB_USER, DB_PASS

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}'

engine = create_engine(DATABASE_URL)

database = Database(DATABASE_URL)
