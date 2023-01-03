"""
(a) dictionary의 key는 유일해야 하지만 value는 유일하지 않아도 됩니다.
(b) count_values() 라는 이름의 함수를 구현합니다.
(c) count_values() 함수는 하나의 dictionary를 입력 파라메타로 받아서, 이 dictionary가 포함한 서로 다른 value의 개수를 반환합니다.
(d) 예를 들어, {'red': 1, 'green': 1, 'blue': 2}가 입력 파라메타로 전달되면, 2를 반환합니다.

"""

def count_values(givenDict):
    A = []
    for item in givenDict:
        if(A.count(givenDict[item]) == 0):
            A.append(givenDict[item])
    return len(A)

print(count_values({'red': 1, 'green': 1, 'blue': 2}))



