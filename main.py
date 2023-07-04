import random, os, time


#Class of Cards
class card:
  def __init__(self, suit, value, card_value):
    #Suit of the card
    self.suit = suit
    #The name of the card 
    self.value = value
    #Value of the card
    self.card_value = card_value

def clear():
  os.system("clear")

#Betting function
def betting(x):
  print("\n**************************************\n\n")
  money = int(input("How much do you want to bet? $"))
  print("\n**************************************\n")
  return money

#Function to print the cards
def print_cards(cards, hidden):
  q = ""
  for card in cards:
    q = q + "\t _________________"
  if hidden:
    q = q + "\t _________________"
  print(q)
  q = ""
  for card in cards:
    q = q + "\t|                 |"
  if hidden:
    q = q + "\t|                 |"
  print(q)
  q = ""
  for card in cards:
    if card.value == '10':
      q = q + "\t|   {}            |".format(card.suit) 
    else:
      q = q + "\t|   {}             |".format(card.suit) 
  if hidden:
    q = q + "\t|                 |"
  print(q)

  q = ""
  for card in cards:
    q = q + "\t|                 |"
  if hidden:
    q = q + "\t|      * *        |"
  print(q)

  q = ""
  for card in cards:
    q = q + "\t|                 |"
  if hidden:
    q = q + "\t|   *        *    |"
  print(q)

  q = ""
  for card in cards:
    q = q + "\t|                 |"
  if hidden:
    q = q + "\t|  *          *   |"
  print(q)

  q = ""
  for card in cards:
    q = q + "\t|                 |"
  if hidden:
    q = q + "\t|  *          *   |"
  print(q)

  q = ""
  for card in cards:
    q = q + "\t|       {}         |".format(card.value)
  if hidden:
    q = q + "\t|            *    |" 
  print(q)

  q = ""
  for card in cards:
    q = q + "\t|                 |"
  if hidden:
    q = q + "\t|        *        |"
  print(q)

  q = ""
  for card in cards:
    q = q + "\t|                 |"
  if hidden:
    q = q + "\t|        *        |"
  print(q)

  q = ""
  for card in cards:
    q = q + "\t|                 |"
  if hidden:
    q = q + "\t|                 |"
  print(q)

  q = ""
  for card in cards:
    q = q + "\t|                 |"
  if hidden:
    q = q + "\t|                 |"
  print(q)

  q = ""
  for card in cards:
    if card.value == '10':
      q = q + "\t|              {}  |".format(card.suit) 
    else:
      q = q + "\t|              {}  |".format(card.suit) 
  if hidden:
    q = q + "\t|        *        |"
  print(q)

  q = ""
  for card in cards:
    q = q + "\t _________________"
  if hidden:
    q = q + "\t _________________"
  print(q)

  print()

