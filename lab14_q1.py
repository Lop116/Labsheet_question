'''Question 1
A supermarket wishes to have a computerised system to manage its items.
For each item, it wishes to store the following information: Item Code, Item
Description, Quantity in stock, Unit Buying Price and Unit Selling Price.
(a) Implement the class Item.
(i) Implement a method display_data to display all the information
for an item.
(ii) Implement a method calculate_profit to calculate the profit on one
item.
Profit = Unit Selling Price – Unit Buying Price

(b) Write a main program to input data for one item named product1.
(c) Write instruction(s) to display all the data for this one item (product1).
(d) Write instruction(s) to compute and display the profit on this item.

Additional questions:
(e)Add a class variable total_items to keep track of the total number of items
added to the system.
(f) Implement a static method calculate_total_profit that takes the total
quantity in stock, unit buying price, and unit selling price as parameters
and returns the total (possible) profit for that item.
(g) (i) Create a list called inventory to store multiple Item objects.
(ii) Write code to input data for 3 items and add them to the inventory.
(iii) Write a loop to display the details of all items in the inventory using
the display_data method.
(iv) Write another loop to compute and display the total (possible)
profit for all items in the inventory.'''

class Item:
    total_items = 0
    def __init__(self, Item_Code, Item_Description, Quantity_in_stock, Unit_Buying_Price, Unit_Selling_Price):
        self.Item_Code = Item_Code
        self.Item_Description = Item_Description
        self.Quantity_in_stock = Quantity_in_stock
        self.Unit_Buying_Price = Unit_Buying_Price
        self.Unit_Selling_Price = Unit_Selling_Price
        Item.total_items += 1

    def display_data(self):
        print("Item_Code = ", self.Item_Code)
        print("Item_Description = ", self.Item_Description)
        print("Quantity_in_stock = ", self.Quantity_in_stock)
        print("Unit_Buying_Price = ", self.Unit_Buying_Price)
        print("Unit_Selling_Price = ", self.Unit_Selling_Price)
        
    def calculate_profit(self):
        return self.Unit_Selling_Price - self.Unit_Buying_Price
    
    @staticmethod
    def calculate_total_profit(Quantity_in_stock,Unit_Buying_Price,Unit_Selling_Price):
        return Quantity_in_stock * (Unit_Selling_Price-Unit_Buying_Price)
        
inventory = []
for i in range(0,3):
    num1 = input("\n Item code = ")
    num2 = input("Item Description = ")
    num3 = int(input("Quantity in stock = ")) 
    num4 = float(input("Unit Buying Price = ")) 
    num5 = float(input("Unit Selling Price = ")) 
    product1 = Item(num1, num2, num3, num4, num5)
    inventory.append(product1)
    
total = 0 
for r in inventory:
    r.display_data()
    

for j in inventory:
    total += j.calculate_total_profit(j.Quantity_in_stock,j.Unit_Buying_Price,j.Unit_Selling_Price)

print("total (possible) profit for all items in the inventory =" ,total)
