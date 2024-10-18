M = int(input("Số bàn: "))
N = int(input("Số chỗ ngồi trong bàn: "))

all = []
for i in range(M):
    table = []
    print(f"Ban so {i+1}: ")
    for j in range(N):
        h = float(input("\tChieu cao cua ban HS: "))
        table.append(h)
    all.append(table)
    
sum = 0
count = 0

for i in range(M):
    for j in range(N):
        h = all[i][j]
        if(h > 0):
            sum = sum + h
            count = count + 1

print(f"Chieu cao trung binh: {sum/count}")
empty = M*N - count 
print(f"So cho trong la: {empty}")