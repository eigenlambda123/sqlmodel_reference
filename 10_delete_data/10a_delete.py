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
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero_1 = results.one()
        print("Hero 1:", hero_1)

        statement = select(Hero).where(Hero.name == "Captain North America")
        results = session.exec(statement)
        hero_2 = results.one()
        print("Hero 2:", hero_2)

        hero_1.age = 16
        hero_1.name = "Spider-Youngster"
        session.add(hero_1)

        hero_2.name = "Captain North America Except Canada"
        hero_2.age = 110
        session.add(hero_2)

        session.commit()
        session.refresh(hero_1)
        session.refresh(hero_2)

        print("Updated hero 1:", hero_1)
        print("Updated hero 2:", hero_2)


def delete_heroes():
    """Delete a hero and print the deleted hero details"""
    with Session(engine) as session:

        # Select the hero to delete
        # This will retrieve the hero with name "Spider-Youngster"
        statement = select(Hero).where(Hero.name == "Spider-Youngster")  
        results = session.exec(statement)  
        hero = results.one()  
        print("Hero: ", hero)  

        # Delete the hero from the session
        # This will remove the hero from the database
        session.delete(hero)  

        # Commit the changes to the database
        # This will save the deletion to the database
        session.commit()  

        # Print the deleted hero details
        # This will show the details of the hero that was deleted
        print("Deleted hero:", hero)  

        # Check if the hero is still in the database
        # This will try to retrieve the hero with name "Spider-Youngster"
        # If the hero is not found, it will return None
        # If the hero is found, it will return the hero object
        statement = select(Hero).where(Hero.name == "Spider-Youngster")  
        results = session.exec(statement)  
        hero = results.first()  
        if hero is None:  
            print("There's no hero named Spider-Youngster")  
        else:  
            print("Hero still exists:", hero)  


def main():
    create_db_and_tables()
    create_heroes()
    update_heroes()
    delete_heroes()


if __name__ == "__main__":
    main()