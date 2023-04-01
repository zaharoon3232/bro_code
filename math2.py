import math

print(math.pi)
print(math.e)

result = math.sqrt(9)
print(result)

result = math.ceil(3.1)
print(result)

result = math.floor(3.9)
print(result)

##Circumference of a circle
radius = float(input("Enter the radius of circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is : {round(circumference,2)}cm")


##Area of the circle A = pi * radius^2
radius = float(input("Enter the radius of circle: "))

area = math.pi * pow(radius,2)

print(f"The area of the circle is: {round(area,2)}cm^2")


##hypotenuse calculator

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b,2))
print(f"Side C = {c}")

