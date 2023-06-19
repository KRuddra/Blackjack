def makeaccount():
  username = input("Enter a username: ")
  password = input("Enter a password:  ")

def updatebet(totalmoney): 
  amountmoney = total + int(input("Enter the amount of money you want in your account: "))
  return amountmoney




print("\n**************************************\n\n")
print("The Options are:\n1.Make Account\n2.Place Bet\n3. Instructions\n4.Stop")
a = int(input("\nEnter one of the options above: "))
print("\n**************************************\n\n")

while a != 4:
  if a == 1:
    makeaccount()
  elif a == 2:
    updatebet(totalmoney)
  elif a == 3:
    print("The person closer to the number 21 wins, and if you get 21 you automatically win. If you exceed the number 21 you automatically loser. At the start of the game you draw 2 cards and the dealer draws two cards, you can only see one of the cards that the dealer has gotten. After those two cards you can either hit or stand. If you hit another card is drawn for you, if you exceed 21 in total you lose, then you can hit and stand again. If you stand the dealer shows you his second card, if it is less then 17 the dealer will draw again until they get to 17 or over 17, if the dealer gets over 21 they lose. In this game, an Ace is worth either 1 or 11, and all the face cards are worth 10. It will display these cards in a proper card fashion, instead of just reading them out.")
  elif a == 4:
    print("Thank you for playing this game made by Ruddra!")
    break
  elif a == 5:
    break
  else:
    print("Please enter a proper number!")