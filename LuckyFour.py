# Authur: Nasir Lawal
# Date: 11th-Aug-2019

"""
Problem Source: <== CodeCheff ==>
"""

def main():
	user_input = int(input())
	for a in range(user_input):
		num_list = input()
		count = 0
		for n in num_list:
			if n == "4":
				count += 1
		print(count)
if __name__ == "__main__":
	main()