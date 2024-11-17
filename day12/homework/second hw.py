price = int(input("enter your price"))

if price == 50: 
    print("you have sale 10%")
    sale = price - 10
    print(sale)
elif price==20 or 50:
    print("you have 5% sale")
    sale = price - 5
    print(sale)

