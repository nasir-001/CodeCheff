def main():

	user_input = int(input())

	for n in range(user_input):
		num = int(input())
		second = num
		reverse = 0
		while num > 0:
			digit = num % 10
			reverse = reverse * 10 + digit
			num = num // 10
		print(reverse)

if __name__ == "__main__":
	main()