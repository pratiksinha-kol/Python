# Coke Machine Simulation
# Amount due is 50 cents
# Accepts only 25, 10, or 5 cent coins
# Outputs amount due after each coin insertion


amount_due = 50
print("Amount Due: ", amount_due)
insert_coin = int(input("Insert Coin: "))

while amount_due > 0:
    if insert_coin in [25, 10, 5]:
        amount_due -= insert_coin
        if amount_due > 0:
            print("Amount Due: ", amount_due)
            insert_coin = int(input("Insert Coin: "))
        elif amount_due == 0:
            print("Change Owed: 0")
        else:
            print("Change Owed: ", abs(amount_due))
    else:
        print("Amount Due: ", amount_due)
        insert_coin = int(input("Insert Coin:"))