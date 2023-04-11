"""有时候你可能想要定义一个能接收 任意个 数参数的函数。例如定义一个参数个数可变的函数，你可以通过使用星号 * 来实现这个功能。"""


def total(a=5, *number, **phonebook):
    print('a', a)
    for single_item in number:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, jack=1123, john=2231, inge=1560))

"""当我们声明一个带星号的参数 *param 时，从这个参数开始，之后的所有参数都会被收集进入一个名为 param 的元组中。
类似的，当我们定义了一个带两个星号的参数 **param 时，从这个参数开始，之后的所有参数都会被收入名为 param 的字典中。"""

print(total())

