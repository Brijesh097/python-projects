# get the input
height = float(input('Enter the height (m): '))
weight = float(input('Enter the weight (kg): '))

# use the formula to calculate --> BMI = WEIGHT / HEIGHT ** 2
bmi = weight / height ** 2

# round it off as a whole number
bmi = round(bmi)

# check if the bmi falls under one of these conditions
if bmi < 18.5:
    print(f'Your bmi is {bmi}, you are underweight')
elif 18.5 < bmi < 25:
    print(f'Your bmi is {bmi}, you have a normal weight')
elif 25 < bmi < 30:
    print(f'Your bmi is {bmi}, you are overweight')
elif 30 < bmi < 35:
    print(f'Your bmi is {bmi}, you are obese')
else:
    print(f'Your bmi is {bmi}, you are clinically obese')