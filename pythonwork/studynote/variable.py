name = 'variable'               # 变量
print(name)                     # 对象由三部分组成
print('标识', id(name))         # 标识(id)：表示对象所储存的内存地址，使用内置函数id(i)获取
print('类型', type(name))       # 类型(type)：表示对象的数据类型，使用内置函数type(i)获取
print('值', name)               # 值(value)：表示对象所存储的具体数据，使用print(i)获取
print('\r')

# 变量和对象的关系
# 创建对象（分配内存）储存值
# 创建变量
# 变量储存对象的id，一个指针的关系
# 变量没有类型，对象有类型，变量类型可任意改变

name = 123
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)
name = 2

# 每一次变量赋值后都会指向新的对象，有不同的地址
# 不被变量使用的对象被称为内存垃圾，会由python的垃圾回收机制回收
