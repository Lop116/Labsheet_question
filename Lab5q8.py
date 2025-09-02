'''To calculate x to power n, (where n is a positive integer), we can use a loop that
multiplies x by itself n times. Write the code that allows for the input of values for x
and n and calculates and displays xn
.'''

sum = int(input())
n = int(input())
if n ==0:
    print(1)
else:
    for i in range(0,n-1):
        sum =sum * sum
    print(sum)