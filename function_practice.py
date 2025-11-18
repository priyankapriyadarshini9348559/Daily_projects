print("welcome to the grocery shop")

def greet():
    name = input("enter your name: ")
    print(f"hello {name} how can we help you !!")

def item():
    dct = {"rice": 120, 'wheat': 175, 'maggi': 250, 'vegetable': 110}
    return dct

def add_item():
    dct = item()
    total_bill = 0

    while True:
        item_name = input("enter the item you want to buy? ").lower()

        if item_name in dct:
            quantity = int(input("enter how much quantity you want: "))
            price = dct[item_name]
            total = price * quantity

            print(f"{item_name} price {price} * {quantity} = {total}")

            total_bill += total
            print("Your total amount:", total_bill)

            again = input("Do you want to buy another item? (yes/no): ").lower()
            if again != "yes":
                break
        else:
            print("Item not found!")

    return total_bill   

def bill(total_amount):
    choice = input("How do you want to pay the bill? (online/offline): ").lower()

    if choice == 'online':
        print("Thank you for paying online. Please collect the bill.")
    else:
        print("Pay the cash.")
        cash = int(input("enter your cash: "))

        if cash > total_amount:
            balance = cash - total_amount
            print(f"Extra money received. Return ₹{balance} to customer.")
        elif cash == total_amount:
            print("Exact amount received. Thank you!")
        else:
            pending = total_amount - cash
            print(f"Cash is less! Customer still needs to pay ₹{pending}.")

greet()
total = add_item()   
bill(total)
