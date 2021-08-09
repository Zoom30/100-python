

list_of_names = []
PLACEHOLDER = "[name]"

with open("Day 24 file handling/Day's exercise/Input/Names/invited_names.txt") as file:

    # creates a list of name_contents
    name_contents = file.readlines()
    for name in name_contents:
        list_of_names.append(name.strip("\n"))


with open("Day 24 file handling/Day's exercise/Input/Letters/starting_letter.txt") as letter:
    x = letter.read()
    for name in list_of_names:
        with open(f"Day 24 file handling/Day's exercise/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as to_be_sent:
            to_be_sent.write(x.replace(PLACEHOLDER, name).replace("Angela", "Dani"))
