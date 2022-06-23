from tqdm import tqdm
def get_reldata():
    with open('test_1.output','r',encoding='utf-8')as f0:
        dat=f0.readlines()
        data=[]
        for da in dat:
            rel=da.split('\t')[1]
            data.append(rel)
    with open('D:\\short_comment\\step3 completion\\transformer\\transformer-main_obj_1\\data\\test_obj.txt','r',encoding='utf-8')as f01:
        datas=f01.readlines()
    with open('D:\\short_comment\\step3 completion\\transformer\\transformer-main_obj_1\\data\\test_obj.code','r',encoding='utf-8')as f1:
        rel_data=f1.readlines()
    with open('D:\\short_comment\\step3 completion\\transformer\\transformer-main_obj_1\\data\\train_obj.code','r',encoding='utf-8')as f2:
        data1=f2.readlines()  
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



