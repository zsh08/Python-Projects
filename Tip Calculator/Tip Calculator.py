print("Welcome to the Tip Calculator!")
bill = float(input("What was your total bill? £")) #assisnging the variable 'bill' a value that the user enters and its a float because its currency
tip = int(input("How much tip would you like to give? 10, 12, or 15? ")) #assigning the variable 'tip' a value that the user will enter
people = int(input("How many people are splitting the bill? ")) #assigning the variable 'people' a vaue that the user will enter

tip_with_bill = tip / 100 * bill + bill #calculating the tip, tip/100*bill will give us the percent the bill will be and then we +100 to show total bill with tip
split_bill = tip_with_bill / people # splitting bill with the number of people the user enters
final_amount = round(split_bill, 2) # rounding to 2 decimal points
print(f"Each persons total bill plus tip is: £{final_amount}") #the f outside bracket is so we can print a statement with different types

input("Press 'enter' to exit")