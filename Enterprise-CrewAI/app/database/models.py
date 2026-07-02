from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(200))
    city = Column(String(100))
    state = Column(String(100))
    join_date = Column(Date)

    orders = relationship("Order", back_populates="customer")


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)

    product_name = Column(String(200))
    category = Column(String(100))
    brand = Column(String(100))
    price = Column(Float)
    stock = Column(Integer)

    items = relationship("OrderItem", back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.customer_id"))

    order_date = Column(Date)

    total_amount = Column(Float)

    status = Column(String(50))

    customer = relationship("Customer", back_populates="orders")

    items = relationship("OrderItem", back_populates="order")

    payment = relationship("Payment", back_populates="order", uselist=False)


class OrderItem(Base):
    __tablename__ = "order_items"

    item_id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey("orders.order_id"))

    product_id = Column(Integer, ForeignKey("products.product_id"))

    quantity = Column(Integer)

    unit_price = Column(Float)

    order = relationship("Order", back_populates="items")

    product = relationship("Product", back_populates="items")


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey("orders.order_id"))

    payment_mode = Column(String(50))

    payment_date = Column(Date)

    amount = Column(Float)

    order = relationship("Order", back_populates="payment")