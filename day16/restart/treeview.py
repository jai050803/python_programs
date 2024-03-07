import tkinter as tk
from tkinter import ttk

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

# Create the main window
root = tk.Tk()
root.title("Pokemon Data")

# Create a Treeview widget
tree = ttk.Treeview(root)

# Define our columns
columns = list(data.keys())
tree['columns'] = columns

# Format our columns
tree.column("#0", width=0, stretch=tk.NO)  # This represents the first column which is hidden by default
for col in columns:
    tree.column(col, anchor=tk.CENTER, width=80)

# Create headings
for col in columns:
    tree.heading(col, text=col, anchor=tk.CENTER)

# Adding data to the treeview
for i in range(len(data["Pokemon name"])):
    values = [data[col][i] for col in columns]
    tree.insert("", tk.END, values=values)

# Pack the treeview finally
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()
