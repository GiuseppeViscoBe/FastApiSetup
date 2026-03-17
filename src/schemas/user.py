from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(ge=0)


class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int

    model_config = {"from_attributes": True}