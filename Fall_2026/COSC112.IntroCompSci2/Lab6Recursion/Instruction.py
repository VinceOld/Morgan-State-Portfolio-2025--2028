Task 1(25pts): Reverse a String Using Recursion
Instructions:
Define a recursive function reverse_string(s) that:

Takes a string s as input.

Returns the reverse of the string.


Example Output:
reverse_string("hello") should return "olleh".

reverse_string("racecar") should return "racecar" (a palindrome remains the same).

Task 2(25pts): Find the Greatest Common Divisor (GCD) Using Recursion
Instructions:
Define a recursive function gcd(a, b) that:

Takes two positive integers a and b as input.

Returns the greatest common divisor of a and b.

Use the following recursive approach (Euclidean Algorithm) to solve the problem:

Base case: If b=0, return a as the GCD.

Recursive case: If b>0, return gcd(b, a % b).

Example Output:
gcd(48, 18) should return 6.

gcd(101, 10) should return 1.

gcd(23, 0) should return 23.
