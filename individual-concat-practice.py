# Keily Drogt
# 11 Sept 2024
# String Concatenation

# Part 1
# Use concatenation to build and display a string that displays which city and state you live in
city = 'Kewadin,m'
state = 'Michigan'

print('Kewadin,' ' Michigan')

# Part 2
# Create a custom message that welcomes the user by first name to a game you created
# Create one variable to store the user's first name
first_name = 'Bethaney'
# Create another variable that stores the welcome message
welcome_message = 'Welcome user '
# Use concatenation to create the customized message
full_message = welcome_message + first_name

print(full_message)

# Part 3
# Assign a number to your age variable
age = '17'
# Use the built-in Python str( ) function to convert your age to a string (when doing concatenation)
my_name = 'Keily,'
# Use concatenation to display a sentence that tells us your first name and age
my_age = 'I, ' + my_name + ' am ' + str(age) + ' years of age'

print(my_age)

# Part 4
# Use an f-string to build and display a string that contains your first name, last name, and your height in inches
full_name = 'Keily Drogt'
height_num = '64'

height = f"{full_name} is {height_num} inches tall"

print(height)
