from tqdm import tqdm
def get_reldata(b):
    with open(f'D:\\short_comment\\step3 completion\lstm\\result\\test_{b}_lstm_final.txt','r',encoding='utf-8')as f0:
        data=f0.readlines()
    with open(f'D:\\short_comment\\step3 completion\lstm\\result\\result_{b}_lstm.txt','r',encoding='utf-8')as f1:
        rel_data=f1.readlines()
        nees=[]
        for dat in rel_data:
            nee1=dat.split(',')[0]
            nee2=dat.split(',')[1]
            nee3=dat.split(',')[2]
            nee4=nee3.split(' ')[0]
            nee5=nee3.split(' ')[1]
            nee=nee1+nee2+nee4+nee5
            nees.append(nee)
    with open(f'D:\\short_comment\\step3 completion\lstm\\result\\train_{b}_lstm_final.txt','r',encoding='utf-8')as f2:
        data1=f2.readlines()  
        alls=[]
        num=0.9*len(data1)
        train_data=data1[0:int(num)]
        for dats in train_data:
            nee1s=dats.split(',')[0]
            nee2s=dats.split(',')[1]
            nee3s=dats.split(',')[2]
            nee4s=nee3s.split(' ')[0]
            nee5s=nee3s.split(' ')[1]
            neess=nee1s+nee2s+nee4s+nee5s
            alls.append(neess)
    list_nee=[]
    dul=[]
    for a in tqdm(nees):
        if a not in alls:
            list_nee.append(nees.index(a))
        else:
            dul.append(nees.index(a))
    with open(f'D:\\short_comment\\step3 completion\lstm\\del_deup\\result_{b}_lstm_deldup.txt','w',encoding='utf-8')as f3:
        for a in list_nee:
            f3.write(rel_data[a])
    with open(f'D:\\short_comment\\step3 completion\lstm\\del_deup\\test_{b}_lstm_deldup.txt','w',encoding='utf-8')as f4:
        for a in list_nee:
            f4.write(data[a])     
    return nees,alls
if __name__=='__main__':
    name=['obj','sub']
    for a in name:
        get_reldata(a)



