import xlsxwriter as xw
from tqdm import tqdm
import random
def replace():
    with open('sample_sub_obj_userstudy.csv','r',encoding='utf-8')as f:
        data=f.readlines()

        new_data=[]
        num_success_sub=0
        num_success_obj=0
        num_fail_sub=0
        num_fail_obj=0

        for dat in data:
            nee=dat.split(',')
            comm=nee[0]
            
            code=nee[1]
            
            rel=nee[2]
            
            success_fail=nee[3]
            sub_obj=nee[4].replace('\n','')
            
            if success_fail == 'success' and sub_obj =='sub':
                num_success_sub +=1
            elif success_fail =='fail' and sub_obj =='sub':
                num_fail_sub +=1
            elif success_fail =='success'and sub_obj =='obj':
                num_success_obj +=1
            elif success_fail =='fail' and sub_obj =='obj':
                num_fail_obj+=1
            else:
                print(dat)
            
            
            if sub_obj =='sub':
                rel_sub=rel.split(' ')[0]
                comm=comm.replace('<PLACE_HOLDER>', rel_sub).replace('@$',',')
                code=code.replace('@$',',')
            elif sub_obj=='obj':
                rel_obj=rel.split(' ')[-1]
                comm=comm.replace('<PLACE_HOLDER>', rel_obj).replace('@$',',')
                code=code.replace('@$',',')
            else:
                print(dat)
            new_dat=comm+'<SEP>'+code+'<SEP>'+rel+'<SEP>'+success_fail+'<SEP>'+sub_obj+'\n'
            new_data.append(new_dat)
        print('----num_success_sub: ' +str(num_success_sub)+'------'+ str(round(num_success_sub/32)))
        print('----num_fail_sub: ' +str(num_fail_sub)+'------'+ str(round(num_fail_sub/32)))
        print('----num_success_obj: ' +str(num_success_obj)+'------'+ str(round(num_success_obj/32)))
        print('----num_fail_obj: ' +str(num_fail_obj)+'------'+ str(round(num_fail_obj/32)))
        
    return new_data

def divided(new_data):
    success_sub=[]
    fail_sub=[]
    success_obj=[]
    fail_obj=[]
    data_nees=[]
    for dat in new_data: 
        nee=dat.split('<SEP>')
        comm=nee[0]
        code=nee[1]            
        rel=nee[2]            
        success_fail=nee[3]
        sub_obj=nee[4].replace('\n','')
     
        if success_fail == 'success' and sub_obj =='sub':
            success_sub.append(dat)
        elif success_fail =='fail' and sub_obj =='sub':
            fail_sub.append(dat)
        elif success_fail =='success'and sub_obj =='obj':
            success_obj.append(dat)
        elif success_fail =='fail' and sub_obj =='obj':
            fail_obj.append(dat)
        else:
            print(dat)
    i=0
    j=0
    for a in tqdm(range(32)):
        print(i,j)
        try:
            success_sub1=success_sub[i:i+4]
            fail_sub1=fail_sub[j:j+2]
            success_obj1=success_obj[i:i+4]
            fail_obj1=fail_obj[j:j+2]
            data_nee=success_sub1+fail_sub1+success_obj1+fail_obj1

            
            # print(len(data_nee))

        except:
            success_sub1=success_sub[i:]
            success_obj1=success_obj[i:]
            fail_sub1=fail_sub[j:]
            fail_obj1=fail_obj[j:]
            data_nee=success_sub1+fail_sub1+success_obj1+fail_obj1

            # print(len(data_nee))
            # continue
        i+=4
        j+=2
        random.shuffle(data_nee)
        data_nees.extend(data_nee)
        workbook=xw.Workbook(f'D:\\short_comment\\step4 user study\\each_data\\questionnaire_{a}.xlsx')
        worksheet1 = workbook.add_worksheet("sheet1")
        worksheet1.activate()
        title = ['comment','code','result','success_or_fail','sub_or_obj']
        worksheet1.write_row('A1',title)
        k=2
        for da in data_nee:
            nees=da.split('<SEP>')
            insertData = [nees[0],nees[1],nees[2],nees[3],nees[4].replace('\n','')]
            row= 'A'+ str(k)
            worksheet1.write_row(row, insertData)
            k+=1
        workbook.close()
    return data_nees

