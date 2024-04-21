class people(object):
    # 类属性 java里的static 静态属性
    number = 0
    level = ['low', 'middle', 'high']

    def __init__(self, name, age, level='low'):
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

    def getweapon(self, weapon):
        self.weapon = weapon

    def showweapon(self):
        for i, j in self.weapon.__dict__.items():
            print(i, j)

    # 类方法
    @classmethod
    def getnumber(cls):
        print('当前人数:', cls.number)
    # 静态方法
    @staticmethod
    def validage(**kwargs):
        if 'age' in kwargs:
            if kwargs['age'] < 18:
                print('未成年')
            else:
                print('成年人')
        else:
            print('年龄输入有误')

infos= {'name':'xiaowang','age':20}
people.validage(**infos)


xiaowang = people('xiaowang', 20)
people.getnumber()
print('小王的level是%s' % xiaowang.level)

class Weapon(object):
    all_weapons = []
    def __init__(self, name, damage,level):
        self.name = name
        self.damage = damage
        self.level = level
        Weapon.all_weapons.append(self)

    def show(self):
        print('武器名称:', self.name, '伤害值:', self.damage)

    @classmethod
    def max_damage(cls):
        max_damage = 0
        for i in cls.all_weapons:
            if i.damage > max_damage:
                max_damage = i.damage
        return max_damage

qiang = Weapon('枪', 300,'high')
jian= Weapon('剑', 100,'low')

gong = Weapon('弓', 200,'middle')


print(Weapon.max_damage())

'''
实例属性
类属性
实例方法
类方法
'''

# 静态方法
