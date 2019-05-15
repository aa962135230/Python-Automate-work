# -*- coding:utf-8 -*-
# 常用Python技巧：在for循环中使用range(len(somelist))，迭代列表的每一个下标
catnames = ['pens', 'staper', 'flame', 'bierder', 'test']
for i in range(len(catnames)):
    print('Index ' + str(i) + ' in catnames is:' + catnames[i])
