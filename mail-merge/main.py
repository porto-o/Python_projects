# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# replace the [name] placeholder with the actual name
# save the letter in the folder "ReadyToSend"


with open("Input/Names/invited_names.txt") as names:
    names = names.readlines()
    with open("Input/Letters/starting_letter.txt") as letter:
            data_letter = letter.read()
    for each_name in names:
        each_name = each_name.strip()
        new_letter = data_letter.replace("[name]",each_name)
        with open(f'Output/ReadyToSend/{each_name}.txt','w') as outfile:
            outfile.write(new_letter)

