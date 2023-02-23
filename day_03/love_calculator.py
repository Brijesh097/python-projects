# greeting message
print('Welcome to love calculator')

# get the inputs
name1 = input('What\'s your name? ')
name2 = input('What\'s their name? ')

# change the input to lowercase
name1 = name1.lower()
name2 = name2.lower()

# count how many times the inputs have any of the following alphabets
# input 1 for true
T1 = name1.count("t")
R1 = name1.count("r")
U1 = name1.count("u")
E1 = name1.count("e")
# input 1 for love
L1 = name1.count("l")
O1 = name1.count("o")
V1 = name1.count("v")
E1 = name1.count("e")
# input 2 for true
T2 = name2.count("t")
R2 = name2.count("r")
U2 = name2.count("u")
E2 = name2.count("e")
# input 2 for love
L2 = name2.count("l")
O2 = name2.count("o")
V2 = name2.count("v")
E2 = name2.count("e")
# combine input 1 & input 2 together - TRUE
T = T1 + T2
R = R1 + R2
U = U1 + U2
E = E1 + E2
# combine input 1 & input 2 together - LOVE
L = L1 + L2
O = O1 + O2
V = V1 + V2
E = E1 + E2
# calculate the total - TRUE
total_1 = T + R + U + E
# calculate the total - LOVE
total_2 = L + O + V + E

# casting both integers to strings, concatenate the strings and then cast the result back to an integer
love_score = int(str(total_1) + str(total_2))

if love_score < 10 or love_score > 90:
    print(f'Your love score is {love_score}%, you go together like coke and mentos.')
elif 40 < love_score < 50:
    print(f'Your love score is {love_score}%, you are alright together.')
else:
    print(f'Your love score is {love_score}%.')