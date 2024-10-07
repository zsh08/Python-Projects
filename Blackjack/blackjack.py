from art import logo
import random

print(logo)


def dealing_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] # the cards in my deck
    card = random.choice(cards) # this will return a random card from the deck
    return (card)

#.............................................................................................................
def calculate_score (cards):
    '''This function takes a list of cards and returns the score calculated from the cards'''
    if sum(cards) ==21 and len(cards) ==2: # if on the first hand the sum of cards is 21 then its a win so no further action 
        return 0

    if sum(cards) >21 and 11 in cards:
        cards.remove(11) # if sum of cards is more than 21 and there is a 11 (ace) then by the rules of black jack, that can be replaced with ace being 1.
        cards.append(1)
    return sum(cards) # returns the sum of the cards dealt to both the user and computer
#..................................................................................................................
def compare (m_score, c_score): # could not use the names my_score and computer_score as they are defined outside of this function, so ive called them something slightly diff.
    if m_score == c_score:
        return "Draw :/"
    elif c_score == 0:
        return "Game over, the Computer has won."
    elif m_score >21:
        return "Game over, your score went over 21, the Computer has won."
    elif c_score >21:
        return "Game over, the score went over 21, the User has won."
    elif m_score > c_score:
        return "Game over, the User has won!"
    else:
        return "You lose :("
        
#...........................................................................................................
def play_game():
    my_cards = [] # empty lists to store the cards the computer and user are handed throughout the game
    computer_cards = []
    computer_score = -1 # defining this variable, i cant assign to 0 as 0 means something in my blackjack game,so i assigned it to a number that would never occur
                        # additionally computer_score had to be defined outside of the while loop so it always has a value even if for some reason the while loop is skipped.
    my_score = -1 # see explanation above

    for _ in range(2): # underscore here, because we dont need a variable there, we just need this loop to run twice to get 2 cards for the user and computer
        my_cards.append(dealing_cards()) # the random card that was chosen in the 'dealing_cards' function is appended to the my_cards list
        computer_cards.append(dealing_cards())

    game_over = False
    while not game_over:
        '''This is where I call my function 'calculate_score', it then goes through my function and works out the 
        score for the user and the computer'''

        my_score = calculate_score(my_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are: {my_cards} and your score is: {my_score} \nComputers's first card is: {computer_cards[0]}")

        game_over =  False
        if my_score ==0 or computer_score ==0 or my_score >21:
            game_over = True
            
        else:
            user_another_card = input("Do you want to get another card? 'yes' or 'no': ").lower()
            
            if user_another_card == "yes":
                my_cards.append(dealing_cards())  #the random card that was chosen in the 'dealing_cards' function is appended to the my_cards list
            else:
                game_over = True


        '''Above is for the user to draw cards etc, below will be for the computer to draw cards 
        as long as the sum of its cards are less that 17'''
        while computer_score != 0 and computer_score< 17 :
            computer_cards.append(dealing_cards())#the random card that was chosen in the 'dealing_cards' function is appended to the computer cards list
            computer_score = calculate_score(computer_cards) # calculating the computer score again to update it and the while loop is evaluated on the latest score


    print(f"Your final hand: {my_cards}, final score: {my_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(my_score, computer_score)) # here im calling my compare function, passing the user_score and computer_score


while input("Do you want to play a game of blackjack? 'yes' or 'no': ") =="yes":
    print("\n" * 30)
    play_game()
