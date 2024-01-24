import math

radius = float(input("Enter radius: "))
area = math.pi * radius**2
print("Area: ", round(area,2))

circumference = 2 * math.pi * radius
print("Circumference: ", round(circumference,2))