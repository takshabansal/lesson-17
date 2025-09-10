def total_calc(bill_amount,tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print(f"Please pay money ${total}")
    return total
print("\nWelcome to the Codingal Restraunt")
def ordering():
    print("\nWhat would you like to have:")
    print("a.Pizza(100$)")
    print("b.Burger(75$)")
    print("c.Garlic Bread(60$)")
    print("d.French fries(50$)")
ordering()
choice=str(input("Please enter choice letter:"))
quantity=int(input("Please tell the quantity of item"))
print("Hope the meal was good")
tip=int(input("Would you like to give a tip?:, If yes please enter the amount percentage:"))
total_bill = 0
if choice=="a":
    total_bill = total_calc(100*quantity,tip)
elif choice=="b":
    total_bill = total_calc(75*quantity,tip)
elif choice=="c":
    total_bill = total_calc(60*quantity,tip)
elif choice=="d":
    total_bill = total_calc(50*quantity,tip)

def calculate_due_amount():
    
    total_paid = 0
    while True:
        payment = float(input("Enter bill/coin: "))
        if payment <= 0:
            print("Invalid bill/coin. Please enter a positive amount.")
            continue
        total_paid += payment
        if total_paid >=total_bill:
            break 
    due=total_bill-total_paid
    return due  
due_amount = calculate_due_amount()
print(f"Remaining due amount: {due_amount}")
if due_amount<=0:
    due_amount=0-due_amount
    print("Here is your money Sir/Ma'am: ",due_amount)