# 列表的修改
lst = [10, 20, 30, 40]
print(lst, id(lst))
print(lst[2], id(lst[2]))
# 一次修改一个值
lst[2] = 20   # 索引2指向一个新对象
print(lst, id(lst))
print(lst[2], id(lst[2]))
# 切片替换
lst[1:3] = [40, 10]
print(lst)
