'''Question 2
A private hospital wishes to have a computerised system to manage staff
information. The attributes for staff are name, address, gender and salary.
(a) Implement the class Staff.
(b) Write a main program to input data for one staff named worker1.
(c) Write instruction(s) to display all the data for this one staff (worker1).
(d) Write instructions to update the address and salary of this staff.
(e) Write instruction(s) to display all the data for worker1.

Additional questions:
(f) Add a class variable total_staff to track the total number of staff
members added.
(g) Implement a static method calculate_annual_income that takes the
salary as an argument and returns the annual income for the staff member.
The annual income is calculated by multiplying the salary by 12.
(h) (i) Create a list called staff_list to store multiple Staff objects.
(ii) Write code to input data for 3 staff members and add them to
staff_list.
(iii) Write a loop to display the details of all staff members.
(i) Write a method filter_high_income_staff that takes a list of staff
members and an annual income threshold as arguments. It should return
a list of staff members earning more than this given threshold. Test this
method by displaying the names of staff earning above this threshold.'''

class staff():
    total_staff = 0
    def __init__(self, name, address, gender, salary):
        self.name = name
        self.address = address
        self.gender = gender
        self.salary = salary
        staff.total_staff += 1
    
    def display_data(self):
        print("name = ", self.name)
        print("address = ", self.address)
        print("gender = ", self.gender)
        print("salary = ", self.salary)
    
    def calculate_annual_income(self):
        return self.salary * 12

    @staticmethod
    def filter_high_income_staff(threshold):
        threshold_above = []
        for r in staff_list:
            if r.calculate_annual_income(r.salary) > threshold:
                threshold_above.append(r.name)
        print(threshold_above)

staff_list = []

for i in range(0,3):
    num1 = input("\n name = ")
    num2 = input("address = ")
    num3 = input("gender = ")
    num4 = float(input("salary = ")) 

    worker1 = staff(num1, num2, num3, num4)
    staff_list.append(worker1)

for r in staff_list:
    r.display_data()

staff.filter_high_income_staff(17000)
