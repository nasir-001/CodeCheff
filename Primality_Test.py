# Authur: Nasir Lawal
# Date: 14-2019

"""
Problem Source <== CodeCheff ==>
"""

def main():
	user_input = int(input())

	for i in range(user_input):
		num = int(input())

		variable = 0
		for i in range(1, num):
			if num % i == 0:
				variable += 1
			if variable > 2:
				break
		if variable > 2:
			print("no")
		else:
			print("yes")

if __name__ == "__main__":
	main()