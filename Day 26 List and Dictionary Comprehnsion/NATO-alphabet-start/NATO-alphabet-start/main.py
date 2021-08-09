import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

phonetic_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# print(phonetic_alphabet_df)

p_a_dict = {row["letter"]: row["code"] for (index, row) in phonetic_alphabet_df.iterrows()}
print(p_a_dict["G"])


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    name = input("What is your name: ").upper()
    try:
        test_list = [p_a_dict[letter] for letter in name]

    except KeyError:
        print("Sorry, only letters")
        generate_phonetic()
    else:
        print(test_list)


generate_phonetic()
