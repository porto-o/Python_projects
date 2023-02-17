import pandas

# Reading csv and saving it into data
data = pandas.read_csv("./nato_phonetic_alphabet.csv")

# Create a dictionary with the format
# {letter: phonetic_word}
# to loop over a dictionary we use the key,value pair
# iterrows() function is panda's function that loop over a dataframe
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def get_word():
    user_word = input("Enter a word: ").upper()
    try:
        nato_help = [nato_alphabet[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the english alphabet please.")
        get_word()
    else:
        print(nato_help)


# Create a list of the phonetic code word from nato_alphabet
# Using list comprehension, each added item is nato_alphabet value where the
# key is the same as the letter x in the user_word


get_word()
