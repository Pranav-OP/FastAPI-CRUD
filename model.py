from sqlalchemy import Column, Integer, String
from database import base

class item(base):
    __tablename__ = 'itemsss'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    content = Column(String(256))
