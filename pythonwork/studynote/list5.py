# 列表的增加
"""
1、.append():在列表末尾增加一个元素
2、.extend():在列表末尾至少添加一个元素
3、.insert():在列表的任意位置添加一个元素 insert(索引位置，一个元素) 索引位置可为负
4、切片:在列表的任意位置添加至少一个元素,切掉范围内的内容，进行替换
"""
# 增加示例
lst = [10, 20, 30]
print('原列表：', lst, id(lst), id(lst[-1]))
lst.append('a')
print('添加后：', lst, id(lst), id(lst[-2]))
lst2 = ['hello', 'world']
lst.append(lst2)  # 将lst2这个列表整体作为一个元素进行添加
print(lst)

lst.extend(lst2)  # 将lst2的列表内容作为元素进行添加，可添加多个元素
print(lst)

lst.insert(-1, 90)  # 在索引为-1的位置添加元素,添加后该元素为-2
print(lst)

lst3 = [True, False, 'hello']
""" lst[-1:-1] = lst3  """     # 当范围为列表中的空位(start>=stop，且start不为0)时，型似插入
lst[-5:-1] = lst3
print(lst)
