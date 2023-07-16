# 列表元素的删除
"""
1、.remove()：一次删除一个元素，重复元素只删除第一个，元素不存在则抛出valueError
2、.pop()：删除一个指定索引位置上的元素，指定索引不存在则IndexError，不指定索引就删除列表中最后一个元素
3、切片：一次至少删除一个元素
4、clear()：清空列表
5、del：删除列表
"""
lst = [10, 20, 30, 40, 30, 20, 10]
lst.remove(30)  # 删除第一个重复元素
# lst.remove('x')  # 运行时间报错
print(lst)

lst.pop(0)
print(lst)
lst.pop(-3)
print(lst)
lst.pop()
print(lst)  # 不指定参数，默认删除最后一个元素

new_lst = lst[1:2]  # 切片1
print(new_lst)
lst[0:1] = []       # 切片2
print(lst)      # 切片有两种方式，第一种会产生新的列表对象，原列表不变，第二种不会产生，原列表改变

""" lst.clear(lst) """
print(lst)    # 空列表

del lst
# print(lst)   del 删除列表，无列表定义
