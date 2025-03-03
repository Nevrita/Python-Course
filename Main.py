def calculate_change(total_bill, amount_paid):  
    if amount_paid < total_bill:  
        return - 1
    change = amount_paid - total_bill  
    if change == 0:  
        return 0
    return change 
total_bill = 2.50  
amount_paid = 4  
change = calculate_change(total_bill, amount_paid)  

if change < 0:  
    print("The payment is insufficient.")  
elif change == 0:  
    print("There will be no changes to return.")  
else:
    print ("The shopkeeper must return Vishal a total of $" + str(change))