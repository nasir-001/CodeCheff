def main():
	user_input = int(input())

	for a in range(user_input):
		new = input()
		sep = list(map(int, new))
		print(sum(sep))

if __name__ == "__main__":
	main()