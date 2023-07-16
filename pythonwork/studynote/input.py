# input()函数
# 作用：接收来自用户的输入
# 值类型：输入值的类型为str
# 值的储存：使用=对输入的值进行储存
present = input('你要干什么？')
print('\r')
print(present, type(present))

# 练习
a = input('请输入一个加数:')
b = input('请输入另一个加数:')
print(int(a)+int(b))
