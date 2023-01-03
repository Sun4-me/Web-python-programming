"""
(a) 다음과 같이 list 하나는 프로그래밍 언어를, 다른 list는 언어의 개발자 이름을 갖도록 선언합니다.

language = ["python", "c++", "javascript", "go"]
author = ["Guido van Rossum", "Bjarne Stroustrup", "Brendan Eich", "Robert Griesemer"]
(b) 함수 matingPairs()를 만드는데, 입력 파라메타로 위의 두 리스트를 받아서, 결과롤 set 타입을 돌려줍니다.
(c) 함수 matingPairs()는 두 리스트에서 각각 하나의 값을 꺼내서 언어 이름별 저자의 tuple을 만든 후,
(d) 함수 matingPairs() 안의 내부 변수인 set 타입 데이터 타입에 (c)에서 만든 tuple을 아이템으로 추가해 줍니다.
(e) 모든 언어에 대한 저자 매핑과, 이를 set에 넣는 과정을 마치면, 함수 matingPairs()은 결과값으로 set를 돌려줍니다.
(f) 함수 matingPairs()의 결과값을 화면에 출력합니다.

"""
language = ["python", "c++", "javascript", "go"]
author = ["Guido van Rossum", "Bjarne Stroustrup", "Brendan Eich", "Robert Griesemer"]

def matingPairs(listLanguage, listAuthor) :
    newSet = set()
    for v in range(len(listLanguage)):
        newSet.add((language[v], listAuthor[v]))
    return newSet

setResult = matingPairs(language, author)

print(type(setResult), setResult)