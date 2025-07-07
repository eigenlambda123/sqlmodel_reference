from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class HeroTeamLink(SQLModel, table=True):
    """
    Link model for many-to-many relationship between Hero and Team
    """
    team_id: int | None = Field(default=None, foreign_key="team.id", primary_key=True)
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)


class Team(SQLModel, table=True):
    """
    Model representing a team of heroes
    """
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    # Define a many-to-many relationship with Hero using the link model
    # This will create a `heroes` attribute in the Team model
    heroes: list["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)


class Hero(SQLModel, table=True):
    """
    Model representing a hero with a many-to-many relationship to teams
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    # Define a many-to-many relationship with Team using the link model
    # This will create a `teams` attribute in the Hero model
    teams: list[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")

        hero_deadpond = Hero(
            name="Deadpond",
            secret_name="Dive Wilson",
            teams=[team_z_force, team_preventers],
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            teams=[team_preventers],
        )
        hero_spider_boy = Hero(
            name="Spider-Boy", secret_name="Pedro Parqueador", teams=[team_preventers]
        )
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()

        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)

        print("Deadpond:", hero_deadpond)
        print("Deadpond teams:", hero_deadpond.teams)
        print("Rusty-Man:", hero_rusty_man)
        print("Rusty-Man Teams:", hero_rusty_man.teams)
        print("Spider-Boy:", hero_spider_boy)
        print("Spider-Boy Teams:", hero_spider_boy.teams)


def main():
    create_db_and_tables()
    create_heroes()


if __name__ == "__main__":
    main()