# initialize CurrentPlayerPokemon and CurrentOpponentPokemon as dictionaries with keys
# right off the bat.
"""
CurrentPlayerPokemon {
	"Name": '',
	"TYPE1": '',
	"TYPE2": '',
	"MOVE1": '',
	"MOVE2": '',
	"MOVE3": '',
	"MOVE4": '',
	"CURRENT ATTACK": '',
	"CURRENT DEFENSE": '',
	"CURRENT SPECIAL": '',
	"CURRENT SPEED": '',
	"CURRENT ACCURACY": '',
	"CURRENT EVASION": '',
	"CURRENT CRITICAL": ''}
"""
	

def fight(CurrentPlayerPokemon, CurrentOpponentPokemon, PlayerParty, OpponentParty, Turn):
	
	from random import sample
	
	if Turn == 0:
		Move1 = PlayerParty[CurrentPlayerPokemon.keys()[0]]["MOVESET"][0]
		Move2 = PlayerParty[CurrentPlayerPokemon.keys()[0]]["MOVESET"][1]
		Move3 = PlayerParty[CurrentPlayerPokemon.keys()[0]]["MOVESET"][2]
		Move4 = PlayerParty[CurrentPlayerPokemon.keys()[0]]["MOVESET"][3]
		OpponentMove1 = OpponentParty[CurrentOpponentPokemon.keys()[0]]["MOVESET"][0]
		OpponentMove2 = OpponentParty[CurrentOpponentPokemon.keys()[0]]["MOVESET"][1]
		OpponentMove3 = OpponentParty[CurrentOpponentPokemon.keys()[0]]["MOVESET"][2]
		OpponentMove4 = OpponentParty[CurrentOpponentPokemon.keys()[0]]["MOVESET"][3]
		CurrentAttack = PlayerParty[CurrentPlayerPokemon.keys()[0]]["BASE STATS"]["BASE ATTACK"]
		CurrentDefense = PlayerParty[CurrentPlayerPokemon.keys()[0]]["BASE STATS"]["BASE DEFENSE"]
		CurrentSpecial = PlayerParty[CurrentPlayerPokemon.keys()[0]]["BASE STATS"]["BASE SPECIAL"]
		CurrentSpeed = PlayerParty[CurrentPlayerPokemon.keys()[0]]["BASE STATS"]["BASE SPEED"]
		CurrentAccuracy = PlayerParty[CurrentPlayerPokemon.keys()[0]]["BASE STATS"]["BASE ACCURACY"]
		CurrentEvasion = PlayerParty[CurrentPlayerPokemon.keys()[0]]["BASE STATS"]["BASE EVASION"]
		CurrentCritical = PlayerParty[CurrentPlayerPokemon.keys()[0]]["BASE STATS"]["BASE CRITICAL"]
		OpponentAttack = PlayerParty[CurrentOpponentPokemon.keys()[0]]["BASE STATS"]["BASE ATTACK"]
		OpponentDefense = PlayerParty[CurrentOpponentPokemon.keys()[0]]["BASE STATS"]["BASE DEFENSE"]
		OpponentSpecial = PlayerParty[CurrentOpponentPokemon.keys()[0]]["BASE STATS"]["BASE SPECIAL"]
		OpponentSpeed = PlayerParty[CurrentOpponentPokemon.keys()[0]]["BASE STATS"]["BASE SPEED"]
		OpponentAccuracy = PlayerParty[CurrentOpponentPokemon.keys()[0]]["BASE STATS"]["BASE ACCURACY"]
		OpponentEvasion = PlayerParty[CurrentOpponentPokemon.keys()[0]]["BASE STATS"]["BASE EVASION"]
		OpponentCritical = PlayerParty[CurrentOpponentPokemon.keys()[0]]["BASE STATS"]["BASE CRITICAL"]
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["MOVE1"] = Move1
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["MOVE2"] = Move2
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["MOVE3"] = Move3
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["MOVE4"] = Move4
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["CURRENT ATTACK"] = CurrentAttack
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["CURRENT DEFENSE"] = CurrentDefense
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["CURRENT SPECIAL"] = CurrentSpecial
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["CURRENT SPEED"] = CurrentSpeed
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["CURRENT ACCURACY"] = CurrentAccuracy
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["CURRENT EVASION"] = CurrentEvasion
		CurrentPlayerPokemon[CurrentPlayerPokemon.keys()[0]]["CURRENT CRITICAL"] = CurrentCritical
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["MOVE1"] = OpponentMove1
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["MOVE2"] = OpponentMove2
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["MOVE3"] = OpponentMove3
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["MOVE4"] = OpponentMove4
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["CURRENT ATTACK"] = OpponentAttack
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["CURRENT DEFENSE"] = OpponentDefense
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["CURRENT SPECIAL"] = OpponentSpecial
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["CURRENT SPEED"] = OpponentSpeed
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["CURRENT ACCURACY"] = OpponentAccuracy
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["CURRENT EVASION"] = OpponentEvasion
		CurrentOpponentPokemon[CurrentOpponentPokemon.keys()[0]]["CURRENT CRITICAL"] = OpponentCritical
	
	print "Moves: \t%s\n\t%s\n\t%s\n\t%s" % (Move1, Move2, Move3, Move4)
	PlayerMove = raw_input("Enter the move you would like to use: ").upper()
	OpponentMove = sample([OpponentMove1, OpponentMove2, OpponentMove3, OpponentMove4], 1)[0]
	
	return CurrentPlayerPokemon, CurrentOpponentPokemon, PlayerParty, OpponentParty
	
	
