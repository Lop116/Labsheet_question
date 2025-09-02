#Create a program that allows the user to guess a secret number between 1 and 100. The
# program should keep prompting the user until they guess the correct number.
import random
a = int(random.randint(1,100))
print(a)
n = int(input())
while n != a:
    print('Wrong')
    n = int(input())
print('Right')