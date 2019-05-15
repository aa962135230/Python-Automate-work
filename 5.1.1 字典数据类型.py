# -*- coding:utf-8 -*-

# 1
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name : (blank to quit)')
    name = input()
    if name == ' ':
        break
    if name in birthdays.keys():  # 2
        print(birthdays[name] + ' is the birthday of ' + name)  # 3
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday  # 4 给字典数据添加表项（键和值）的方法
        print('birthday database updated.')
    print(birthdays)

# 1.你创建了一个初始的字典，将它保存在birthdays中❶。
# 2.用in关键字，可以看看输入的名字是否作为键存在于字典中❷，就像查看列表一样。
# name in birthdays 实际上是 name in birthdays.keys() 的简写版本
# 3.如果该名字在字典中，你可以用方括号访问关联的值❸。
# 4.如果不在，你可以用同样的方括号语法和赋值操作符添加它❹。
