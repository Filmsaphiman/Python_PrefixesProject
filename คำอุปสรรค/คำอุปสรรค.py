Number = float(input("ป้อนตัวเลข :"))
Prefixes = input("ป้อนหน่วยคำอุปสรรคของโจทย์ :")
Prefixes_2 = input("ป้อนหน่วยคำอุปสรรคที่ต้องการแปลงเป็น :")


E = 10**18
P = 10**15
T = 10**12
G = 10**9
M = 10**6
k = 10**3
h = 10**2
da = 10**1
d = 10**-1
c = 10**-2
m = 10**-3
u = 10**-6
p = 10**-12
f = 10**-15
a = 10**-18


print(int(Prefixes))


result = (Number*Prefixes)/Prefixes_2
    

print("แปลงค่าของ ",Number,Prefixes,"เป็น",result)