scores = {
    'john': 1200,
    'bob': 2000,
    'janny': 4200
}

print(scores)
print(scores['bob'])

# เพิ่มสมาชิกใหม่เข้า
scores['roger'] = 3000

print(scores)

# การสร้าง dictionary ว่าง
points = {}

# เพิ่มค่าเข้าไป
points['mr_a'] = 10.2
points['mr_b'] = 15.4  # เพิ่มค่าเข้าไป
points['mr_c'] = 22.8  # เพิ่มค่าเข้าไป

print(points)

# การ loop อ่านสมาชิกจาก dictionary vvd,k
for k, v in scores.items():
    print(k, v)
