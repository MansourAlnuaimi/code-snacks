from random import choice

options = []            # initialize a list of options
while True:
    try:                # try getting an input from the user
        option = input('Option: ')
    except EOFError:    # if user typed ctrl + D : exit the loop
        print('\n')    
        break
    else:               # if user typed a valid string, add it to the list
        options.append(option)

# choose a random option from options and output it
random_decider = lambda ls: choice(ls)
print('Go for: ' + random_decider(options))
