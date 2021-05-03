# Authur: Nasir Lawal
# Date: 14th-Aug-2019
"""
Problem Source: <== CodeCheff ==>
"""

user_input = int(input())

even_num = 0
odd_num = 0

num = list(map(int, input().strip().split()))

for a in num:
	if a % 2 == 0:
		even_num += 1
	else:
		odd_num += 1

if even_num > odd_num:
	print("READY FOR BATTLE")
else:
	print("NOT READY")
