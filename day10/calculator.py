def add(n1,n2):
    """
    Adds two numbers together and returns the result.
    """
    return n1+n2
def subtract(n1,n2):
    """
    Subtracts two numbers and returns the result.
    Parameters:
    - n1: a number
    - n2: a number
    Return type: a number
    """
    return n1-n2
def multiply(n1,n2):
    """
    Multiplies two numbers and returns the result.
    Parameters:
    - n1: first number (int or float)
    - n2: second number (int or float)
    Returns:
    - product of n1 and n2 (int or float)
    """
    return n1*n2
def divide(n1,n2):
    """
    A function to divide two numbers and return the result.
    Parameters:
    - n1: the numerator (dividend)
    - n2: the denominator (divisor)
    Return:
    - The result of dividing n1 by n2
    """
    return n1/n2
dictionary = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    n1 = float(input("enter the first number : "))
    for j in dictionary.keys():
        print(j)
    should_continue = True
    while should_continue == True:
        operations = input("Pick the operation from above example : ")
        if operations in dictionary.keys():
            n2 = int(input("enter the second number : "))
            operation_function = dictionary[operations]
            answer1 = operation_function(n1,n2)
            print(f"{n1} {operations} {n2} = {answer1}")
        else:
            print("invalid operator")
        
        if input("do you want to continue with same answer (y/n)? ") == "y":
            n1 = answer1
        else:
            should_continue = False
        
calculator()
