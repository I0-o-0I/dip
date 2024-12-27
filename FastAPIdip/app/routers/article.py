from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated

from app.models.article import Article
from app.routers.schemas import *

from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from app.backend.db_depends import get_db

router: APIRouter = APIRouter(prefix='/article', tags=['article'])


@router.get('/')
async def article_all(db: Annotated[Session, Depends(get_db)]):
    return db.scalars(select(Article)).all()


@router.get('/search')
async def title_search(db: Annotated[Session, Depends(get_db)], article_title: str | None):
    articles = db.query(Article).all()
    if article_title is not None:
        articles = [i for i in articles if article_title.lower() in i.title.lower() or article_title.lower() in i.content.lower()]

    return [{
        "id": j.id,
        "title": j.title,
        "content": j.content
    } for j in articles]


@router.post('/create')
async def article_create(db: Annotated[Session, Depends(get_db)], create_article: CreateArticle):
    db.execute(insert(Article).values(title=create_article.title,
                                      content=create_article.content))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/update')
async def article_update(db: Annotated[Session, Depends(get_db)], article_title: str, update_article: UpdateArticle):
    article = db.scalar(select(Article).where(Article.title == article_title))
    if article is None:
        raise HTTPException(status_code=404, detail='Article was not found')

    db.execute(update(Article).where(Article.title == article_title).values(title=update_article.title,
                                                                            content=update_article.content))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful'
    }


@router.delete('delete')
async def article_delete(db: Annotated[Session, Depends(get_db)], article_title: str):
    article = db.scalar(select(Article).where(Article.title == article_title))

    if article is None:
        raise HTTPException(status_code=404, detail='Article was not found')

    db.execute(delete(Article).where(Article.title == article_title))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Successful'
    }