#The function to run the blackjack game
def blackjack(deck, x):
  print("\n**************************************")
  if x == "No Account":
    print("\nYou have not made an account therefore you will not be able to bet\n")
  else: 
    print("Welcome back", x)
    money = betting(x)

  #Wins and Losses
  wins = 0
  losses = 0
  ties = 0
  
  #Card list for player/dealer
  player_cards = []
  dealer_cards = []

  #The score for player/dealer
  player_score = 0
  dealer_score = 0

  clear()

  #The first dealings for player/dealer
  while len(player_cards) < 2:
    #Dealing the cards,adding to player card list,removing that card
    oneplayercard = random.choice(deck)
    player_cards.append(oneplayercard)
    deck.remove(oneplayercard)
    #Updating player score
    player_score += int(oneplayercard.card_value)

    #Printing the player cards
    print("PLAYER CARD: ")
    print_cards(player_cards, False)
    print("Player score: ", player_score)

    input()

    #Dealing the cards,adding to player card list,removing that card
    onedealercard = random.choice(deck)
    dealer_cards.append(onedealercard)
    deck.remove(onedealercard)
    #Updating player score
    dealer_score += int(onedealercard.card_value)

    #Printing the dealer cards
    if len(dealer_cards) == 1:
      print("DEALER CARD: ")
      print_cards(dealer_cards, False)
      print("Dealer score: ", dealer_score)
    else:
      print_cards(dealer_cards[:-1], True)
      print("Dealer score: ", dealer_score - dealer_cards[-1].card_value)

    input()

  #If player gets BlackJack
  if player_score == 21:
    print("PLayer has won!\nPlayer got blackjack!")
    money = money * 2
    wins = wins + 1
    print("You won the bet you have $", money)
    a = menuoptions()
    return a, money, wins, losses, ties

  clear()
  
  #Print the player and dealer cards
  print("DEALER CARD: ")
  print_cards(dealer_cards[:-1], True)
  print("Dealer score: ", dealer_score - dealer_cards[-1].card_value)
  print()
  print("PLAYER CARD: ")
  print_cards(player_cards, False)
  print("Player score: ", player_score)

  #Player moves
  while player_score != 21:
    choice = input("Enter H to Hit or S to Stand: ").upper()

    #If player chooses to Hit
    if choice == "H":
      #Dealing the cards
      oneplayercard = random.choice(deck)
      player_cards.append(oneplayercard)
      deck.remove(oneplayercard)
      #Updating player score
      player_score += oneplayercard.card_value
      clear()

      #Printing player and dealer cards again
      print("DEALER CARD: ")
      print_cards(dealer_cards[:-1], True)
      print("Dealer score: ", dealer_score - dealer_cards[-1].card_value)
      print()
      print("PLAYER CARD: ")
      print_cards(player_cards, False)
      print("Player score: ", player_score)
      # Check if player busts
      if player_score > 21:
        print("PLAYER BUSTED!!! GAME OVER!!!")
        money = 0
        losses = losses + 1
        print("Your lost the bet you have $", money)
        a = menuoptions()
        return a, money, wins, losses, ties
    #If player choose to Stand
    elif choice == "S":
      break
    else:
      print("Please enter a proper choice from above! ")
      choice = input("Enter H to Hit or S to Stand: ")
  clear()

  # Print player and dealer cards
  print("PLAYER CARDS: ")
  print_cards(player_cards, False)
  print("Player score: ", player_score)
 
  print()
  print("DEALER IS REVEALING THE CARDS....")
 
  print("DEALER CARDS: ")
  print_cards(dealer_cards, False)
  print("Dealer score: ", dealer_score)
 
  # Check if player has a Blackjack
  if player_score == 21:
    print("PLAYER HAS A BLACKJACK")
    money = money * 2
    wins = wins + 1
    print("You won the bet you have", money)
    a = menuoptions()
    return a, money, wins, losses, ties
    
  # Check if player busts
  if player_score > 21:
    print("PLAYER BUSTED!!! GAME OVER!!!")
    money = 0 
    losses = losses + 1
    print("Your lost the bet you have $", money)
    a = menuoptions()
    return a, money, wins, losses, ties
 
  input() 

  #The dealer moves
  while dealer_score < 17:
    clear()
    print("DEALER DECIDES TO HIT.....")
 
    # Dealing card for dealer
    onedealercard = random.choice(deck)
    dealer_cards.append(onedealercard)
    deck.remove(onedealercard)
 
    # Updating the dealer's score
    dealer_score += onedealercard.card_value
    # Print player and dealer cards
    print("PLAYER CARDS: ")
    print_cards(player_cards, False)
    print("Player score: ", player_score)
 
    print()
 
    print("DEALER CARDS: ")
    print_cards(dealer_cards, False)
    print("Dealer score: ", dealer_score)

    input()
  # Dealer busts
  if dealer_score > 21:        
    print("DEALER BUSTED!!! YOU WIN!!!")
    money = money * 2
    wins = wins + 1
    print("You won the bet you have $", money)
    a = menuoptions()
    return a, money, wins, losses, ties
      
 
  # Dealer gets a blackjack
  if dealer_score == 21:
    print("DEALER HAS A BLACKJACK!!! PLAYER LOSES")
    money = 0 
    losses = losses + 1
    print("Your lost the bet you have $", money)
    a = menuoptions()
    return a, money, wins, losses, ties
    
    
  # TIE Game
  if dealer_score == player_score:
    print("TIE GAME!!!!")
    ties = ties + 1
    print("Your bet has stayed the same, $", money)
    a = menuoptions()
    return a, money, wins, losses, ties
  
  # Player Wins
  elif player_score > dealer_score:
    print("PLAYER WINS!!!")  
    money = money * 2
    wins = wins + 1
    print("You won the bet you have $", money)
    a = menuoptions()
    return a, money, wins, losses, ties
  
  # Dealer Wins
  else:
    print("DEALER WINS!!!") 
    money = 0
    losses = losses + 1 
    print("Your lost the bet you have $", money)
    a = menuoptions()
    return a, money, wins, losses, ties 

#Function to run the blackjack game
def runblackjack(x):
  #The type of suits 
  suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
  #The value of the suit
  suits_value = {"Spades":"\u2664", "Hearts":"\u2661",     "Diamonds":"\u2662", "Clubs":"\u2667"}
  #The type of card
  cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
  #The value of each card
  cards_value = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "J":10, "Q":10, "K":10, "A":11}
  #Initilizes the deck
  deck = []
  #Loop for every suit
  for suit in suits:
    #Loop for everytype of card in cards
    for Card in cards:
      #Adds the card to the deck
      deck.append(card(suits_value[suit], Card, cards_value[Card]))
  a, money, wins, losses, ties = blackjack(deck, x)
  return a, money, wins, losses, ties

#Function to run the menu options
def menuoptions():
  print("\n\n**************************************\n\n")
  print("The Options are:\n1.Play\n2.Instructions\n3.Stop\n4.Make an Account\n5.Log In\n6.Stats of the Game")
  a = int(input("\nEnter one of the options above: "))
  print("\n\n**************************************\n\n")
  return a

