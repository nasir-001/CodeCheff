# Authur: Nasir Lawal
# Date: 11th-Aug-2019

# Problem Source: <== CodeCheff ==>

def main():
	user_input = int(input())
	for a in range(user_input):
		num = int(input())
		if num < 10:
			print("What an obedient servant you are!")
		else:
			print(-1)
if __name__ == "__main__":
	main()