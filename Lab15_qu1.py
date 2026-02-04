'''Question 1
A property agency performs the sales of both immovable and movable
properties. Immovable properties consist of land with or without a building.
Movable properties are vehicles.

It wishes to have a computerised system to manage its transactions.

For all properties on its sales list, it needs to store: Property Id, the surname,
first name and address of the owner and the cost of the property.

For immovable properties, it needs to store the location (name of the town
or village), the area of the land, whether it contains a building or not and the
area of the building (if any.

For movable properties, it should store the type (car, lorry, bus), the engine
capacity, model and the make.

(a)Develop a suitable base class (super class) and two suitable subclasses to
represent immovable and movable properties.

(b) Write a main() function that inputs data for five movable properties and
five immovable properties and stores the data in relevant lists.

(c) For each class of properties, the program should calculate the average
cost and display the details of all properties (of the class) which are above
the average cost.'''

class properties():
    def __init__(self,Property_Id, Surname, first_name, address_of_the_owner, cost_of_the_property):
        self.Property_Id = Property_Id
        self.Surname = Surname
        self.first_name = first_name
        self.address_of_the_owner = address_of_the_owner
        self.cost_of_the_property = cost_of_the_property
    
    def display(self):
        print("Property Id = " , self.Property_Id )
        print("The surname = " , self.Surname )
        print("The first name = " , self.first_name )
        print("The address of the owner = " , self.address_of_the_owner )
        print("The cost of the property = " , self.cost_of_the_property )
        
class immovable_properties(properties):
    def __init__(self,Property_Id, Surname, first_name, address_of_the_owner, cost_of_the_property, location, area_of_the_land, building, area_of_the_building = 0):
        super().__init__(Property_Id, Surname, first_name, address_of_the_owner, cost_of_the_property)
        self.location = location
        self.area_of_the_land = area_of_the_land
        self.building = building
        self.area_of_the_building = area_of_the_building
        
    def display(self):
        super().display()
        print("location = " , self.location )
        print("The area of the land = " , self.area_of_the_land )
        print("The building = " , self.building )
        print("The area of the building = " , self.area_of_the_building )
         
class movable_properties(properties):
    def __init__(self,Property_Id, Surname, first_name, address_of_the_owner, cost_of_the_property, type, engine_capacity, model, the_make):
        super().__init__(Property_Id, Surname, first_name, address_of_the_owner, cost_of_the_property)
        self.type = type
        self.engine_capacity = engine_capacity
        self.model = model
        self.the_make = the_make
        
    def display(self):
        super().display()
        print("type = " , self.type )
        print("The engine capacity = " , self.engine_capacity )
        print("The model = " , self.model )
        print("The make = " , self.the_make )
        
immovable_list = []
movable_list = []
Sum_cost_immovable = 0
Sum_cost_movable = 0
for i in range(5):
    #the surname, first name and address of the owner and the cost of the property.
    #location (name of the town or village), the area of the land, whether it contains a building or not and the area of the building (if any
    
    pid = input("\nEnter Property Id= ")
    sname = input("Enter the surname= ")
    fname = input("Enter first name= ")
    addr = input("Enter address of the owner= ")
    cost = int(input("Enter the cost of the property= "))
    Sum_cost_immovable += cost
    loc = input("Enter location (name of the town or village)= ")
    land = int(input("Enter the area of the land= "))
    has_building = (input("Enter whether it contains a building or not(yes or no)= ")).lower()
    if has_building == "yes":
        build_area = int(input("Enter the area of the building= "))
    else:
        build_area = 0 
    i = immovable_properties(pid, sname, fname, addr, cost, loc, land, has_building, build_area)
    immovable_list.append(i)
    
for j in range(5):
    #the type (car, lorry, bus), the engine capacity, model and the make.

    pid = input("\nEnter Property Id= ")
    sname = input("Enter the surname= ")
    fname = input("Enter first name= ")
    addr = input("Enter address of the owner= ")
    cost = int(input("Enter the cost of the property= "))
    Sum_cost_movable += cost
    vtype = input("Enter the type (car, lorry, bus)")
    engine = int(input("Enter the engine capacity= "))
    model = input("Enter the model= ")
    make = input("Enter the make= ")
    j = movable_properties(pid, sname, fname, addr, cost,vtype, engine, model, make)
    movable_list.append(j)

for x in immovable_list:
    if x.cost_of_the_property > (Sum_cost_immovable/5):
        x.display()
        
for z in movable_list:
    if z.cost_of_the_property > (Sum_cost_movable/5):
        z.display()
