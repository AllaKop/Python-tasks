# Program that simulates a basic inventory system.
# Use a dictionary to store items and their corresponding quantities.
# Implement options to add items, view the inventory and update quantities.


inventory = {}

while True:
    choice = int(input("""Please enter your choice 
                          1: Add Item 
                          2: View Inventory
                          3: Update Quantity
                          4: Exit 
                                """))
    if choice == 1:
        product = str(input("Please enter a product "))
        quantity = int(input("Please enter a quantity "))
        inventory.setdefault(product, quantity) 
    elif choice == 2:
        print(inventory)
    elif choice == 3:
        product = str(input("Please enter the product "))
        quantity = int(input("Please enter the new quantity "))
        if product in inventory:
            inventory[product] = quantity
        else:
            raise Exception("The product is not in the inventory")
    elif choice == 4:
        break
    else:
        raise Exception("""Wrong option. Please enter your choice 
                          1: Add Item 
                          2: View Inventory
                          3: Update Quantity
                          4: Exit 
                                """)
