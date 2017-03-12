# -*- coding:utf-8 -*- 

""" 字符串是字符的有序集合，
并且不可以改变，可以使用单引号，双引号，三引号来定义"""

#定义字符串，在ipython下可以直接使用tab键查看其方法
In [1]: s = "python is fun"
In [2]: s.
           s.capitalize s.decode     s.expandtabs s.index      s.isdigit    s.istitle    s.ljust      s.partition  s.rindex     s.rsplit     s.splitlines s.swapcase   s.upper      
           s.center     s.encode     s.find       s.isalnum    s.islower    s.isupper    s.lower      s.replace    s.rjust      s.rstrip     s.startswith s.title      s.zfill      
           s.count      s.endswith   s.format     s.isalpha    s.isspace    s.join       s.lstrip     s.rfind      s.rpartition s.split      s.strip      s.translate          
In [10]: s.split()
Out[10]: ['python', 'is', 'fun']

In [22]: s * 2
Out[22]: 'python is funpython is fun'

#计算字符串长度
In [23]: len(s)
Out[23]: 13

In [25]: s[:6]
Out[25]: 'python'
