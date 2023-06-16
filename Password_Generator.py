import random

print('Welcome to Your Random Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()_+?'

number = int(input('Amount of passwords to generate: '))

length = int(input('What do want your password length to be: '))

print('\nPaswword Generated - ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)