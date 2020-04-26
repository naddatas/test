# การสร้างข้อมูลแบบ List
number = [5, 6, 13, 24, 7, 16]
name = ['John', 'Jane', 'jum', 'Wasan']
mix = [10, 25.75, True, 'Samit']

# การเข้าถึงสมาชิกใน List
print(number[1])
print(number[3])
print(mix[2], mix[3])

# การนับสมาชิก
print("สมาชิกทั้งหมดของ number=", len(number))


# การสร้าง list แบบว่าง
data = []

# การเพิ่มสมาชิดเข้า list
data.append(10)
data.append(15)
data.append(20)

print(data)

# การ update ใน list
data[1] = 12

print(data)

# ฟังก์ชัน loop อ่านสมาชิกทั้งหมด
for n in number:
    print(n)

# loop แล้วหาผลรวม
sum = 0
for num in number:
    sum += num

print(sum)

