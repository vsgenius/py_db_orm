import json
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from models import Pablisher, Book, Shop, Stock, Sale, create_tables


def load_json(file_path, session):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for s in data:
            if s['model'] == 'publisher':
                session.add(Pablisher(id=s['pk'], name=s['fields']['name']))
                session.commit()
            elif s['model'] == 'book':
                session.add(Book(id=s['pk'], title=s['fields']['title'], publisher_id=s['fields']['publisher']))
                session.commit()
            elif s['model'] == 'shop':
                session.add(Shop(id=s['pk'], name=s['fields']['name']))
                session.commit()
            elif s['model'] == 'stock':
                session.add(Stock(id=s['pk'], shop_id=s['fields']['shop'], book_id=s['fields']['book'],
                                  count=s['fields']['count']))
                session.commit()
            elif s['model'] == 'sale':
                session.add(Sale(id=s['pk'], price=s['fields']['price'], date_sale=s['fields']['date_sale'],
                                 count=s['fields']['count'], stock_id=s['fields']['stock']))
                session.commit()
    print('Загрузка данных завершена')


def find_publisher(session):
    field = input('Введите данные для поиска: ')
    if field.isdigit():
        for s in session.query(Pablisher).filter(Pablisher.id==field):
            print(s)
    else:
        for s in session.query(Pablisher).filter(Pablisher.name.like(field)):
            print(s)


def main():
    DSN = f"postgresql://postgres:postgres@localhost:5432/netology_sqlalchemy"
    engine = sa.create_engine(DSN)
    create_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    load_json('tests_data.json',session)
    find_publisher(session)


if __name__ == '__main__':
    main()
