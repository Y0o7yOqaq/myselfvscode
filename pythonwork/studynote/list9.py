# 列表生成式
"""
[ i*i for i in range(1,10)]
i:表示列表元素的表达式(例如：i，i*i等)
i:自定义变量
range:可迭代对象
"""
lst = [i for i in range(1, 11)]
print(lst)
lst = [i*i for i in range(1, 11)]
print(lst)
lst = [i % 2 == 0 for i in range(1, 11)]
print(lst)
