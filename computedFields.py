from pydantic import BaseModel, computed_field, field_validator
from datetime import datetime


class Person(BaseModel):
    name: str
    birth_year: int

    @computed_field
    @property
    def get_age(self) -> int:
        current_year = datetime.now().year
        return current_year - self.birth_year
    
    @field_validator("birth_year")
    @classmethod
    def validate_age(cls, value: int):
        current_year = datetime.now().year
        if current_year - value < 18:
            raise ValueError("Person isn't adult")
        return value

person = Person(name="Lee Doe", birth_year=2001)
print(person)
print(person.model_dump())
