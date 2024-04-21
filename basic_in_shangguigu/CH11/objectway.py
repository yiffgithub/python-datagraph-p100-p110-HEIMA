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


xiaowang = people('xiaowang', 20)
# print(xiaowang.name)
# print(xiaowang.__dict__)
# print(people.number)
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()
xiaowang.levelup()
xiaowang.show()


class weapon(object):
    lowdamage = 10
    middledamage = 50
    highdamage = 100
    maxdamage = 2000
    level = ['low', 'middle', 'high']

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

        if damage > weapon.lowdamage and damage <= weapon.middledamage:
            self.level = weapon.level[0]
        elif damage > weapon.middledamage and damage <= weapon.highdamage:
            self.level = weapon.level[1]
        elif damage > weapon.highdamage and damage <= weapon.maxdamage:
            self.level = weapon.level[2]
        else:
            raise Exception('damage out of range')



try:
    sword = weapon('sword', 100)
    aoxue = weapon('aox', 200)
    hamer = weapon('hamer', 3000000)
except Exception as e:
    print(e)

# print(sword.__dict__)
# print(aoxue.__dict__)
# print('aoxue的级别是'+ aoxue.level)
xiaowang.getweapon(aoxue)
xiaowang.showweapon()