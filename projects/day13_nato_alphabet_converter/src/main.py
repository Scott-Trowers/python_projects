import pandas as pd

phon_alpha = pd.read_csv('../data/nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index, row) in phon_alpha.iterrows()}

user_input = input("Enter prompt: ").upper().split(' ')

char_breakdown = [list(word) for word in user_input]
print(char_breakdown)

nato_output = [[nato_dict[letter] if letter in nato_dict.keys() else letter for letter in word] for word in char_breakdown]

for word in nato_output:
    print(word)
    print('\n')
