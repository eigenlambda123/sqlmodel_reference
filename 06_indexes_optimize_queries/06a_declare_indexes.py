from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True) # create an index on the name field for faster lookups
    secret_name: str
    age: int | None = Field(default=None, index=True) # create an index on the age field for faster lookups