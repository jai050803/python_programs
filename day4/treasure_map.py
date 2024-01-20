print("\n....Can Your reach to the treasure hidden?......\n")

print("..use map position to reach to the final destination")
print('''columns   1    2    3
a         a1   a2   a3   
b         b1   b2   b3
c         c1   c2   c3''')

print("\n..enter the column and row number to get the treasure.. its all about luck....")
print("\n...you will get three chances....")
row1 = ["👎","👎","👎"]
row2 = ["👎","👎","👎"] 
row3 = ["👎","🎁","👎"]
lst = [row1,row2,row3]
found = 0
for i in range(0,3):
    a = input("\nenter the row and column (a1,b1..) :")
    rows = a[0].lower()
    col = int(a[1])
    row = 0
    if a == "a":
        row = 0
    elif a == "b":
        row = 1
    else:
        row = 2
    
    if lst[col][row-1] == "👎":
        print(f"you lost...{lst[col][row-1]}")
    else:
        print(f"you found the treasure {lst[col][row-1]}.. well done")
        found = 1
        break

if found == 0:
    print("\noops! you tried all your three chances.. but failed to find the treasure..")