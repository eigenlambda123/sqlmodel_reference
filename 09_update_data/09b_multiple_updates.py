from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
    hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
    hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
    hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)

        session.commit()


def update_heroes():
    with Session(engine) as session:
        # Select Hero 1
        # This will retrieve the hero with name "Spider-B
        statement = select(Hero).where(Hero.name == "Spider-Boy") 
        results = session.exec(statement)  
        hero_1 = results.one()
        print("Hero 1:", hero_1) 

        # Select Hero 2
        # This will retrieve the hero with name "Captain North America"
        statement = select(Hero).where(Hero.name == "Captain North America") 
        results = session.exec(statement) 
        hero_2 = results.one()
        print("Hero 2:", hero_2)

        # Update Hero 1
        # This will change the age of hero_1 to 16 and name to "Spider-Youngster"
        hero_1.age = 16
        hero_1.name = "Spider-Youngster"
        session.add(hero_1)

        # Update Hero 2
        # This will change the age of hero_2 to 110 and name to "Captain North America Except Canada"
        hero_2.name = "Captain North America Except Canada"
        hero_2.age = 110
        session.add(hero_2)

        # Commit the changes to the database
        # This will save the changes made to hero_1 and hero_2
        session.commit()

        # Refresh the hero objects to get the updated data from the database
        # This will reload the hero objects with the latest data from the database
        session.refresh(hero_1)
        session.refresh(hero_2)

        # Print the updated hero details to verify the changes
        print("Updated hero 1:", hero_1)  # (18)!
        print("Updated hero 2:", hero_2)  # (19)!
    # (20)!


def main():
    create_db_and_tables()
    create_heroes()
    update_heroes()


if __name__ == "__main__":
    main()