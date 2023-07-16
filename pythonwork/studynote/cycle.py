# 嵌套循环
""" 输出一个三行四列的矩阵 """
for _ in range(3):
    for _ in range(4):
        print('*', end=' ')  # 不换行输出
    print('\t')  # 换行

print('\t')
""" 输出一个99乘法表 """
for i in range(9):
    for j in range(i+1):
        print(i, '*', j, '=', i*j, end='\t')  # 不换行输出
    print('\t')  # 换行
