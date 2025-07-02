from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
    """Hero model class for the database table"""
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sqlite_file_name = "database.db" # Name of the SQLite database file
sqlite_url = f"sqlite:///{sqlite_file_name}" # URL for the SQLite database

engine = create_engine(sqlite_url, echo=True) # Create the database

SQLModel.metadata.create_all(engine) # Create the tables in the database