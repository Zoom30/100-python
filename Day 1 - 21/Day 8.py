import math

# def greet_with(name, location):
#     print(f"hello {name}, welcome to {location}")

# greet_with(location="Earth")
# ========================================================================
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width)/cover)
#     print(f"You'll need {number_of_cans} of paint")

# paint_calc(test_h, test_w, coverage)
# ========================================================================
# n = int(input("Check this number: "))
# def prime_checker(number):
#     num_times_divided_without_remainder = 0
#     for x in range(1, number + 1):

#         if number % x == 0:
#             num_times_divided_without_remainder += 1
#     if num_times_divided_without_remainder == 2:
#         print("It is prime")
#     else:
#         print("It is not prime")


# prime_checker(n)
# ========================================================================
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt_decrypt, type 'decode' to decrypt:\n")
coding = True
while coding:
    text = input("Type your message:\n").lower()
    if text == "exit()":
        coding = False
    else:
        shift = int(input("Type the shift number:\n"))
        direction = input("Would you like to encode or decode your text? (e - encode or d - decode) \n")
        if direction == "e":
            shift *= 1
        else:
            shift *= -1


        def encrypt_decrypt(text, shift):

            list_of_text = list(text)
            list_of_encrypted_text = []

            for n in range(0, len(list_of_text)):
                if list_of_text[n] == " " or list_of_text[n] not in alphabet:
                    list_of_encrypted_text.append(list_of_text[n])

                elif not list_of_text[n] == " " and list_of_text[n] in alphabet:
                    current_alphabet_index = alphabet.index(list_of_text[n])
                    encrypted_location = current_alphabet_index + shift

                    if encrypted_location < 26:
                        while encrypted_location < 0:
                            encrypted_location += 26
                        list_of_encrypted_text.append(alphabet[encrypted_location])
                    else:
                        while encrypted_location > 26:
                            if encrypted_location > 26:
                                encrypted_location -= 26
                        list_of_encrypted_text.append(alphabet[encrypted_location])
            print("".join(list_of_encrypted_text))


        encrypt_decrypt(text, shift)
