
"""
(a) 앞서 숫자 추측 게임 개발하기 (1) 문제와 반대되는 문제입니다.
(b) 이번에는 사용자(당신)가 0에서 100 사이 숫자 중 하나를 골라 머리 속에 기억합니다.
(c) 프로그램이 그 숫자가 무엇인지 맞히도록 합니다.
(d) 프로그램이 숫자를 guess할때마다 사용자는 그 숫자가 자신이 생각한 수 보다 큰지(2), 작은지(0), 혹은 똑같은지(1) 입력합니다.
(e) 프로그램이 숫자를 맞히면 종료됩니다.
"""

import random

limitLow = 1
limitHigh = 101

while True :
    intRandom = random.randrange(limitLow,limitHigh)
    print("MY GUESS: ", intRandom)
    userInput=int(input())
    if userInput == 2 :
        limitLow = intRandom+1
    
    elif userInput == 0 :
        limitHigh = intRandom
    
    else :
        print("I got it!!")
        break

