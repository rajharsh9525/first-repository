for i in range(10,40):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")