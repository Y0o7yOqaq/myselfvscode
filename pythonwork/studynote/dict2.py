# 字典元素的获取
# 1. [] ：    例 ：scores[键]
# 2. get()：  例 ：scores.get(键)
# 区别：
# []方法：若字典中不存在指定的key，会报'keyError'异常
# get()方法：若字典中不存在指定的key，会返回None，可以通过参数设置默认的value，以便指定的key不存在时返回

scores = {'张三': 100, '李四': 80}
# 方法1 []
print(scores['张三'])
# 方法2 get()
print(scores.get('张三'))
