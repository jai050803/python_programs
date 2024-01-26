from logo import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("\n......Welcome to cesar cipher...... \n")

def ceasar(text,shift,direction):
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = position + shift
            if new_pos in range(-len(alphabet),len(alphabet)):
                cipher_text += alphabet[new_pos]
            else:
                cipher_text += alphabet[new_pos - len(alphabet)]
        else:
            cipher_text += char
                
    print(f"your {direction}d text is: {cipher_text}")
    
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text=text,shift=shift,direction=direction)
    rerun = input("\n..do you want to re-run the program(y/n)?\n").lower()
    if shift > 26:
        shift = shift % 26
    if rerun == "n":
        should_continue = False
        print("goodbye")
    

