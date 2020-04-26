# การสร้างฟังก์ชันแบบไม่มี return value
def hello(name):
    print(f"hello {name}")


# สร้างฟังก์ชันแบบมี return value
def area(width, height):
    total = width*height
    return total


# เรียกใช้ฟังก์ชัน hello
hello("samit")

# เรียกใช้งานฟังก์ชัน area()

print(area(5, 8))
print(area(15, 6))

# ฟังก์ชันแบบมีค่าเริ่มต้น


def show_info(name="", salary=0.00, lang="not define"):
    print(f"name:{name}")
    print(f"salaray:{salary}")
    print(f"language:{lang}")


# เรียกใช้งาน function
show_info()
print()
show_info('samit', 12000, 'PHP')
