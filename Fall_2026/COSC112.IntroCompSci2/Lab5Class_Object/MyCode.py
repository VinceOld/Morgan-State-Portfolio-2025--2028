class Rectangle:

    # Task1(10pts): Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Task 2(20pts): Method to return the area of Rectangle
    def calculate_area(self):
        return self.length * self.width
    # define Method to return the perimeter of Rectangle
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
        

    # Task 3(10pts): define Mutator methods 
    def set_length(self, new_length):
        self.length = new_length
    

    def set_width(self, new_width):
        self.width = new_width

        


# Task 4(20pts)Test Program

# Create three rectangle objects
# named as r1, r2 and r3
r1 = Rectangle(5,3)
r2 = Rectangle(10,4)
r3 = Rectangle(7,2)

# Print the area of each rectangle
# Print the perimeter of each rectangle
print(f"Rectangle 1 - Area:{r1.calculate_area()}, Perimeter: {r1.calculate_perimeter()}")
print(f"Rectangle 2 - Area:{r2.calculate_area()}, Perimeter: {r2.calculate_perimeter()}")
print(f"Rectangle 3 - Area:{r3.calculate_area()}, Perimeter: {r3.calculate_perimeter()}")
# Modify r3 using mutator methods, give new width and height
r3.set_length(8)
r3.set_width(6)

# Print new area of r3
# print new perimeter of r3
print(f"Modified Rectangle 3 - New Area: {r3.calculate_area()}, New Perimeter: {r3.calculate_perimeter()}")
