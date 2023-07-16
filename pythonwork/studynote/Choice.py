# 选择结构

# 单分支结构
"""
if 条件表达式：
   条件执行体
 """

money = 1000  # 余额
s = int(input('请输入取款金额：'))  # 取款金额
if money >= s:
    money = money-s
    print('取款成功，余额为:', money)
print('\t')

# 双分支结构(双选一)
"""
if 条件表达式:
    条件执行体1
else:
    条件执行体2
 """
num = int(input('请输入一个整数：'))
if num % 2 == 0:
    print(num, '是偶数')
else:
    print(num, '是奇数')
print('\t')

# 多分支结构(多选一)
"""
if 条件表达式1:
    条件执行体1
elif 条件表达式2:
    条件执行体2
.    .
.    .
.    .
elif 条件表达式n:
    条件执行体n
[else:
    条件执行体n+1]   else可写可不写
"""
score = float(input('请输入你的成绩:'))
if 90 <= score <= 100:    # 在python中可以这么写
    print('A')
elif score >= 60 and score <= 89:
    print('B')
elif score >= 0 and score <= 59:
    print('C')
else:
    print('数据非法！')
