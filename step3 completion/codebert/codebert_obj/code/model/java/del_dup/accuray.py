
from sklearn.metrics import precision_score,recall_score,f1_score


def hebing_obj():
    with open('result_obj_deldup.txt','r',encoding='utf-8')as f:
        data=f.readlines()
        rels=[]
        for dat in data:
            dat=dat.replace('.',' ')
            nee=dat.split(' ')[0].replace('\n','')
            # rel=dat.split('\t')[1]
            rels.append(nee)
    with open('test_obj_input_deldup.txt','r',encoding='utf-8')as ff:
        data1=ff.readlines()
    with open('test_obj_output_deldup.txt','w',encoding='utf-8')as fff:
        
        for i in range(len(rels)):
            fff.write(data1[i].replace('\n','')+ ' '+rels[i]+'\n')

def obj():
    with open('test_obj_output_deldup.txt','r',encoding='utf-8')as f:
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
    print(len(nees))
    print(len(codes))
    with open('test_obj_deldup.txt','r',encoding='utf-8')as f1:
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
    print(len(nee2s))
    print(len(codes2))

    recal = recall_score(test,result,average='macro',zero_division =1)
    precision = precision_score(test,result,average='macro',zero_division =1)
    print("sklearn recall:{},precision:{}".format(recal,precision))
    print("sklearn F1-score:{}".format((2*recal*precision)/(recal+precision)))
    
    
    pre = precision_score(test,result,average='macro',zero_division =1)
    # 
    rec = recall_score(test,result,average='macro',zero_division =1)
    # 
    f1_scores=f1_score(test,result,average='macro')
    print(pre)
    print(rec)
    print(f1_scores)
    # 
if __name__ == '__main__':
    hebing_obj()
    obj()