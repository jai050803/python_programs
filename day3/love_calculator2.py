print("\n.... Try this love calculator to know how much compatible you are together....\n")

print("\n...Try out....\n")

name1 = input("\nEnter Your full name :")
name2 = input("Enter your partners full Name :")

combined_names = name1+name2

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

e = combined_names.count("e")
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")

ones = t + r + u + e
tens = l + o + v + e

score = tens*10 + ones

print(f"your score is {score}")

if score <=20:
    print("you are just okay together")
elif score in range(21, 50):
    print("you are a normal couple")
elif score in range(50, 80):
    print("wow! you both love each other a lot")
else:
    print("your relationship is made in heaven")