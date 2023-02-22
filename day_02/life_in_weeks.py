# get the age as an input
age = input('What\'s your current age? ')

# convert the "str" input to "int"
age = int(age)

# this program assumes that a person lives till their 90 years old
# calculate the number of days in total
number_of_days_total = 365 * 90
# calculate the number of weeks in total
number_of_weeks_total = 52 * 90
# calculate the number of months in total
number_of_months_total = 12 * 90

# the age that the user inputted is in years, so let's calculate the following
# calculate the number of days of the user
number_of_days_user = 365 * age
# calculate the number of weeks of the user
number_of_weeks_user = 52 * age
# calculate the number of months of the user
number_of_months_user = 12 * age

days_left = number_of_days_total - number_of_days_user
weeks_left = number_of_weeks_total - number_of_weeks_user
months_left = number_of_months_total - number_of_months_user

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')