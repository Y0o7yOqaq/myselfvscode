# 赋值运算符
# 执行顺序：右->左
# 支持链式赋值       a=b=c=20
# 支持参数赋值       +=、-=、*=、/=、//=%=
# 支持系列解包赋值   a,b,c=20,30,40

a = b = c = 20
d = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))  # 变量a,b,c的内存地址相同
print(d, id(d))
print('\r')

a, b, c = 20, 30, 40   # 符号两边个数要相同，且变量和值一一对应
print(a)
print(b)
print(c)
print('\r')

print('交换之前', a, b)
a, b = b, a
print('交换之后', a, b)           # 交换两个变量的值
