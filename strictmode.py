
from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str 

try:
    print(User.model_validate({"id": "7", "name": "Lo Lo"}, strict=True))
    # print(User.model_validate({"id": "7", "name": "Lo Lo"}))
except ValidationError as exc:
    print(exc) 