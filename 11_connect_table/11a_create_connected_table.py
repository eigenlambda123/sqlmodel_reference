from sqlmodel import Field, SQLModel, create_engine


class Team(SQLModel, table=True):
    """Team model representing a team of heroes"""
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str


class Hero(SQLModel, table=True):
    """Hero model representing a hero with a connection to a team"""
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    # Foreign key to the Team table
    # This field will create a connection between the Hero and Team tables
    team_id: int | None = Field(default=None, foreign_key="team.id")




sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def main():
    create_db_and_tables()

if __name__ == "__main__":
    main()
