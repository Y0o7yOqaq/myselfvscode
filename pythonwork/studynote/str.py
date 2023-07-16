# 字符串称为不可变的字符序列
# 可以使用单引号、双引号、三引号(""" """/''' ''')来定义
# 单引号和双引号定义的字符串必须在一行
# 三引号定义的字符串可以分布在连续的多行
str1 = 'hello world'
str2 = "hello world"
str3 = """hello
world"""
str4 = '''hello
world'''
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))
