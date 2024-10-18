N = int(input("So cay co tren doan duong Ta Quang Buu la:"))
H = []
R = []
Hmax = float(input("Chieu cao toi da cua cay la:"))
for i in range (1,N+1):
    h = float(input(f"Chieu cao cua cay so {i} la:"))
    r = int(input(f"Loai re cua cay so {i} la:"))
    H.append(h)
    R.append(r)
file = open('trees.txt', 'w')
for i in range(len(H)):
    if H[i] > Hmax:
        if R[i] == 0:#re chum
          H[i]=0
        else:
          H[i]=Hmax
    file.writelines(f"{H[i]}\n")
file.close()
