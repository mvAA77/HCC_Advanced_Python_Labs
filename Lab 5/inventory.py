### Tanya Kadiyala
### CMSY-257-300
### Lab 5
### Problem 3

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    
    print("\n" + "="*50)
    print(f"{'Item':<20} {'Quantity':<10} {'Price':<10} {'Value':<10}")
    print("="*50)
    
    total_value = 0
    for item in inventory:
        name, qty, price = item
        value = qty * price
        total_value += value
        print(f"{name:<20} {qty:<10} ${price:<9.2f} ${value:<9.2f}")
    
    print("="*50)
    print(f"{'TOTAL VALUE':<40} ${total_value:.2f}")
    print("="*50)

def add_item(inventory):
    print("\n--- Add New Item ---")
    name = input("Enter item name: ").strip()
    
    try:
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: $"))
    except ValueError:
        print("Error: Quantity must be integer, price must be number.")
        return inventory
    
    for item in inventory:
        if item[0].lower() == name.lower():
            update = input(f"Item '{name}' already exists. Update instead? (y/n): ")
            if update.lower() == 'y':
                item[1] = qty
                item[2] = price
                print(f"Updated {name}")
            return inventory
    
    inventory.append([name, qty, price])
    print(f"Added {name} to inventory")
    return inventory

def update_quantity(inventory):
    """Update quantity of existing item"""
    if not inventory:
        print("Inventory is empty. Add items first.")
        return
    
    print("\n--- Update Quantity ---")
    search_name = input("Enter item name to update: ").strip().lower()
    
    for item in inventory:
        if item[0].lower() == search_name:
            try:
                new_qty = int(input(f"Enter new quantity for {item[0]}: "))
                item[1] = new_qty
                print(f"Updated {item[0]} quantity to {new_qty}")
                return
            except ValueError:
                print("Error: Quantity must be an integer.")
                return
    
    print(f"Item '{search_name}' not found in inventory.")

def main():
    print("=== Inventory Tracker ===")
    inventory = []
    
    print("Please enter at least 5 items for your inventory:")
    while len(inventory) < 5:
        inventory = add_item(inventory)
    
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Display Inventory")
        print("2. Add New Item")
        print("3. Update Quantity")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            inventory = add_item(inventory)
        elif choice == '3':
            inventory = update_quantity(inventory)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()