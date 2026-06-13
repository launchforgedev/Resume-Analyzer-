from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")
SSL_CA_PATH = os.getenv("SSL_CA_PATH")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ca": SSL_CA_PATH
        }
    }
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()