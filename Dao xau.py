import math
x = input("Nhap xau:")
start = input("Ki tu dau:")
next = input("Ki tu tiep theo:")
def cmove(x):
    x1 = x.find(f"{start}")
    x2 = x.find(f"{next}")
    num = abs(x1-x2)
    return num
num = cmove(x)
print(f"Số lần di chuyển từ ký tự start đến ký tự next trong xâu:{num}")

pos = x.find(f"{start}") +1
part1 = x[:pos]
part2 = x[pos:]
new_string = part2 + part1
num1 = cmove(new_string)
print(f"Số lần di chuyển từ ký tự start đến ký tự next trong xâu mới:{num1}")