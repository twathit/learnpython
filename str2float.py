def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':0}[s]
    for i in range(len(s)):
        if s[i]=='.':
            L=list(map(char2num,s[i+1:]))
            L.reverse()
            return reduce(lambda x,y:x*10+y,map(char2num,s[:i]))+(reduce(lambda x,y:x*0.1+y,L))*0.1