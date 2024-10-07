from art import logo
import random

print(logo)

def dealing_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # the cards in my deck
    card = random.choice(cards)  # this will return a random card from the deck
    return card

def calculate_score(cards):
    """This function takes a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:  # if on the first hand the sum of cards is 21 (blackjack)
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)  # if sum is more than 21 and there is an ace (11), replace it with 1
        cards.append(1)
    return sum(cards)  # returns the sum of the cards dealt

def compare(m_score, c_score): # could not use the names my_score and computer_score as they are defined outside of this function, so ive called them something slightly diff.
    """Compares user and computer scores"""
    if m_score == c_score:
        return "Draw :/"
    elif c_score == 0:
        return "Game over, the Computer has won with Blackjack."
    elif m_score == 0:
        return "Game over, you have Blackjack! You win!"
    elif m_score > 21:
        return "Game over, your score went over 21. You lose."
    elif c_score > 21:
        return "Game over, the Computer's score went over 21. You win!"
    elif m_score > c_score:
        return "Game over, you win!"
    else:
        return "Game over, you lose :("

def play_game():
    my_cards = []  # Empty lists to store the cards for the player and computer
    computer_cards = []

    for _ in range(2):  # underscore here, because I dont need a variable there, I just need this loop to run twice to get 2 cards for the user and computer
        my_cards.append(dealing_cards())# the random card that was chosen in the 'dealing_cards' function is appended to the my_cards list
        computer_cards.append(dealing_cards())
     

    game_over = False

    while not game_over:
        '''This is where I call my function 'calculate_score', it then goes through my function and works out the 
        score for the user and the computer'''
        my_score = calculate_score(my_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {my_cards}, current score: {my_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if my_score == 0 or computer_score == 0 or my_score > 21:
            game_over = True
        else:
            user_another_card = input("Do you want to get another card? 'yes' or 'no': ").lower()
            if user_another_card == "yes":
                my_cards.append(dealing_cards())  #the random card that was chosen in the 'dealing_cards' function is appended to the my_cards list
            else:
                game_over = True

    # Computer's turn
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(dealing_cards()) #the random card that was chosen in the 'dealing_cards' function is appended to the computer cards list
            computer_score = calculate_score(computer_cards) # calculating the computer score again to update it and the while loop is evaluated on the latest score

    print(f"Your final hand: {my_cards}, final score: {my_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(my_score, computer_score)) # here im calling my compare function, passing the user_score and computer_score


while input("Do you want to play a game of blackjack? 'yes' or 'no': ").lower() == "yes":
    print("\n" * 30)  # Clears the screen
    play_game()