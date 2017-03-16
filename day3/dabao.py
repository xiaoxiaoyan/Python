from __future__ import  print_function
import glob
import tarfile

def dabao(l):
    bao = tarfile.open('xxxxoooo.tar', 'w')
    for i in l:
        bao.add(i)
    bao.close()
    print ("tar file succefull")

if __name__ == '__main__':
    l = glob.glob("*.txt")
    dabao(l)
    
