print("The Sum of your Squares!")

number = int(input("Please enter a whole number: "))
total = 0
# Number can be whatever the user inputs, and will be the maximum number within the range.

# Number + 1 is necessary because the range function does not include the final number, so it needs to be one number higher.
for i in range (1, number + 1):
  total += i * i
# += allows me to reassign a new value to the total, which is the old value of total plus the new value of i * i.
# As the program works through the range, it adds the square of each number including the number provided by user input.

# f string allows me to use {} to insert a value into the string.
print(f"Your total is: {total}!") 