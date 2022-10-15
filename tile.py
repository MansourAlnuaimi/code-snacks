CENTI = 10**(-2)     # centi = 10^-2 of the unit
# Room's dimensions
rLength = float(input("Room's length (m): "))
rWidth = float(input("Room's width (m): "))

# Tile's dimension;  convert cm -> m
tLength = float(input("\nTile's length (cm): "))*CENTI
tWidth = float(input("Tile's width (cm): "))*CENTI

# Calculating areas
rArea = rLength * rWidth
tArea = tLength * tWidth

# calculating how many tiles for the room
tile_quantity = round(rArea / tArea, 2)

# output 
print(f'\nYou will need {tile_quantity} tiles.')
