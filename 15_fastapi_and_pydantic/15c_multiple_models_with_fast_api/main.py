from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select


class HeroBase(SQLModel):
    """
    Base model for Hero, used for both creation and public response
    """
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)


class Hero(HeroBase, table=True):
    """
    Hero model for database representation
    """
    id: int | None = Field(default=None, primary_key=True)


class HeroCreate(HeroBase):
    """
    Hero model for creation, does not include ID
    """
    pass


class HeroPublic(HeroBase):
    """
    Hero model for public response, includes ID
    """
    id: int


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/heroes/", response_model=HeroPublic)
def create_hero(hero: HeroCreate):
    with Session(engine) as session:
        db_hero = Hero.model_validate(hero)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero


@app.get("/heroes/", response_model=list[HeroPublic])
def read_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes