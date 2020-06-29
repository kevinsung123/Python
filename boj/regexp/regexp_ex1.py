import re

import string
def remove_control_characters(str):
    return re.sub(string.printable,'',str)


if __name__=='__main__':
    a="123456790 ABC#%? .(朱惠英)  "
    print(a)
    print(chr(13))
    print(''.join([s for s in a if ord(s)>32]))

    for i in range(130):
        print(i,chr(i),end=" ,")
    for i in range(200,300):
        print(i,chr(i))