# YOUR NAME(S)
# 7th Grade Computer Science
# Caesar Cipher Program
# TODAY’S DATE
# Caesar Cipher Program
# Caesar Cipher program will ask for a user input and the key they want to shift
# And encrypt/decrypt accordingly

message = input("Enter your message to encrypt: ")
shift = int(input("How many letters to shift by? "))
encrypted = ""

for letter in message:
    if letter.islower():
        shifted = (ord(letter) - ord('a') + shift) % 26
        encrypted += chr(shifted + ord('a'))
    else:
        encrypted += letter  # leave everything else unchanged (for now)

print("Encrypted message:", encrypted)
