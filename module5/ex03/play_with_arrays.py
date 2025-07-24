numbers = [1, 19, 45, -852, 55, -8, 19]
print(f"Original array: {numbers}")
new_numbers = set()
for number in numbers:
    if number > 5:
        new_numbers.add(number + 2)
print(f"New array: {new_numbers}")