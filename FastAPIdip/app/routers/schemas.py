from pydantic import BaseModel

class CreateArticle(BaseModel):
    title: str
    content: str

class UpdateArticle(BaseModel):
    title: str
    content: str