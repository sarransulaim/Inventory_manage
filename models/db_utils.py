from sqlalchemy.orm import sessionmaker
from models import engine, Item, Department, StockHistory

Session = sessionmaker(bind=engine)
session = Session()

def add_item(name, barcode, quantity, low_stock, department_id):
    item = Item(
        name=name,
        barcode=barcode,
        quantity=quantity,
        low_stock_threshold=low_stock,
        department_id=department_id
    )
    session.add(item)
    session.commit()

def update_stock(item_id, quantity_change):
    item = session.query(Item).filter(Item.id == item_id).first()
    if item:
        item.quantity += quantity_change
        session.commit()

def get_item_by_name(name):
    return session.query(Item).filter(Item.name.like(f"%{name}%")).all()

def get_inventory():
    return session.query(Item).all()
  
