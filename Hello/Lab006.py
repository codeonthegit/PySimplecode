shopping_list = ["Milk", "Bread", "Butter", "Poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-2])

shopping_list.append("Curd")  # Add item in the end
print(shopping_list)
shopping_list.insert(3, "Jam")  # Add item in the middle
print(shopping_list)

shopping_list.extend("Chips", "Salt")  # Add multiple items in the end
print(shopping_list)

shopping_list.remove("Bread")  # Remove item
print(shopping_list)
