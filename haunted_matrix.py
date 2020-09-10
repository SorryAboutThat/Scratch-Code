def matrixElementsSum(m):
    r = len(m)
    c = len(m[0])
    total=0
    for j in range(c):
        #print(j)
        for i in range(r):
            #print(i)
            if m[i][j]!=0:
                total+=m[i][j]
                print(total)
            else:
                break
    return total
    

print(matrixElementsSum([[0,1,1,2], [0,5,0,0], [2,0,3,3]]))
