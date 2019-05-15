# -*- coding:utf-8 -*-
'''
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
'''

import pyperclip
text = pyperclip.paste()
print(text)
# TODO: 分割行并添加*星号在行首
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
