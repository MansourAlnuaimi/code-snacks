import random


def main():
    # initialize an array to store password's characters
    password = []
    # ask the user for the length
    length = int(input('Password length: '))
    # iterate through the loop 'length' times.
    for i in range(length):
        # add to the password's array a random generated character by the function
        password.append(random_char())

    # print the password array, join the characters using .join() method to display it as single string,
    # '' is a seperator between elements
    print(f"Password: {''.join(password)}")


def random_char():
    # arrays to store characters
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['*', '@', '#', '$', '%', '^', '&', '_', '+', '=']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # a variable that stores an integer in the range [1, 4]
    chooser = random.randint(1, 4)
    # look for the chooser's value, return a random character from certain array based on it
    match chooser:
        case 1: return random.choice(numbers)
        case 2: return random.choice(symbols)
        case 3: return random.choice(letters)
        case 4: return random.choice(letters).upper()


# Generate passwords infinitely
while True: main()
