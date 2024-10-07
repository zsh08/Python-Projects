from art import logo
import random

print(logo)


celebs = {
    "Kim Kardashian" : "360000000",
    "Kanye West" : "210000000",
    "Taylor Swift" : "284000000",
    "Kylie Jenner" : "396000000",
    "Emma Watson" : "74000000",
    "Lana Del Ray" : "19000000",
    "Justin Bieber" : "294000000",
    "Selena Gomez" : "424000000",
    "Hailey Bieber" : "53000000",
    "Gigi Hadid" : "77000000",
    "Bella Hadid" : "61000000",
    "Kendall Jenner" : "291000000",
    "Khloe Kardashian" : "306000000",
    "Kourtney Kardashian" : "221000000",

}

user_score = 0
game_over = False

while not game_over:
    celeb1 = random.choice(list(celebs.keys()))  # Choosing a random key (celebrity name)
    celeb2 = random.choice(list(celebs.keys()))  # Choosing a random key (celebrity name)



    #ensuring celeb1 and celeb2 are different
    while celeb1 == celeb2:
        celeb2 = random.choice(list(celebs.keys()))


    #getting follower counts as integers
    celeb1_followers = int(celebs[celeb1])
    celeb2_followers = int(celebs[celeb2])


    #asking the user to make a guess
    guess = input(f"Compare User A: {celeb1}: with {celebs[celeb1]} followers on Instagram, with User B: {celeb2}.\nDoes user B have a higher or lower follower count than user A? Type 'H' or 'L' ").lower()



     # Function to compare followers
    def compare(celeb1_followers, celeb2_followers, guess):
            global game_over
            if celeb1_followers < celeb2_followers and guess == "h":
                return True
                
            elif celeb1_followers > celeb2_followers and guess == "l":
                return True
            else:
                return False

    # Call the compare function and handle result
    if compare(celeb1_followers, celeb2_followers, guess):
        user_score += 1
        print(f"Correct! Your score is now {user_score}.")

    else:
        game_over = True
        print(f"That's incorrect. Game over. Your final score was {user_score}.")


