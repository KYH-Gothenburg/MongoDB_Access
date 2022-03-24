from abc import ABC
from pymongo import MongoClient

client = MongoClient('mongodb://root:s3cr37@localhost:27017')
db = client.mydb


class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None


class Document(ABC):
    collection = None

    def __init__(self, data):
        self.__dict__ = data

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def save(self):
        if '_id' not in self.__dict__:
            self.collection.insert_one(self.__dict__)
        else:
            self.collection.replace_one({'_id': self._id}, self.__dict__)

    def delete(self):
        self.collection.delete_one(self.__dict__)

    def delete_field(self, field):
        self.collection.update_one({'_id': self._id}, {"$unset": {field: ""}})

    @classmethod
    def all(cls):
        return [cls(item) for item in cls.collection.find()]

    @classmethod
    def insert_many(cls, items):
        for item in items:
            cls(item).save()

    @classmethod
    def delete_many(cls, **kwargs):
        cls.collection.delete_many(kwargs)

    @classmethod
    def find(cls, **kwargs):
        return ResultList(cls(item) for item in cls.collection.find(kwargs))


class Person(Document):
    collection = db.users


class Product(Document):
    collection = db.products


def main():
    user = {
        'first_name': 'Petra',
        'last_name': 'Svensson',
        'phone_numbers': ['1212121', '456345343'],
        'address': {
            'street_address': 'Stora gränd 4',
            'zip_code': '543 21',
            'city': 'Storköping'
        }
    }

    # person = Person.find(last_name='Svensson').first_or_none()
    #
    # person.delete()

    item = {
            'name': 'Chair',
            'price': 45.67
        }

    product = Product(item)

    products = [
        {
            'name': 'Chair',
            'price': 45.67
        },
        {
            'name': 'Car',
            'price': 23.56
        }
    ]

    # TODO: Create this method
    Product.insert_many(products)

    # TODO: Create this method
    Person.delete_many(last_name='Svensson')

    person = Person.find(age=34).first_or_none()
    if person:
        # TODO: Create this method
        # Hint: db.collection.update_one({'_id': id}, {"$unset": {field: ""}})
        person.delete_field('age')



if __name__ == '__main__':
    main()
