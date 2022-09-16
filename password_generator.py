# to try it online, go to https://onlinegdb.com/c7LP2p61qr
import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['*', '@', '#', '$', '%', '^', '&', '_', '+', '=']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm','n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
animals = ['cat', 'lion', 'dog', 'fish', 'cow', 'bull', 'goat', 'ant', 'fly', 'ape', 'frog', 'crab', 'bee']
adjectives = ['huge', 'tiny', 'red', 'gold', 'blue', 'ugly', 'fast', 'evil', 'good', 'nice', 'fat', 'sad', 'fool']
stop = 'text'
while stop != '0':
    password = random.choice(letters).upper() + random.choice(letters).lower() + random.choice(numbers) \
               + random.choice(numbers) + '_' + random.choice(adjectives) + '_' + random.choice(animals) \
               + '_' + random.choice(numbers).lower() + random.choice(letters).upper() + 2*random.choice(symbols)
    print(f"\nYour password is: {password}")
    stop = input("Enter any key for another password, enter 0 to stop.  ")
