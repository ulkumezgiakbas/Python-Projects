import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

#create a dictionary
p_dictionary = {row.letter:row.code for (index,row) in data.iterrows()}
print(p_dictionary)

#input and convert
word = input("enter a word: ").upper()
output = [p_dictionary[letter] for letter in word]
print(output)



