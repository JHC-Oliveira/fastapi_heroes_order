from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base

#this choice type is like an ENUM but with tuple with key, value. It will be our order status.
from sqlalchemy_utils.types import ChoiceType
from datetime import datetime

# Create the connection with database
db = create_engine("sqlite:///data/database.db")

# Create the database base
Base = declarative_base()

# Create tables:
class User(Base):
    __tablename__ = "users"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String)
    password = Column("password", String)
    active = Column("active", Boolean)
    admin = Column("admin", Boolean, default=False)
    
    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin        
        
class Order(Base):
    __tablename__= "orders"
    
    ORDER_STATUS = (
        ("PENDING","PENDING"),
        ("CANCELED", "CANCELED"),
        ("FINALIZED", "FINALIZED")
    )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(choices=ORDER_STATUS)) #pending, canceled, finilized
    user_id = Column("user", ForeignKey("users.id"), nullable=False) 
    total_price = Column("total_price", Float)
    #items =
    date = Column("date", DateTime, default=datetime.utcnow)
    
    def __init__(self, user_id, status="PENDING", total_price=0):
        self.user_id = user_id
        self.status = status        
        self.total_price = total_price
        
        
        
class OrderItem(Base):
    __tablename__ = "order_itens"
    
    ITEM_SIZE = (
        ("SMALL", "SMALL"),
        ("MEDIUM", "MEDIUM"),
        ("LARGE", "LARGE")
    )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity", Integer, nullable=False)
    hero_name = Column("name", String, nullable=False)
    size = Column("size", ChoiceType(choices=ITEM_SIZE), nullable=False)
    unit_price = Column("unit_price", Float, nullable=False)
    order_id = Column("order_id", ForeignKey("orders.id"), nullable=False)
    
    def __init__(self, quantity, hero_name, size, unit_price, order_id):
        self.quantity = quantity
        self.hero_name = hero_name
        self.size = size
        self.unit_price = unit_price
        self.order_id = order_id