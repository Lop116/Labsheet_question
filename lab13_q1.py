#Question 1
#A supermarket wishes to have a computerised system to manage its items.
#For each item, it wishes to store the following information: Item Code, Item
#Description, Quantity in stock, Unit Buying Price and Unit Selling Price.
#(a) Implement the class Item.
        #(i) Implement a method display_data to display all the information for an item.
        #(ii) Implement a method calculate_profit to calculate the profit on one item.
             #Profit = Unit Selling Price – Unit Buying Price

#(b) Write a main program to input data for one item named product1.
#(c) Write instruction(s) to display all the data for this one item (product1).
#(d) Write instruction(s) to compute and display the profit on this item.

class Item:
    def __init__(self, Item_Code, Item_Description, Quantity_in_stock, Unit_Buying_Price, Unit_Selling_Price):
        self.Item_Code = Item_Code
        self.Item_Description = Item_Description
        self.Quantity_in_stock = Quantity_in_stock
        self.Unit_Buying_Price = Unit_Buying_Price
        self.Unit_Selling_Price = Unit_Selling_Price

    def display_data(self):
        print("Item_Code = ", self.Item_Code)
        print("Item_Description = ", self.Item_Description)
        print("Quantity_in_stock = ", self.Quantity_in_stock)
        print("Unit_Buying_Price = ", self.Unit_Buying_Price)
        print("Unit_Selling_Price = ", self.Unit_Selling_Price)
        
    def calculate_profit(self):
        return self.Unit_Selling_Price - self.Unit_Buying_Price
    

 
num1 = input("Item code = ")
num2 = input("Item Description = ")
num3 = int(input("Quantity in stock = ")) 
num4 = float(input("Unit Buying Price = ")) 
num5 = float(input("Unit Selling Price = ")) 

product1 = Item(num1, num2, num3, num4, num5)

product1.display_data()
print("profit =" ,product1.calculate_profit())
