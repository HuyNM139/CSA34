# Việc viết những thuộc tính có trong class Cha => tốn effort, dài dòng, thiếu sự liên kết
# class Car:
#     def __init__(self, name, color, type, wheels, slots, speed):
#         self.name = name
#         self.color = color
#         self.type = type
#         self.wheels = wheels
#         self.slots = slots
#         self.speed = speed
from day1 import Vehicle
# Kể thừa có thể chứa toàn bộ thuộc tính và chức năng của class cha

class Employee:
    def __init__(self, age, position):
        self.age = age
        self.position = position

class Car(Vehicle, Employee):
    def __init__(self, name, color, type, wheels, slots, speed, items, age, position, fuel, price):
        Vehicle.__init__(self, name, color, type, wheels, slots, speed, items)
        Employee.__init__(self, age,position)

        self.fuel = fuel
        self.price = price

    # information:
    def information(self):
        print("Fuel: " , self.fuel)
        print("Price: " , self.price)
        super().information()

    # __str__: In ra object ở dạng string
    def __str__(self):
        return f"Name: {self.name}"

    def __add__(self, object):
        self.age + object.age
car1 = Car("Volvo","red","super-car",4,4,400,[],10,"leader",1000,3000)
car2 = Car("Toyota","black","normal",5,3,200,[],30,"middle",2000,1500)
# car.information()
print(car1+car2)