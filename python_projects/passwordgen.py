# Importing random to be able to create random outputs for the password
import random

# Importing string to be able to use strings with more complexity
import string

# Ask user to create a name and if they would like to use the password generator
user = input('Create Username: ')
passw = input('Would you like to generate a password yes/no?: ')


# Create a function called passgen taking the parameter of Lenght with the integer set to a default number
def passgen(length: int = 10):

    # Making a big list with concatenated character to ramndomly choose the password
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Making the password itselft and storing it in the variable 'password' using choice from random to choose characters from alphabet for the length we set
    password = ''.join(random.choice(alphabet) for i in range(length))

    # Return the password for it to be used
    return password

# Conditonal statement to check if the user used the password generator or not
if passw == 'no':
    passw = input('Create Password: ')
elif passw == 'yes':
    passw = passgen()
else:
    print('Invalid Input')

# Return to the user their inputs
print(f'Your username is: {user}')
print(f'Your password is: {passw}')
