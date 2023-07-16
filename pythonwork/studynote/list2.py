""" 1.获取列表中指定元素的索引： """
# 使用index()方法 格式：列表对象名.index(value) 返回值为元素在列表中的索引(位置)
lst = ['hello', 'world', 10, 'hello']
print(lst.index('hello'))  # 当列表中有多个相同元素，只返回相同元素中第一个元素的索引
# 若查询元素不存在，valueError

# 可以在指定的start和stop间进行查找
print(lst.index('hello', 1, 4))  # 在lst中索引为1到4(不包括4)间查找‘hello’

""" 2. 获取列表中的单个元素"""
# 正向索引从0到n-N  (N为元素个数)
# 逆向索引从-1到-N
# 指定索引不存在，indexError
print(lst[0], lst[-4])
# print(lst[10])
