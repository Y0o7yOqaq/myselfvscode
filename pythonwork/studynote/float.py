from decimal import Decimal    # 解决方法：导入模块decimal
a = 3.14159
print(a, type(a))        # 浮点数据储存时有不精确性
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1+n2)                # 使用浮点数进行计算时，可能会出现小数位数不确定的情况
print(n1+n3)
print('\r')

print(Decimal('1.1')+Decimal('2.2'))
