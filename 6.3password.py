import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

# sys.argv获取运行python文件的时候命令行参数，sys.argv[]说白了就是一个从程序外部获取参数的桥梁
# 我们从外部取得的参数可以是多个，所以获得的是一个列表（list)，
# 也就是说sys.argv其实可以看作是一个列表，所以才能用[]提取其中的元素。
# 其第一个元素是程序本身，随后才依次是外部给予的参数。
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copy to clipboard.')
else:
    print('There is no account named ' + account)
