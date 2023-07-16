# 1.转义字符 反斜杠+想要实现的转移功能的字符

print('http:\\\\baidu.com ')
print(' \'大家好\' ')
print(' \"大家好\" ')
# 2.当字符串中包含反斜杠、单引号和双引号等有特殊用途的符号时，必须使用反斜杠对这些字符进行转义
# 单引号 “ \' ”
# 双引号 “ \"" ”
# 反斜杠 “ \\ ” 等

print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')  # 输出world
print('hello\bworld')
# 3.当字符串中包含换行、回车、水平制表符或退格符等无法直接表示的特殊字符
# 换行 “ \n ”
# 回车 “ \r ” 回车：将光标移至当前行的第一格
# 水平制表符 “ \t ”
# 退格 “ \b ”

print(r'hello\nworld')
print(R'hello\nworld')
print(r'hello\\world')
print(r'new life\new world')
# 原字符，不希望字符串中的转义字符起作用，只是用原字符，就在字符串前加r或R

'''
print(r'hello\nworld\')
注意事项：最后一个字符不能为\
eerfwaerf
'''

print(chr(0b100111001011000))  # 0b表示该数字为二进制 chr(i)函数：返回整数i对应的字符
print(ord('乘'))               # ord("字符"/'字符')：返回对应的ASCII码值
print('乘')
