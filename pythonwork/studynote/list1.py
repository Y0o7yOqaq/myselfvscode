# 列表
# 相当于其他语言中的列表
# 列表的创建
# 1.lst=[...]  使用方括号
# 2.lst=list([...])  使用list()函数
lst = ['hello', 'world', 10, 'hello']  # 有str类型，有int类型，可以混存
lst2 = list(['hello', 'world', 10, 'hello'])  # 可以存放两个‘hello’
print(id(lst), id(lst2))
print(type(lst), type(lst2))
print(lst, lst2)
print('\t')
print(id(lst[0]))
print(type(lst[0]))
print(lst[0], lst[-3])   # 正序（左到右）从0开始，逆序（右到左）从-1开始
# 列表的特点：
# 列表元素按顺序 有序排序
# 索引映射唯一个数据
# 列表可以存储重复数据
# 任意数据类型混存
# 根据需要动态分配和回收内存
