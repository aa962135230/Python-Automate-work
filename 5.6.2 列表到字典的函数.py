# -*- coding:utf-8 -*-
# 5.6.2 列表到字典的函数
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print('inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print('Total number of items: ' + str(item_total))

# displayInventory(stuff)


def addToInventory(inventory, addedItems):
    for addlist in addedItems:
        if addlist in inventory.keys():
            inventory[addlist] = inventory[addlist]+1
        else:
            inventory[addlist] = 1
    return(inventory)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
