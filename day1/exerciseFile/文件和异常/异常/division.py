# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'



print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")

    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try: #使用异常避免崩溃
      answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:#else 代码块
        """通过将可能引发错误的代码放在try-except 代码块中，可提高这个程序抵御错误的能力。
# 错误是执行除法运算的代码行导致的，因此我们需要将它放到try-except 代码块
中。这个示例还包含一个else 代码块；依赖于try 代码块成功执行的代码都应放到else 代码块中."""
        print(answer)