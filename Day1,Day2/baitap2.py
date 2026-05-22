# Bài 1:
# class Rectangle:
#     def __init__(self,height,width):
#         self.height=height
#         self.width=width
#     def __str__(self):
#         return f"Rectangle object with height = {self.height} and width = {self.width} "
# rectangle = Rectangle(2, 1)
# print(rectangle)

# Bài 2:
# class MathList:
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return str(self.data)
#     def __add__(self, value):
#         return MathList([x + value for x in self.data])
#     def __sub__(self, value):
#         return MathList([x - value for x in self.data])
# m_list = MathList([1, 2, 3, 4, 5])
# print(m_list)
# m_list = m_list + 2
# print(m_list)

# Bài 3:
class Square:
    def __init__(self, side):
        self.side = side
    def cal_area(self):
        return self.side * self.side
class Cube(Square):
    def cal_area(self):
        return 6 * (self.side ** 2)
    def cal_volume(self):
        return self.side ** 3
square = Square(2)
print(f"Square area: {square.cal_area()}")
cube = Cube(2)
print(f"Cube area: {cube.cal_area()}")
print(f"Cube volume: {cube.cal_volume()}")