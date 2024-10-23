import turtle
import pandas

screen = turtle.Screen()
screen.title("USA Game") # title of the pop up screen that opens
usa_image = "blank_states_img.gif" # creating variable to store this file path to make it easier to use elsewhere in my code
screen.addshape(usa_image) # the image i will load into my screen will be the shape of my selected image
turtle.shape(usa_image)

data = pandas.read_csv("50_states.csv") # Reading the Csv file with all the states and coordinates
all_states = data.state.to_list() # gets me the data series which is the first column of my data list "50_states"
# and converts to list
user_guesses = []

while len(user_guesses) < 50:
    state_guess = screen.textinput(title = f"{len(user_guesses)} / 50 correct", prompt = "Please write a state name: ").title() # a pop to ask the user to enter a state name.
    #print(state_guess)


    if state_guess == "Exit": # when typing exit, program will end
        missing_states = []
        for state in all_states:
            if state not in user_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv") # new csv will be created with all the states the user did not guess.
        break


    if state_guess in all_states: # can only do this because i tranformed the column to a list 
        user_guesses.append(state_guess)
        
        trtle = turtle.Turtle() # to construct a new turtle
        trtle.hideturtle()# hides turtle shape
        trtle.penup() # doesnt do any drawing
        
        state_info = data[data.state == state_guess] # will pull out the row where the users guess is equal to the correct state
        
        trtle.goto(state_info.x.item(), state_info.y.item())# I want it to go to a particular x and y location, using '.item()' to access the series of a dataframe
        trtle.write(state_guess)









