def makeBirthdayString(socialSecurityNumber):
    birthYear = int(socialSecurityNumber[0:2]) + 1900
    birthMonth = int(socialSecurityNumber[2:4]) 
    birthDay = int(socialSecurityNumber[4:6])
    strAnswer = "당신의 생일은 " + str(birthYear) + "년 " + str(birthMonth) + "월 " + str(birthDay) + "일 입니다"
    return strAnswer

userInput = input()

resultRight = makeBirthdayString(userInput)
print(resultRight)