N = int(input("Số ngày theo dõi lượng khách ra vào siêu thị: "))
M = int(input("Số lượng người trùng ra vào siêu thị trong cả năm nay: "))


def getVariance(n):
    ps1 = ((M - n)**2 / N)**0.5
    ps = ((ps1*(i-1)+(M-customer)**2)/i)**0.5
    return ps

for i in range(1,N+1):
    customer = int(input(f"Số người vào siêu thị trong ngày {i}: "))
    ps = getVariance(customer)
    UCL = M + ps
    LCL = M + ps

    if customer > UCL: print("Đông khách")
    elif customer < LCL: print("Ít khách")
    else: print("Bình thường")