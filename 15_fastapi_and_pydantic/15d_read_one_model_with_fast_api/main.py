from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class HeroCreate(HeroBase):
    pass


class HeroPublic(HeroBase):
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


@app.get("/heroes/{hero_id}", response_model=HeroPublic) # Endpoint to read a single hero by ID
def read_hero(hero_id: int):
    """Retrieve a hero by ID"""
    with Session(engine) as session:
        # Using session.get to retrieve a single hero
        hero = session.get(Hero, hero_id) 

        # If the hero is not found, raise a 404 HTTP exception
        # This is a more efficient way to retrieve a single record by primary key
        if not hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        return hero