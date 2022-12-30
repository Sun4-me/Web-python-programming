
"""
(a) 1에서 9 사이의 숫자(1과 9 포함) 중 하나를 랜덤하게 생성합니다.
(b) 사용자에게 숫자를 추측하여 입력하게 하고, 입력한 수가 생성된 수보다 큰지, 작은지, 같은지를 알립니다.
(c) 사용자가 생성된 수와 같은 수를 입력할 때까지 프로그램은 끝나지 않고 반복됩니다.
"""

import random
intRandom = random.randrange(0, 10)

while True:
    userInput = int(input())
    if(userInput > intRandom):
        print("You entered large number.")
    elif(userInput < intRandom):
        print("You entered small number.")
    else:
        print("Matched!")
        break