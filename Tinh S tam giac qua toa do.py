import math 
xA = float(input("Toa do x cua dinh A: "))
yA = float(input("Toa do y cua dinh A: "))

xB = float(input("Toa do x cua dinh B: "))
yB = float(input("Toa do y cua dinh B: "))

c = math.sqrt((xA - xB)**2 + (yA - yB)**2)

while(True):
    xC = float(input("Toa do x cua dinh C: "))
    yC = float(input("Toa do y cua dinh C: "))
    a = math.sqrt((xC - xB)**2 + (yC - yB)**2)
    b = math.sqrt((xC - xA)**2 + (yC - yA)**2)
    if a < b + c and c < a + b and b < a + c:
        p = (a + b + c)/2
        S = math.sqrt(p*(p - a)*(p - b)*(p - c))
        print(S)
        break
    else:
        print("Can nhap lai xC, yC")