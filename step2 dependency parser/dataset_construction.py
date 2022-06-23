import random 
# import string

def reverse(string):
    list1 = string.split()
    string = ' '.join(list1[::-1])
    return string

def completelink(a):
    # a=1

    with open (f'D:\\short_comment\\step2 dependency parser\\dependency_result\\complete_{a}.csv','r',encoding='utf-8')as f1:
        num=[]
        complete=[]
        data=f1.readlines()
        for dat in data:
            num.append(dat.split(',')[1].replace("\n", ''))
            complete.append(dat.split(',')[0])
    with open('D:\\short_comment\\step1 data clean\\cleancomment_final.txt','r',encoding='utf-8') as f2:
        codes=[]
        comms=[]
        data2=f2.readlines()
        for dat in data2:
            nee=dat.split('\",\"')
            comm=nee[0].replace("\"",'').replace(",", '@$')
            comms.append(comm)
            code=nee[2].replace("\"",'').replace('\n', '').replace(",", '@$')
            codes.append(code)
    with open(f'complete_{a}_all.csv','w',encoding='utf-8')as f3:
        
        for k in range(len(num)):
            n=num[k]
            # print(n)
            try:
                j=int(float(n))   
                f3.write(str(comms[j])+','+str(codes[j])+','+str(complete[k])+'\n')

            except:
                pass
def ellipsis1link(a):   
    #ellipsis1
    with open (f'D:\\short_comment\\step2 dependency parser\\dependency_result\\ellipsis1_{a}.csv','r',encoding='utf-8')as f4:
        num=[]
        complete=[]
        data=f4.readlines()
        for dat in data:
            num.append(dat.split(',')[1].replace("\n", ''))
            complete.append(dat.split(',')[0])

    with open('D:\\short_comment\\step1 data clean\\cleancomment_final.txt','r',encoding='utf-8') as f5:
        codes=[]
        comms=[]
        data2=f5.readlines()
        for dat in data2:
            nee=dat.split('\",\"')
            comm=nee[0].replace("\"",'').replace(",", '@$')
            comms.append(comm)
            code=nee[2].replace("\"",'').replace('\n', '').replace(",", '@$')
            codes.append(code)

    with open(f'ellipsis1_{a}_all.csv','w',encoding='utf-8')as f6:
        for k in range(len(num)):
            n=num[k]
            try:
                j=int(float(n))               
                f6.write(str(comms[j])+','+str(codes[j])+','+str(complete[k])+'\n')
            except:
                pass
def ellipsis2link(a):
    #ellipsis2
    with open (f'D:\\short_comment\\step2 dependency parser\\dependency_result\\ellipsis2_{a}.csv','r',encoding='utf-8')as f7:
        num=[]
        complete=[]
        data=f7.readlines()
        for dat in data:
            num.append(dat.split(',')[1].replace("\n", ''))
            complete.append(dat.split(',')[0])

    with open('D:\\short_comment\\step1 data clean\\cleancomment_final.txt','r',encoding='utf-8') as f8:
        codes=[]
        comms=[]
        data2=f8.readlines()
        for dat in data2:
            nee=dat.split('\",\"')
            comm=nee[0].replace("\"",'').replace(",", '@$')
            comms.append(comm)
            code=nee[2].replace("\"",'').replace('\n', '').replace(",", '@$')
            codes.append(code)

    with open(f'ellipsis2_{a}_all.csv','w',encoding='utf-8')as f9:
        for k in range(len(num)):
            n=num[k]
            try:
                
                j=int(float(n))               
                f9.write(str(comms[j])+','+str(codes[j])+','+str(complete[k])+'\n')
            except:
                pass
