from sqlmodel import Field, Relationship, SQLModel, create_engine


class Weapon(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    # back_populates is used to link this relationship to the Hero model
    hero: "Hero" = Relationship(back_populates="weapon")


class Power(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    hero_id: int = Field(foreign_key="hero.id")

    # back_populates is used to link this relationship to the Hero model
    hero: "Hero" = Relationship(back_populates="powers")


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    # back_populates is used to link this relationship to the Hero model
    heroes: list["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    # back_populates is used to link this relationship to the Team model
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")

    # back_populates is used to link this relationship to the Weapon model
    weapon_id: int | None = Field(default=None, foreign_key="weapon.id")
    weapon: Weapon | None = Relationship(back_populates="hero")

    # back_populates is used to link this relationship to the Power model
    powers: list[Power] = Relationship(back_populates="hero")


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()