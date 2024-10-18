def getArea(a, b, c):
    p = (a + b + c)/2
    S = p*(p - a)*(p - b)*(p - c )
    S = S**0.5
    return S
a = float(input("Cạnh a của tam giác: "))
b = float(input("Cạnh b của tam giác: "))
c = float(input("Cạnh c của tam giác: "))
S = getArea(a, b, c)
print(f'Diên tích tam giác là: {S}')