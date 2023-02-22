# get the height and weight
height = input('Enter the height in (m): ')
weight = input('Enter the weight in (kg): ')

# use the formula to calculate --> BMI = WEIGHT / HEIGHT**2
bmi = float(weight)/float(height)**2

# display the type of the output along with the rounded answer
print(type(bmi), round(bmi))