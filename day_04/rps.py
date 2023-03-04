import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("*** Rock Paper Scissors ***\n")
print("What do you choose?")

choice = int(input("Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

computer_chose = random.randint(0, 2)

print("Computer chose: ")

if computer_chose == 0:
    print(rock)
elif computer_chose == 1:
    print(paper)
elif computer_chose == 2:
    print(scissors)

if choice == 0:
    if computer_chose == 0:
        print("It's a tie!")
    elif computer_chose == 1:
        print("Computer wins!")
    elif computer_chose == 2:
        print("You win!")
elif choice == 1:
    if computer_chose == 0:
        print("You win!")
    elif computer_chose == 1:
        print("It's a tie!")
    elif computer_chose == 2:
        print("Computer wins!")
elif choice == 2:
    if computer_chose == 0:
        print("Computer wins!")
    elif computer_chose == 1:
        print("You win!")
    elif computer_chose == 2:
        print("It's a tie!")
else:
    print("Oye, come on! Choose something...")