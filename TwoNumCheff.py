# Authur: Nasir Lawal
# Date: 5th-Aug-2019

"""
The input begins with two positive integers 
n k (n, k<=107). The next n lines of input contain
one positive integer ti, not greater than 109, each.
"""
# Problem Source: <== CodeCheff ==>

def main():
	user_input = int(input())
	for a in range(user_input):
		new = input()
		seperate = new.split()
		first = int(seperate[0])
		second = int(seperate[1])
		answer = first + second
		print(answer)


if __name__ == "__main__":
	main()