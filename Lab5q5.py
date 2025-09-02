#Finding the sum of the 50 even numbers using the while loop
n= 0
sum = 0
i = 0
while n<51:
    print(i,' ',n)
    if i%2 ==0:
        sum = sum + i
        n+=1
    i += 1
print(sum)