"""一组用于表示燃油汽车和电动汽车的类"""

class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #该属性指定默认值
    
    def update_odometer(self, mileage):     #通过方法修改属性的值
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("禁止往回调里程数")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        if miles<0.0:
            print("不能减少里程数，请输入大于零的里程数")
        else:
            self.odometer_reading+=miles

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank():
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


#类继承
class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """电动汽车的独特之处
        
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery=Battery()

#测试