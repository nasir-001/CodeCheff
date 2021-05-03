# Authur: Nasir Lawal
# Date: 5th-Aug-2019

"""
Description:


"""
user_input = int(input())
num_list = []

for b in range(user_input):
	num_list.append(int(input()))
num_list.sort()

for i in num_list:
	print(i)