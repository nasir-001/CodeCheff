"""
Now that Chef has finished baking and frosting
his cupcakes, it's time to package them.
Chef has N cupcakes, and needs to decide how many
cupcakes to place in each package. Each package
must contain the same number of cupcakes.
Chef will choose an integer A between 1 and N, inclusive,
and place exactly A cupcakes into each package.
Chef makes as many packages as possible. Chef then gets
to eat the remaining cupcakes. Chef enjoys eating cupcakes very much.
Help Chef choose the package size A that will let him eat as many cupcakes as possible.

For each test case, output the package size that
will maximize the number of leftover cupcakes.
If multiple package sizes will result in the same number
of leftover cupcakes, print the largest such size.
"""

def main():

	cake_list = []

	user_input = int(input())

	for a in range(user_input):
		cake = cake_list.append(int(input()))

	for a in cake_list:
		mini = min(cake_list)
		if a == mini:
			print(a)
		else:
			if a > mini:
				print(a-mini)

if __name__ == "__main__":
	main()