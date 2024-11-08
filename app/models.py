from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str  # "в процессе" или "завершена"


class User(BaseModel):
    id: int
    username: str
    password: str  # Храните хэш пароля в реальном приложении
