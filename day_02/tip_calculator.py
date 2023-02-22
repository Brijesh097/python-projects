# get the input
print('< Welcome to the tip calculator />\n')
total = input('What\'s the total bill? $')
# convert the "str" input to "float"
total = float(total)

# get the percentage tip as input
percentage_tip = input('What percentage tip would you like to give (Recommended: 10, 12, 15)? ')
# convert the "str" input to "float"
percentage_tip = float(percentage_tip)

# get the number of people to split the bill
number_of_people = input('How many people to split the bill? ')
# convert the "str" input to "float"
number_of_people = float(number_of_people)

# add the tip to the total
new_total = total + (total * (percentage_tip / 100))
# total += (total * percentage_tip)

# calculate the split
split = new_total / number_of_people

# round it off
split = round(split, 2)

# display the output
print(f'Each person should pay: ${split}')