def replace2():
    with open('sample_pre_userstudy.csv','r',encoding='utf-8')as f:
        data=f.readlines()

        new_data2=[]
        num_success_pre=0
        # num_success_obj=0
        num_fail_pre=0
        # num_fail_obj=0

        for dat in data:
            nee=dat.split(',')
            comm=nee[0]
            
            code=nee[1]
            
            rel=nee[2]
            
            success_fail=nee[3]
            pre=nee[4].replace('\n','')
            
            if success_fail == 'success' and pre =='pre':
                num_success_pre +=1
            elif success_fail =='fail' and pre =='pre':
                num_fail_pre +=1
            # elif success_fail =='success'and pre =='obj':
            #     num_success_obj +=1
            # elif success_fail =='fail' and pre =='obj':
            #     num_fail_obj+=1
            else:
                print(dat)
            
            
            # if sub_obj =='sub':
            #     rel_sub=rel.split(' ')[0]
            #     comm=comm.replace('<PLACE_HOLDER>', rel_sub).replace('@$',',')
            #     code=code.replace('@$',',')
            if pre=='pre':
                rel_pre=rel.split(' ')[-1]
                comm=comm.replace('<PLACE_HOLDER>', rel_pre).replace('@$',',')
                code=code.replace('@$',',')
            else:
                print(dat)
            new_dat=comm+'<SEP>'+code+'<SEP>'+rel+'<SEP>'+success_fail+'<SEP>'+pre+'\n'
            new_data2.append(new_dat)
        print('----num_success_pre: ' +str(num_success_pre)+'------'+ str(round(num_success_pre/5)))
        print('----num_fail_pre: ' +str(num_fail_pre)+'------'+ str(round(num_fail_pre/5)))
        # print('----num_success_obj: ' +str(num_success_obj)+'------'+ str(round(num_success_obj/32)))
        # print('----num_fail_obj: ' +str(num_fail_obj)+'------'+ str(round(num_fail_obj/32)))
        
    return new_data2

def divided2(new_data2):
    success_pre=[]
    fail_pre=[]
    # success_obj=[]
    # fail_obj=[]
    data_nees=[]
    for dat in new_data2: 
        nee=dat.split('<SEP>')
        comm=nee[0]
        code=nee[1]            
        rel=nee[2]            
        success_fail=nee[3]
        pre=nee[4].replace('\n','')
     
        if success_fail == 'success' and pre =='pre':
            success_pre.append(dat)
        elif success_fail =='fail' and pre =='pre':
            fail_pre.append(dat)
        # elif success_fail =='success'and sub_obj =='obj':
        #     success_obj.append(dat)
        # elif success_fail =='fail' and sub_obj =='obj':
        #     fail_obj.append(dat)
        else:
            print(dat)
    i=0
    j=0
    for a in tqdm(range(5)):
        print(i,j)
        try:
            success_pre1=success_pre[i:i+15]
            fail_pre1=fail_pre[j:j+9]
            # success_obj1=success_obj[i:i+4]
            # fail_obj1=fail_obj[j:j+2]
            data_nee=success_pre1+fail_pre1

            
            # print(len(data_nee))

        except:
            success_pre1=success_pre[i:]
            # success_obj1=success_obj[i:]
            fail_pre1=fail_pre[j:]
            # fail_obj1=fail_obj[j:]
            data_nee=success_pre1+fail_pre1

            # print(len(data_nee))
            # continue
        i+=15
        j+=9
        random.shuffle(data_nee)
        data_nees.extend(data_nee)
        workbook=xw.Workbook(f'D:\\short_comment\\step4 user study\\each_data\\z_pre_questionnaire_{a}.xlsx')
        worksheet1 = workbook.add_worksheet("sheet1")
        worksheet1.activate()
        title = ['comment','code','result','success_or_fail','pre']
        worksheet1.write_row('A1',title)
        k=2
        for da in data_nee:
            nees=da.split('<SEP>')
            insertData = [nees[0],nees[1],nees[2],nees[3],nees[4].replace('\n','')]
            row= 'A'+ str(k)
            worksheet1.write_row(row, insertData)
            k+=1
        workbook.close()
    return data_nees
if __name__=='__main__':
    # new_data=replace()
    # data_nees=divided(new_data)
    
    # need_tobe_added=[]
    # for dat in new_data:
    #     if dat not in data_nees:
    #         need_tobe_added.append(dat)
    #     else:
    #         pass
    # # write_data=data_nees+
    # with open('data_cannot_write.txt','w',encoding='utf-8')as f:
    #     for a in need_tobe_added:
    #         f.write(a)
            
    new_data2=replace2()
    data_nees2=divided2(new_data2)
    
    need_tobe_added=[]
    for dat in new_data2:
        if dat not in data_nees2:
            need_tobe_added.append(dat)
        else:
            pass
    # write_data=data_nees+
    with open('data_cannot_write_pre.txt','w',encoding='utf-8')as f:
        for a in need_tobe_added:
            f.write(a)            