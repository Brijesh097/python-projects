# greeting message
print('Welcome to Python Pizza Deliveries!')

# get the size of the pizza
size = input('What size pizza do you want? [S, M, L]: ')

# asking user for the extra add-ons
add_pepperoni = input('Do you want pepperoni? [Y, N]: ')
extra_cheese = input('Do you want extra cheese? [Y, N]: ')

# initializing the bill and setting it to 0
bill = 0

# checking what's the user's preference and summing up the total accordingly
if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
elif size == 'L':
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1

print(f'Your final bill is ${bill}.')