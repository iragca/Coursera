"""This module is sample python file for learning PEP8 standards

blablaljl;ajsdf
"""

# Define a function named 'add' that takes two arguments, 'number1' and 'number2'.
# The purpose of this function is to add the two numbers and return the result.
def add(number1, number2):
    """This function adds two (int) numbers.

    Args:
        number1: The first number to add
        number2: The second number to add

    Returns:
        A single int value
    """
    return number1 + number2

# Initialize the constant variable 'NUM1' with the value 4.
# Constants are usually written in uppercase letters to indicate that they should not be changed.
NUM1 = 4

# Initialize the variable 'num2' with the value 5.
# This variable will be used as the second input to the 'add' function.
NUM2 = 5

# Call the 'add' function with 'NUM1' and 'num2' as arguments.
# The result of this addition operation is stored in the variable 'total'.
TOTAL = add(NUM1, NUM2)

# Print a formatted string that displays the sum of 'NUM1' and 'num2'.
# The 'format' method is used to insert the values of 'NUM1', 'num2', and 'total' into the string.
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
