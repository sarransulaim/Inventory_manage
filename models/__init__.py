from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    items = relationship("Item", back_populates="department")

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    barcode = Column(String(50), unique=True)
    quantity = Column(Integer)
    low_stock_threshold = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.id'))
    last_updated = Column(DateTime, default=datetime.now)
    department = relationship("Department", back_populates="items")

class StockHistory(Base):
    __tablename__ = 'stock_history'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    change = Column(Integer)
    timestamp = Column(DateTime, default=datetime.now)
    note = Column(String(200))

DATABASE_URL = "sqlite:///inventory.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

