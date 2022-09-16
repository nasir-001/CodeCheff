# Authur: Nasir Lawal
# Date: 22-05-2022

'''
Chef is struggling to pass a certain college course.

The test has a total of NNN question, each question carries 333 marks for a correct answer and 
-1 for an incorrect answer. Chef is a risk-averse person so he decided to attempt all the questions. 
It is known that Chef got X questions correct and the rest of them incorrect. For Chef to pass the 
course he must score at least PPP marks.

Will Chef be able to pass the exam or not?
'''

def main():
    test_cases = int(input())
    for i in range(test_cases):
        scores = list(map(int, input().split(" ")))
        n = scores[0]
        x = scores[1]
        p = scores[2]
        passes = x * 3
        losses = n - x
        expect = passes - losses
        if expect >= p:
            print('PASS')
        else:
            print('FAIL')

if __name__ == '__main__':
    main()