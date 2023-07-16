# 获取列表中的多个元素 切片操作
# 切片格式：列表名[start:stop:step]
# 切片结果：原列表片段的拷贝
# 切片范围：(start,stop)不包括stop
# step默认为1，可简写为[start:stop]/[start:stop:]
# step为正数：
"""
1.[:stop:step]: 切片的start默认为第一个元素，从start开始往后计算切片
2.[start::step]:切片的stop默认为最后一个元素，从start开始往后计算切片
"""
# step为负数:
"""
1.[:stop:step]: 切片的start默认为最后一个元素，从start开始往前计算切片
2.[start::step]:切片的stop默认为第一个元素，从start开始往前计算切片
"""

lst = [0, 10, 20, 30, 40, 50, 60, 70]
print("原列表", id(lst))
lst2 = lst[1:6:1]
print('切片', id(lst2))  # 切片为一个新的列表对象，为原列表片段的拷贝

# 默认step为1
print(lst[1:6])
# start=1,stop=6,step=2
print(lst[1:6:2])
# stop=6,step=2,start默认为第一个元素
print(lst[:6:2])
# start=1,step=2,stop默认为最后一个元素
print(lst[1::2])
print(lst[::1])

# step为负数
print(lst[::-1])
print(lst[7::-1])


print(lst[-1:-1])   # 输出为空
