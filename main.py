# import ทั้งหมดทุกฟังก์ชันใน module
#import number

# importมาบางฟังก์ชัน
#from number import factorial, fibonacci

# import ทุกฟังก์ชัน แบบนี้เจอบ่อยสุด
#from number import*

from number import factorial as fa, fibonacci as fi

# เรียกใช้งาน
# print(number.factorial(5))
# print(number.fibonacci(100))
print(fa(5))
print(fi(5))
