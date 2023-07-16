# 嵌套if
"""
if 条件表达式1:
    if 内层表达式:
        内层执行体1
    else:
        内层执行体2
else:
    条件执行体
"""
answer = input('您是会员吗？y/n\n\r')
money = float(input('您的购物金额为:'))
if answer == 'y':
    if money >= 200:
        print('8折，您的付款金额为', money*0.8)
    elif money >= 100:
        print('9折，您的付款金额为', money*0.9)
    else:
        print('不打折，您的付款金额为', money)
else:
    if money >= 200:
        print('95折，您的付款金额为', money*0.95)
    else:
        print('不打折，您的付款金额为', money)
