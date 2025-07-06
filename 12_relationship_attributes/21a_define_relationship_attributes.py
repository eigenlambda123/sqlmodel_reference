from sqlmodel import Field, Relationship, SQLModel


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    # Define a one-to-many relationship with Hero
    # This will create a `heroes` attribute in the Team model
    # that will hold a list of Hero instances associated with the team
    heroes: list["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(default=None, foreign_key="team.id")

    # Define a many-to-one relationship with Team
    # This will create a `team` attribute in the Hero model
    # Hero will be able to access its associated Team instance
    team: Team | None = Relationship(back_populates="heroes")
