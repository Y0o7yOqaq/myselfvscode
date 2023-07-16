# 条件表达式（是if···else的简写）
# 结构： x if 判断条件 else y
# 规则：如果判断条件的布尔值为Ture，条件表达式的返回值为x，否则为y

num_a = int(input('请输入整数a:'))
num_b = int(input('请输入整数b:'))
print(num_a, '大于等于', num_b) if num_a >= num_b else print(num_a, '小于', num_b)
print(str(num_a)+' 大于等于 '+str(num_b) if num_a >= num_b else str(num_a)+' 小于 '+str(num_b))

# pass语句 只是一个占位符，用在语法上需要语句的地方，先搭建语法结构
# 常与以下语句一起使用：
# if语句的条件执行体
# for-in语句的循环体
# 定义函数的函数体
