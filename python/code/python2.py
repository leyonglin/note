
# def power2(x):
# 	return x**2

# for x in map(power2, range(1, 10)):
# 	print(x)

# print(sum(map(lambda x: x**2, range(1, 10))))
# def mypow(x,y):
# 	return x**y
# for i in map(mypow,[1,2,3,4],(4,3,2,1)):
# 	print(i)

# L=[1,-2,5,-3]
# L1=sorted(L,key=abs,reverse=True)
# print(L1)

# s='1+2+3'
# print(eval(s))

# def func(a, b, *args):    
# 	print(a, b)           
# 	print(len(args), args)
# 	#return sum(args)     
# #func()
# func(0, 1, 2, 3)     #args输出的是元组

# # 求阶乘
# def myfac(n):
# 	#用递归来实现 5！ = 5 * 4！
# 	if n == 1:
# 		return 1 
# 	return n * myfac(n-1)
# print(myfac(5))

# def make_power(y):
# 	def fn(x):
# 		return x ** y
# 	return fn
# pow2 = make_power(2)
# print('5的平方是：', pow2(5))

# #阶乘和
# def jiecheng(n):
# 	if n == 1:
# 		return 1
# 	return n * jiecheng(n-1)
# # def all_sum(n):
# # 	if n == 1:
# # 		return 1 
# # 	return jiecheng(n) + all_sum(jiecheng(n-1))

# L = []
# n = int(input("num:" ))
# # for i in range(1,n+1):
# # 	print(jiecheng(i))
# for i in range(1, n+1):
# 	L.append(jiecheng(i))
# print(L)	
# print(sum(L))

# 杨辉三角未完成
# def eline(n):
# 	if n == 1:
# 		return [1]
# 	L2 = [1]
# 	for i in range(1,n):
# 		L2.append(L[i] + L[i-1])
# 	L2.append(1)
# 	return L2
# n = 4
# L = [1, 3, 3, 1]
# print(eline(4))
# # L2 = [1, 4, 6, 4, 1]

# def mydeco(fn):            #装饰器函数
# 	def fx():
# 		print('1')
# 		fn()
# 		print('2')
# 	return fx

# @mydeco          
# def  myfun():
# 	 print('myfun')

# #@mydeco 相当于myfunc()被调用了后，先fn=myfun 再myfun=mydeco(myfun)   
# myfun()

# def  chengfabiao(n):
# 	for i in range(1,n+1):
# 		for j in range(1,i+1):
# 			if j<=i:
# 				print("%d*%d=%d\t" % (i,j,i*j),end=' ')
# 		print()
# chengfabiao(5)

# L=[1,3,5]
# it=iter(L)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# def myyield():  #生成器函数
# 	yield 2
# 	yield 3
# 	print(1)
# 	yield 5
# 	print(10)
# gen = myyield()   #调用生成器函数来创建一个生成器
# it = iter(gen)    #用生成器获取对应的迭代器
# print(next(it))   #访问迭代器，每次访问，从上一个yield语句之后执行直至yield语句为止
# print(next(it))   #访问迭代器
# print(next(it))   #访问迭代器,会打印出1和5，1是函数内print(1)打印出来的，5是print(next(it))
# print(next(it))   #输出10，但由于没有yield语句，会报错StopIteration

# L1=[1,2,3,4]
# L2=['a','b','c']
# for t in enumerate(L2,2):
# 	print(t)

# def myfactorial(n):
# 	s=1                     #只传递一次
# 	for x in range(1,n+1):
# 		s*=x
# 		yield s             #保留上次s的值

# print(list(myfactorial(5)))

# L = { x + str(y) for x in 'ABC' for y in range(6) if y % 2 ==1 }
# print(L)

# t = tuple(range(5))
# print(t)

# def say_hello():  
# 	return 2      
# 	print("hello world")
# 	return 1
# # say_hello()				
# v=say_hello()			
# print(v)				

# import sys
# print(sys.stdin.readline())           #从键盘读取
# sys.stdout.write("标准输出\n")         #标准输出
# sys.stderr.write("错误输出\n")         #错误输出

# try
#     fr=open('mynote.txt', 'rb')  #二进制读方式打开
#     b = fr.read()                #返回字节串，不会自动解码
#     print(b)
#     fr.close()
# except OSError:
# 	print("打开文件失败")

# try:
# 	fbw = open('mybinary.bin', 'wb')   #二进制写入文件
#     s = '你好'                         #输入字符串
#     b=s.encode('utf-8')                #对字符串进行编码，不编码会报错
#     fbw.write(b)
#     fbw.close()
#     print('文件写入成功')
# except OSError:
# 	print("打开文件失败")