# Hilda Liu
# 7th Grade Computer Science
# Caesar Cipher Program
# 5/1/25
# This program lets the user encrypt or decrypt messages
# using a Caesar Cipher. It loops until the user types "quit",
# only accepts shift keys from 1 to 25, and leaves
# numbers, spaces, and symbols unchanged.

while True:
    option = input("Type 'encrypt', 'decrypt', or 'quit': ").lower()
    if option == "quit":
        print("Goodbye!")
        break
    if option != "encrypt" and option != "decrypt":
        print("Invalid option. Please type 'encrypt', 'decrypt', or 'quit'.")
        continue
    
    shift = int(input("Enter shift amount (1–25): "))
    letters_count = 0
    symbols_count = 0
    if shift < 1 or shift > 26:
        print("Please enter a number between 1 and 25.")
        continue
    
    message = input("Enter your message: ")

    
    result = ""

    # Process each character
    for letter in message:
        # Encrypt or decrypt
        if option == "encrypt":
            if letter.islower():
                shifted = (ord(letter) - ord('a') + shift) % 26
                result += chr(shifted + ord('a'))
                letters_count += 1
            elif letter.isupper():
                shifted = (ord(letter) - ord('A') + shift) % 26
                result += chr(shifted + ord('A'))
                letters_count += 1
            else:
                # Non-letter characters are unchanged
                result += letter
                symbols_count += 1
        else:  # decrypt
            if letter.islower():
                shifted = (ord(letter) - ord('a') - shift) % 26
                result += chr(shifted + ord('a'))
                letters_count += 1
            elif letter.isupper():
                shifted = (ord(letter) - ord('A') - shift) % 26
                result += chr(shifted + ord('A'))
                letters_count += 1
            else:
                # Non-letter characters are unchanged
                result += letter
                symbols_count += 1

    # Display the result
    if option == "encrypt":
        print("Encrypted message:", result)
        print("You encrypted", letters_count, "letters and ignored", symbols_count, "symbols, numbers, and space.")
    else:
        print("Decrypted message:", result)
        print("You decrypted", letters_count, "letters and ignored", symbols_count, "symbols, numbers, and space.")