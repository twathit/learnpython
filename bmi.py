weight=float(input('please input your weight:'))
height=float(input('please input your height:'))
name=input('please input your name:')
print('%s,your weight is %dkg,your height is %dm,and your bmi is...' %(name,weight,height))
bmi = weight/height**2
if bmi<=18.5:
    print('过轻')
elif bmi<=25:
    print('正常')
elif bmi<=28:
    print('过重')
elif bmi<=32:
    print('肥胖')
else:
    print('严重肥胖')