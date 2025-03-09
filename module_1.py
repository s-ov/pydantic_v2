import pydantic
# print(pydantic.__version__) 2.10.6


class User:
    def __init__(self, id: int, name="John Doe") -> None:
        if not isinstance(id, int):
            raise TypeError(
                f"Expected id to be int, got {type(id).__name__}",
                )
        if not isinstance(name, str):
            raise TypeError(
                f"Expected name to be str, got {type(name).__name__}",
                )
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"User -> N.{self.id}: {self.name}"


try:
    user = User(id=123)
except TypeError as e:
    print(e)
finally:
    print(user)
