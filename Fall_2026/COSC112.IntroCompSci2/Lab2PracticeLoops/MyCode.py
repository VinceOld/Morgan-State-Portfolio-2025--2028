#Task1(25 pts): Nested Loops - Pattern Printing
def print_pattern():
    n = int(input("Enter a number (3-10):  "))
# Questioning using 'while' loop
    while n < 3 or n > 10:
        print("Invalid input. Please enter a number between 3 and 10.")
        n = int(input("Enter a number(3-10): "))
    
# Pattern for nested for loops
    for i in range(1,  n +1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
   
# test your function 1 with examples
print_pattern()
print_pattern()



# Task2: While Loop with Validation and For Loop (25 pts)

def sum_even_numbers():
    
    x = int(input("Enter a number(5-20):  "))
    while x < 5 or x > 20:
        print("Invalid input. Please enter anumber between 5 and 20.")
        x = int(input("Enter a number (5-20): "))

    total = 0

    for i in range(1, x+1):
        total = total + (2 * i)
    
    print ("the sum of the first", x, "even numbers is", total)
     

# Test your function 2 with at least 3 examples
sum_even_numbers()
sum_even_numbers()
sum_even_numbers()
