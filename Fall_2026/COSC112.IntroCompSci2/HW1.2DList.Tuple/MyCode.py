import random
# Task 1(30pts): Regular Matrix with Two-Dimensional List
def sum_matrix(matrix):
    # Calculate and return the sum of all elements in the matrix
    total = 0 
    for row in matrix:
        for element in row:
            total += element
    return total


# Define the 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Output the sum of all elements in the matrix
print(f"Sum of matrix elements: {sum_matrix(matrix)}")

# Task 2(40pts):Jagged Array of Days and Temperatures Using a Loop
# Define the number of days in each month of a non-leap year
days_in_month = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]# fill in the num of days in each month

# Initialize the temperatures list using a loop
temperatures = []

# For each month, generate a list with 'days' number of random temperatures
# Fill in each row with Random temperatures between -10 and 40 degrees Celsius
for days in days_in_month:
    month_temps = []
    for _ in range(days):
        temp = random.randint(-10, 40)
        month_temps.append(temp)
    temperatures.append(month_temps)

# Output both the days in each month and the temperature data
for i in range(12):
    print(f"Month {i+1} has {days_in_month[i]} days, temperatures: {temperatures[i]}")


# Task 3(30pts):Tuple Practice
def min_max(nums):
    # Return a tuple with the minimum and maximum values in the num list
    return (min(nums), max(nums))

# Define the list of numbers
nums = [13, 1, 4, 31, 5, 9, 2, 6, 5, 3, 5]

# Output the tuple containing the min and max values
print(f"Minimum and Maximum values: {min_max(nums)}")
# expected (1, 31)
