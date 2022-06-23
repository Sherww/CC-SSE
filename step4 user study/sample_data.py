
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
#数据筛选
def sample():
    with open('sub_obj_test.txt','r',encoding='utf-8')as f:
        data=f.readlines()
        nees=[]
        not_nees=[]
        nees_final=[]
        nees=data
        
        for da in nees:
            nee_code=da.split(',')[1]
            code=nee_code.split(' ')
            nee_comm=da.split(',')[0]
            comm=nee_comm.split(' ')
            if len(code)>=15 and len(code)<=91 and len(comm) >=5 and len(comm) <=12:
                nees_final.append(da)
            else:
                pass
    random.shuffle(nees_final)
    sample_data=random.sample(nees_final, 384)
    sub_success=0
    obj_success=0
    sub_fail=0
    obj_fail= 0  
    for dat in sample_data:
            nee=dat.split(',')[-1].replace('\n','')
            choice=dat.split(',')[-2]
            code=dat.split(',')[1]
            
            # code=code.split(' ')
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
    with open('sample_sub_obj_userstudy.csv','w',encoding='utf-8')as ff:
        for i in range(len(sample_data)):
            ff.write(sample_data[i])
    # return sample_data
def reverse_data():
    with open('test_sub.txt','r',encoding='utf-8')as f:
        data=f.readlines()
        dats=[]
        for dat in data:
            comm=dat.split(',')[0]
            code=dat.split(',')[1]
            rel=dat.split(',')[2].replace('\n','')
            comm=reverse(comm)
            code=reverse(code)
            rel=reverse(rel)
            dat_new= comm+','+code+','+rel 
            dats.append(dat_new)
    with open('test_sub_reverse.txt','w',encoding='utf-8')as ff:
        for i in range(len(dats)):
            ff.write(dats[i]+'\n')                    
if __name__=='__main__':
    # hebing()
    # reverse_data()
    sample()
