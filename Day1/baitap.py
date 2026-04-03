# 1
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#     def hi(self):
#         print(f"Hi, my name is {self.name}.")
#     def tellposition(self):
#         print(f"I am a {self.position}.")
# john = Employee("John", "Software Engineer")
# john.hi()
# john.tellposition()

# 2
# import math
# class Rectangle:
#     def __init__(self, h, w): self.h, self.w = h, w
#     def perimeter(self): return 2*(self.h+self.w)
#     def area(self): return self.h*self.w
# class Circle:
#     def __init__(self, r): self.r = r
#     def perimeter(self): return 2*math.pi*self.r
#     def area(self): return math.pi*self.r**2
# shape = input("Shape (rectangle|circle): ").lower()
# if shape == "rectangle":
#     h = float(input("Height: "))
#     w = float(input("Width: "))
#     r = Rectangle(h,w)
#     print(r.perimeter(), r.area())
# elif shape == "circle":
#     r = float(input("Radius: "))
#     c = Circle(r)
#     print(c.perimeter(), c.area())
# else:
#     print("Invalid!")

# 3
# from datetime import datetime
# class CustomDate:
#     def __init__(self):
#         self.now = datetime.now()
#     def get_date(self):
#         return f"{self.now.day:02d}/{self.now.month:02d}/{self.now.year}"
#     def get_time(self):
#         return f"{self.now.hour:02d}:{self.now.minute:02d}:{self.now.second:02d}"
# now = CustomDate()
# print(now.get_date())
# print(now.get_time())

# 4
# from datetime import datetime
# class DateHandler:
#     @staticmethod
#     def format_date(d): return f"{d.day:02d}/{d.month:02d}/{d.year}"
#     @staticmethod
#     def get_days_between(d1, d2): return (d2 - d1).days
# start = datetime(2021,1,1)
# end = datetime(2022,1,1)
# print(DateHandler.format_date(start))
# print(DateHandler.format_date(end))
# print(DateHandler.get_days_between(start, end))