from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, URL
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True)
    Name = Column(String, unique=True, index=True)
    img = Column(String)

    items = relationship("dishes", back_populates="owner")