#######first question######
##########################
# Caesar cipher algorithm
###########################


# Assumptions:
# - Non-alphabetic characters are left as they are.
# - No distinction is made between uppercase and lowercase for alphabetical characters.
# - The result is always returned in uppercase, as per the requested output.
# The user is prompted to enter a correct key until a valid key is provided.

# pip install pyperclip
#need to install
import pyperclip # used pyperclip  library for  clipboard operations

import pyperclip

# Caesar cipher algorithm
def caesar_cipher(text, key, mode):
    result = ""
    for char in text:
        #check if character is alphabetic
        if char.isalpha():
            #chr(...): Converts the ASCII value back to a character.
            #ord(char.upper()): Retrieves the ASCII value of the uppercase letter.
            #  Computes the new position for Caesar encryption or decryption.
            #  This expression represents a shift of key positions on the ASCII values of uppercase letters.
            result += chr((ord(char.upper()) + key - 65) % 26 + 65) if mode == 'e' else chr((ord(char.upper()) - key - 65) % 26 + 65)
        else:
            # Directly append non-alphabetic characters to result
            result += char

    return result

# Main function
def main():
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    #get input from user for the action
    mode = input("> ").lower()

    if mode not in ['e', 'd']:
        print("Invalid choice. Exiting.")
        return

    while True:
        try:
            if mode == 'e':
                #ask for the key encryption
                key = int(input("Please enter the key (0 to 25) to use: "))
            else:
                # ask for the key decryption
                key = int(input("Please enter the key (0 to 26) to use: "))
            if not (0 <= key <= 26):
                print("Invalid key. Key must be in the range of 0 to 25 for encryption or 0 to 26 for decryption. Please enter a valid key.")
                continue
            break
        except ValueError:
            print("Invalid key. Please enter a valid key.")

    message = input("Enter the message: ")

    if mode == 'e':
        # Work in encryption mode
        encrypted_text = caesar_cipher(message, key, 'e')
        print(f"Full encrypted text: {encrypted_text}")
        pyperclip.copy(encrypted_text)
        print("Full encrypted text copied to clipboard.")
    else:
        # Work in decryption mode
        decrypted_text = caesar_cipher(message, key, 'd')
        print(f"Full decrypted text: {decrypted_text}")
        pyperclip.copy(decrypted_text)
        print("Full decrypted text copied to clipboard.")

if __name__ == "__main__":
    main()
