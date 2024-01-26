#project

#part 1 - encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(text,shift):
    cipher_text = ""
    for char in text:
        if char ==" ":
            cipher_text = cipher_text + " "
            continue
        position = alphabet.index(char)
        if direction == "encode":
            new_pos = position + shift
            if new_pos in range(0,len(alphabet)):
                cipher_text += alphabet[new_pos]
            else:
                cipher_text += alphabet[new_pos - len(alphabet)]
        elif direction == "decode":
            new_pos = position - shift
            cipher_text += alphabet[new_pos]
        else:
            print("Invalid input try again")
            input("Type 'encode' or 'decode' to encrypt or decrypt:\n").lower()
            
            
    print(cipher_text)

ceasar(text,shift)