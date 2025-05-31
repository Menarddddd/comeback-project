from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    tweets = relationship("Tweet", back_populates="author")


class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    caption = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("User.id"))

    author = relationship("User", back_populates="tweets")

