"""
It's not good practice to combine 
dataclasses with dataclasses
"""

from dataclasses import dataclass, field
from typing import List, Optional
from dataclasses import Field


@dataclass
class User:
    id: int
    name: str = "John Doe"
    age: Optional[int] = field(
        default=None,
        metadata=dict(title="Age", description="Desc of age", ge=18)
    )
    height:  Optional[int] = Field(None, title="Age", ge=18, le=200)
    friends: List[int] = field(default_factory=lambda: [0])
