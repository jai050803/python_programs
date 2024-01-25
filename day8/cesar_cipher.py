#project

#part 1 - encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    for char in text:
        pos = text.index(char) #initial position of character
        new_pos = pos + shift
        if new_pos > len(alphabet):
            new_pos = new_pos - len(alphabet)
        new_char = alphabet[new_pos]
        text = text.replace(char,new_char)
    print(text)
    
