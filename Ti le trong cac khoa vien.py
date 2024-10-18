import math
N = int(input("So Khoa/Vien/Truong co sinh vien nam nhat nam hoc 2024-2025:"))
minE = 100000
maxp = 0
min1 = 100000
for i in range (N):
    name = input("Ten Khoa/Vien/Truong:")
    b = int(input("So SV nam:"))
    g = int(input("So SV nu:"))
    p = int(input("So ban duoc mien the duc:"))
    t = int(input("So ban duoc mien mon triet hoc:"))
    e = int(input("So ban duoc mien mon Tieng Anh:"))
    percent = (t+p)/(b+g)#cau b
    o = b/g
    y = abs(1-o)
    if minE > e:#cau a
        minE = e 
        name1 = name
    if maxp < percent:
        maxp = percent
        name2 = name
    if min1 > y:#cau c
        min1 = y
        name3 = name
        count = 1
    elif min1 == y:
        count = count + 1
print(f"Truong co so SV mien Tieng Anh be nhat la:{name1}")
print(f"Truong co ti le SV mien cac mon phu cao nhat la:{name2}")
if count == 1:
    print(f"Truong co ti le nam nu can bang nhat la:{name3}")
else:
    print(f"So truong co ti le nam nu can bang nhat la:{count}")