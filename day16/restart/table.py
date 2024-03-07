import pandas as pd

data = {
    "Pokemon name" : ["Pikachu", "Squirtle", "Charmender"],
    "Type" : ["Electric", "Water", "Fire"],
    "Total" : [90, 60, 80],
    "HP" : [90, 60, 80],
    "Attack" : [90, 60, 80],
    "Defense" : [90, 60, 80],
    "Sp. Atk" : [90, 60, 80],
    "Sp. Def" : [90, 60, 80],
    "Speed" : [90, 60, 80]
}

df = pd.DataFrame(data)
print(df)