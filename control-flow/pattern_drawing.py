# pattern_drawing.py

# Prompt the user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in each column
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
