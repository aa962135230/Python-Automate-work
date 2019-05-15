# 使用字典包含其他字典，用于记录谁为野餐带来了什么食物。totalBrought()函数可以读取这个数据结构，计算所有客人带来的食物的总数。


allGuests = {'Alice': {'apples': 5, 'pretzels': 12},

             'Bob': {'ham sandwiches': 3, 'apples': 2},

             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):

    numBrought = 0  
    # for循环迭代guests中的每个键值对。在这个循环里，客人的名字字符串赋给k，他们带来的野餐食物的字典赋给v。
    for k, v in guests.items():   

        # 如果食物参数是字典中存在的键，它的值（数量）就添加到numBrought❷。如果它不是键，get()方法就返回0，添加到numBrought。
        numBrought = numBrought + v.get(item, 0)

    return numBrought


print('Number of things being brought:')

print(' - Apples ' + str(totalBrought(allGuests, 'apples')))

print(' - Cups ' + str(totalBrought(allGuests, 'cups')))

print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))

print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))

print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))
