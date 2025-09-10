def total_calc(bill_amount,tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print(f"Please pay money ${total}")
    return total

def calculate_due_amount(total_bill):
    
    total_paid = 0
    while True:
        payment =input("Enter bill/coin: ")
        if is_number(payment, "Sorry, we didn't get your note/coin correctly") == False:
            continue
        payment=float(payment)
        if payment <= 0:
            print("Invalid bill/coin. Please enter a positive amount.")
            continue
        total_paid += payment
        if total_paid >=total_bill:
            break 
    due=total_bill-total_paid
    return due  

def ordering():
    print("\nWhat would you like to have:")
    print("1.Pizza(100$)")
    print("2.Burger(75$)")
    print("3.Garlic Bread(60$)")
    print("4.French fries(50$)")

def is_number(s, msg):
    try:
        float(s)
        return True
    except ValueError:
        print(msg)
        return False

def main():
    print("\nWelcome to the Codingal Restraunt")

    ordering()
    choice=input("Please enter choice number:")
    if is_number(choice, "Sorry, we didn't get your choice correctly") == False:
        return
    choice = int(choice)
    if choice < 0 or choice > 4:
        print("Sorry, we didn't get your choice correctly")
        return
    
    quantity=input("Please tell the quantity of item:")
    if is_number(quantity, "Sorry, we didn't get your quantity correctly") == False:
        return
    quantity=float(quantity)
    print("Hope the meal was good")
    tip=(input("Would you like to give a tip?:, If yes please enter the amount percentage:"))
    if is_number(tip, "Sorry, we didn't get your tip percentage correctly") == False:
        return
    tip=float(tip)
    total_bill = 0
    if choice==1:
        total_bill = total_calc(100*quantity,tip)
    elif choice==2:
        total_bill = total_calc(75*quantity,tip)
    elif choice==3:
        total_bill = total_calc(60*quantity,tip)
    elif choice==4:
        total_bill = total_calc(50*quantity,tip)


    due_amount = calculate_due_amount(total_bill)
    print(f"Remaining due amount: {due_amount}")
    if due_amount<=0:
        due_amount=0-due_amount
        print("Here is your change Sir/Ma'am: ",due_amount)

main()