# Authur: Nasir Lawal
# Date: 23-05-2022

'''
After a very long time, the Chef has a vacation. Chef has planned for two trips during this vacation - one 
with his family and the other with his friends. The family trip will take X days and the trip with friends 
will take Y days. Currently, the dates are not decided but the vacation will last only for Z days.

Chef can be in at most one trip at any time and once a trip is started, Chef must complete 
it before the vacation ends. Will Chef be able to go on both these trips if he chooses the dates optimally?
'''

def main():
    test_cases = int(input())
    for i in range(test_cases):
        days = list(map(int, input().split(" ")))
        family = days[0]
        freinds = days[1]
        total = days[2]
        familyAndFriends = family + freinds
        if familyAndFriends <= total:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()