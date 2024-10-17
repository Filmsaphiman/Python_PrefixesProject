Number = float(input("ป้อนตัวเลข :"))
Prefixes = str(input("ป้อนหน่วยคำอุปสรรคของโจทย์ [ถ้าไม่มีให้เชียน No]:"))

if Prefixes == "E" :
    Prefixes = 10**18
if Prefixes == "P" :
    Prefixes = 10**15
if Prefixes == "T" :
    Prefixes = 10**12
if Prefixes == "G" :
    Prefixes = 10**9
if Prefixes == "M" :
    Prefixes = 10**6
if Prefixes == "k" :
    Prefixes = 10**3
if Prefixes == "h" :
    Prefixes = 10**2
if Prefixes == "da" :
    Prefixes = 10**1
if Prefixes == "d" :
    Prefixes = 10**-1
if Prefixes == "c" :
    Prefixes = 10**-2
if Prefixes == "m" :
    Prefixes = 10**-3
if Prefixes == "u" :
    Prefixes = 10**-6
if Prefixes == "n" :
    Prefixes = 10**-9
if Prefixes == "p" :
    Prefixes = 10**-12
if Prefixes == "f" :
    Prefixes = 10**-15
if Prefixes == "a" :
    Prefixes = 10**-18
if Prefixes == "No" :
    Prefixes = 1

result = (Number*Prefixes)

Prefixes_2 = str(input("ป้อนหน่วยคำอุปสรรคที่ต้องการแปลงเป็น [ถ้าไม่มีให้เชียน No]:"))

if Prefixes_2 == "E" :
    Prefixes_2 = 10**18
if Prefixes_2 == "P" :
    Prefixes_2 = 10**15
if Prefixes_2 == "T" :
    Prefixes_2 = 10**12
if Prefixes_2 == "G" :
    Prefixes_2 = 10**9
if Prefixes_2 == "M" :
    Prefixes_2 = 10**6
if Prefixes_2 == "k" :
    Prefixes_2 = 10**3
if Prefixes_2 == "h" :
    Prefixes_2 = 10**2
if Prefixes_2 == "da" :
    Prefixes_2 = 10**1
if Prefixes_2 == "d" :
    Prefixes_2 = 10**-1
if Prefixes_2 == "c" :
    Prefixes_2 = 10**-2
if Prefixes_2 == "m" :
    Prefixes_2 = 10**-3
if Prefixes_2 == "u" :
    Prefixes_2 = 10**-6
if Prefixes_2 == "n" :
    Prefixes_2 = 10**-9
if Prefixes_2 == "p" :
    Prefixes_2 = 10**-12
if Prefixes_2 == "f" :
    Prefixes_2 = 10**-15
if Prefixes_2 == "a" :
    Prefixes_2 = 10**-18
if Prefixes_2 == "No" :
    Prefixes_2 = 1


result_2 = result/Prefixes_2
    

print(result_2)