def battle(player, opponent):

	from random import randint
	from random import sample
	from pokemon import Gen1PokemonStats
	from pokemon import Gen1PokemonMovesets
	PlayerParty = {}
	OpponentParty = {}
	
	for player_pokemon in player["Party"]:
		PlayerParty[player_pokemon] = Gen1PokemonStats[player_pokemon]
		MinHP = Gen1PokemonStats[player_pokemon]["BASE STATS"]["BASE HP"]["MIN HP"]
		MaxHP = Gen1PokemonStats[player_pokemon]["BASE STATS"]["BASE HP"]["MAX HP"]
		MinAttack = Gen1PokemonStats[player_pokemon]["BASE STATS"]["BASE ATTACK"]["MIN ATTACK"]
		MaxAttack = Gen1PokemonStats[player_pokemon]["BASE STATS"]["BASE ATTACK"]["MAX ATTACK"]
		MinDefense = Gen1PokemonStats[player_pokemon]["BASE STATS"]["BASE DEFENSE"]["MIN DEFENSE"]
		MaxDefense = Gen1PokemonStats[player_pokemon]["BASE STATS"]["BASE DEFENSE"]["MAX DEFENSE"]
		MinSpecial = Gen1PokemonStats[player_pokemon]["BASE STATS"]["BASE SPECIAL"]["MIN SPECIAL"]
		MaxSpecial = Gen1PokemonStats[player_pokemon]["BASE STATS"]["BASE SPECIAL"]["MAX SPECIAL"]
		MinSpeed = Gen1PokemonStats[player_pokemon]["BASE STATS"]["BASE SPEED"]["MIN SPEED"]
		MaxSpeed = Gen1PokemonStats[player_pokemon]["BASE STATS"]["BASE SPEED"]["MAX SPEED"]
		PlayerParty[player_pokemon]["BASE STATS"]["BASE HP"] = randint(MinHP, MaxHP)
		PlayerParty[player_pokemon]["BASE STATS"]["BASE ATTACK"] = randint(MinAttack, MaxAttack)
		PlayerParty[player_pokemon]["BASE STATS"]["BASE DEFENSE"] = randint(MinDefense, MaxDefense)
		PlayerParty[player_pokemon]["BASE STATS"]["BASE SPECIAL"] = randint(MinSpecial, MaxSpecial)
		PlayerParty[player_pokemon]["BASE STATS"]["BASE SPEED"] = randint(MinSpeed, MaxSpeed)
		PlayerParty[player_pokemon]["BASE STATS"]["BASE ACCURACY"] = 1
		PlayerParty[player_pokemon]["BASE STATS"]["BASE EVASION"] = 1
		PlayerParty[player_pokemon]["BASE STATS"]["BASE CRITICAL"] = PlayerParty[player_pokemon]["BASE STATS"]["BASE SPEED"] / 512.0
		MovesByLevel = Gen1PokemonMovesets[player_pokemon]["MOVESET"]["MOVES BY LEVEL"]
		MovesByTMHM = Gen1PokemonMovesets[player_pokemon]["MOVESET"]["MOVES BY TM/HM"]
		PlayerParty[player_pokemon]["MOVESET"] = sample(MovesByLevel, 2) + sample(MovesByTMHM, 2)
	
	for opponent_pokemon in opponent["Party"]:
		OpponentParty[opponent_pokemon] = Gen1PokemonStats[opponent_pokemon]
		MinHP = Gen1PokemonStats[opponent_pokemon]["BASE STATS"]["BASE HP"]["MIN HP"]
		MaxHP = Gen1PokemonStats[opponent_pokemon]["BASE STATS"]["BASE HP"]["MAX HP"]
		MinAttack = Gen1PokemonStats[opponent_pokemon]["BASE STATS"]["BASE ATTACK"]["MIN ATTACK"]
		MaxAttack = Gen1PokemonStats[opponent_pokemon]["BASE STATS"]["BASE ATTACK"]["MAX ATTACK"]
		MinDefense = Gen1PokemonStats[opponent_pokemon]["BASE STATS"]["BASE DEFENSE"]["MIN DEFENSE"]
		MaxDefense = Gen1PokemonStats[opponent_pokemon]["BASE STATS"]["BASE DEFENSE"]["MAX DEFENSE"]
		MinSpecial = Gen1PokemonStats[opponent_pokemon]["BASE STATS"]["BASE SPECIAL"]["MIN SPECIAL"]
		MaxSpecial = Gen1PokemonStats[opponent_pokemon]["BASE STATS"]["BASE SPECIAL"]["MAX SPECIAL"]
		MinSpeed = Gen1PokemonStats[opponent_pokemon]["BASE STATS"]["BASE SPEED"]["MIN SPEED"]
		MaxSpeed = Gen1PokemonStats[opponent_pokemon]["BASE STATS"]["BASE SPEED"]["MAX SPEED"]
		OpponentParty[opponent_pokemon]["BASE STATS"]["BASE HP"] = randint(MinHP, MaxHP)
		OpponentParty[opponent_pokemon]["BASE STATS"]["BASE ATTACK"] = randint(MinAttack, MaxAttack)
		OpponentParty[opponent_pokemon]["BASE STATS"]["BASE DEFENSE"] = randint(MinDefense, MaxDefense)
		OpponentParty[opponent_pokemon]["BASE STATS"]["BASE SPECIAL"] = randint(MinSpecial, MaxSpecial)
		OpponentParty[opponent_pokemon]["BASE STATS"]["BASE SPEED"] = randint(MinSpeed, MaxSpeed)
		OpponentParty[opponent_pokemon]["BASE STATS"]["BASE ACCURACY"] = 1
		OpponentParty[opponent_pokemon]["BASE STATS"]["BASE EVASION"] = 1
		OpponentParty[opponent_pokemon]["BASE STATS"]["BASE CRITICAL"] = OpponentParty[opponent_pokemon]["BASE STATS"]["BASE SPEED"] / 512.0
		MovesByLevel = Gen1PokemonMovesets[opponent_pokemon]["MOVESET"]["MOVES BY LEVEL"]
		MovesByTMHM = Gen1PokemonMovesets[opponent_pokemon]["MOVESET"]["MOVES BY TM/HM"]
		OpponentParty[opponent_pokemon]["MOVESET"] = sample(MovesByLevel, 2) + sample(MovesByTMHM, 2)
	
	Turn = 0
	CurrentPlayerPokemon = {PlayerParty.keys()[0]: {}}
	CurrentOpponentPokemon = {OpponentParty.keys()[0]: {}}
	print "%s wants to fight!" % opponent["Name"]
	print "%s sent out %s!" % (opponent["Name"], CurrentOpponentPokemon.keys()[0])
	print "Go! %s!" % CurrentPlayerPokemon.keys()[0]
	while player["Party Fainted"] == False and opponent["Party Fainted"] == False:
		print "What will you do?"
		print "Fight or switch Pokemon?"
		Move = ''
		while Move.upper() != "FIGHT" and Move.upper() != "PKMN":
			Move = raw_input("Enter \'Fight\' to fight or \'PKMN\' to switch Pokemon: ")
		if Move.upper() == "FIGHT":
				# figure out body
		elif Move.upper() == "PKMN":
				# figure out body
		Turn += 1