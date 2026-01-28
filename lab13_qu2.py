#Question 2
#A private hospital wishes to have a computerised system to manage staff
#information. The attributes for staff are name, address, gender and salary.
#(a) Implement the class Staff.
#(b) Write a main program to input data for one staff named worker1.
#(c) Write instruction(s) to display all the data for this one staff (worker1).
#(d) Write instructions to update the address and salary of this staff.
#(e) Write instruction(s) to display all the data for worker1.

class staff():
    def __init__(self, name, address, gender, salary):
        self.name = name
        self.address = address
        self.gender = gender
        self.salary = salary
    
    def display_data(self):
        print("name = ", self.name)
        print("address = ", self.address)
        print("gender = ", self.gender)
        print("salary = ", self.salary)
    
    
num1 = input("name = ")
num2 = input("address = ")
num3 = input("gender = ")
num4 = float(input("salary = ")) 

worker1 = staff(num1, num2, num3, num4)
worker1.display_data()

num2 = input("address = ")
num4 = float(input("salary = ")) 
worker1.address = num2
worker1.salary = num4

worker1.display_data()
