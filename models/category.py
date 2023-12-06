from pydantic import BaseModel

class Category(BaseModel):
    name: str
    department: str