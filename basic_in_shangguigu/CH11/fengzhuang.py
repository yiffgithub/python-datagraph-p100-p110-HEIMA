class user (object):
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def __show(self):
        print('name:', self._name, 'age:', self.__age)

    @property #作用就是把一个方法当作属性来用变量来用
    def age(self):
        return self.__age
    @age.setter #设置属性，相当于给属性赋值，名字必须和属性名一样
    def age(self, age):
        if isinstance(age, int):

            self.__age = age
        else:
            print('年龄必须是整数')
            #raise ValueError('年龄必须是整数')



mia= user('mia', 20)
# print(dict(mia.__dict__))
# print(mia._name)
# print(mia. _user__age)
# mia._user__show()

print(mia.age)
mia.age = 30
print(mia.age)
mia.age = 'dhdh'
