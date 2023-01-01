def decideLarger(a,b) :
    if a!=b :
        if a > b :
            return a
        if a < b : 
            return b
    else : 
        return "a=b"
    
a = int(input(prompt= "정수를 입력하세요: "))
b = int(input(prompt= "정수를 입력하세요: "))

print(decideLarger(a,b))