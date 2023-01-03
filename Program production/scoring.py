############################################################
# (A) ANSWER START
#1
def addInteger(a,b):
    return int(a+b)

#2
def addFloat(a,b):
    return float(a+b)

#3
def addFloatToString(a,b):
    return str(float(a+b))

#4
def addFloatToStringList(a,b):
    return [a,b,a+b]

#5
def calcGugudanToListInList(a):
    danlist=[]
    for i in range(1,10):
        danlist.append([a,i,a*i])
    return danlist






# (A) ANSWER END
############################################################

############################################################
# (B) STANDARD ANSWER START


def standard_addInteger(lvalue, rvalue):
    return lvalue + rvalue


def standard_addFloat(lvalue, rvalue):
    return float(lvalue + rvalue)


def standard_addFloatToString(lvalue, rvalue):
    return "{}".format(float(lvalue + rvalue))


def standard_addFloatToStringListv1(lvalue, rvalue):
    tmp = []
    tmp.append(str(lvalue))
    tmp.append(str(rvalue))
    tmp.append("{}".format(float(lvalue + rvalue)))
    return tmp


def standard_addFloatToStringListv2(lvalue, rvalue):
    tmp = []
    tmp.append(str(lvalue))
    tmp.append(str(rvalue))
    tmp.append("{}".format(lvalue + rvalue))
    return tmp


def standard_calcGugudanToListInList(dan):
    tmpOuter = []
    tmpInner = []
    for i in range(1, 10):
        tmpInner.append(dan)
        tmpInner.append(i)
        tmpInner.append(dan*i)
        tmpOuter.append(tmpInner)
        tmpInner = []
    return tmpOuter

# (B) STANDARD ANSWER END
############################################################

############################################################
# (C) SCORING START


totalScore = 0


def printAnswers(yourAnser, rightAnswer):
    print("     Your Answer  : (", yourAnser, ") -->", type(yourAnser))
    print("     Right Answer : (", rightAnswer, ") -->", type(rightAnswer))


try:
    lv = 3
    rv = 6
    res = standard_addInteger(lv, rv)

    result = addInteger(lv, rv)

    if result == res:
        totalScore += 1
        print("[01] Question - Correct [+1].")
        printAnswers(result, res)
    else:
        print("[01] Question - Fail.")
        printAnswers(result, res)
except:
    print("[01] Question - Exception.")

try:
    lv = 3
    rv = 6.0
    res = standard_addFloat(lv, rv)

    result = addFloat(lv, rv)

    if result == res:
        totalScore += 1
        print("[02] Question - Correct [+1].")
        printAnswers(result, res)
    else:
        print("[02] Question - Fail.")
        printAnswers(result, res)
except:
    print("[02] Question - Exception.")

try:
    lv = 3
    rv = 6.0
    res = standard_addFloatToString(lv, rv)

    result = addFloatToString(lv, rv)

    if result == res:
        totalScore += 2
        print("[03] Question - Correct [+2].")
        printAnswers(result, res)
    else:
        print("[03] Question - Fail.")
        printAnswers(result, res)
except:
    print("[03] Question - Exception.")

try:
    lv = 3
    rv = 6.0
    res1 = standard_addFloatToStringListv1(lv, rv)
    res2 = standard_addFloatToStringListv2(lv, rv)

    result = addFloatToStringList(lv, rv)

    if result == res1 or result == res2:
        totalScore += 3
        print("[04] Question - Correct [+3].")
        printAnswers(result, str(res1) + " OR " + str(res2))
    else:
        print("[04] Question - Fail.")
        printAnswers(result, str(res1) + " OR " + str(res2))
except:
    print("[04] Question - Exception.")

try:
    dan = 3
    res = standard_calcGugudanToListInList(dan)

    result = calcGugudanToListInList(dan)

    if result == res:
        totalScore += 3
        print("[05] Question - Correct [+3].")
        printAnswers(result, res)
    else:
        print("[05] Question - Fail.")
        printAnswers(result, res)
except:
    print("[05] Question - Exception.")

print("[**] Total Score : ", totalScore, "(MAX: 10)")

# (C) SCORING END
############################################################