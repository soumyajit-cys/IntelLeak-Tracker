from pydantic import BaseModel

class BreachData(BaseModel):
    email: str | None
    username: str | None
    password_hash: str | None