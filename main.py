from art import logo, smileys
import random
from replit import clear
clear()
print(logo)

cguess = random.randint(0, 100)
print("The Computer has guessed a number between 0 and 100. Guess it to win!")
print(smileys)
print(cguess)
print("/n You have 10 guesses")
lives = 10
success = False
while lives > 0 and not success:
  g = int(input("Enter your guess: "))
  if g == cguess:
    print(f"That is the right answer {g} {smileys['cool']}")
    success = True
  elif g > cguess:
    print("Too high. Guess again")
    lives -= 1
  else:
    print("Too low. Guess again")
    lives -= 1

  print(f"Lives left {lives}")  