print("\n .. find highest score from list of numbers...\n")

print(".. just a replicate of max function using for loops.....")

scores = input("type marks here :").split()

for i in scores:
    scores[scores.index(i)] = int(i)

highest = scores[0]

for i in scores:
    if i > highest:
        highest = i

print(f"highest score is {highest}")