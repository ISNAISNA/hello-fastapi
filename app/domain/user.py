from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

from db.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(100))

    items = relationship("Item", back_populates="user")




