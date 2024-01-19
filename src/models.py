import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(200), nullable = False)
    password = Column(String(500), nullable = False)
    username = Column(String(200), nullable = False)

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key = True)
    description = Column(Text, nullable = False)
    photo = Column(String(250), nullable = False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key = True)
    description = Column(Text, nullable = False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False)
    user_id = Column(Integer , ForeignKey("user.id"), nullable = False)

class Like(Base):
    __tablename__ = "like"

    id = Column(Integer, primary_key = True)
    count = Column(Integer, nullable = False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
