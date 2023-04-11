class Robot:
    '''代表一个机器人，拥有一个名字属性'''

    # 类属性，统计机器人个数
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(初始化 {})".format(self.name))

        Robot.population += 1

    def die(self):
        print("{} is being destoryed!".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} is the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """显示当前人口数。"""
        print("We have {:d} robots.".format(cls.population))
droid1=Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2=Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

droid1.die()
droid2.die()