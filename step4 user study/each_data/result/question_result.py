
import xlsxwriter as xw



import pandas as pd
import os
import openpyxl

def write_file(): 
    #文件路径
    #构建新的表格名称
    new_filename = 'questionnaire_all.xlsx'
    #找到文件路径下的所有表格名称，返回列表
    file_list=[]
    for a in range(32):
        file_dir= 'D:\\short_comment\\step4 user study\\each_data\\'+f'questionnaire_{a}.xlsx'
        file_list.append(file_dir)
    # file_list = os.listdir(file_dir)
    
    new_list = []
     
    for file in file_list:
        #重构文件路径
        file_path = os.path.join(file_dir,file)
        #将excel转换成DataFrame
        dataframe = pd.read_excel(file_path)
        #保存到新列表中
        new_list.append(dataframe+'\n')
     
    #多个DataFrame合并为一个
    df = pd.concat(new_list)
    #写入到一个新excel表中
    df.to_excel(new_filename,index=False)
def count():

    dataframe = pd.read_excel('questionnaire_all.xlsx')
    nee= pd.Series.to_list (dataframe.iloc[1:,5])
    befores=[]
    afters=[]
    for dat in nee:
        if type(dat) != float:
            before=dat.split(',')[0].replace('\n','')
            after=dat.split(',')[2].replace('\n','')
            befores.append(before)
            afters.append(after)
        else:
            befores.append(' ')
            afters.append(' ')

    comm=pd.Series.to_list (dataframe.iloc[1:,0])
    code=pd.Series.to_list (dataframe.iloc[1:,1])
    rel=pd.Series.to_list (dataframe.iloc[1:,2])
    succc_fail=pd.Series.to_list (dataframe.iloc[1:,3])
    sub_obj=pd.Series.to_list (dataframe.iloc[1:,4])
    xueli=pd.Series.to_list (dataframe.iloc[1:,6])
    experience=pd.Series.to_list (dataframe.iloc[1:,7])
    java_expe=pd.Series.to_list (dataframe.iloc[1:,8])
    work=pd.Series.to_list (dataframe.iloc[1:,9])
    role=pd.Series.to_list (dataframe.iloc[1:,10])
    program=pd.Series.to_list (dataframe.iloc[1:,11])
    all_data=[]
    print(len(befores))
    for i in range(len(befores)):
        all_dat=str(comm[i]).replace('\n','').replace(',','@$')+','+str(code[i]).replace('\n','').replace(',','@$')+','+str(rel[i]).replace('\n','').replace(',','@$')+','+str(succc_fail[i]).replace('\n','').replace(',','@$')+','+str(sub_obj[i]).replace('\n','').replace(',','@$')+','+str(befores[i]).replace('\n','').replace(',','@$')+','+str(afters[i]).replace(',','@$').replace('\n','')+','+str(xueli[i]).replace(',','@$').replace('\n','')+','+str(experience[i]).replace(',','@$').replace('\n','')+','+str(java_expe[i]).replace(',','@$').replace('\n','')+','+str(work[i]).replace(',','@$').replace('\n','')+','+str(role[i]).replace(',','@$').replace('\n','')+','+str(program[i]).replace(',','@$').replace('\n','')+'\n'
        all_data.append(all_dat)
    print(len(all_data))
    success_sub=[]
    success_obj=[]
    fail_sub=[]
    fail_obj=[]
    for da in all_data:
        nee=da.split(',')
        success=nee[3]
        sub=nee[4]
        if success =='success' and sub =='sub':
            success_sub.append(da)
        elif success =='success' and sub =='obj':
            success_obj.append(da)
        elif success =='fail' and sub =='sub':
            fail_sub.append(da)
        elif success =='fail' and sub =='obj':
            fail_obj.append(da)    
        else:
            print(da)
    all_data_final=success_sub+success_obj+fail_sub+fail_obj
    print(len(all_data_final))
    with open('before_after_result.csv','w',encoding='utf-8')as f:
        for i in range(len(all_data_final)):
            f.write(all_data_final[i])
if __name__=='__main__':
    # write_file()
    count()