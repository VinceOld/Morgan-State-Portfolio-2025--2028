Task 1(30pts): Regular Matrix with Two-Dimensional List
Write a Python program to create a 2D matrix representing a grid, and calculate the sum of all the elements.

Instructions:

Define a 3x3 matrix (2D list) with the following values:


[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

Write a Python function sum_matrix(matrix) that calculates and returns the sum of all the elements in the matrix.

Output the sum of all elements in the matrix.

Task2(40pts)Jagged Array of Days and Temperatures Using a Loop
Create a jagged 2D array where each row represents a month in a non-leap year. Each row will contain the number of days for that month, and the corresponding temperatures for each day will be initialized to 0 using a loop.

Instructions

Define a list days_in_month that contains the number of days in each month of a non-leap year, as follows:

January: 31 days

February: 28 days

March: 31 days

April: 30 days

May: 31 days

June: 30 days

July: 31 days

August: 31 days

September: 30 days

October: 31 days

November: 30 days

December: 31 days

Use a loop to dynamically create the temperatures list. Each element in this list will represent a month, and each month will contain another list with the number of days in that month. Initialize the daily temperatures using random values. Use Python's random module to generate random temperatures within a realistic range (e.g., between -10 and 40 degrees Celsius).

After constructing the temperatures list, output:

The number of days for each month (from days_in_month).

The corresponding list of randomly generated temperatures for each month.

Note: Ensure that the temperature for each day of the month is generated randomly and printed along with the month's name and the number of days.

Example output:

Month 1 has 31 days, temperatures: [15, 22, 10, 18, 25, 29, 30, 35, 20, 16, 19, 26, 28, 30, 22, 31, 25, 18, 14, 21, 30, 24, 22, 17, 23, 29, 31, 26, 24, 27, 35]
Month 2 has 28 days, temperatures: [2, 6, 13, 19, 21, 18, 17, 4, 12, 20, 28, 26, 15, 10, 19, 21, 5, 11, 8, 6, 9, 3, 17, 16, 11, 22, 27, 13]
Month 3 has 31 days, temperatures: [24, 16, 29, 18, 20, 30, 32, 28, 17, 25, 33, 27, 16, 26, 18, 31, 21, 34, 30, 32, 19, 35, 22, 30, 28, 27, 29, 32, 19, 24, 21]
...
# should list all 12 months in your output


Task 3(30pts):Tuple Practice

Write a Python program to practice using tuples and demonstrate their typical use in returning multiple values from a function.

Instructions:

Write a Python function min_max(nums) that takes a list of integers and returns a tuple containing the minimum and maximum values in the list.

The function should return a tuple with two elements: the first being the minimum value, and the second being the maximum value.

Output the tuple with the minimum and maximum values.

Example Output:


nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# min_max(nums) will return (1, 9)
