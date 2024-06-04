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

#Write your code below this line 👇
import random
selection_user = input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
selection = int(selection_user)
if selection > 2:
    print ("F-you")
    exit()
option = [rock, paper, scissors]
player = option[selection]
print (player)
print ("Computer chose:\n")
computer = option[random.randint(0, 2)]
print (computer)

if player == rock and computer ==  scissors:
    print ("you won")
elif player == paper and computer == rock:
    print ("you won")
elif player == scissors and computer == paper:
    print ("you won")
elif player == computer:
    print ("draw")
else:
    print ("you lose")