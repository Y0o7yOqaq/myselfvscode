# continue语句
# 用于结束当前循环，进入下一次循环，通常与分支结构中的if一起使用
# 在二重循环中控制当前循环
"""
for ... in...:
    ......
    if ...:
        continue
    ...
"""
"""
while(条件):
    ......
    if ...:
        continue
    ...
"""
for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)
