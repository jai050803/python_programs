print("\n......... calculate the amount of tip you should give........\n\n")

bill = input("what was the total bill in rupees ? ")
tip = input("what percentage tip would you like to give ? ")
members = input("how many people to split the bill ? ")

tip_amount = int(bill) * (int(tip) / 100)
total_bill = int(bill) + tip_amount

split = int(total_bill) / int(members)

print(f"each person should pay : {split} rupees")