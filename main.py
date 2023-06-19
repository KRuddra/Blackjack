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
def blackjack(deck):
  print("\n**************************************")
  money = int(input("How much do you want to bet? $"))
  print("\n**************************************\n")
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
    print("You won the bet you have $", money)
    a = menuoptions()
    return a

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
        print("Your lost the bet you have $", money)
        a = menuoptions()
        return a
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
    print("You won the bet you have", money)
    a = menuoptions()
    return a
    
  # Check if player busts
  if player_score > 21:
    print("PLAYER BUSTED!!! GAME OVER!!!")
    money = 0 
    print("Your lost the bet you have $", money)
    a = menuoptions()
    return a
 
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
    print("You won the bet you have $", money)
    a = menuoptions()
    return a
      
 
  # Dealer gets a blackjack
  if dealer_score == 21:
    print("DEALER HAS A BLACKJACK!!! PLAYER LOSES")
    money = 0 
    print("Your lost the bet you have $", money)
    a = menuoptions()
    return a
    
    
  # TIE Game
  if dealer_score == player_score:
    print("TIE GAME!!!!")
    print("Your bet has stayed the same, $", money)
    a = menuoptions()
    return a
  
  # Player Wins
  elif player_score > dealer_score:
    print("PLAYER WINS!!!")  
    money = money * 2
    print("You won the bet you have $", money)
    a = menuoptions()
    return a
  
  # Dealer Wins
  else:
    print("DEALER WINS!!!") 
    money = 0 
    print("Your lost the bet you have $", money)
    a = menuoptions()
    return a 


#Function to run the blackjack game
def runblackjack():
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
  a = blackjack(deck)
  return a

def menuoptions():
  print("\n**************************************\n\n")
  print("The Options are:\n1.Play\n2.Instructions\n3.Stop")
  a = int(input("\nEnter one of the options above: "))
  print("\n**************************************\n\n")
  return a




print("        Welcome to BlackJack         ")

a = menuoptions()
while a != 3:
  if a == 1:
    a = runblackjack()
  elif a == 2:
    print("The person closer to the number 21 wins, and if you get 21 you automatically win. If you exceed the number 21 you automatically loser. At the start of the game you draw 2 cards and the dealer draws two cards, you can only see one of the cards that the dealer has gotten. After those two cards you can either hit or stand. If you hit another card is drawn for you, if you exceed 21 in total you lose, then you can hit and stand again. If you stand the dealer shows you his second card, if it is less then 17 the dealer will draw again until they get to 17 or over 17, if the dealer gets over 21 they lose. In this game, an Ace is worth either 1 or 11, and all the face cards are worth 10. It will display these cards in a proper card fashion, instead of just reading them out.")
    a = menuoptions()
  else:
    print("Please choose a correct option from above! ")
    a = menuoptions()
if a == 3:
  print("Thank you for playing this game made by Ruddra Kantaria")



