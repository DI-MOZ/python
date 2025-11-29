import math

# Solve quadratic equation ax^2 + bx + c = 0

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Two real solutions: x1 = {x1}, x2 = {x2}")

elif d == 0:
    x = -b / (2*a)
    print(f"One real solution: x = {x}")

else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-d) / (2*a)
    print(f"Two complex solutions: {real_part}+{imaginary_part}i and {real_part}-{imaginary_part}i")
