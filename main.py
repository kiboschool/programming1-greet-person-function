# Prints personalized greetings
def greet(name):
  print(f"Welcome to Kibo, {name}")
  # add two more greetings using the name parameter
  print(f"We're glad you're here, {name}")
  print(f"{name}, how did you hear about us?")

# The code below calls your function. Modify the line below to use your function with argument "Keno"
greet("Keno")

# Call the function two more times with two different names as arguments
greet("Mohammed")
greet("Seun")