import re
# 通过在字符串的第一个引号之前加上r，可以将该字符串标记为原始字符串，它不包括转义字符。
# 正则表达式字符串中的第一对括号是第1组。第二对括号是第2组。
phonenumregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phonenumregex.search('my number is 415-555-2222.')
print('Phone number found: ' + mo.group())
# 向group()匹配对象方法传入整数1或2，就可以取得匹配文本的不同部分。
print(mo.group(1))
print(mo.group(2))
# 向group()方法传入0或不传入参数，将返回整个匹配的文本。
print(mo.group(0))
print(mo.group())
# 如果想要一次就获取所有的分组，请使用groups()方法
print(mo.groups())
areacode, mainnumber = mo.groups()
print(areacode)
print(mainnumber)
