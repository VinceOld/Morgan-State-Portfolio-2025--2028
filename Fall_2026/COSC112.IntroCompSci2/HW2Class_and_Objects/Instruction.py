Classes Implementation and Inheritance
Implementing 3D Shapes Using Classes and Inheritance
Due: Nov 4th, 11:59pm

Task 1(20pts): Creating the Base Class
Create a class called Shape3D that serves as the parent class for all 3D shapes.

Attributes (use encapsulation: make them private with a single underscore _): 

_name (string): Name of the shape.

Methods: 

get_name(): Returns the name of the shape.

volume(): A placeholder method (return NotImplementedError).

surface_area(): A placeholder method (return NotImplementedError).

__str__(): Returns a formatted string with all properties.

Task 2(45pts): Implementing Subclasses
1. Sphere
Attribute: _radius (float)

Methods: 

volume(): Returns the volume using the formula

V
=
3
4
π
R
3
V= 
4
3
​
 πR 
3
 



surface_area(): Returns the surface area using the formula 

A
=
4
π
R
2
A=4πR 
2
 

       __str__(): Returns a formatted string with all properties.

2. Cube
Attribute: _side_length (float)

Methods: 

volume(): Returns the volume using the formula V=s3

surface_area(): Returns the surface area using the formula A=6s2

__str__(): Returns a formatted string with all properties.

3. Cylinder
Attributes: _radius (float), _height (float)

Methods: 

volume(): V=πr2h

surface_area(): A=2πrh+2πr2

__str__(): Returns a formatted string with all properties.

Task 3(15pts): Testing the Classes
Write a test program that:

Creates objects of Sphere, Cube, and Cylinder.

Prints their names, volumes, and surface areas.

Expected output:

Sphere (radius=3)
  Volume: 63.62
  Surface Area: 113.10

Cube (side length=4)
  Volume: 64.00
  Surface Area: 96.00

Cylinder (radius=2, height=5)
  Volume: 62.83
  Surface Area: 87.96
