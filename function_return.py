def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y


print(maximum(2, 2))

"""注意没有返回值的 return 语句等价于 return None。
   None 在 Python 是一种代表「没有任何东西」特殊的类型。
   例如：如果一个变量的值是 None，则说明这个变量尚未被赋值或值已被清空。"""
