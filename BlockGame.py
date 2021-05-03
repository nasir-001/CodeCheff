# Authur: Nasir Lawal
# Date: 26-Aug-2019

"""
Problem Source <== CodeCheff ==>
"""


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

		if (second == reverse):
			print("wins")
		else:
			print("losses")

if __name__ == "__main__":
	main()