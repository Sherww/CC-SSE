import re,string
from oxford import Word
from tqdm import tqdm
import random
def reverse(s):
    return ' '.join(s.split(' ')[::-1])
def get_abbr_extension():
    with open('abbr_sample_sub_obj.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nees=[]
        abbrs=[]
        for dat in data:
            nee=dat.split(',')[-1]
            nees.append(nee)
        for da in nees:
            if da!='None':
                abbr=da.replace('\n','').split(' <SEP> ')
                abbrs.extend(abbr)
            else:
                pass
    abbrs_deldup=[]
    for a in abbrs:
        if a not in abbrs_deldup:
            abbrs_deldup.append(a)
    with open('abbr_need.txt','w',encoding='utf-8')as ff:
        for i in abbrs_deldup:
            ff.write(i+'\n')
def del_dup():
    with open('abbr_need.txt','r',encoding='utf-8')as f:
        data=f.readlines()
        deldata=[]
        for i in data:
            if i not in deldata:
                deldata.append(i)
    with open('abbr_nees_deldup.txt','w',encoding='utf-8')as ff:
        for a in deldata:
            ff.write(a)
if __name__=='__main__':
    # get_abbr_extension()
    del_dup()