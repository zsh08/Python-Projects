# Building a digital form of the caeser cipher
# Type of substitution cipher in which each letter in the plaintext is replaced by a 
# Letter some fixed number of positions down the alphabet
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser (original_text, shift_amount, encode_or_decode):
    
    cipher_text = "" # Lets me create a list, everytime the for loop occurs, so my new cipher can be saved in this list.
    
    if encode_or_decode == "decode": # if decode is chosen the shift amount will be multiplied by -1 so it moves backwards
        shift_amount *= -1 
    
    for letter in original_text:
        if letter not in alphabet: # for symbols and spaces 
            cipher_text += letter # will add the space or symbol to our cypher_text list and not shift them.
        else:
            shifted_position = alphabet.index(letter) + shift_amount # Index allows me to see the position of a character in my list, so for each letter in my input im locating their position then adding the shift amount 
            shifted_position %= len(alphabet) # This line is important, if a text entered has 'z' and shift was 9, then there would be an error, this line forces the range to stay as 0-25 (as per the alphabet) so the new shifted letter would be 'i'
            cipher_text += alphabet[shifted_position] # Adding the shifted position of letters in my list 'cipher_text'
            
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")


should_continue = True 

while should_continue: # while loop so the user can encode/decode more than one time per run of the program

    direction = input ("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input ("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser (original_text = text, shift_amount = shift, encode_or_decode = direction) # calling my function with a keyword argument, text and shift and direction entered in by user are the arguments.

    restart = input("Do you want to restart the program? 'yes' or 'no'\n").lower()
    if restart == "no": # if users say no, then program will end, otherwise, if user says yes then it will refer back to the while loop and restart
        should_continue = False
        print("Goodbye")







