class people(object):
    # 类属性 java里的static 静态属性
    number = 0
    level = ['low', 'middle', 'high']

    def __init__(self, name, age,level='low'):
        self.name = name
        self.age = age
        self.level = level
        people.number += 1

    def show(self):
        print('name:', self.name, 'age:', self.age, 'number:', people.number, 'level:', self.level)

    n = 0

    def levelup(self):
        if self.level in people.level:
            # 执行某些操作

            index1 = people.level.index(self.level)
            if index1 <= len(people.level) - 2:
                print('index1:', index1)
                self.level = people.level[index1 + 1]
            else:
                people.n = people.n + 1
                self.level = '高级' + str(people.n) + '星'

        else:
            people.n = people.n + 1
            self.level = '高级' + str(people.n) + '星'
    def getweapon(self,weapon):
        self.weapon = weapon
    def showweapon(self):
        for i,j in self.weapon.__dict__.items():
            print(i, j)

class Vip_people(people):
    #重写父类的属性
    def __init__(self,name,age,coins,level= 'high'):
        super().__init__(name,age,level)

        self.coins = coins
    #重写父类的方法
    def show(self):
        print('name:', self.name, 'age:', self.age, 'number:', people.number, 'level:', self.level,'coins:',self.coins)

    def levelup(self):

                people.n = people.n + 1
                self.level = '高级' + str(people.n) + '星'


xiaoli= Vip_people('xiaoli', 20,100)
xiaoli.show()
xiaoli.levelup()
xiaoli.show()
xiaoli.levelup()
xiaoli.show()
xiaoli.levelup()
xiaoli.show()
xiaoli.levelup()
xiaoli.show()

#多态笔记
#多态是指一类事物有多种形态
#多态性是指在父类中定义的属性和方法被子类继承之后，可以具有不同的数据类型或表现形式
#多态性是面向对象编程的一个重要特点，多态性可以增加程序的灵活性

class animal(object):
    def bark(self):
        print('animal is barking')

class dog(animal):
    def bark(self):
        print('dog is barking')

class cat(animal):
    def bark(self):
        print('cat is barking')

def bark(object):
    object.bark()

class test(object):
    def bark(self):
        print('test is barking')

dog1 = dog()
animal1 = animal()
cat1 = cat()
bark(dog1)
bark(animal1)
bark(cat1)
test1 = test()
bark(test1)