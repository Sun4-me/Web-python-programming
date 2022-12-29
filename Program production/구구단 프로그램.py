listMatrix=[]

for i in range(1,10):
    line=[]
    for k in range(1,10):
        line.append(str(i * k).center(5))
    listMatrix.append(line)     

for i in range(0,9):
    print(listMatrix[i])
    

  