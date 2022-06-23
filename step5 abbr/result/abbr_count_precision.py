import re
def sub_all():
    with open('abbr_sample_sub_obj_num_only_sub.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nums_abbr=[]
        nums_abb_exten1=[]
        nums_abb_exten2=[]
        nums_abb_exten3=[]
        for dat in data:
            abbr=dat.split(',')[5]
            if abbr == 'None':
                num = 0
            elif '<SEP>' not in abbr:
                num= 1
            else:
                n=abbr.split('<SEP>')
                num=len(n)
            nums_abbr.append(num)
            
            abb_exten1=dat.split(',')[8]
            num1=re.findall("\d+", abb_exten1) 
            num1=" ".join(num1)
            if num1=="":
                num1= 0
            else:
                num1=int(num1)
            nums_abb_exten1.append(num1)
    
                   
            abb_exten2=dat.split(',')[9]
            num2=re.findall("\d+", abb_exten2) 
            num2=" ".join(num2)
            if num2=="":
                num2= 0
            else:
                num2=int(num2)
            nums_abb_exten2.append(num2)
            
            abb_exten3=dat.split(',')[10]
            num3=re.findall("\d+", abb_exten3) 
            num3=" ".join(num3)
            if num3 =="":
                num3 = 0
            else:
                num3 =int(num3)
            nums_abb_exten3.append(num3)        
    
        print('---sub_nums_abbr---'+ str(sum(nums_abbr)))   
        print('---sub_nums_abb_exten1---'+ str(sum(nums_abb_exten1)))   
        print('---sub_nums_abb_exten2---'+ str(sum(nums_abb_exten2)))   
        print('---sub_nums_abb_exten3---'+ str(sum(nums_abb_exten3)))   
        
def obj_all():
    with open('abbr_sample_sub_obj_num_only_obj.csv','r',encoding='utf-8')as f:
        data=f.readlines()
    
        nums_abbr=[]
        nums_abb_exten1=[]
        nums_abb_exten2=[]
        nums_abb_exten3=[]
        for dat in data:
            abbr=dat.split(',')[5]
            if abbr == 'None':
                num = 0
            elif '<SEP>' not in abbr:
                num= 1
            else:
                n=abbr.split('<SEP>')
                num=len(n)
            nums_abbr.append(num)
            
            abb_exten1=dat.split(',')[8]
            num1=re.findall("\d+", abb_exten1) 
            num1=" ".join(num1)
            if num1=="":
                num1= 0
            else:
                num1=int(num1)
            nums_abb_exten1.append(num1)
    
                   
            abb_exten2=dat.split(',')[9]
            num2=re.findall("\d+", abb_exten2) 
            num2=" ".join(num2)
            if num2=="":
                num2= 0
            else:
                num2=int(num2)
            nums_abb_exten2.append(num2)
            try:
                abb_exten3=dat.split(',')[10]
            except:
                print(dat)
            num3=re.findall("\d+", abb_exten3) 
            num3=" ".join(num3)
            if num3 =="":
                num3 = 0
            else:
                num3 =int(num3)
            nums_abb_exten3.append(num3)        
    
        print('---obj_nums_abbr---'+ str(sum(nums_abbr)))   
        print('---obj_nums_abb_exten1---'+ str(sum(nums_abb_exten1)))   
        print('---obj_nums_abb_exten2---'+ str(sum(nums_abb_exten2)))   
        print('---obj_nums_abb_exten3---'+ str(sum(nums_abb_exten3)))   
def sub_success():
    with open('abbr_sample_sub_obj_num_only_sub.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nums_abbr=[]
        nums_abb_exten1=[]
        nums_abb_exten2=[]
        nums_abb_exten3=[]
        #from 76,  success
        for dat in data[76:]:
            abbr=dat.split(',')[5]
            if abbr == 'None':
                num = 0
            elif '<SEP>' not in abbr:
                num= 1
            else:
                n=abbr.split('<SEP>')
                num=len(n)
            nums_abbr.append(num)
            
            abb_exten1=dat.split(',')[8]
            num1=re.findall("\d+", abb_exten1) 
            num1=" ".join(num1)
            if num1=="":
                num1= 0
            else:
                num1=int(num1)
            nums_abb_exten1.append(num1)
    
                   
            abb_exten2=dat.split(',')[9]
            num2=re.findall("\d+", abb_exten2) 
            num2=" ".join(num2)
            if num2=="":
                num2= 0
            else:
                num2=int(num2)
            nums_abb_exten2.append(num2)
            
            abb_exten3=dat.split(',')[10]
            num3=re.findall("\d+", abb_exten3) 
            num3=" ".join(num3)
            if num3 =="":
                num3 = 0
            else:
                num3 =int(num3)
            nums_abb_exten3.append(num3)        
    
        print('---success_sub_nums_abbr---'+ str(sum(nums_abbr)))   
        print('---success_sub_nums_abb_exten1---'+ str(sum(nums_abb_exten1)))   
        print('---success_sub_nums_abb_exten2---'+ str(sum(nums_abb_exten2)))   
        print('---success_sub_nums_abb_exten3---'+ str(sum(nums_abb_exten3)))   
        
def obj_success():
    with open('abbr_sample_sub_obj_num_only_obj.csv','r',encoding='utf-8')as f:
        data=f.readlines()
    
        nums_abbr=[]
        nums_abb_exten1=[]
        nums_abb_exten2=[]
        nums_abb_exten3=[]
        # from 60, success
        for dat in data[60:]:
            abbr=dat.split(',')[5]
            if abbr == 'None':
                num = 0
            elif '<SEP>' not in abbr:
                num= 1
            else:
                n=abbr.split('<SEP>')
                num=len(n)
            nums_abbr.append(num)
            
            abb_exten1=dat.split(',')[8]
            num1=re.findall("\d+", abb_exten1) 
            num1=" ".join(num1)
            if num1=="":
                num1= 0
            else:
                num1=int(num1)
            nums_abb_exten1.append(num1)
    
                   
            abb_exten2=dat.split(',')[9]
            num2=re.findall("\d+", abb_exten2) 
            num2=" ".join(num2)
            if num2=="":
                num2= 0
            else:
                num2=int(num2)
            nums_abb_exten2.append(num2)
            try:
                abb_exten3=dat.split(',')[10]
            except:
                print(dat)
            num3=re.findall("\d+", abb_exten3) 
            num3=" ".join(num3)
            if num3 =="":
                num3 = 0
            else:
                num3 =int(num3)
            nums_abb_exten3.append(num3)        
    
        print('---success_obj_nums_abbr---'+ str(sum(nums_abbr)))   
        print('---success_obj_nums_abb_exten1---'+ str(sum(nums_abb_exten1)))   
        print('---success_obj_nums_abb_exten2---'+ str(sum(nums_abb_exten2)))   
        print('---success_obj_nums_abb_exten3---'+ str(sum(nums_abb_exten3)))   
def conut_all_abbr_num():
    with open('abbr_sample_sub_obj.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nums=[]
        for dat in data:
            abbr=dat.split(',')[-1].replace('\n','')
            if abbr == 'None':
                num = 0
            elif '<SEP>' not in abbr:
                num= 1
            else:
                ns=[]
                n=abbr.split('<SEP>')
                for i in n:
                    if 'str' or 'equals' or 'events' or 'tasks' or 'names' or 'num' or 'int' == i:
                        n.remove(i)
                    # elif 'num' == i:
                    #     n.remove(i)
                    # elif 'int' == i:
                    #     n.remove(i)
                    elif len(i)>=10:
                        n.remove(i)
                    else:
                        pass
                num=len(n)
            nums.append(num)
    print('----conut_all_abbr_num---'+str(sum(nums)))
                        
if __name__ =='__main__':
    #after   sub  +10
    sub_all() 
    
    #after   obj +14
    obj_all()
    
    #after   sub +10
    sub_success()
    
    #after   obj   +14
    obj_success()
    
    conut_all_abbr_num()