def all_complete(b):
    data_all=[]
    with open(f'complete_{b}_all.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        data_all.extend(data)
    with open('complete_all.csv','a',encoding='utf-8')as ff:
        for i in range(len(data_all)):
            ff.write(data_all[i])
def clean_pron():
    with open('complete_all.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nee_data=[]
        # i=0

        for dat in data:
            ne=dat.split(",")[-1]
            # print(ne)
            sub=ne.split()[0]
            obj=ne.split()[-1]
            if "," in ne:
                print('yes')
                pass
            
            elif len(ne.split())!=3:
                print(ne)
                pass
            elif sub == "my" or sub == "us" or sub == "we" or sub == "it" or sub == "they" or sub == "i" or sub == "you" or sub == "he" or sub=="she" or sub == "this" or sub=="that" or sub=="there":
                pass
            elif obj == "my" or obj == "us" or obj == "we" or obj == "it" or obj == "they" or obj == "i" or obj == "you" or obj == "he" or obj=="she" or obj == "this" or obj=="that" or obj=="there":
                pass

            else:
                nee_data.append(dat)
    with open('complete_all_clean.csv','w',encoding='utf-8')as ff:
        for i in range(len(nee_data)):
            ff.write(nee_data[i])

def divided():
    with open('complete_all_clean.csv','r',encoding='utf-8')as f1:

        data=f1.readlines()
        
        random.shuffle(data)
        print(len(data))
        num_train=int(len(data)*0.8)
        num_valid=int(len(data)*0.9)
        num_test=int(len(data))
        # a=random.sample(data,1000)
        # print(len(a))
    with open('D:\\short_comment\\step2 dependency parser\\divided\\train_pre.txt','w',encoding='utf-8')as f2: 
        for i in range(len(data[0:num_train])):
            f2.write(data[i])
    
    with open('D:\\short_comment\\step2 dependency parser\\divided\\valid_pre.txt','w',encoding='utf-8')as f3:
        for j in range(num_train,num_valid):
            f3.write(data[j])
    with open('D:\\short_comment\\step2 dependency parser\\divided\\test_pre.txt','w',encoding='utf-8')as f4:
        for k in range(num_valid,num_test):
            f4.write(data[k])
        
def dataset_train():
    with open('D:\\short_comment\\step2 dependency parser\\divided\\train_pre.txt','r',encoding='utf-8')as f:
        comms1=[]
        comms2=[]
        codes=[]
        completes=[]
        data=f.readlines()
        for dat in data:
           nee=dat.split(',')
           complete=nee[2].replace('\n','')
           
           completes.append(complete)
           try:
               zhu=complete.split()[0]
               bins=complete.split()[2]
           except:
               print(complete)
           comm=nee[0]
           code=nee[1]
           comm1=comm.replace(zhu,'<PLACE_HOLDER>')
           comm2=comm.replace(bins,'<PLACE_HOLDER>')
           comms1.append(comm1)
           comms2.append(comm2)
           codes.append(code)
    with open('D:\\short_comment\\step2 dependency parser\\dataset\\train_sub.txt','w',encoding='utf-8')as ff:
        for i in range(len(comms1)):
            #reverse
            ff.write(reverse(reverse(comms1[i])+','+codes[i])+','+reverse(completes[i])+'\n')
    with open('D:\\short_comment\\step2 dependency parser\\dataset\\train_obj.txt','w',encoding='utf-8')as fff:
        for i in range(len(comms2)):
            fff.write(comms2[i]+','+codes[i]+','+completes[i]+'\n')               
            # fff.write(codes[i]+','+comms2[i]+','+completes[i]+'\n')               
def dataset_valid():
 
    with open('D:\\short_comment\\step2 dependency parser\\divided\\valid_pre.txt','r',encoding='utf-8')as f:
        comms1=[]
        comms2=[]
        codes=[]
        completes=[]
        data=f.readlines()
        for dat in data:
           nee=dat.split(',')
           complete=nee[2].replace('\n','')
           completes.append(complete)
           zhu=complete.split()[0]
           bins=complete.split()[2]
           comm=nee[0]
           code=nee[1]
           comm1=comm.replace(zhu,'<PLACE_HOLDER>')
           comm2=comm.replace(bins,'<PLACE_HOLDER>')
           comms1.append(comm1)
           comms2.append(comm2)
           codes.append(code)
    with open('D:\\short_comment\\step2 dependency parser\\dataset\\valid_sub.txt','w',encoding='utf-8')as ff:
        for i in range(len(comms1)):
            #reverse
            ff.write(reverse(comms1[i])+','+reverse(codes[i])+','+reverse(completes[i])+'\n')
    with open('D:\\short_comment\\step2 dependency parser\\dataset\\valid_obj.txt','w',encoding='utf-8')as fff:
        for i in range(len(comms2)):
            fff.write(comms2[i]+','+codes[i]+','+completes[i]+'\n')               
            # fff.write(codes[i]+','+comms2[i]+','+completes[i]+'\n')               
 
def dataset_test():
    
    with open('D:\\short_comment\\step2 dependency parser\\divided\\test_pre.txt','r',encoding='utf-8')as f:
        comms1=[]
        comms2=[]
        codes=[]
        completes=[]
        test_input_zhus=[]
        test_input_bins=[]
        data=f.readlines()
        for dat in data:
           nee=dat.split(',')
           complete=nee[2].replace('\n','')
           completes.append(complete)
           zhu=complete.split()[0]
           bins=complete.split()[2]
           test_input_bin=complete.split()[0:2]
           test_input_zhu=complete.split()[1:]

           test_input_zhus.append(str(test_input_zhu).replace('[','').replace(']','').replace('\'','').replace(',',''))
           test_input_bins.append(str(test_input_bin).replace('[','').replace(']','').replace('\'','').replace(',',''))
           comm=nee[0]
           code=nee[1]
           comm1=comm.replace(zhu,'<PLACE_HOLDER>')
           comm2=comm.replace(bins,'<PLACE_HOLDER>')
           comms1.append(comm1)
           comms2.append(comm2)
           codes.append(code)
    with open('D:\\short_comment\\step2 dependency parser\\dataset\\test_sub.txt','w',encoding='utf-8')as ff:
        for i in range(len(comms1)):
            #reverse
            ff.write(reverse(comms1[i])+','+reverse(codes[i])+','+reverse(completes[i])+'\n')

    with open('D:\\short_comment\\step2 dependency parser\\dataset\\test_obj.txt','w',encoding='utf-8')as fff:
        for i in range(len(comms2)):
            fff.write(comms2[i]+','+codes[i]+','+completes[i]+'\n')   
            # fff.write(codes[i]+','+comms2[i]+','+completes[i]+'\n')   
            
    with open('D:\\short_comment\\step2 dependency parser\\dataset\\test_sub_input.txt','w',encoding='utf-8')as f1:
        for i in range(len(comms1)):
            #reverse
            f1.write(reverse(comms1[i])+','+reverse(codes[i])+','+reverse(test_input_zhus[i])+'\n')
    with open('D:\\short_comment\\step2 dependency parser\\dataset\\test_obj_input.txt','w',encoding='utf-8')as f2:
        for i in range(len(comms2)):
            f2.write(comms2[i]+','+codes[i]+','+test_input_bins[i]+'\n')               
            # f2.write(codes[i]+','+comms2[i]+','+test_input_bins[i]+'\n')               
  
def divided_lstm():
    with open('complete_all_clean.csv','r',encoding='utf-8')as f1:

        data=f1.readlines()
        
        random.shuffle(data)
        print(len(data))
        num_train=int(len(data)*0.9)
        # num_valid=int(len(data)*0.9)
        num_test=int(len(data))

    with open('D:\\short_comment\\step2 dependency parser\\divided\\train_pre_lstm.txt','w',encoding='utf-8')as f2: 
        for i in range(0,num_train):
            f2.write(data[i])
    
    with open('D:\\short_comment\\step2 dependency parser\\divided\\test_pre_lstm.txt','w',encoding='utf-8')as f3:
        for j in range(num_train,num_test):
            f3.write(data[j])
    
def dataset_train_lstm():
        
    with open('D:\\short_comment\\step2 dependency parser\\divided\\train_pre_lstm.txt','r',encoding='utf-8')as f:
        comms1=[]
        comms2=[]
        codes=[]
        completes=[]

        data=f.readlines()
        for dat in data:
           nee=dat.split(',')
           complete=nee[2].replace('\n','')
           completes.append(complete)
           zhu=complete.split()[0]
           try:
               bins=complete.split()[2]
           except:
               print(complete)
           comm=nee[0]
           code=nee[1]
           comm1=comm.replace(zhu,'<PLACE_HOLDER>')
           comm2=comm.replace(bins,'<PLACE_HOLDER>')
           comms1.append(comm1)
           comms2.append(comm2)
           codes.append(code)
    with open('D:\\short_comment\\step2 dependency parser\\dataset-lstm\\train_sub_lstm.txt','w',encoding='utf-8')as ff:
        for i in range(len(comms1)):
            #reverse
            ff.write(reverse(comms1[i])+','+reverse(codes[i])+','+reverse(completes[i])+'\n')
    with open('D:\\short_comment\\step2 dependency parser\\dataset-lstm\\train_obj_lstm.txt','w',encoding='utf-8')as fff:
        for i in range(len(comms2)):
            fff.write(comms2[i]+','+codes[i]+','+completes[i]+'\n')   
            # fff.write(codes[i]+','+comms2[i]+','+completes[i]+'\n')  

def dataset_test_lstm():
    with open('D:\\short_comment\\step2 dependency parser\\divided\\test_pre_lstm.txt','r',encoding='utf-8')as f:
        comms1=[]
        comms2=[]
        codes=[]
        completes=[]
        test_input_zhus=[]
        test_input_bins=[]
        
        data=f.readlines()
        for dat in data:
           nee=dat.split(',')
           complete=nee[2].replace('\n','')
           completes.append(complete)
           zhu=complete.split()[0]
           bins=complete.split()[2]
           test_input_bin=complete.split()[0:2]
           # print(test_input_zhu)
           test_input_zhu=complete.split()[1:]

           test_input_zhus.append(str(test_input_zhu).replace('[','').replace(']','').replace('\'','').replace(',',''))
           test_input_bins.append(str(test_input_bin).replace('[','').replace(']','').replace('\'','').replace(',',''))
           comm=nee[0]
           code=nee[1]
           comm1=comm.replace(zhu,'<PLACE_HOLDER>')
           comm2=comm.replace(bins,'<PLACE_HOLDER>')
           comms1.append(comm1)
           comms2.append(comm2)
           codes.append(code)
    with open('D:\\short_comment\\step2 dependency parser\\dataset-lstm\\test_sub_lstm.txt','w',encoding='utf-8')as ff:
        for i in range(len(comms1)):
            #reverse
            ff.write(reverse(comms1[i])+','+reverse(codes[i])+','+reverse(completes[i])+'\n')
    with open('D:\\short_comment\\step2 dependency parser\\dataset-lstm\\test_obj_lstm.txt','w',encoding='utf-8')as fff:
        for i in range(len(comms2)):
            fff.write(comms2[i]+','+codes[i]+','+completes[i]+'\n')               
            # fff.write(codes[i]+','+comms2[i]+','+completes[i]+'\n')               
            
    with open('D:\\short_comment\\step2 dependency parser\\dataset-lstm\\test_sub_lstm_input.txt','w',encoding='utf-8')as f1:
        for i in range(len(comms1)):
            #reverse
            f1.write(reverse(comms1[i])+','+reverse(codes[i])+','+reverse(test_input_zhus[i])+'\n')

    with open('D:\\short_comment\\step2 dependency parser\\dataset-lstm\\test_obj_lstm_input.txt','w',encoding='utf-8')as f2:
        for i in range(len(comms2)):
            f2.write(comms2[i]+','+codes[i]+','+test_input_bins[i]+'\n') 
            # f2.write(codes[i]+','+comms2[i]+','+test_input_bins[i]+'\n') 
    
if __name__ == "__main__":
    
    # # step1 
    # # input: complete_{a}.csv, ellipsis1_{a}.csv, ellipsis2_{a}.csv, cleancomment_final.txt  
    # # output: complete_{a}_all.csv, ellipsis1_{a}_all.csv, ellipsis2_{a}_all.csv
    # for i in range(8):
    #     a=i+1
    #     completelink(a)
    #     ellipsis1link(a)
    #     ellipsis2link(a)
    
    # # step2
    # # input: complete_{b}_all.csv, ellipsis1_{b}_all.csv, ellipsis2_{b}_all.csv
    # # output: complete_all.csv
    # for i in range(8):
    #     b=i+1
    # # b=1
    #     all_complete(b)
    
    # # step2.5 
    # # input:  complete_all.csv
    # # output: complete_all_clean.csv
    # # Todo: wheter delete repeat
    # clean_pron()
    
    # # step3
    # # input:  complete_all_clean.csv
    # # output: train_pre.txt, valid_pre.txt, test_pre.txt 
    # divided()

    
    # # step4 
    # # input:  train_pre.txt, valid_pre.txt, test_pre.txt
    # # output: train_sub.txt, train_obj.txt, valid_sub.txt, valid_obj.txt, test_sub.txt, test_obj.txt
    # dataset_train()
    # dataset_valid()
    # dataset_test()
    
    # # step5
    # # input:  complete_all_clean.csv
    # # output: train_pre_lstm.txt, test_pre_lstm.txt 
    # divided_lstm()
    
    # step6
    # input:  train_pre_lstm.txt, test_pre_lstm.txt 
    # output:  train_sub_lstm, train_obj_lstm.txt, train_sub_lstm_input.txt,  test_sub_lstm.txt, test_obj_lstm.txt,  test_obj_lstm_input.txt
    dataset_train_lstm()
    dataset_test_lstm()