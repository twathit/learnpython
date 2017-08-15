def is_palindrome(n):
    s=str(n)
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    L=list(map(char2num,s))
    return L==L[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
