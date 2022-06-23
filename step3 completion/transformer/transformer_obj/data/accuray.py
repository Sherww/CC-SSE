
from sklearn.metrics import precision_score,recall_score,f1_score


def hebing_obj():
    with open('predict_test_obj.txt','r',encoding='utf-8')as f:
        data=f.readlines()
        rels=[]
        for dat in data:
            dat=dat.replace('.',' ')
            nee=dat.split(' ')[0].replace('\n','')
            # rel=dat.split('\t')[1]
            rels.append(nee)
    with open('test_obj.code','r',encoding='utf-8')as ff:
        data1=ff.readlines()
    with open('test_obj_output.txt','w',encoding='utf-8')as fff:
        
        for i in range(len(rels)):
            fff.write(data1[i].replace('\n','')+ ' '+rels[i]+'\n')

def obj():
    with open('test_obj_output.txt','r',encoding='utf-8')as f:
        data=f.readlines()
        result=[]
        nees=[]
        codes=[]
        for line in data:
            nee=line.split(',')[2]
            resul=nee.split(' ')[2].replace('\n','')
            result.append(resul)
            nees.append(nee)
            code=line.split(',')[0]+line.split(',')[1]
            codes.append(code)
    with open('test_obj.txt','r',encoding='utf-8')as f1:
        data=f1.readlines()
        test=[]
        nee2s=[]
        codes2=[]
        for line in data:
            nee2=line.split(',')[2]
            tes=nee2.split(' ')[2].replace('\n','')
            test.append(tes)
            nee2s.append(nee2)
            code2=line.split(',')[0]+line.split(',')[1]
            codes2.append(code2)
    with open('D:\\short_comment\\step3 completion\\transformer\\transformer-main_obj_1\\data\\yizhi_result\\result_obj_all_succ_or_fail.txt','w',encoding='utf-8')as f0:
        succ=[]
        # fail=[]

        for i in range(len(test)):
            if test[i] == result[i]:
                succ.append(codes[i]+","+nees[i].replace('\n','')+','+'success'+'\n')
            else:
                succ.append(codes[i]+","+nees[i].replace('\n','')+','+'fail'+'\n')

        for i in range(len(succ)):
            f0.write(succ[i])
            
    with open('D:\\short_comment\\step3 completion\\transformer\\transformer-main_obj_1\\data\\yizhi_result\\result_obj_yizhi.txt','w',encoding='utf-8')as f2:
        a=[]
        b=[]
        c=[]
        d=[]
        for i in range(len(test)):
            if test[i] == result[i]:
                a.append(codes[i]+","+nees[i])
            else:
                b.append(codes[i]+","+nees[i])

        for i in range(len(a)):
            f2.write(a[i])
            
    with(open('test_obj_input.txt','r',encoding='utf-8'))as f4:
        e=f4.readlines()
           
    with open('D:\\short_comment\\step3 completion\\transformer\\transformer-main_obj_1\\data\\yizhi_result\\result_yizhi_obj.txt','w',encoding='utf-8')as f3:
    
        c=[]
        d=[]
        for i in range(len(test)):
            if test[i] == result[i]:
                c.append(e[i])
            else:
                d.append(e[i])
        for i in range(len(a)):
            f3.write(c[i])
    
    # print(test)
    # print(result)
    # test=np.array(test)
    # result=np.array(result)
    
    # print("the result of sklearn package")
    # auc = roc_auc_score(test,result,average='macro')
    # print("sklearn auc:",auc)
    # accuracy = accuracy_score(test,result,average='macro')
    # print("sklearn accuracy:",accuracy)
    
    # recal = recall_score(test,result,average='macro')
    # precision = precision_score(test,result,average='macro')
    # print("sklearn recall:{},precision:{}".format(recal,precision))
    # print("sklearn F1-score:{}".format((2*recal*precision)/(recal+precision)))
    
    
    pre = precision_score(test,result,average='macro',zero_division =1)
    # 
    rec = recall_score(test,result,average='macro',zero_division =1)
    # 
    f1_scores=f1_score(test,result,average='weighted')
    print(pre)
    print(rec)
    print(f1_scores)
    # 
if __name__ == '__main__':
    # hebing_obj()
    obj()