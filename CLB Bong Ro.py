N = int(input("So luong ban trong CLB bong ro la:"))
Hmin = 1.6
Hmax = 1.99
H = 1.7
count = 0

for i in range (1, N+1):
    h = float(input(f"Diem so cua HV {i} la:"))
    if h >= Hmin and h <= Hmax:
        if h > H:
            count = count + 1
    else:
        pass
print(f"So ban cao tren 1.7m la:{count}")