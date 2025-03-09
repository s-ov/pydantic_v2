from typing import List, Any
# pip install pydantic[email]
from pydantic import (
    BaseModel, 
    EmailStr, 
    PositiveInt, 
    conlist, 
    model_validator,
    field_validator,
    Field, 
    HttpUrl,
    )


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class Employee(BaseModel):
    name: str
    position: str
    email: EmailStr


class Owner(BaseModel):
    name: str 
    email: EmailStr

    @model_validator(mode="before")
    @classmethod
    def check_sensetive_info_omited(cls, data: Any) -> Any:
        if isinstance(data, dict):
            if "password" in data:
                raise ValueError("Password shouldn'n be included")
            if "card_number" in data:
                raise ValueError("Card number shouldn'n be included")
            return data
        
    @model_validator(mode="after")
    def check_name_contains_space(self) -> "Owner":
        if not " " in self.name:
            raise ValueError("Owner name must contain a space.")
        return self.name.title()

    @field_validator("name")
    @classmethod
    def name_must_contain_space(cls, value: str) -> str:
        if not " " in value:
            raise ValueError("Owner name must contain a space.")
        return value.title()
    
    def __str__(self) -> str:
        return f"{self.name}"


class Restaurant(BaseModel):
    name: str = Field(..., pattern=r"^[a-zA-Z0-9-' ]+$")
    owner: Owner
    email: EmailStr
    address: Address
    employees: conlist(Employee, min_length=2)      # type: ignore 
    number_of_seats: PositiveInt
    delivery: bool
    website: HttpUrl

    def __str__(self) -> EmailStr:
        return f"Restaurant '{self.name}'"


restaurant = Restaurant(
    name="Imbiss",
    owner={
        "name": "John Doe",
        "email": "j.doe@gmail.com"
    },
    address={
        "street": "123, Dodik str",
        "city": "NY",
        "state": "NJ",
        "zip_code": "12345"
    },
    email="contact@imbiss.com",
    employees=[
        {
            "name": "Jane Doe", 
            "position": "Chef", 
            "email": "jane.doe@gmail.com",
        },
        {
            "name": "Mike Johnes", 
            "position": "Waiter", 
            "email": "m.johnes@gmail.com",
        },
    ],
    number_of_seats=30,
    delivery=True,
    website="https:///www.dbjdfkjef.net"
)


try:
    owner = Owner(name="Mike Johnes", email="m.johnes@gmail.com",)
    print(owner)
except ValueError as e:
    print(e)

print(restaurant)
