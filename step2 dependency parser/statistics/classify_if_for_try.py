#import stat
from tqdm import tqdm

def classify_all():
    with open('D:\\short_comment\\step1 data\\comment_code.txt','r',encoding='utf-8')as f:
        data=f.readlines()
        codes_if=[]
        comments_if=[]
        types_if=[]
        codes_for=[]
        comments_for=[]
        types_for=[]
        codes_try=[]
        comments_try=[]
        types_try=[]
        codes_state=[]
        comments_state=[]
        types_state=[]
        for dat in data:
            try:
                code=dat.split('\",\"')[2]
            except:
                print(dat)
            comment=dat.split('\",\"')[0]
            typee=dat.split('\",\"')[1]
    
            if code.startswith(('if','switch','else')):
                codes_if.append(code)
                comments_if.append(comment)
                types_if.append(typee)
            elif code.startswith(('for','while','do','break','cotinue','case')):
                
                codes_for.append(code)
                comments_for.append(comment)
                types_for.append(typee)
            elif  code.startswith(('try','exception','return','throw')):
                codes_try.append(code)
                comments_try.append(comment)
                types_try.append(typee)
            else:
                codes_state.append(code)
                comments_state.append(comment)
                types_state.append(typee)
    with open('D:\\short_comment\\step2 dependency parser\\statistics\\all_if_try_for\\comment_code_if.csv','w',encoding='utf-8')as ff:
        for i in range(len(codes_if)):
            ff.write(comments_if[i].replace(',','@$').replace("\"",'')+','+types_if[i].replace(',','@$').replace("\"",'')+','+codes_if[i].replace(',','@$').replace("\"",''))
    print('num_if_all:---- '+str(len(codes_if)))
    with open('D:\\short_comment\\step2 dependency parser\\statistics\\all_if_try_for\\comment_code_for.csv','w',encoding='utf-8')as fff:
        for i in range(len(codes_for)):
            fff.write(comments_for[i].replace(',','@$').replace("\"",'')+','+types_for[i].replace(',','@$').replace("\"",'')+','+codes_for[i].replace(',','@$').replace("\"",''))
    print('num_for_all:---- '+str(len(codes_for)))

    with open('D:\\short_comment\\step2 dependency parser\\statistics\\all_if_try_for\\comment_code_try.csv','w',encoding='utf-8')as ffff:
        for i in range(len(codes_try)):
            ffff.write(comments_try[i].replace(',','@$').replace("\"",'')+','+types_try[i].replace(',','@$').replace("\"",'')+','+codes_try[i].replace(',','@$').replace("\"",''))
    print('num_try_all:---- '+str(len(codes_try)))
            
    with open('D:\\short_comment\\step2 dependency parser\\statistics\\all_if_try_for\\comment_code_state.csv','w',encoding='utf-8')as fffff:
        for i in range(len(codes_state)):
            fffff.write(comments_state[i].replace(',','@$').replace("\"",'')+','+types_state[i].replace(',','@$').replace("\"",'')+','+codes_state[i].replace(',','@$').replace("\"",'')) 
    print('num_state_all:---- '+str(len(codes_state)))
            
