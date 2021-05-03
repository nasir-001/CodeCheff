def main():

	user_input = int(input())

	for a in range(user_input):
		ID = input()
		if ID == "B" or ID == "b":
			print("BattleShip")
		elif ID == "C" or ID == "c":
			print("Cruiser")
		elif ID == "D" or ID == "d":
			print("Destroyer")
		elif ID == "F" or ID == "f":
			print("Frigate")

if __name__ == "__main__":
	main()