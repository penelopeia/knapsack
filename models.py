from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Instructions(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    period = Column(Integer)
    
    def __repr__(self):
        return "<Instructions(period='{}'>"\
                .format(self.period)