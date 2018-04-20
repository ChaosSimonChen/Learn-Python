height = float(input('请输入您的身高，单位为米：'))
weight = float(input('请输入您的体重，单位为千克：'))	#忘了加float函数的话就会报错，input函数取的str字符类型
bmi = weight/(height*height)
print('你的BMI指数为%.2f' % bmi)
if bmi <= 18.5:
	print('过轻')
elif bmi <=	25:
	print('正常')
elif bmi <= 28:
	print('过重')
elif bmi <= 32:
	print('肥胖')
else:
	print('严重肥胖')