def all_complete(b):
    data_all=[]
    # num=0
    with open(f'D:\\short_comment\\step2 dependency parser\\complete_{b}_all.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        data_all.extend(data)
    #     num+=len(data_all)
    # print(num)
    with open('complete_all.csv','a',encoding='utf-8')as ff:
        for i in range(len(data_all)):
            ff.write(data_all[i]+'\n')
    return len(data_all)
def all_ellipsis1(b):
    data_all=[]
    # num=0
    with open(f'D:\\short_comment\\step2 dependency parser\\ellipsis1_{b}_all.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        data_all.extend(data)
    #     num+=len(data_all)
    # print(num)
    with open('ellipsis1_all.csv','a',encoding='utf-8')as ff:
        for i in range(len(data_all)):
            ff.write(data_all[i]+'\n')
    return len(data_all)                        
def all_ellipsis2(b):
    data_all=[]
    # num=0
    with open(f'D:\\short_comment\\step2 dependency parser\\ellipsis2_{b}_all.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        data_all.extend(data)
    #     num+=len(data_all)
    # print(num)
    with open('ellipsis2_all.csv','a',encoding='utf-8')as ff:
        for i in range(len(data_all)):
            ff.write(data_all[i]+'\n')
    return len(data_all)
def deldup(c):
    with open(f'{c}_all.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        comms=[]
        codes=[]
        rels=[]
        data=data
        for dat in data:
            nee=dat.split(',')
            comm=nee[0]
            comms.append(comm)
            code=nee[1]
            codes.append(code)
            rel=nee[2]
            rels.append(rel)
        print(len(comms))
        index=[]
        for i in tqdm(range(len(comms))):
            for ref in data[i:i+50]:
                nee2=ref.split(',')
                if comms[i] == nee2[0] and codes[i] == nee2[1] and rels[i] != nee2[2]:
                    nee_del=data.index(ref)
                    index.append(nee_del)
                else:
                    pass
        # print(index)
        indexnew=list(set(index))
        indexnew.sort()
        # print(indexnew)
        data = [n for i, n in enumerate(data) if i not in indexnew]
    with open(f'{c}_all_deldup.csv','w',encoding='utf-8')as ff:
            for j in range(len(data)):
                ff.write(data[j])

        
def classify(c):
    with open(f'{c}_all_deldup.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        codes_if=[]
        comments_if=[]
        codes_for=[]
        comments_for=[]
        codes_try=[]
        comments_try=[]
        codes_state=[]
        comments_state=[]
        for dat in data:
            try:
                code=dat.split(',')[1]
            except:
                print(dat)
            comment=dat.split(',')[0]
            if code.startswith(('if','switch','else')):
                codes_if.append(code)
                comments_if.append(comment)
            elif code.startswith(('for','while','do','break','cotinue','case')):                
                codes_for.append(code)
                comments_for.append(comment)
            elif  code.startswith(('try','exception','return','throw')):
                codes_try.append(code)
                comments_try.append(comment)
            else:
                codes_state.append(code)
                comments_state.append(comment)
    with open(f'D:\\short_comment\\step2 dependency parser\\statistics\\result\\{c}_if.csv','w',encoding='utf-8')as ff:
        for i in range(len(codes_if)):
            ff.write(comments_if[i]+','+codes_if[i]+'\n')
    print(f'{c}: ---success if----' + str(len(codes_if)))
    with open(f'D:\\short_comment\\step2 dependency parser\\statistics\\result\\{c}_for.csv','w',encoding='utf-8')as fff:
        for i in range(len(codes_for)):
            fff.write(comments_for[i]+','+codes_for[i]+'\n')
    print(f'{c}: ---success for----' + str(len(codes_for)))

    with open(f'D:\\short_comment\\step2 dependency parser\\statistics\\result\\{c}_try.csv','w',encoding='utf-8')as ffff:
        for i in range(len(codes_try)):
            ffff.write(comments_try[i]+','+codes_try[i]+'\n')
    print(f'{c}: ---success try----' + str(len(codes_try)))
    
    with open(f'D:\\short_comment\\step2 dependency parser\\statistics\\result\\{c}_state.csv','w',encoding='utf-8')as fffff:
        for i in range(len(codes_state)):
            fffff.write(comments_state[i]+','+codes_state[i]+'\n')         
    print(f'{c}: ---success state----' + str(len(codes_state)))

if __name__ =='__main__':
    
    # classify_all()
    #-------------------------------------------------------
    # # step2
    # # input: complete_{b}_all.csv, ellipsis1_{b}_all.csv, ellipsis2_{b}_all.csv
    # # output: complete_all.csv
    # num_complete=0
    # num_ellipsis1=0
    # num_ellipsis2=0
    # for i in range(8):
    #     b=i+1
    #     num_complete += all_complete(b)
    #     num_ellipsis1 += all_ellipsis1(b)
    #     num_ellipsis2 += all_ellipsis2(b)
    # print('num_complete: '+ str(num_complete))
    # print('num_ellipsis1: '+ str(num_ellipsis1))
    # print('num_ellipsis2: '+ str(num_ellipsis2)) 
    
    # # #-----------------------------------------------------------
    name= ['complete','ellipsis1','ellipsis2']
    for c in name:
        deldup(c)
    
    # #-----------------------------------------------------------
    # for d in name:
    #     classify(d)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            