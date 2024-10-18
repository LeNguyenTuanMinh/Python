def getCost(price, num, vat, discount):
    cost = num *(price - discount)*(1 + vat/100)
    return cost
num = int(input("Số sản phẩm: "))
price = int(input("Đơn giá sản phẩm: "))
discount = int(input("Số sản phẩm: "))
vat = float(input("Thuế suất VAT Theo % là: "))
print(f'Số tiền cần trả: {S}')