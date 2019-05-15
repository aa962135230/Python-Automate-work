spam = 'Helloworld!'
# 通过spam[0:5]得到的子字符串，将包含spam[0]到spam[4]的全部内容，而不包括下标5处的空格。
fizz = spam[0:5]
print(fizz)

# join()方法在一个字符串上调用，参数是一个字符串列表，返回一个字符串。
# 返回的字符串由传入的列表中每个字符串连接而成。
s = ['cats', 'rats', 'bats']
list_f = ','.join(s)
print(list_f)

# split()方法针对一个字符串调用，返回一个字符串列表
# 默认情况下，字符串'My name is Simon'按照各种空白字符分割，诸如空格、制表符或换行符。
# 这些空白字符不包含在返回列表的字符串中。
# 也可以向split()方法传入一个分割字符串，指定它按照不同的字符串分割
ss = 'My name is Simon'.split()
print(ss)
