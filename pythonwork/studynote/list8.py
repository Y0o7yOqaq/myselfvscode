# 列表元素的排序
# 1、调用sort()方法，列表中的所有元素按照从小到大的顺序进行排序，可以指定reverse=Ture进行降序排序。
# 2、调用内置函数sorted()，可以指定reverse=Ture进行降序排序;会产生新的列表对象，原列表不发生改变。

lst = [10, 20, 60, 50, 90, 80, 30]
print('原列表:', lst, id(lst))
lst.sort()              # 调用sort()方法，默认为升序，参数为reverse=False
print('排序后:', lst, id(lst))
lst.sort(reverse=True)  # 使用参数进行降序排序
print('排序后:', lst, id(lst))
print('\t')
""" """ """ """ """ """ """ """  """ """ """ """ """ """ """ """
lst = [10, 20, 60, 50, 90, 80, 30]
new_list = sorted(lst)
desc_list = sorted(lst, reverse=True)
print('原列表:', lst, id(lst))
print('排序后:', new_list, id(new_list))
print('排序后:', desc_list, id(desc_list))
