# Authur: Nasir Lawal
# Date: 8th-2019

""" Description
The first line of the input contains an integer T, 
the number of test cases. T lines follow. Each T contains
an integer N whose square root needs to be computed.
For each line of input output the square root of the input integer.
"""

import math
def main():

	user_input = int(input())
	for a in range(user_input):
		num = int(input())
		print("{:.0f}".format(math.sqrt(num)))

if __name__ == "__main__":
	main()