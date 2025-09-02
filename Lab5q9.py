'''Your job is to spend money from a piggy bank until there is none left, however, you
can only spend $10 at a time. You will have $100 to start with. Each time you spend
money, you will print the remaining amount of money left in the piggy bank.'''
store = 100
while store != 0:
    n = int(input("Enter 1 if you want to spend money"))
    if n == 1:
        store -= 10
        print('$',store)
    