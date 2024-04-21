class user (object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        return 'name:%s age:%s' % (self.name, self.__age)

    def __add__(self, other):
        return self.name + other.name
    def __eq__(self, other):
        return self.__age == other.__age

mia= user('mia ', 20)
print(mia)
print(str(mia))
jack= user('jack', 30)
print(mia + jack)
print(mia == jack)