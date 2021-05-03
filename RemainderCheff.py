# Authur: Nasir Lawal
# Date: 7th-Aug-2019

"""Description
The first line contains an integer T, 
total number of test cases. Then follow T lines,
each line contains two Integers A and B.
Find remainder when A is divided by B.
"""

def main():
	user_input = int(input())
	for a in range(user_input):
		num = input()
		sep = num.split()
		first = int(sep[0])
		second = int(sep[1])
		answer = first % second
		print(answer)

if __name__ == "__main__":
	main()