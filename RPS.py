from random import randint

while True:
  choise = input("What is your choise?")
  
  number = randint(1, 3)
  if number == 1:
    print("Computer chose Scissors")
    if choise == "Scissors":
      print("It's a draw!")
    elif choise == "Paper":
      print("Computer Wins!")
    elif choise == "Rock":
      print("User wins!")
  elif number == 2:
    print("Compuiter chose Rock")
    if choise == "Scissors":
      print("Computer Wins!")
    elif choise == "Paper":
      print("User wins!")
    elif choise == "Rock":
      print("It's a draw!")
  else:
    print("Computer chose Paper")
    if choise == "Scissors":
      print("User wins!")
    elif choise == "Paper":
      print("It's a draw!")
    elif choise == "Rock":
      print("Computer Wins!")

