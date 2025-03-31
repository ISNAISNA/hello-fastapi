from sqlalchemy import Column, ForeignKey, Integer, String, Sequence
from sqlalchemy.orm import relationship

from db.database import Base

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    title = Column(String(100))
    description = Column(String(255))
    
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="items")

