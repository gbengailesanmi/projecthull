from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    student = "student"
    teacher = "teacher"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    gender: Gender
    roles: Optional[List[Role]]