#project

#part 1 - encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    cipher_text = ""
    for char in text:
        if char ==" ":
            cipher_text = cipher_text + " "
            continue
        position = alphabet.index(char)
        new_index = position + shift
        if new_index in range(0, len(alphabet)):
            cipher_text += alphabet[new_index]
        elif new_index >= len(alphabet):
            index_n = new_index - len(alphabet)
            cipher_text += alphabet[index_n]
    
    print(cipher_text)

def decrypt(text,shift):
    cipher_text = ""
    for char in text:
        if char ==" ":
            cipher_text = cipher_text + " "
            continue
        position = alphabet.index(char)
        new_index = position - shift
        # if new_index in range(0, len(alphabet)):
        cipher_text += alphabet[new_index]
        # elif new_index >= len(alphabet):
        #     index_n = new_index + len(alphabet)
            # cipher_text += alphabet[index_n]
    print(cipher_text)
    
if direction == "encode":
    encrypt(text,shift)
    
if direction == "decode":
    decrypt(text,shift)
    
