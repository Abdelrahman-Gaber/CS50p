'''
    Coke is for 50 cents
    I need to tell the customer the amount due
    Use a while true loop to tell the customer the amount due and allow him to input a number
    my variable which is coke_price holds 50 that I minus from it whatever the user input (only legit inputs)
    After that I check if the amount due is positive still due or negative amount owned
'''

amounts_allowed = [25,10,5]
amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))

    if insert_coin in amounts_allowed:
        amount_due -= insert_coin

print(f"Change Owned: {amount_due}") if amount_due == 0 else print(f"Change Owned :{amount_due * -1}")
