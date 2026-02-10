# Pythagoras' Theorem Calculator

a = int(input("What is the length of your shortest triangle side?"))
print ("Your shortest side is:")
print (a)

b = int(input("What is the length of your OTHER short side?"))
print ("Your OTHER short side is:")                #Variables to be substituted into the equation.
print (b)

c = (a ** 2 + b ** 2) ** 0.5

print ("Your hypotenuse is:")
print (c)