# Authur: Nasir Lawal
# Date: 25-05-2022

'''
Suppose Chef is stuck on an island and currently he has x units of food supply and y units of water supply 
in total that he could collect from the island. He needs xr​ units of food supply and yr​ units of water 
supply per day at the minimal to have sufficient energy to build a boat from the woods and also to live 
for another day. Assuming it takes exactly D days to build the boat and reach the shore, tell whether 
Chef has the sufficient amount of supplies to be able to reach the shore by building the boat?
'''

def main(): 
    test_cases = int(input())

    for i in range(test_cases):
        samplesList = []
        requirements = list(map(int, input().split(" ")))
        foodS = requirements[0]
        waterS = requirements[1]
        foodR = requirements[2]
        waterR = requirements[3]
        daysR = requirements[4]
        foods = foodS / foodR
        water = waterS / waterR
        samplesList.append(foods)
        samplesList.append(water)
        if min(samplesList) >= daysR:
            print("Yes")
        else:
            print("NO")

if __name__ == '__main__':
    main()