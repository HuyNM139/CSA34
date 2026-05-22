import sqlite3

conn = sqlite3.connect("C:/Users/Dell/Downloads/CSA34/Day3/homework.db")

cursor = conn.cursor()

# cursor.execute("""
#     Create table users(
#         id number,
#         name varchar(255)           
#     )
# """)

listUser = [
    {}
]

data = [
    {"id": 4, "name": "Alice"},
    {"id": 5, "name": "Bob"},
    {"id": 6, "name": "Charlie"},
    {"id": 7, "name": "David"},
    {"id": 8, "name": "Emma"}
]

values = ""

for i in range(0, len(data)):
    if i < len(data) - 1:
        values = values + f"({data[i]["id"]}, '{data[i]["name"]}')" + ","
    else:
        values = values + f"({data[i]["id"]}, '{data[i]["name"]}')"

# print(values)

# THÊM dữ liệu
# cursor.execute("""Insert into users (id, name) 
#                values 
#                (2, 'Long'), 
#                (3, 'Tung Anh')
#             """)

# cursor.execute(f"""Insert into users (id, name) values {values}""")

# Lấy ra dữ liệu trong SQL thông qua Python
cursor.execute("Select * from users")
output = cursor.fetchall()
# print(output)
for val in output:
    print(val[1])
conn.commit()
conn.close()

# Thêm 1 cột password
# Dùng input để định nghĩa password cho 1 user có name nằm trong bảng