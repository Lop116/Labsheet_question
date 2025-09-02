'''Write a program that uses a while loop to determine how long it takes for an investment
to double at a given interest rate. The input will be an annualized interest rate, and the
output is the number of years it takes an investment to double.
Note: the amount of the initial investment does not matter; you can use MUR 100.'''
n = float(input())
b = 100
sum = 100.0
i = 0
while sum < b*2:
    i+=1
    sum = sum + (sum*n)
    print(sum)
print(i)