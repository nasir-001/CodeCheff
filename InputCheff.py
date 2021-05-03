# Authur: Nasir Lawal
# Date: 4th-Aug-2019

"""
The input begins with two positive integers n k (n, k<=107).
The next n lines of input contain one positive integer ti, 
not greater than 109, each.

Write a single integer to output, 
denoting how many integers ti are divisible by k.
"""

# Problem Source: <== CodeCheff ==>

def main():

	user_input = input("Enter the number here: ")
	seperate = user_input.split()
	ti = 0
	n = int(seperate[0])
	k = int(seperate[1])

	

	for i in range(n):
		z = int(input("Another: "))
		if z % k == 0:
			ti += 1
	print(ti)

if __name__ == "__main__":
	main()