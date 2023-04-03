# Define the Caesar Cipher functions
def encrypt(text, key):
    result = ""

    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        # Do not encrypt spaces or other characters
        else:
            result += char

    return result


def decrypt(ciphertext, key):
    result = ""

    for char in ciphertext:
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - key - 97) % 26 + 97)
        # Do not decrypt spaces or other characters
        else:
            result += char

    return result


# Test the Caesar Cipher code with a message
message = "This is a secret message"
key = 3

# Encrypt the message
ciphertext = encrypt(message, key)
print("Encrypted ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_message = decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message)
