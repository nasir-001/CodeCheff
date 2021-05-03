def main():

	import string
	user_input = int(input())
	for a in range(user_input):
		while True:
			for b in range(user_input):
				if a * b == user_input:
					print("1 " + str(user_input))
					print(a, b)
					print(str(user_input) + " 1")
			
			break

if __name__ == "__main__":
	main()