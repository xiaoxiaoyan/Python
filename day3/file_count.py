# --*-- coding:utf-8 __*__
from __future__ import  print_function
from collections import  Counter
import sys

def count_num(filename):
    ip_addr = []
    web_resource = []
    with open(filename) as f:
        for i in f:
	    ip_addr.append(i.split()[0])
            web_resource.append(i.split()[6])
    c_ip = Counter(ip_addr)
    c_resouce = Counter(web_resource)
    return c_ip.most_common(5),c_resouce.most_common(5)
def main():
#    filename = raw_input('pls input the filename:')
    filename = sys.argv[1]
    res = count_num(filename)
    print ("ip most:{0}" .format(res[:5]))
    print ("resource most:{0}" .format(res[5:]))
    

if __name__ == "__main__":
    main()
