# Aurthur: Nasir Lawal
# Date: 8th-Aug-2019

"""

"""

user_input = int(input())

for a in range(user_input):
	num_list = list(map(int, input()))
	first = num_list[0]
	last = num_list[-1]
	answer = first + last
	print(answer)
