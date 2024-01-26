#project

#part 1 - encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    cipher_text = ""
    new_text = text.replace(" ", "")
    for char in new_text:
        position = alphabet.index(char)
        new_index = position + shift
        cipher_text += alphabet[new_index]
    
    return cipher_text
encrypt(text,shift)
    
