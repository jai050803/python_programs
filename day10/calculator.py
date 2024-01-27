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
print(dictionary)

# resume = True
# while resume == True:
#     n1 = int(input("enter the first number : "))
#     print("+ \n- \n* \n/")
#     op = input("enter the operator : ")
#     n2 = int(input("enter the second number : "))
#     if op == "+":
#         print(add(n1,n2))
#     elif op == "-":
#         print(subtract(n1,n2))
#     elif op == "*":
#         print(multiply(n1,n2))
#     elif op == "/":
#         print(divide(n1,n2))
#     else:
#         print("invalid operator")
#     cont = input("do you want to continue y/n : ").lower()
#     if cont == "n":
#         resume == False