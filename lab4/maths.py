import math

#1
degree = int(input("Input degree: "))
radian=float((degree/180)*math.pi)
print("Output radian:", radian)

#2
def trapezoid_area(height, base1, base2):
	return 0.5 * (base1 + base2) * height

height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))

area = trapezoid_area(height, base1, base2)
print("Expected Output:", area)

#3
def regular_polygon_area(n, side_length):
	return (n * side_length ** 2) / (4 * math.tan(math.pi / n))

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = regular_polygon_area(num_sides, side_length)

print("The area of the polygon is:", area)

#4
base = int(input("Length of base: "))
height = int(input("Length of base: "))
input("Expected output: ", base * height)