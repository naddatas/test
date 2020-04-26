print("----------------------------")
print("# โปรแกรมหาผลรวม")
print("# Type 'exit' to end program")
print("----------------------------")

# 9ตัวแผรไว้เก็บผลรวม
sumdata = 0
count = 1

while True:
    data = input(f"Enter number {count}:")
    #count = count + 1
    if data == "exit":
        break
    sumdata += int(data)
    count = count + 1

print(f"Sum valau is {sumdata}")
