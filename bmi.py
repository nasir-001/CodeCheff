# Authur: Nasir Lawal
# Date: 22-05-2022

'''
You are given the height HHH (in metres) and mass MMM (in kilograms) of Chef. The Body Mass Index (BMI) of a person is computed as M*2.

Report the category into which Chef falls, based on his BMI:

    Category 1: Underweight if BMI ≤18\leq 18≤18
    Category 2: Normal weight if BMI ∈{19\in \{19∈{19, 202020,…\ldots…, 24}24\}24}
    Category 3: Overweight if BMI ∈{25\in \{25∈{25, 262626,…\ldots…, 29}29\}29}
    Category 4: Obesity if BMI ≥30\geq 30≥30
'''

def main():
    test_cases = int(input())
    for i in range(test_cases):
        bmi = list(map(int, input().split(" ")))
        m = bmi[0]
        h = bmi[1]
        computed = m // h ** 2
        if computed <= 18:
            print('1')
        elif computed > 18 and computed <= 24:
            print('2')
        elif computed > 24 and computed <= 29:
            print('3')
        elif computed >= 30:
            print('4')

if __name__ == '__main__':
    main()