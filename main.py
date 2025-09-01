def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

# Example usage
num1 = 5
num2 = 3
result = add_numbers(num1, num2)
print(f"{num1} + {num2} = {result}")

# You can also get input from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
sum_result = add_numbers(first_number, second_number)
print(f"The sum of {first_number} and {second_number} is {sum_result}")