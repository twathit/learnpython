def triangles():
    t=[1]   
    while True:
        yield t
        t.append(0)
        t=[t[i-1]+t[i] for i in range(len(t))]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break