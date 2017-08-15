import math
a,b,c=map(int,input('Please input a,b,c:').split(','))
def quadratic(a, b, c):

   d=b*b-4*a*c
   if a==0:
      return 'a不能为0'
   else:
      if d<0:
         return '无解'
      else:
         x1=(-b+math.sqrt(d))/(2*a)
         x2=(-b-math.sqrt(d))/(2*a)
         return x1,x2
# 测试:
print(quadratic(a,b,c))		 
#print(quadratic(0,1,1))
#print(quadratic(2,1,1))
#print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
#print(quadratic(1, 3, -4)) # => (1.0, -4.0)