#Function to create an account
def makeaccount():
  username = input("Enter a username: ")
  password = input("\nEnter a password: ")
  return username, password, 1

#Function to log into the account
def login(username, password, usernamelist, passwordlist):
  clear()
  print("**************************************\n\n")
  print("Enter Menu to go back to the main menu\n")
  username1 = input("What is your username? ")
  password1 = input("What is your password? ")
  if username1 == "Menu" or password1 == "Menu":
    return 0 

  if username1 in usernamelist:
    username2 = usernamelist.index(username1)
  if password1 in passwordlist:
    password2 = passwordlist.index(password1)
    
  while username1 not in usernamelist or password1 not in passwordlist:
    if username1 not in usernamelist:
      print("\n\n**************************************\n\n")
      print("Enter Menu to go back to the main menu")
      print("\nPlease enter a correct username")
      username1 = input("What is your username? ")
      if username1 == "Menu" or password1 == "Menu":
        return 0  
    if password1 not in passwordlist:
      print("\n\n**************************************\n\n")
      print("Enter Menu to go back to the main menu")
      print("\nPlease enter a correct password")
      password1 = input("What is your password? ")
      if username1 == "Menu" or password1 == "Menu":
        return 0
        
  if username1 in usernamelist:
    username2 = usernamelist.index(username1)
  if password1 in passwordlist:
    password2 = passwordlist.index(password1)    

  while password2 != username2:
    print("\n\n**************************************\n\n")
    print("Enter Menu to go back to the main menu")
    print("The username and passwords do not match")
    print("\nPlease enter a correct password and username")
    username1 = input("What is your username? ")
    password1 = input("What is your password? ")
    if username1 in usernamelist:
      username2 = usernamelist.index(username1)
    if password1 in passwordlist:
      password2 = passwordlist.index(password1) 
      
  if username2 == password2:
    print("\n\n**************************************\n\n")
    print("Welcome back to BlackJack, ", username1)
    return (usernamelist.index(username1) + 1)
    
  if username1 in usernamelist:
    username2 = usernamelist.index(username1)
  if password1 in passwordlist:
    password2 = passwordlist.index(password1)


print("        Welcome to BlackJack         ")
a = menuoptions()
checkifrun = 0
usernamelist = []
passwordlist = []
z = 0
d = 0
wins1 = 0
money1 = 0
losses1 = 0
ties1 = 0
while a != 3:
  if a == 1:
    d = 1 
    if z != 0:
      x = usernamelist[(z-1)]
      a, money, wins, losses, ties = runblackjack(x)
    else:
      x = "No Account"
      a, money, wins, losses, ties = runblackjack(x)
     
    money1 = money1 + money
    wins1 = wins1 + wins
    losses1 = losses1 + losses
    ties1 = ties1 + ties
  elif a == 2:
    print("The person closer to the number 21 wins, and if you get 21 you automatically win. If you exceed the number 21 you automatically loser. At the start of the game you draw 2 cards and the dealer draws two cards, you can only see one of the cards that the dealer has gotten. After those two cards you can either hit or stand. If you hit another card is drawn for you, if you exceed 21 in total you lose, then you can hit and stand again. If you stand the dealer shows you his second card, if it is less then 17 the dealer will draw again until they get to 17 or over 17, if the dealer gets over 21 they lose. In this game, an Ace is worth either 1 or 11, and all the face cards are worth 10. It will display these cards in a proper card fashion, instead of just reading them out.")
    a = menuoptions()
  elif a == 4:
    username, password, checkifrun = makeaccount()
    usernamelist.append(username)
    passwordlist.append(password)
    a = menuoptions()
  elif a == 5:
    if checkifrun != 1:
      print("You have not made an account yet!")
      a = menuoptions()
    else:  
      z = login(username, password, usernamelist, passwordlist)
      a = menuoptions()
  elif a == 6:
    if d == 1:
      if x == "No Account":
        print("You have not logged in/made an account to dispay your stats in")
        a = menuoptions()
      else:
        print("\n**************************************")
        print("\n\nWelcome back", x)
        print("\nWins:", wins1)
        print("\nLosses:", losses1)
        print("\nTies:", ties1)
        print("\nPercentage Win: %", (wins1 // (wins1 + losses1 + ties1) * 100))
        print("\nPercentage Loss: %", (losses1 // (wins1 + losses1 + ties1)* 100))
        print("\nPercentage Ties: %", (ties1 // (wins1 + losses1 + ties1)* 100))
        print("\nCurrernt Money Won: $", money1)
        a = menuoptions()
    else:
      print("Please play the game first")
      a = menuoptions()
      
  else:
    print("Please choose a correct option from above! ")
    a = menuoptions()
if a == 3:
  print("Thank you for playing this game made by Ruddra Kantaria")



#USING A LIST INDEX TO  STORE IN VARIBLE Z U CAN USE IT TO TRACK AND IDSPLAY SINCE THE LIST IS NOT IN A FUNCTION