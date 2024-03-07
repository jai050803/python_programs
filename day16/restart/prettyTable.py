from prettytable import PrettyTable

# Your data
data = {
    "Pokemon name": ["Pikachu", "Squirtle", "Charmender"],
    "Type": ["Electric", "Water", "Fire"],
    "Total": [90, 60, 80],
    "HP": [90, 60, 80],
    "Attack": [90, 60, 80],
    "Defense": [90, 60, 80],
    "Sp. Atk": [90, 60, 80],
    "Sp. Def": [90, 60, 80],
    "Speed": [90, 60, 80]
}

# Initialize PrettyTable with the columns
columns = list(data.keys())
table = PrettyTable()
table.field_names = columns

# Add rows to the table
for i in range(len(data["Pokemon name"])):
    row = [data[col][i] for col in columns]  # Extract each row's data
    table.add_row(row)

# Print the table
print(table)
