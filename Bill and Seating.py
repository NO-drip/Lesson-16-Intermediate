def total_bill (bill_amount, tip_perc):
    total_amount = bill_amount * (1 + 0.01 * tip_perc)
    total_amount = round(total_amount,2)
    print(f"Your total amount is ${total_amount} ")
    return total_amount

total_bill(150,20)
def seating_arrangements(guests):
    """This is to calculate the number of seating arrangements for guests"""
    if guests == 0 or guests == 1:
        return (1)
    else:
        return guests * seating_arrangements(guests - 1)

print (seating_arrangements.__doc__)

print ("Seating arrangements for guests:", seating_arrangements(1))
print("Seating arrangements for guests:", seating_arrangements(2))
print("Seating arrangements for guests:", seating_arrangements(5))
print("Seating arrangements for guests:", seating_arrangements(9))

