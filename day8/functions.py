def greet():
    print("hello")
    print(f"hello {input("type your name :")}")

greet()

#function that allows the input

def greet_with_name(name):
    print(f"hello {name}")
    print("how are you doing today")
    
greet_with_name("jai") #take one input for our function

def greet_with(name,area):
    print(f"hello {name} from {area}")

greet_with("jai","delhi") #positional arguement


#keyword arguement

greet_with(name="Jai", area = "New Delhi")