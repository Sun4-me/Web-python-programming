def decideNumber(intNumber) :
    if intNumber / 2 == 1:
        return "Even number"
    else :
        return "Odd number"

userInput=int(input(prompt = "정수를 입력하세요: "))

print(decideNumber(userInput))


