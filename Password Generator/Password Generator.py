import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome to the Password Generator!")
num_letters = int(input("How many letters would you like in your password? "))   
num_numbers = int(input("How many numbers would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))

password = ""
for char in range (1, num_letters + 1):
   # random_char = random.choice(letters)        # creating variable called random char that will have random letters 
    #password += random_char                     # the random letters are added to the password

    # the above 2 lines can be made shorter with the below and we can do the same for symbols and numbers
    password += random.choice(letters)

for char in range (1, num_numbers + 1): # we add +1 at the end because the loop will stop at the second last item in the above list so to make sure it goes through the whole loop we add a +1
    password += random.choice(numbers)

for char in range (1, num_symbols + 1):
    password+= random.choice(symbols)

print(password) #the above will give me a random pass with the nom of letters/numbers and symbols i state,
                # however, it will be in order and not in a random order abc123! -> a1b!c32


# instead of using pass string "" im going to use a list [] to get the pass to be in a random order
password_list = []
for char in range (1, num_letters + 1):
   
    password_list.append(random.choice(letters))

for char in range (1, num_numbers + 1): 
    password_list.append(random.choice(numbers)) # append adds existing item to the end of a list

for char in range (1, num_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list) # shuffle will change the order of my password, making it random order
print(password_list) # this will print my password like so: ['u', '#', '6', '4', '1', 'n', 'd', '&', '#']
                        # to make it look like a string and not a list, do the below
password = ""
for char in password_list:
    password += char
print(password)

input("Press 'enter' to exit")
