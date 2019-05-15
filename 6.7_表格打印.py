# -*- coding:utf-8 -*-

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# 思路分析：
# 这个列表中有三个子列表tabledata[]，要先用一个循环每个子列表的第一个项目打印出来(即tabledata[0][1],tabledata[1][1],tabledata[2][1])，并且按一定宽度右对齐，有多少个子列表就要跑多少次循环，因此，这个循环要跑三次。右对齐的宽度数据需要三个。
# 先跑的循环放在内层
# 然后打印第各子列表的第二个项目，各个子列表的第三个项目，各个子列表的第四个项目，每个子列表有4个项目，因此，这个循环要跑4次
# 后跑的循环放在外层

# 怎么获取右对齐的宽度？需要找出每个子列表的最长宽度，然后记录到一个列表里面


def printTable(dtt):
    rlist_1 = []  # 获取子列表的各个项目的长度，生成一个列表包含各个项目的长度值
    rlist_2 = []  # 获取子列表中最长项目的长度值，生成一个新列表，对应要设置的对齐宽度
    for i in range(len(dtt)):
        for j in range(len(dtt[0])):
            rlist_1.append(len(dtt[i][j]))
        rlist_2.append(max(rlist_1))
        rlist_1 = []  # 清空这个列表，需要重新计算下一个子列表中哪个项目是最长的
    # print(rlist_2)
    for i in range(len(dtt[0])):
        for j in range(len(dtt)):
            print(dtt[j][i].rjust(rlist_2[j]), end='  ')
        print()

printTable(tableData)
