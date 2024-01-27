def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
dictionary = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

n1 = int(input("enter the first number : "))
for j in dictionary.keys():
    print(j)
operations = input("Pick the operation from above example : ")
if operations in dictionary.keys():
    n2 = int(input("enter the second number : "))
    operation_function = dictionary[operations]
    answer1 = operation_function(n1,n2)
    print(f"{n1} {operations} {n2} = {answer1}")
    operation2 = input("Pick another operation from above: ")
    n3 = int(input("enter the third number : "))
    answer2 = operation_function(answer1,n3)
    print(f"{answer1} {operation2} {n3} = {answer2}")
    
    
    
else:
    print("invalid operator")
