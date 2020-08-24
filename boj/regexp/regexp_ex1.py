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
    tbl='gs://uplus-airflow-bucket1/test.csv'
    print(tbl)
    a=tbl.split('/')[3]
    print(a)
    print(a.replace('.csv','.txt'))
    print(re.sub(tbl,'gs://uplus-airflow',''))
    log_txt = "Summary" +  " ========================" + "\n"
    log_txt += ("Count : " + a) + "\n"
    log_txt += ("Starting time : " + a) + "\n"
    print(log_txt)