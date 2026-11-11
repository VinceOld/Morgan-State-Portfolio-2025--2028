#Task1 (25 pts)Returns the reversed string using recursion.
def reverse_string(s):
    if len(s)<= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
    
print(f'reverse_string("hello") returns: "{reverse_string("hello")}"')
print(f'reverse_string("racecar") returns: "{reverse_string("racecar")}"')


# Task2(25pts)Returns the GCD of a and b using recursion.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b , a % b)
    
print(f"gcd(48, 18) returna: {gcd(48, 18)}")
print(f"gcd(101, 10) returns: {gcd(101, 10)}")
print(f"gcd(23, 0) returns: {gcd(23, 0)}")
