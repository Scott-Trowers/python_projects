import pandas as pd

phon_alpha = pd.read_csv('../data/nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index, row) in phon_alpha.iterrows()}

user_input = input("Enter prompt: ").upper().split(' ')

char_list = [list(word) for word in user_input]

nato_output = [[nato_dict[letter] if letter in nato_dict.keys() else letter for letter in word] for word in char_list]

for word in nato_output:
    print(word)
    print('\n')
