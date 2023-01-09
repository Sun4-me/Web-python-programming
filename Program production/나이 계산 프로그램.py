def calcAge(currentAge, currentYear, comingYear):
    return currentAge + (comingYear - currentYear)

userName = input()
userCurrentAge = int(input())
currentYear = int(input())

strAnswer = userName + " is " + str(userCurrentAge) + \
            " years old."
print(strAnswer)

strAnswer = userName + " becoms " + str(calcAge(userCurrentAge, currentYear, currentYear+10)) + \
            " years old after 10 years."
print(strAnswer)

strAnswer = userName + " becoms " + str(calcAge(userCurrentAge, currentYear, 2098)) + \
            " years old in 2098."
print(strAnswer)