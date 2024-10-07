from art import logo
print(logo)

# defining my operation functions
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

# adding all my operation functions in a dictionary
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator (): # created this function near the end of my code so when my elif statement is no, my code will start from the begining again and ask the user for their first number.
    first_num = float(input("What is your first number?\n")) # outside of the while loop so when users answer'yes' to continuing this question wont be asked again.
    continue_calculating = True
    while continue_calculating:

        for symbol in operations: # for each symbol in the operations dictionary print the symbols
            print(symbol)
        pick_operation = input("Pick one of these operations: ")
        next_num = float(input("What is your next number?\n"))
        answer = operations[pick_operation](first_num, next_num) # from the operations dictionary, choose the symbol entered into input 'pick_operation' and perform the relevant action to the 2 numbers inputed by the user
        print(f"{first_num} {pick_operation} {next_num} = {answer}") # printing the operation that has been done in my calculator to give the user better visibility

        choice = input(f"Would you like to continue with {answer}? type 'yes' or to start again, type 'no'\n").lower()
        if choice == "yes":
            first_num = answer
        
        
        elif choice =="no":
            continue_calculating = False
            print("\n" * 20)
            calculator() # calling a function inside of itself, this is called 'recursion'


calculator() # calling this outside the function so it runs after the program starts
        
        

 





 
























