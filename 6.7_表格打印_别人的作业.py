# -*- coding:utf-8 -*-

# 要求输出如下：
#   apples  Alice  dogs
#  dranges  Bob    cats
# cherries  Carol  moose
#   banana  David  goose
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
    colWidths = [0] * len(data)
    for y in range(len(data[0])):
        for x in range(len(data)):
            if colWidths[x] < len(data[x][y]):
                colWidths[x] = len(data[x][y])

    for y in range(len(data[0])):
        for x in range(len(data)):
            if x == 0:
                print(data[x][y].rjust(colWidths[x]), end=' ')
            else:
                print(data[x][y].ljust(colWidths[x]), end=' ')

        print()


printTable(tableData)
