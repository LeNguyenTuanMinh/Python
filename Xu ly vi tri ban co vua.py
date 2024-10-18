lst = [ "CR1A", "VR1D", "CR2C", "KR2G", "PB3C", "QR3E", "PB5A", "QB6F", "VB7C"]
cr = 0
cb = 0
cpr = 0
cpb = 0
ckr = 0
ckb = 0
cer = 0 
ceb = 0
for xyzt in lst:
    x = xyzt[:1]
    y = xyzt[1:2]
    z = xyzt[2:3]
    t = xyzt[3:4]
    if y == "R":
        cr = cr + 1
        if x == "P":
            cpr = cpr + 1
        if x == "V":
            ckr = ckr + 1
        if x == "C" or x == "B" or x == "K" or x == "Q":
            cer = cer + 1
    if y == "B":
        cb = cb + 1
        if x == "P":
            cpb = cpb + 1
        if x == "V":
            ckb = ckb + 1
        if x == "C" or x == "B" or x == "K" or x == "Q":
            ceb = ceb + 1
d = abs(cr-cb)
if cr > cb:
    print("R>B")
    print(f"Chenh lech so quan cua moi phe la: {d}")
if cr < cb:
    print("R<B")
    print(f"Chenh lech so quan cua moi phe la: {d}")
if cr == cb:
    print("R=B")
if cpr > 8:
    print("So quan tot cua phe do vuot qua 8") #quan tot
else:
    print("So quan tot cua phe do khong vuot qua 8")
if cpb > 8:
    print("So quan tot cua phe den vuot qua 8") #quan tot 
else:
    print("So quan tot cua phe den khong vuot qua 8")
if ckr == 1:
    print("Quan vua phe do bang 1")
if ckb == 1:
    print("Quan vua phe den bang 1")
if cer > 14:
    print("Tong so xe tuong ma hau vuot qua 14")
else:
    print(f"So quan xe tuong ma hau la: {cer}")
if ceb > 14:
    print("Tong so xe tuong ma hau vuot qua 14")
else:
    print(f"So quan xe tuong ma hau la: {ceb}")