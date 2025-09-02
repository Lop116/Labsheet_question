#Write a program to accept a number from a user and calculate the sum of all numbers
#from 1 to a given number. For example, if the user entered 10 the output should be 55
#(1+2+3+4+5+6+7+8+9+10).
n = int(input("Enter the number: "))
value = ''
sum = 0
for i in range(1,n):
    print(i)
    sum = sum + i
    print(sum)
    if sum == 1:
        print('first')
        value = str(i)
        print(value)
    else:
        value =value+' + '+str(i)
        print(value)
print(str(sum)+'('+ value +')')
