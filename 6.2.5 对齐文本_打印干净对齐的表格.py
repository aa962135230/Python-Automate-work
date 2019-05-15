# -*- coding:utf-8 -*-

# rjust()和ljust()字符串方法返回调用它们的字符串的填充版本，通过插入空格来对齐文本。
# 这两个方法的第一个参数是一个整数长度，用于对齐字符串
# 第二个可选参数将指定一个填充字符，取代空格字符。

# center()字符串方法与ljust()与rjust()类似，但它让文本居中，而不是左对齐或右对齐。
import pyperclip


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

printPicnic(picnicItems, 20, 6)

print(pyperclip.paste())
