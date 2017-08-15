def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c,'2')
        print(a,b,c)
        return
    move(n-1,a,c,b)
    print(a,b,c)
    print('move',a,'-->',c,'1')
    move(n-1,b,a,c)
    #move(3,A,B,C)
    #MOVE(2,A,C,B)
    #MOVE(1,A,B,C)
    #<
    #MOVE(1,C,A,B)
    #MOVE(2,B,A,C)
    #MOVE(1,B,C,A)
    #<
    #MOVE(1,A,B,C)