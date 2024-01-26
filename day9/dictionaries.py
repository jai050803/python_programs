programming_dictionary = {
    "Bug" : "An error in a program that prevent the program from running as expected",
    "Function" : "A piece of code that you can easily call over and over again",
    "Loop" : "The action of doing something over and over again"
}

#adding an item in dictionary

programming_dictionary['program'] = "A set of instructions given to computer to perform a particular task"

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])  
