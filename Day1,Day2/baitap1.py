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
#     def __init__(self,height,width):
#         self.height = height
#         self.width = width
#     def chuvi(self):
#         return (self.height + self.width) * 2
#     def dientich(self):
#         return self.height * self.width
# class Circle:
#     def __init__(self, r):
#         self.r = r
#     def chuvi(self):
#         return 2 * math.pi * self.r
#     def dientich(self):
#         return math.pi * self.r * self.r
# shape = input("Nhap hinh (rectangle/circle): ")
# if shape == "rectangle":
#     height = float(input("Nhap chieu cao: "))
#     width = float(input("Nhap chieu rong: "))
#     rect = Rectangle(height, width)
#     print("Chu vi:", rect.chuvi())
#     print("Dien tich:", rect.dientich())
# elif shape == "circle":
#     r = float(input("Nhap ban kinh: "))
#     cir = Circle(r)
#     print("Chu vi:", cir.chuvi())
#     print("Dien tich:", cir.dientich())
# else:
#     print("Ko hop le")

# 3
# from datetime import datetime
# class CustomDate:
#     def __init__(self):
#         self.now = datetime.now()
#     def get_date(self):
#         return str(self.now.day)+"/"+str(self.now.month)+"/"+str(self.now.year)
#     def get_time(self):
#         return str(self.now.hour)+":"+str(self.now.minute)+":"+str(self.now.second)
# today = CustomDate()
# print("Ngay:", today.get_date())
# print("Gio:", today.get_time())

# 4
# from datetime import datetime
# class DateHandler:
#     def format_date(self, d):
#         return str(d.day)+"/"+str(d.month)+"/"+str(d.year)
#     def get_days_between(self, d1, d2):
#         return (d2 - d1).days
# date = DateHandler()
# start = datetime(2021, 1, 1)
# end = datetime(2022, 1, 1)
# print(date.format_date(start))
# print(date.format_date(end))
# print("So ngay:", date.get_days_between(start, end))