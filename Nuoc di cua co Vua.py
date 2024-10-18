hang1 = str(input("Nhap chi so hang ban dau:"))
cot1 = int(input("Nhap chi so cot ban dau:"))
loai = str(input("Nhap loai quan co:"))
hang2 = str(input("Nhap chi so hang luc sau:"))
cot2 = int(input("Nhap chi so cot luc sau:"))
if loai == "P": #con tot
    if hang1 == "B":
        if hang2 == "C" or hang2 == "D":
            print(True)
        else:
            print(False)
    else:
        if ord(hang2) == ord(hang1) + 1:
            if cot1 == cot2:
                print(True)
            else:
                print(False)
elif loai == "C": #con xe
    if hang1 != hang2 and cot1 == cot2:
        print(True)
    else:
        if hang1 == hang2 and cot1 != cot2:
           print(True)
        else:
           print(False)
elif loai == "B": #con tuong
    if abs(ord(hang1) - ord(hang2)) == abs(cot1 - cot2):
        print(True)
    else:
        print(False)
elif loai == "Q": #con hau
    if abs(ord(hang1) - ord(hang2)) == abs(cot1 - cot2):
        print(True)
    else:
        if hang1 != hang2 and cot1 == cot2:
         print(True)
        else:
         if hang1 == hang2 and cot1 != cot2:
           print(True)
         else:
           print(False)
elif loai == "V": #con Vua
    if abs(ord(hang1) - ord(hang2)) == 1 and abs(cot1 - cot2) == 1:
        print(True)
    else:
        if abs(ord(hang1) - ord(hang2)) == 1 and cot1 == cot2:
         print(True)
        else:
         if hang1 == hang2 and abs(cot1 - cot2) == 1:
           print(True)
         else:
           print(False)
elif loai == "K":
    if abs(ord(hang1) - ord(hang2)) == 2 and abs(cot1 - cot2) == 1 or abs(cot1 - cot2) == 2 and abs(ord(hang1) - ord(hang2)) == 1:
        print(True)
    else:
        print(False)
        