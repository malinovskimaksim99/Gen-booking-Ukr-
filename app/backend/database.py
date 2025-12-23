from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import uuid, os

Base = declarative_base()
engine = create_engine("sqlite:///gen_booking.db", echo=False)
SessionLocal = sessionmaker(bind=engine)

class PlotNode(Base):
    __tablename__ = "plot_node"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    book_id = Column(String, nullable=False)
    parent_id = Column(String)
    title = Column(String)
    desc = Column(Text)
    level = Column(Integer, default=0)
    pos_x = Column(Integer, default=0)
    pos_y = Column(Integer, default=0)
    collapsed = Column(Integer, default=0)
    tag = Column(String, default="neutral")
    written = Column(Integer, default=0)

Base.metadata.create_all(engine)
