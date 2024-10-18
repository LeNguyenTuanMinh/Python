N = int(input("So ban duoc khao sat la:"))
a = 0
b = 0
c = 0
d = 0
for i in range (1,N+1):
    y = input(f"Mon kho nhat cua ban {i}: ")
    x = y.upper()
    c1 = x.count("TCC")
    c2 = x.count("THDC")
    c3 = x.count("VLDC")
    c4 = x.count("GT1")
    if c1 == 1:
        a = a + 1
    if c2 == 1:
        b = b + 1
    if c3 == 1:
        c = c + 1
    if c4 == 1:
        d = d + 1
numbers = [a, b, c, d]
max_num = max(numbers)
min_num = min(numbers)
count_max = numbers.count(max_num)
count_min = numbers.count(min_num)
print(f"So mon kho nhat la: {count_max}")
print(f"So mon de nhat la: {count_min}")
    