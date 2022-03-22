from abc import ABC
from pymongo import MongoClient

client = MongoClient('mongodb://root:s3cr37@localhost:27017')
db = client.mydb


class Document(ABC):
    collection = None

    def __init__(self, data):
        self.__dict__ = data

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def save(self):
        self.collection.insert_one(self.__dict__)


class Person(Document):
    collection = db.users


class Product(Document):
    collection = db.products


def main():
    user = {
        'first_name': 'Lars',
        'last_name': 'Svensson',
        'phone_numbers': ['1212121', '456345343'],
        'address': {
            'street_address': 'Stora gränd 4',
            'zip_code': '543 21',
            'city': 'Storköping'
        }
    }

    user2 = {
        'name': 'Lisa Lax'
    }

    product_dict = {
        'name': 'Ball',
        'price': 3.45
    }

    product = Product(product_dict)
    product.save()

    person = Person(user2)

    person.save()

    # person.__dict__ = user

    print(person)




if __name__ == '__main__':
    main()
