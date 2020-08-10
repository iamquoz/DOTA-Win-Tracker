import requests
from os import system, name
import matplotlib.pyplot as plt

def conclear(): 
	# windows 
	if name == 'nt': 
		_ = system('cls') 
	# unix
	else: 
		_ = system('clear') 

conclear()

def check_input(msg, upper_limit):
	x = input(msg)
	while (not x.isdigit()) or int(x) > upper_limit:
		print("\nInput is either not a number or goes above the limit of", upper_limit)
		x = input(msg)
	return int(x)

account_id = check_input("Enter your account ID: ", 1000000000)

queries = {}


def change_queries(queries):
	conclear()
	print("Would you like to change some of the queries?\n\nOptions include: \n the max amouut of games you'd want to parse, \n patch, \n played hero, \n lobby type")
	choice = check_input("Enter 1 if you'd want to, enter anything else to not change anything (default is every game you've played): ", 10000000000)
	if choice != 1:
		return queries
	else:
		while True:
			choice = check_input("\nEnter 1-4 to change one of the aforementioned queries, 5 to exit: ", 5)
			if choice == 1: 

				queries["limit"] = check_input("\nEnter the amount of matches you want to parse: ", 100000)

			elif choice == 2: 

				patches_data = requests.get('https://raw.githubusercontent.com/odota/dotaconstants/master/build/patch.json')

				patches = patches_data.json()

				print("Patches and corresponding IDs: \n")

				for patch in patches:
					if int(patch["id"]) % 20 == 0 and int(patch["id"]) != 0:
						input ("Next page on input")
						conclear()
					print(patch["name"], " - ", patch["id"])

				queries["patch"] = check_input("\nEnter the patch id: ", int(patches[-1]["id"])) # should always return the element in an array of patches that is obtained through opendota

			elif choice == 3: 

				heroes_data = requests.get('https://raw.githubusercontent.com/odota/dotaconstants/master/build/heroes.json')

				heroes = heroes_data.json()

				print("Heroes and corresponding IDs:")

				for hero in heroes:
					hero_data = heroes[hero]
					if int(hero) % 20 == 0:
						input("Next page on input")
						conclear()
					print(hero_data["localized_name"], " - ", hero_data["id"])

				queries["hero_id"] = check_input("\nEnter the hero id: ", int(hero_data["id"])) # hero_data will always be the latest added to Dota hero, using this because for some reason heroes[-1] didn't work.

			elif choice == 4:

				lobbies_data = requests.get('https://raw.githubusercontent.com/odota/dotaconstants/master/build/lobby_type.json')

				lobbies = lobbies_data.json()

				print("Lobbies and corresponding IDs: \n")

				for lobby in lobbies:
					lobby_info = lobbies[lobby]
					print(lobby_info["name"], " - ", lobby_info["id"]) # same as hero_data

				queries["lobby_type"] = check_input("Enter the lobby id: ", int(lobby_info["id"]))

			else:
				break
	return queries

change_queries(queries)

res = requests.get(f'https://api.opendota.com/api/players/{account_id}/Matches', params = queries)

data = res.json()

def check_wins(data):
	match_results = []
	for matches in data:
		if matches['radiant_win'] == True and matches['player_slot'] <= 127:
			match_results.append('Win')
		elif matches['radiant_win'] == False and matches['player_slot'] > 127:
			match_results.append('Win')
		else:
			match_results.append('Loss')
	match_results.reverse() #reverses list to set origin from furthest back requested match
	return match_results

wins = check_wins(data)

def wins_numerically(match_results): #converts list with history of win loss into plot points for scatter plot +1
									 #for a win, -1 for a loss
	match_history = [0]
	for results in match_results:
		if results == 'Win':
			match_history.append(match_history[-1] + 1)
		else:
			match_history.append(match_history[-1] - 1)
	return match_history

results = wins_numerically(wins)

plt.scatter(range(len(results)), results)
plt.plot(range(len(results)), results)

plt.show()
