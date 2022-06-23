from tqdm import tqdm
def get_reldata():
    with open('D:\\short_comment\\step3 completion\\transformer\\transformer-main_obj_1\\data\\predict_test_obj.txt','r',encoding='utf-8')as f0:
        data=f0.readlines()
    with open('D:\\short_comment\\step3 completion\\transformer\\transformer-main_obj_1\\data\\test_obj.txt','r',encoding='utf-8')as f01:
        datas=f01.readlines()
    with open('D:\\short_comment\\step3 completion\\transformer\\transformer-main_obj_1\\data\\test_obj.code','r',encoding='utf-8')as f1:
        rel_data=f1.readlines()
        # nees=[]
        # for dat in rel_data:
        #     nee1=dat.split(',')[0]
        #     nee2=dat.split(',')[1]
        #     nee3=dat.split(',')[2]
        #     nee4=nee3.split(' ')[0]
        #     nee5=nee3.split(' ')[1]
        #     nee=nee1+nee2+nee4+nee5
        #     nees.append(nee)
    with open('D:\\short_comment\\step3 completion\\transformer\\transformer-main_obj_1\\data\\train_obj.code','r',encoding='utf-8')as f2:
        data1=f2.readlines()  
        # alls=[]
        # num=0.9*len(data1)
        # train_data=data1[0:int(num)]
        # for dats in train_data:
        #     nee1s=dats.split(',')[0]
        #     nee2s=dats.split(',')[1]
        #     nee3s=dats.split(',')[2]
        #     nee4s=nee3s.split(' ')[0]
        #     nee5s=nee3s.split(' ')[1]
        #     neess=nee1s+nee2s+nee4s+nee5s
        #     alls.append(neess)
    list_nee=[]
    dul=[]
    for a in tqdm(rel_data):
        if a not in data1:
            list_nee.append(rel_data.index(a))
        else:
            dul.append(rel_data.index(a))
    with open('result_obj_deldup.txt','w',encoding='utf-8')as f3:
        for a in list_nee:
            f3.write(data[a])
    with open('test_obj_input_deldup.txt','w',encoding='utf-8')as f4:
        for a in list_nee:
            f4.write(rel_data[a])     
    with open('test_obj_deldup.txt','w',encoding='utf-8')as f5:
        for a in list_nee:
            f5.write(datas[a])     
    # return nees,alls
if __name__=='__main__':

    get_reldata()



