# 位运算符 将数据转成二进制进行计算
# 位与 & 对应数位都为1，结果数位才为1，否则结果数位为0
# 位或 | 对应数位都为0，结果数位才为0，否则结果数位为0
# 左移位运算符 << 高位溢出舍弃，低位补0
# 右移位运算符 >> 低位溢出舍弃，高位补0（左高右低）

print(4 & 8)  # 0
'''
转换为二进制4：00000100
           8：00001000
      result：00000000=0
位与运算(按位与) 对应数位上有0，结果数位上为0
'''
print(4 | 8)  # 12
'''
转换为二进制4：00000100
           8：00001000
      result：00001100=12
位或运算(按位或) 对应数位上有1，结果数位上为1
'''
print(4 << 1)  # 4左移一位 8 左移一位相当于乘2
'''
      转换为二进制4：00000100
shift left one bit：00001000=8
二进制左移一位，高位溢出舍弃，低位补0
'''
print(4 >> 1)  # 4右移一位 2 右移一位相当于除以2
'''
       转换为二进制4：00000100
shift right one bit：00000010=2
二进制右移一位，低位溢出舍弃，高位补0
'''