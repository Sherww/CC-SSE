import re,string
from oxford import Word
from tqdm import tqdm
import random
def reverse(s):
    return ' '.join(s.split(' ')[::-1])
#合并主语宾语数据
def hebing():
    with open('D:\\short_comment\\step3 completion\\codebert\\result\\codebert_sub\\code\\model\\java\\yizhi_result\\result_sub_all_succ_or_fail.txt','r',encoding='utf-8')as f:
        data=f.readlines()
        datts=[]
        for dat in data:
            nee=dat.replace('\n','')
            ne=nee.split(',')
            code=ne[1]
            comm=ne[0]
            rel=ne[2]
            su_or_fi=ne[3]
            code=reverse(code)
            comm=reverse(comm)
            rel=reverse(rel)
            new_nee=comm+','+code+','+rel+','+su_or_fi
            datt=new_nee+','+'sub'+'\n'
            datts.append(datt)
    with open('D:\\short_comment\\step3 completion\\codebert\\result\\codebert_obj\\code\\model\\java\\yizhi_result\\result_obj_all_succ_or_fail.txt','r',encoding='utf-8')as ff:
        data1=ff.readlines()     
        datts1=[]
        for dat1 in data1:
            datt1=dat1.replace('\n','')
            datt1=datt1+','+'obj'+'\n'
            datts1.append(datt1)
    nees=datts+datts1
    with open('sub_obj_test.txt','w',encoding='utf-8')as fff:
        
        for i in range(len(nees)):
            fff.write(nees[i].replace('\n','')+'\n')
#随即选择
def sample():
    with open('sub_obj_test.txt','r',encoding='utf-8')as f:
        data=f.readlines()
        random.shuffle(data)
    flag=True
    while(flag):        
        sample_data=random.sample(data, 384)
 
    # sub=0
    # obj=0  

        sub_success=0
        obj_success=0
        sub_fail=0
        obj_fail= 0  
        for dat in sample_data:
            nee=dat.split(',')[-1].replace('\n','')
            choice=dat.split(',')[-2]
            if nee == 'sub' and choice == 'success':
                sub_success +=1
            elif nee == 'sub' and choice == 'fail':
                sub_fail +=1
            elif nee == 'obj' and choice == 'success':
                obj_success +=1
                                
            elif nee =='obj'  and choice == 'fail':
                obj_fail +=1
            else:
                print(dat)
        print('--sub_success: ' + str(sub_success))
        print('--obj_success: ' + str(obj_success))
        print('--sub_fail: ' + str(sub_fail))
        print('--obj_fail: ' + str(obj_fail))    
        if sub_success >=110 and obj_success >= 132:
            flag= False
            continue
    sub=0
    obj=0    
    for dat in sample_data:
        nee=dat.split(',')[-1].replace('\n','')
        if nee == 'sub' :
            sub+=1
        elif nee =='obj':
            obj+=1
        else:
            print(dat)
    print('--sub_num: ' + str(sub))
    print('--obj_num: ' + str(obj))
    with open('sample_sub_obj.csv','w',encoding='utf-8')as ff:
        for i in range(len(sample_data)):
            ff.write(sample_data[i])
    # return sample_data
#缩写获取
def get_abbr():
    with open('sample_sub_obj.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        codes=[]
        comms=[]

        abbrs=[]
        for dat in data:
            code=dat.split(',')[1]
            code1=re.sub(r'[^\w\s]','',code)
            code1=re.sub(r'_','',code1)
            # print(code1)
            comm=dat.split(',')[0]
            codes.append(code1)
            comms.append(comm)
        for a in tqdm(codes):
            words=a.split(' ')
            abbr=[]
            for wor in words:
                a=wor
                try:
                    Word.get(a)
                except:
                    # print('word not found')
                    abbr.append(wor)
            if len(abbr)>0:
                
                abbr_each=" <SEP> ".join(abbr)
            else:
                abbr_each="None"
            abbrs.append(abbr_each)
        # print(abbr)
    return abbrs     
def write_to_file(abbrs,sample_data):
    
    with open('abbr_sample_sub_obj.csv','w',encoding='utf-8')as ff:
        for i in range(len(abbrs)):
            ff.write(sample_data[i].replace('\n','')+','+abbrs[i]+'\n')
                    
if __name__=='__main__':
    # hebing()
    # sample()
    abbrs= get_abbr()       
    with open('sample_sub_obj.csv','r',encoding='utf-8')as ff:
        sample_data=ff.readlines()
           
    write_to_file(abbrs, sample_data)