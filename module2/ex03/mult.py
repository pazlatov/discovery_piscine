first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
result = first_number * second_number
print(first_number, "x", second_number, "=", result)
if result > 0:
    print("The result is positive.")
if result < 0:
    print("The result is negative.")
if result == 0:
    print("The result is positive and negative.")