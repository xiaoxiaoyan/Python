from __future__ import  print_function
import  os
import  sys



def count_word(filename):
    """open the input file and count ery words """
    dic = {}
    with open(filename) as f:
        for line in f:
            for word in line.strip().split(":"):
                if len(word) > 10:
                    dic.setdefault(word,0)
                    dic[word] += 1
    return dic

def main():
    if len(sys.argv) != 2:
        print ("Usage: " ,sys.argv[0] ,"filename")
        sys.exit(10000)
    file_input = sys.argv[1]
    if not os.path.isfile(file_input):
        raise SyntaxError('{0} is not found' .format(file_input))
    else:
        res = count_word(file_input)
        return res


if __name__ == '__main__' :
    kk = main()
    for key,val in kk.iteritems():
        print(key, ':', val)

