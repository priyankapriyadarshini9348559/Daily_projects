#Grocery Store Billing System
print("welcome to D-mart")
cart=[]
while True:
    print("choose what you want")
    print("1. Add Item to Cart")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Generate Bill")
    print("5. Exit")
    choice=input("enter your choice:")
    if choice =="1":
        name=input("enter item name:")
        price=float(input("enter price:"))
        qty=int(input("enter quantity:"))
        cart.append((name,price,qty))
        print("item added!")
        print(cart)
    elif choice=="2":
        print("\n-----------your cart------------")
        if len(cart)==0:
            print("cart is empty")
        else:
            for item in cart:
                name,price,qty=item
                print(f"{name} - rs.{price} x {qty}")