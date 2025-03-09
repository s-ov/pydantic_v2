from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"

user = User(id=123)

print(user.model_dump())
print(user.model_dump_json())
print(user.model_json_schema())
