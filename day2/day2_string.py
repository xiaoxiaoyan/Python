# -*- coding:utf-8 -*- 
from __future__ import  print_function

""" 字符串是字符的有序集合，
并且不可以改变，可以使用单引号，双引号，三引号来定义"""

#定义字符串，在ipython下可以直接使用tab键查看其方法
s = "python is fun"
""" s.
           s.capitalize s.decode     s.expandtabs s.index      s.isdigit    s.istitle    s.ljust      s.partition  s.rindex     s.rsplit     s.splitlines s.swapcase   s.upper      
           s.center     s.encode     s.find       s.isalnum    s.islower    s.isupper    s.lower      s.replace    s.rjust      s.rstrip     s.startswith s.title      s.zfill      
           s.count      s.endswith   s.format     s.isalpha    s.isspace    s.join       s.lstrip     s.rfind      s.rpartition s.split      s.strip      s.translate"""
print ("按空格分隔{1},结果是{0}" .format(s.split(),s))
"""Out: ['python', 'is', 'fun']"""

print ("s * 2 结果是将字符串打印两遍:{0}" .format(s*2))
"""Out: 'python is funpython is fun'"""

#计算字符串长度
print ("length of '{1}' is {0} " .format(len(s),s))
"""Out: 13"""

#字符串截取，从开始截取到第六个
print ("{0}从开始截取到第六个:{1}" .format(s,s[:6]))
"""Out[25]: 'python' """

print ("打印从开始到结束:{0}" .format(s[::]))
""" Out: 'python is fun' """
