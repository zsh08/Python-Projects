
menu = { # Defining what is on the menu for my coffee machine and how much resources each drink will require and the cost
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5,
    },
    "latte": {
        "ingredients": {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,

        },
        "cost" : 2.5,
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,

        },
        "cost" : 3.0,
    }

}

profit = 0 # To accumulate profits made by my working coffee machine
resources = { # Resources the coffee machnine starts off with
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}
def sufficient_resource(order_ingredients):
    """Returns True when order can be made and False if there are insufficient ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]: # Comparing the ingredients needed for new drink compared to coffee machine resources
           print(f"Sorry there is not enough {item}.")
           return False # Program stops
    return True # If my program goes through the for loop and it doesnt return false due to having enough resources, then it can return True
        
        
def process_coins ():
    """Returns the total calculated coins inserted by user"""
    print("Please insert coins")
    total = int(input("How many £1 coins do you want to insert? ")) * 1.00 #Multiplying with the value of each coin to get the total value of how much of each coin the user wants to insert
    total += int(input("How many £0.50p coins do you want to insert? ")) * 0.5 # Doing 'total +=...' to get the value added on for each question
    total += int(input("How many £0.20p coins do you want to insert? ")) * 0.2
    total += int(input("How many £0.01p coins do you want to insert? ")) * 0.01
    return total 


def transaction_successful(money_recieved, drink_cost):
    """Return True when payment accepted or False when insufficient funds"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2) # Calculating how much change to give a user, rounding to 2 decimal places
        print(f"Here is £{change} in change")
        global profit # Profit in global scope above and I want to use it in local scope so I have written 'global scope' to access it
        profit += drink_cost
        return True
    else: 
        print("Sorry that's not enough money. Money has been refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item] # Look inside resources and subtract the amount thats in order ingredients
    print(f"Here is your {drink_name}")

coffee_machine_on = True
while coffee_machine_on is True:
    coffee_choice = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
    if coffee_choice == "off": # Creating an option to turn the machine off, this will be a 'secret' response known by a maitenance worker.
        coffee_machine_on = False
        print("This machine is now switched off, Goodbye. ")

    elif coffee_choice == "report": # The 'report' response will print the current resource levels and how much profits the machine has made thus far.
        print(f"water : {resources['water']}ml") # Making this dynamic to print the most up to date levels of resources in my coffee machine
        print(f"milk : {resources['milk']}ml") # Using single quotes '' because I cant have a double quote inside another double quote
        print(f"coffee : {resources['coffee']}ml")
        print(f"money : £{profit}")
    
    else:
        drink = menu.get(coffee_choice)
        if drink:  # Check if the drink exists in the menu
            if sufficient_resource(drink["ingredients"]):  # Check if resources are sufficient
                print(f"The cost of a {coffee_choice} is £{drink['cost']}")  # Show the cost before processing payment
                payment = process_coins()  # Process the coins
                if transaction_successful(payment, drink["cost"]):  # Check if payment is successful
                    make_coffee(coffee_choice, drink["ingredients"])  # Make the coffee
        else:
            print("Sorry, we don't serve that drink.")


