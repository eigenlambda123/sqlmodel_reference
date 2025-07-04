from sqlmodel import Field, SQLModel, create_engine
from sqlmodel import Session


class Hero(SQLModel, table=True):
    """Hero model class for the database table"""
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sqlite_file_name = "database.db" 
sqlite_url = f"sqlite:///{sqlite_file_name}" 
engine = create_engine(sqlite_url, echo=True) 
SQLModel.metadata.create_all(engine) 


def create_heroes():
    """Create and return a list of data instances"""
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    # Session is used to manage the database session
    # and perform operations like adding, committing, etc.
    session = Session(engine)

    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)

    session.commit()

create_heroes()
