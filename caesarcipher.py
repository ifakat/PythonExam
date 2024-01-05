import pyperclip

# Caesar cipher algorithm
def caesar_cipher(text, key, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                # Encrypt or decrypt uppercase letters
                result += chr((ord(char) + key - 65) % 26 + 65) if mode == 'e' else chr((ord(char) - key - 65) % 26 + 65)
            else:
                # Encrypt or decrypt lowercase letters
                result += chr((ord(char) + key - 97) % 26 + 97) if mode == 'e' else chr((ord(char) - key - 97) % 26 + 97)
        else:
            # Directly append non-alphabetic characters
            result += char

    return result

# Main function
def main():
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    mode = input("> ").lower()

    if mode not in ['e', 'd']:
        print("Invalid choice. Exiting.")
        return

    while True:
        try:
            if mode == 'e':
                key = int(input("Please enter the key (0 to 25) to use: "))
            else:
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
        print(f"Full encrypted text: {encrypted_text.upper()}")
        pyperclip.copy(encrypted_text)
        print("Full encrypted text copied to clipboard.")
    else:
        # Work in decryption mode
        decrypted_text = caesar_cipher(message, key, 'd')
        print(f"Full decrypted text: {decrypted_text.upper()}")
        pyperclip.copy(decrypted_text)
        print("Full decrypted text copied to clipboard.")

if __name__ == "__main__":
    main()