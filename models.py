from sqlalchemy.orm import declarative_base
import sqlalchemy as sa

Base = declarative_base()


class Pablisher(Base):
    __tablename__ = 'pablisher'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(length=30), nullable=False)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Book(Base):
    __tablename__ = 'book'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(length=40), nullable=False)
    publisher_id = sa.Column(sa.Integer, sa.ForeignKey('pablisher.id'), nullable=False)

    def __str__(self):
        return f'{self.id}: ({self.title}, {self.publisher_id})'


class Shop(Base):
    __tablename__ = 'shop'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(length=30), nullable=False)

    def __str__(self):
        return f'{self.id}: ({self.name})'


class Stock(Base):
    __tablename__ = 'stock'
    id = sa.Column(sa.Integer, primary_key=True)
    book_id = sa.Column(sa.Integer, sa.ForeignKey('book.id'), nullable=False)
    shop_id = sa.Column(sa.Integer, sa.ForeignKey('shop.id'), nullable=False)
    count = sa.Column(sa.Integer, nullable=False)

    def __str__(self):
        return f'{self.id}: ({self.book_id}, {self.shop_id}, {self.count})'


class Sale(Base):
    __tablename__ = 'sale'
    id = sa.Column(sa.Integer, primary_key=True)
    price = sa.Column(sa.Float, nullable=False)
    date_sale = sa.Column(sa.DateTime, nullable=False)
    stock_id = sa.Column(sa.Integer, sa.ForeignKey('stock.id'), nullable=False)
    count = sa.Column(sa.Integer, nullable=False)

    def __str__(self):
        return f'{self.id}: ({self.price}, {self.date_sale}, {self.stock_id}, {self.count})'


def create_tables(engine):
    Base.metadata.create_all(engine)