from sqlalchemy import create_engine
from models import Base, get_engine


def create_database():
    engine = get_engine()
    Base.metadata.create_all(engine)
    print("Database and tables created.")


if __name__ == "__main__":
    create_database()
