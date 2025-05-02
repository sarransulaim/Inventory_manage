from sqlalchemy.orm import sessionmaker
from models import engine, Item, Department, StockHistory

Session = sessionmaker(bind=engine)
session = Session()

# Add a new item to the database
def add_item(name, barcode, quantity, low_stock_threshold, department_id):
    try:
        new_item = Item(
            name=name,
            barcode=barcode,
            quantity=quantity,
            low_stock_threshold=low_stock_threshold,
            department_id=department_id
        )
        session.add(new_item)
        session.commit()
        return new_item
    except Exception as e:
        session.rollback()
        return f"Error adding item: {e}"

# Get items by name
def get_item_by_name(name: str):
    session = Session(bind=engine)
    item = session.query(Item).filter(Item.name.ilike(f"%{name}%")).all()
    session.close()
    return item

# Add a new department
def add_department(name):
    try:
        new_dept = Department(name=name)
        session.add(new_dept)
        session.commit()
        return new_dept
    except Exception as e:
        session.rollback()
        return f"Error adding department: {e}"

# Retrieve all departments
def get_all_departments():
    return session.query(Department).all()

# Update an existing item
def update_item(item_id, name=None, barcode=None, quantity=None, low_stock_threshold=None):
    item = session.query(Item).filter(Item.id == item_id).first()
    if not item:
        return "Item not found"
    if name:
        item.name = name
    if barcode:
        item.barcode = barcode
    if quantity is not None:
        item.quantity = quantity
    if low_stock_threshold is not None:
        item.low_stock_threshold = low_stock_threshold
    session.commit()
    return item

# Delete an item
def delete_item(item_id):
    item = session.query(Item).filter(Item.id == item_id).first()
    if item:
        session.delete(item)
        session.commit()
        return f"Item {item.name} deleted."
    return "Item not found"

# Retrieve stock history for an item
def get_item_history(item_id):
    return session.query(StockHistory).filter(StockHistory.item_id == item_id).all()

# Record stock change
def record_stock_change(item_id, change, note=""):
    new_history = StockHistory(item_id=item_id, change=change, note=note)
    session.add(new_history)
    session.commit()
    return new_history
