#exceptation practice
print("----- Start of the program -----")
try:
    a = int(input("\n Enter the num1"))
    b = int(input("\n Enter the num2"))
    c = a / b
    print("Result Div is", c)
except Exception as e:
    print(e)
    print("Please enter integer!")

print("---- End of the program ----")