# Made by: Guillaume Amorim
# November/16/2026
# Class: Intro to programming, COSC1100
# Assignment 2: Secret Codes (Arrays & Functions)

# PROBLEM:
# Create a simple Python application that lets a user encode English text into Al Bhed,
# or decode Al Bhed text back into English, using a substitution cipher that can be
# repeated a number of times set by a key.

# INPUTS:
# Menu choice: "1" to encode, "2" to decode, or "3" to exit.
# Enter the text to be encoded when option 1 is selected, and enter text to be decoded when option 2 is selected.
# Key: how many times to run the cipher used by the encode and decode functions, default is set to 1.

# OUTPUTS:
# Output will be based on the main menu option selected, 
# "1" will display the encoded text, 
# "2" will display the decoded text,
# "3" will exit program.
# Invalid menu choice will produce an Error message

# PLAN(PSEUDOCODE):
# Define constants: ENGLISH_ALPHABET and AL_BHED_ALPHABET
# 
# Define encode(message, key=1):
#   Set current_text to message
#   Repeat key number of times:
#       Start with empty string called encrypted_string
#       For each letter_index, counting up from 0 to the length of input: current_text
#           Assume that there is no match found (match_found = False)
#           For each alphabet_index in English alphabet:
#               If the letter at letter_index matches the letter at alphabet_index:
#                   Add the Al Bhed letter at alphabet_index to the encrypted_string
#                   Set match_found to True
#           If after going through whole alphabet, match_found is False
#               Add the original letter at letter_index to the encrypted string
#       Set current_text to encrypted_string
#   Return current_text
# 
# Define decode(message, key=1):
#   Same as the steps we did for encode, but instead we match against Al Bhed alphabet
#   Match the letter positioning of English alphabet

# Main program:
#   Define start() to hold the menu loop
#   Keep showing the menu until the user chooses to exit
#   Each time, display the three options: encode, decode, or exit
#   Ask the user to pick an option
#   If the user picks menu option 1:
#       Ask for the text the user wishes to encode
#       Encode the input and print the result
#   If the user picks menu option 2:
#       Ask for the text to decode
#       Decode the input and print the result
#   If the user picks 3:
#       End the program
#   Validation:
#   If user does not select a valid choice, tell the user input is invalid and show the menu again
#   Call start() at the bottom of the file to run the program

# PROGRAM:
# Constants:
ENGLISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
AL_BHED_ALPHABET = "YPLTAVKREZGMSHUBXNCDIJFQOWypltavkrezgmshubxncdijfqow"


def encode(message, key=1):
    current_text = message

    for count in range(key):
        encrypted_string = ""

        # Check each of the character in the message
        for letter_index in range(len(current_text)):
            match_found = False

            # Comparing to each character in the English alphabet
            for alphabet_index in range(len(ENGLISH_ALPHABET)):
                if current_text[letter_index] == ENGLISH_ALPHABET[alphabet_index]:
                    encrypted_string += AL_BHED_ALPHABET[alphabet_index]
                    match_found = True

            # Keep non-alphabet characters like spaces and punctuations
            if not match_found:
                encrypted_string += current_text[letter_index]

        current_text = encrypted_string

    return current_text


def decode(message, key=1):
    current_text = message

    # Decode the message 'key' number of times
    for count in range(key):
        decrypted_string = ""

        # Check each character in the message
        for letter_index in range(len(current_text)):
            match_found = False

            # Compare to each character in the Al Bhed alphabet
            for alphabet_index in range(len(AL_BHED_ALPHABET)):
                if current_text[letter_index] == AL_BHED_ALPHABET[alphabet_index]:
                    decrypted_string += ENGLISH_ALPHABET[alphabet_index]
                    match_found = True

            # Keep non-alphabet chracter
            if not match_found:
                decrypted_string += current_text[letter_index]

        current_text = decrypted_string

    return current_text


# This is where the main program starts:
# Defined start() to keep showing the menu until user chooses to exit.
def start():
    is_running = True

    while is_running:
        print()
        print("1) Encode text")
        print("2) Decode text")
        print("3) Exit program")
        menu_choice = input("Please select an option (1-3): ")

        if menu_choice == "1":
            user_text = input("Please enter the text to encode: ")
            encoded_result = encode(user_text)
            print(f"Encoded text: {encoded_result}")

        elif menu_choice == "2":
            user_text = input("Please enter the text to decode: ")
            decoded_result = decode(user_text)
            print(f"Decoded text: {decoded_result}")

        elif menu_choice == "3":
            is_running = False

        else:
            print()
            print("Please select a valid option between 1 and 3.")


start()

# DESKCHECK:
# Menu choice 1, 2 or 3: runs encode, decode or exit
# Any other input such as "4","0" or "a", or just pressing Enter):
#   outputs "Please select a valid option between 1 and 3." and shows the menu again.
#
# Option 1, text to encode: Hello, it's nice to meet you.
#   Expected according to Sample Output: Rammu, ed'c hela du saad oui.
#   Actual: Rammu, ed'c hela du saad oui.
#
# Option 2, text to decode: Rammu, ed'c hela du saad oui.
#   Expected According to Sample Output: Hello, it's nice to meet you.
#   Actual: Hello, it's nice to meet you.
#
# Option 3: the program exits.