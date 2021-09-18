from sqlalchemy import Column, Integer, String, Float

from connections.sqlite import Base


class Close_RSI(Base):
    __tablename__ = 'Close_RSI'

    index = Column(Integer, nullable=False, primary_key=True, index=True)
    timestamp = Column(Integer, nullable=False)
    datetime = Column(String, nullable=False)
    close = Column(Float, nullable=False)
    RSI = Column(Float, nullable=True)
