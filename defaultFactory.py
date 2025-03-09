import uuid
from typing import List
from pydantic import BaseModel, Field, EmailStr
from decimal import Decimal


class User(BaseModel):
    id: uuid.UUID = Field(
        default_factory=lambda: uuid.uuid4()
        )
    name: str = Field(..., min_length=5, max_length=30, alias="username", pattern="^\w+$")
    email: EmailStr = Field(...,)
    age: int = Field(..., gt=0, le=110,)
    height: float = Field(..., gt=0.0,)
    is_active: bool = Field(True)
    balance: Decimal = Field(..., max_digits=6, decimal_places=2,)
    favorite_numbers: List[int] = Field(..., min_items=1)

    def __str__(self) -> str:
        return f"User: {self.name}"


user = User(username="Leigh Grand")
print(user)
print(user.id)
print(user.model_dump(by_alias=True))
