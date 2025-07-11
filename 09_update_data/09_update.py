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
    """Update a hero's age and print the updated hero details."""
    with Session(engine) as session:

        # Select the hero to update
        # This will retrieve the hero with name "Spider-B
        statement = select(Hero).where(Hero.name == "Spider-Boy")   
        results = session.exec(statement)  
        hero = results.one()  
        print("Hero:", hero)  

        # Update the hero's age
        # This will change the age of the hero to 16
        hero.age = 16  

        # Add the updated hero back to the session and commit the changes
        # This will save the changes to the database
        session.add(hero)  
        session.commit()  

        # Refresh the hero object to get the updated data from the database
        # This will reload the hero object with the latest data from the database
        session.refresh(hero)  

        # Print the updated hero details to verify the changes
        print("Updated hero:", hero)  


def main():
    create_db_and_tables()
    create_heroes()
    update_heroes()


if __name__ == "__main__":
    main()