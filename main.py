from pymongo import MongoClient

client = MongoClient('mongodb://root:s3cr37@localhost:27017')
db = client.testing


def main():
    user = {
        'first_name': 'Stina',
        'last_name': 'Bengtsson',
        'phone_numbers': ['1212121', '456345343'],
        'address': {
            'street_address': 'Stora gränd 4',
            'zip_code': '543 21',
            'city': 'Storköping'
        }
    }

    # db.customers.insert_one(user)

    users = db.users.find({'first_name': '/Sti/'})  # SELECT * FROM users WHERE first_name LIKE '%Sti%'
    for user in users:
        print(user)


if __name__ == '__main__':
    main()
