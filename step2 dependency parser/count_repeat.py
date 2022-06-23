import random
from tqdm import tqdm
import math
def repeat_all():
    with open('zhuweibin_all_clean.csv','r',encoding='utf-8')as f1:
        data=f1.readlines()
        random.shuffle(data)
        print(len(data))
        num=0
        data2 = []
        for dat in tqdm(data):
            if not dat in data2:
                data2.append(dat)
            else:
                num+=1
                # pass
        print('num_repet_all:--'+str(num))
        print('num_repet_ratio_all:--'+str(num/len(data)))

def repeat_10_fold():
    with open('zhuweibin_all_clean.csv','r',encoding='utf-8')as f1:

        data=f1.readlines()
        random.shuffle(data)
        count = len(data)
        # Get the amount of data 
        num = math.ceil(count/10)
    test0=data[num * 0: num * 1]
    dev0=data[num * 1: num * 2]
    train0=data[num*2:]  
    test1=data[num * 1: num * 2]
    dev1=data[num * 2: num * 3]
    train1=data[num*3:] + data[num*0:num*1]  
    test2=data[num * 2: num * 3]
    dev2=data[num * 3: num * 4]
    train2=data[num*4:] + data[num*0:num*2]
    test3=data[num * 3: num * 4]
    dev3=data[num * 4: num * 5]
    train3=data[num*5:]+ data[num*0:num*3]
    test4=data[num * 4: num * 5]
    dev4=data[num * 5: num * 6]
    train4=data[num*6:]+ data[num*0:num*4]
    test5=data[num * 5: num * 6]
    dev5=data[num * 6: num * 7]
    train5=data[num*7:]+ data[num*0:num*5]
    test6=data[num * 6: num * 7]
    dev6=data[num * 7: num * 8]
    train6=data[num*8:]+ data[num*0:num*6]
    test7=data[num * 7: num * 8]
    dev7=data[num * 8: num * 9]
    train7=data[num*9:]+ data[num*0:num*7]
    test8=data[num * 8: num * 9]
    dev8=data[num * 9: num * 10]
    train8=data[num*0:num*8]
    test9=data[num * 9: num * 10]
    dev9=data[num * 0: num * 1]
    train9=data[num*1:num*9]

    val1=[test0,test1,test2,test3,test4,test5,test6,test7,test8,test9]
    val2=[train0,train1,train2,train3,train4,train5,train6,train7,train8,train9]
    for i in range(len(val1)):
        num=0
        list1=val1[i]
        list2=val2[i]
        for dat in tqdm(list1):
            if dat in list2:
                num+=1
            else:
                pass
        print('num_repet_:--'+str(i)+'---------'+str(num))
        print('num_repet_ratio:--'+str(i)+'---------'+str(num/len(list1)))

if __name__=='__main__':
    repeat_all()
    repeat_10_fold()
