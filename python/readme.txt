https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
https://www.python.org/downloads/

>python
>>>print('你好')
>>>name = input()
...print(name)
>>>print('aaa','bbb','ccc')//可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
aaa bbb ccc
>>>name = input('请输入：')
>>>print(name)
请输入：ly//输入的
ly//打印的



>>>exit()

>python hello.py

>>>print(r'\\\t\n')	//r''表示不转意
\\\t\n
>>>print('''你好	//'''...'''表示多行内容
... python''')
你好
python



整数 浮点数 字符串 布尔值 bytes类型 空值(用None表示。None不能理解为0，因为0是有意义的)

>>>9/3
3.0
>>>10/3
3.3333333333333335
>>>10//3
3

>>>ord('A')
65
>>>chr(66)
B

>>>b'ABC'//要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节

//str通过encode()方法可以编码为指定的bytes
>>>'ABC'.encode('ascii')
b'ABC'
>>>'中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
//纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错


//bytes变为str，就需要用decode()
>>>b'ABC'.decode('ascii')
ABC
>>>b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
中文
//bytes中包含无法解码的字节，decode()方法会报错
//bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
'中
//str包含多少个字符，可以用len()函数
>>> len('ABC')
3
>>> len('中文')
2

//格式化方式和C语言是一致的，用%实现
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
占位符	替换内容
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数

>>> print('%2d-%02d' % (3, 1))
>>> print('%.2f' % 3.1415926)
//你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
//字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'
//format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'












