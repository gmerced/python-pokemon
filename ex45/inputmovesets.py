from sys import argv

next_entry = "Y"
target = open("C:\Users\Gerard\Desktop\pokemon1.txt", "w")

while next_entry.upper() == "Y":

	level_moveset = []
	tmhm_moveset = []
	pokemon_name = raw_input("Pokemon Name: ")
	
	raw_level_moveset = raw_input("Moves by level? (Separate each move with a comma and space): ").split(", ")
	for move in raw_level_moveset:
		if move not in level_moveset:
			level_moveset.append(move)
	
	raw_tmhm_moveset = raw_input("Moves by TM/HM? (Separate each move with a comma and space): ").split(", ")
	for move in raw_tmhm_moveset:
		if move not in tmhm_moveset:
			tmhm_moveset.append(move)
	
	target.write("\t\"")
	target.write(pokemon_name)
	target.write("\": {\n")
	target.write("\t\t\t\t\"MOVESET\": {\n")
	target.write("\t\t\t\t\t\"MOVES BY LEVEL\": [")
	
	for move in level_moveset:
	
		target.write("\n\t\t\t\t\t\t\"")
		target.write(move)
		target.write("\"")
		if move != level_moveset[len(level_moveset)-1]:
			target.write(",")

	target.write("]},\n")
	target.write("\t\t\t\t\t\"MOVES BY TM/HM\": [")
	
	for move in tmhm_moveset:
	
		target.write("\n\t\t\t\t\t\t\"")
		target.write(move)
		target.write("\"")
		if move != tmhm_moveset[len(tmhm_moveset)-1]:
			target.write(",")
	
	target.write("]},\n")
	
	next_entry = raw_input("Continue? ")

target.close()
