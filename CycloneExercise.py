# The Cyclone Exercise

height = float(input("What is your height? (cm): "))
credits = float(input("How many credits do you have?: "))  # Variables will be assigned according to the user input.

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("You have not met either requirement for this ride.")