"""
练习: break和continue语句

描述：
返回从1到n的所有非3的倍数的整数列表。

请补全下面的函数，使用continue语句跳过3的倍数。
"""

def skip_multiples_of_three(n):
    """
    返回从1到n的所有非3的倍数的整数列表

    参数:
    - n: 正整数上限

    返回:
    - 从1到n中所有不是3的倍数的整数列表
    """
    # 请在下方编写代码
    not3_multiple = []
    i = 1;

    while True:
        if i > n:
            break

        if i % 3 == 0:
            i += 1
            continue

        not3_multiple.append(i)
        i += 1

    return not3_multiple
