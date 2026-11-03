import math

# Base class
class Shape3D:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def volume(self):
        return NotImplementedError
    
    def surface_area(self):
        return NotImplementedError
    
    def __str__(self):
        return f"Shape: {self._name}"
   

# Sphere class
class Sphere(Shape3D):
    def __init__(self, radius):
        super().__init__("Sphere")
        self._radius = radius

    def volume(self):
        return(3/4) * math.pi * (self._radius ** 3)
    
    def surface_area(self):
        return 4 * math.pi * (self._radius ** 2)

    def __str__(self):
        return f"Sphere: radius = {self._radius}"
    
# Cube class
class Cube(Shape3D):
    def __init__(self, side_length):
        super().__init__("Cube")
        self._side_length = side_length
    
    def volume(self):
        return self._side_length ** 3

    def surface_area(self):
        return 6 * (self._side_length ** 2)

    def __str__(self):
        return f"Cube: side_length = {self._side_length}"
    
# Cylinder class
class Cylinder(Shape3D):
    def __init__(self, radius, height):
        super().__init__("Cylinder")
        self._radius = radius
        self._height = height
    
    def volume(self):
        return math.pi * (self._radius ** 2) * self._height

    def surface_area(self):
        return (2 * math.pi * self._radius * self._height) + (2 * math.pi * (self._radius ** 2))

    def __str__(self):
        return f"Cylinder: radius = {self._radius}, height = {self._height}"
   

# Testing the 3D shape classes
# Prints their names, volumes, and surface areas as expected output.

sphere_obj = Sphere(3)
cube_obj = Cube(4)
cylinder_obj = Cylinder(2, 5)

print(sphere_obj)
print(f" Volume: {sphere_obj.volume():.2f}")
print(f" Surface Area: {sphere_obj.surface_area():.2f}")

print(cube_obj)
print(f" Volume: {cube_obj.volume():.2f}")
print(f" Surface Area: {cube_obj.surface_area():.2f}")

print(cylinder_obj)
print(f" Volume: {cylinder_obj.volume():.2f}")
print(f" Surface Area: {cylinder_obj.surface_area():.2f}")
