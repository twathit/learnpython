import os
def find_file(path,str):
    #L1=[x for x in os.listdir(path) if os.path.isfile(x) and str in x]
    #for x in L1:
        #print(os.path.join(path,x)
    for x in os.listdir(path):
        if os.path.isfile(x) and str in x:
            print(os.path.join(path,x))
        if os.path.isdir(x):
            find_file(os.path.join(path,x),str)

find_file(r'e:/python','co')