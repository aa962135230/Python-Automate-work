# -*- coding:utf-8 -*-

catnames = []
while True:
    print('Enter the name of cat ' + str(len(catnames)+1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catnames = catnames + [name]  # 列表连接
print('the cat names are:')
for name in catnames:
    print('    ' + name)
