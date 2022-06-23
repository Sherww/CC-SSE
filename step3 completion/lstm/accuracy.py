from nltk.translate.bleu_score import sentence_bleu
from sklearn.metrics import precision_score,recall_score,f1_score
import numpy as np
from keras.preprocessing.text import Tokenizer

with open('result_obj_lstm.txt','r',encoding='utf-8')as f:
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
with open('test_obj_lstm.txt','r',encoding='utf-8')as f1:
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
with open('result_obj_yizhi.txt','w',encoding='utf-8')as f2:
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
with(open('test_obj_lstm_input.txt','r',encoding='utf-8'))as f4:
    e=f4.readlines()
with open('result_yizhi.txt','w',encoding='utf-8')as f3:
    c=[]
    d=[]
    for i in range(len(test)):
        if test[i] == result[i]:
            c.append(e[i])
        else:
            d.append(e[i])
    for i in range(len(a)):
        f3.write(c[i])

pre = precision_score(test,result,average='macro',zero_division =1)
# 
rec = recall_score(test,result,average='macro',zero_division =1)
# 
f1_score=f1_score(test, result, average='macro')
print(pre)
print(rec)
print(f1_score)
# 




