from sqlalchemy import Column, Integer, String
from . import DeclarativeBase

class DMOZEntry(DeclarativeBase):

    __tablename__ = 'dmoz_entry'

    id = Column(Integer, primary_key=True, nullable=False)
    url = Column(String)
    title = Column(String)
    description = Column(String)

    def __init__(self, page, content):
        self.url = page
        self.title = content.get(u'd:Title', u'')
        self.description = content.get(u'd:Description', u'')