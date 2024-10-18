x1 = float(input("Toa do x cua diem tren ben trai la:"))
y1 = float(input("Toa do y cua diem tren ben trai la:"))
x2 = float(input("Toa do x cua diem duoi ben phai la:"))
y2 = float(input("Toa do y cua diem duoi ben phai la:"))
import math
d1 = abs(x1-x2)
d2 = abs(y1-y2)
if d1 == d2:
    print("HINH VUONG")
    S = (d1/2)**2*3.14
    print(f"Dien tich duong tron noi tiep la: {S}")
else:
    print("HINH CHU NHAT")
    a = d1**2+d2**2
    R = (a**0.5)/2
    S = 3.14*R**2
    print(f"Dien tich duong tron noi tiep la: {S}")