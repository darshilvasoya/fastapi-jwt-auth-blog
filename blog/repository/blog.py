from blog import database
from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from blog import oauth2


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    try:
        new_blog = models.Blog(
            title=request.title,
            body=request.body,
            user_id=1  # assuming FK to user
        )
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return new_blog
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def destroy(id: int,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= (f"Blog with id {id} not found"))
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:schemas.Blog,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= (f"Blog with id {id} not found"))
    blog.update({"title": request.title, "body": request.body})
    db.commit()
    return 'updated'

def show(id:int,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available"
        )
    return blog