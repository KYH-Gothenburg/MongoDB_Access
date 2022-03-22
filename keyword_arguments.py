def func(*args, **kwargs):
    print(args)
    print(kwargs)


def main():
    # func({'name': 'Anna', 'age': 33})
    func(name='Jöns', age=34)


if __name__ == '__main__':
    main()
