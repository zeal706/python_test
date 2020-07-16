n = "李海灵"
print(n)
print("python")

class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make 
        self.model = model
        self.year = year
    def update_odometer(self, mileage):
        """新的里程数"""
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading+= miles
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()