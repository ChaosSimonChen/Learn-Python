# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
	if not(isinstance(a and b and c,(int,float))):
		raise TypeError('bad orerand type')
	n = b**2-4*a*c
	if n < 0:
		print('无解')
	elif a == 0:
		x = -c/b
		return x
	elif n == 0:
		x = -b/2/a
		return x
	else:
		x1 = (-b+math.sqrt(n))/2/a
		x2 = (-b-math.sqrt(n))/2/a
		return x1,x2 
	
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
