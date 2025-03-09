from typing import List, Optional
from pydantic import BaseModel


class Food(BaseModel):
    name: str
    price: float
    ingredients: Optional[List[str]] = None


class Restaurant(BaseModel):
    name: str
    location: str
    food: List[Food]


restaurant = Restaurant(
    name="Imbiss",
    location="123, Dodik str, Dublin",
    food=[
        {"name": "Pizza", "price": 5.93, "ingredients": ["cheese", "tomato",]},
        {"name": "Sushi", "price": 6.25,},
    ]
)

print(restaurant)
print(restaurant.model_dump())
