name = input("กรอกชื่อลูกค้า ")
print("ลูกค้าชื่อ :" , name)
price = float(input("ราคาสินค้า :" ))
vat =0.07
tPrice = (price*vat)+price
print("ราคาสินค้า รวมภาษี7%  : ",tPrice)
