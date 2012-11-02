from sqlalchemy import Column, Integer, String, DateTime
from . import DeclarativeBase

class DmozTopic(DeclarativeBase):

    __tablename__ = 'dmoz_topic'

    id = Column(Integer, primary_key=True, nullable=False)
    catid = Column(Integer)
    topic = Column(String)
    title = Column(String)
    description = Column(String)

    def __init__(self, content):
        self.catid = int(content.get(u'catid', 0))
        self.topic = content.get(u'id', u'')
        self.title = content.get(u'd:Title', u'')
        self.description = content.get(u'd:Description', u'')