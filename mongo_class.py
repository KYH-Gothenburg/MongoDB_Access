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

    @classmethod
    def all(cls):
        return [cls(item) for item in cls.collection.find()]

    @classmethod
    def find(cls, **kwargs):
        return [cls(item) for item in cls.collection.find(kwargs)]

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

    result = Person.all()
    result = Person.find(first_name='Fia', last_name='Svensson')
    person = result[0]
    person.first_name = 'Inga'
    person.save()
    result = [Person(item) for item in db.users.find({'last_name': 'Svensson'})]
    print()




if __name__ == '__main__':
    main()
