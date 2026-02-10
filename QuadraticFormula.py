# Quadratic Formula Calculator

a = float(input("Please enter your 'a' value: "))
print ("Okay!")

b = float(input("Please enter your 'b' value: "))         # Variables to be substituted into the equation.
print ("Almost there!")

c = float(input("Please enter your 'c' value: "))
print ("Here we go!")

d = ((b**2 - 4*a*c)**0.5) # Discriminant

x1 = (-b + (d)) / (2*a)
x2 = (-b - (d)) / (2*a)

print(x1)
print(x2)