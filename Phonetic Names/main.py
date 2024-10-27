import pandas

data = pandas.read_csv("phonetic_alphabet.csv") # reading my CSV file with the phonetic alphabet
print(data.to_dict())

phonetic_dict = {row.letter:row.code for(index, row) in data.iterrows()} #created a dictionary to store my csv data in


user_input = input ("Enter a word: ").upper() # user will type a word and will be changed to upper case
output = [phonetic_dict[letter] for letter in user_input] # from the 'user_input' each letter will be compared to the letters in the phonetic dictonary and the word or 'code' will be printed 
print(output)