N = int(input("So luong ban HV la:"))
i = 0
sum = 0
sum1 = 0
a = 0
while i < N:
    i = i +1
    score = float(input(f"Diem so cua HV {i} la:"))
    if score >= 0 and score <= 10:
        a = a + 1
    else:
        break
    sum = sum + score
if a == 0:
    print("Khong co gia tri nao hop le")
else:
    average = sum/a
    print(f"So lan diem hop le la:{a}")
    print(f"Diem trung binh la:{average}")