from sklearn.metrics import precision_score,recall_score,f1_score

with open('result_sub_lstm_deldup.txt','r',encoding='utf-8')as f:
    data=f.readlines()
    result=[]
    nees=[]
    codes=[]
    for line in data:
        nee=line.split(',')[2]
        resul=nee.split(' ')[2]
        result.append(resul)
        nees.append(nee)
        code=line.split(',')[0]+line.split(',')[1]
        codes.append(code)

with open('test_sub_lstm_deldup.txt','r',encoding='utf-8')as f1:
    data=f1.readlines()
    test=[]
    nee2s=[]
    codes2=[]
    for line in data:
        nee2=line.split(',')[2]
        tes=nee2.split(' ')[2]
        test.append(tes)
        nee2s.append(nee2)
        code2=line.split(',')[0]+line.split(',')[1]
        codes2.append(code2)

with open('result_sub_yizhi_deldup.txt','w',encoding='utf-8')as f2:
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
recal = recall_score(test,result,average='macro',zero_division =1)
precision = precision_score(test,result,average='macro',zero_division =1)
print("sklearn recall:{},precision:{}".format(recal,precision))
print("sklearn F1-score:{}".format((2*recal*precision)/(recal+precision)))
    
# pre = precision_score(test,result,average='macro',zero_division =1)
# 
# rec = recall_score(test,result,average='macro',zero_division =1)
# 
# f1_score=f1_score(test, result, average='macro')
# print(pre)
# print(rec)
# print(f1_score)
