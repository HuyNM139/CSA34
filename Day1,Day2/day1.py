class Vehicle:
    # Thuộc tính: wheels, name, color, type, slots, speed
    def __init__(self, name, color, type, wheels, slots, speed, items):
        self.name = name
        self.color = color
        self.type = type
        self.wheels = wheels
        self.slots = slots
        self.speed = speed
        self.items = items

    # Chưc năng:
    def information(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Type:", self.type)
        print("Wheels:", str(self.wheels))
        print("Slots:", str(self.slots))
        print("Speed:", str(self.speed))
        print(f"Vận tốc: {self.wheels * self.slots + self.speed}")

# Tạo những object từ class
# car = Vehicle("Mercedes", "white", "car", 4, 4, 300)
# bike = Vehicle("BMW", "black", "bicycle", 2, 2, 10)

# Cách để object truy cập vào lấy ra giá trị của các thuộc tính trong class
# print("Vehicle's name: " + car.name)
# print("Vehicle's color: " + car.color)
# print("Vehicle's type: " + car.type)
# print("Vehicle's wheels: " + str(car.wheels))
# print("Vehicle's slots: " + str(car.slots))
# print("Vehicle's speed: " + str(car.speed))

# car.information()
# bike.information()

# Viết 1 hàm tính vận tốc của xe: CT => wheels x slot + speeds, hàm này trả về vận tốc của xe

# class Character:
#     def __init__(self, name, lane, role, HP, mana, Q, W, E, R, items):
#         self.name = name
#         self.lane = lane
#         self.role = role
#         self.HP = HP
#         self.mana = mana
#         self.Q = Q
#         self.W = W
#         self.E = E
#         self.R = R
#         self.items = items
#     def intrinsic(self):
#         print(f"{self.name} sử dụng intrinsic")
#     def useQ(self):
#         print(f"{self.name} sử dụng {self.Q}")
#     def useW(self):
#         print(f"{self.name} sử dụng {self.W}")
#     def useE(self):
#         print(f"{self.name} sử dụng {self.E}")
#     def useR(self):
#         print(f"{self.name} sử dụng {self.R}")
#     def info(self):
#         print("Name:", self.name)
#         print("Lane:", self.lane)
#         print("Role:", self.role)
#         print("HP:", str(self.HP))
#         print("mana:", str(self.mana))
#         print("Items:", self.items)
#     def add_items(self):
#         for i in range(6):
#             item = input(f"Nhập item thứ {i+1}: ")
#             self.items.append(item)
# charac = Character("Darius", "dominant", "Fighter / Tank", 652, 263, "Massacre", "Crippled", "Arrest", "Noxus Guillotine", [])
# charac.info()
# charac.add_items()
# charac.info()
# charac.useQ()
# charac.useW()
# charac.useE()
# charac.useR()
