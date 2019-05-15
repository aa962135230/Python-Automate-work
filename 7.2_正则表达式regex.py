import re
# 通过在字符串的第一个引号之前加上r，可以将该字符串标记为原始字符串，它不包括转义字符。
phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumregex.search('my number is 415-555-2222.')
print('Phone number found: ' + mo.group())

# 我们将期待的模式传递给re.compile()，并将得到的Regex对象保存在phoneNumRegex中。

# 然后我们在phoneNumRegex上调用search()，向它传入想查找的字符串。查找的结果保存在变量mo中。

# 在Python中使用正则表达式有几个步骤，但每一步都相当简单。

# 1．用import re导入正则表达式模块。

# 2．用re.compile()函数创建一个Regex对象（记得使用引号之前加上r，标记为原始字符串）。

# 3．向Regex对象的search()方法传入想查找的字符串。它返回一个Match对象。

# 4．调用Match对象的group()方法，返回实际匹配文本的字符串。
