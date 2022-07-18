import textstat
import re
import numpy as np 

def reverse(string):
    list1 = string.split()
    string = ' '.join(list1[::-1])
    return string


def after_predict_read(a):
    
    with open(f'D:\\short_comment\\step3 completion\\codebert\\result\\codebert_{a}\\code\\model\\java\\yizhi_result\\result_{a}_all_succ_or_fail.txt','r',encoding='utf-8')as f1:
        data=f1.readlines()
        comms=[]
        rels=[]
        after_complete=[]
        if a =='sub':
            for dat in data:
                comm=dat.split(',')[0].replace('@$',',')
                rel=dat.split(',')[2]
                rell=rel.split(' ')[-1]
                rels.append(rell)
                comm=reverse(comm)
                comms.append(comm)
        else:
            for dat in data:
                comm=dat.split(',')[0].replace('@$',',')
                rel=dat.split(',')[2]
                rell=rel.split(' ')[-1].replace('\n','')
                rels.append(rell)
                # comm=reverse(comm)
                comms.append(comm)
        for i in range(len(comms)):
            neee=comms[i].replace('<PLACE_HOLDER>',rels[i])
            after_complete.append(neee)
            
        # nees=[]
        flesch_reading_eases=[]
        smog_indexs=[]
        flesch_kincaid_grades=[]
        coleman_liau_indexs=[]
        automated_readability_indexs=[]
        dale_chall_readability_scores=[]
        difficult_wordss=[]
        linsear_write_formulas=[]
        gunning_fogs=[]
        text_standards=[]
        for nee in after_complete:
            # nee=dat.split(',')[0].replace('@$',',')
            #The Flesch Reading Ease formula
            flesch_reading_ease=textstat.flesch_reading_ease(nee)
            smog_index=textstat.smog_index(nee)
            # Flesch-Kincaid Grade Level 
            flesch_kincaid_grade=textstat.flesch_kincaid_grade(nee)
            coleman_liau_index=textstat.coleman_liau_index(nee)
            #Automated Readability Index
            automated_readability_index=textstat.automated_readability_index(nee)
            dale_chall_readability_score=textstat.dale_chall_readability_score(nee)
            difficult_words=textstat.difficult_words(nee)
            linsear_write_formula=textstat.linsear_write_formula(nee)
            #The Fog Scale (Gunning FOG Formula)
            gunning_fog=textstat.gunning_fog(nee)
    
            #所有可读性的一致性
            text_standar=textstat.text_standard(nee)
            text_standar1=text_standar.split('and')[0]
            text_standar2=text_standar.split('and')[1]
            text_standar1=re.sub("\D","",text_standar1)
            text_standar2=re.sub("\D","",text_standar2)
            # print(text_standar1,text_standar2)
            text_standard=(int(text_standar1)+int(text_standar2))/2


            flesch_reading_eases.append(flesch_reading_ease)
            smog_indexs.append(smog_index)
            flesch_kincaid_grades.append(flesch_kincaid_grade)
            coleman_liau_indexs.append(coleman_liau_index)
            automated_readability_indexs.append(automated_readability_index)
            dale_chall_readability_scores.append(dale_chall_readability_score)
            difficult_wordss.append(difficult_words)
            linsear_write_formulas.append(linsear_write_formula)
            gunning_fogs.append(gunning_fog)
            text_standards.append(text_standard)
      
    with open(f'after_predict_{a}_read.csv','w',encoding='utf-8')as f2:       

            for i in range(len(flesch_reading_eases)):
                f2.write(str(flesch_reading_eases[i])+','+str(flesch_kincaid_grades[i])+','+str(coleman_liau_indexs[i])+','+str(automated_readability_indexs[i])
                         +','+str(dale_chall_readability_scores[i])+','+str(difficult_wordss[i])+','+str(linsear_write_formulas[i])+','+
                         str(gunning_fogs[i])+','+str(text_standards[i])+'\n')  
            # nees.append(nee)
    arr_mean_flesch_reading_eases = np.mean(flesch_reading_eases)
    print('after_predict_:------arr_mean_flesch_reading_eases----------'+ str(arr_mean_flesch_reading_eases))
    
    # arr_mean_smog_indexs = np.mean(smog_indexs)
    # print('complete:------arr_mean_smog_indexs----------'+ str(arr_mean_smog_indexs))

    # print(arr_mean_smog_indexs)
    
    arr_mean_flesch_kincaid_grades = np.mean(flesch_kincaid_grades)
    print('after_predict_:------arr_mean_flesch_kincaid_grades----------'+ str(arr_mean_flesch_kincaid_grades))

    # print(arr_mean_flesch_kincaid_grades)
        
    arr_mean_coleman_liau_indexs = np.mean(coleman_liau_indexs)
    print('after_predict_:------arr_mean_coleman_liau_indexs----------'+ str(arr_mean_coleman_liau_indexs))

    # print(arr_mean_coleman_liau_indexs)
    
    arr_mean_automated_readability_indexs = np.mean(automated_readability_indexs)
    print('after_predict_:------arr_mean_automated_readability_indexs----------'+ str(arr_mean_automated_readability_indexs))

    # print(arr_mean_automated_readability_indexs)
    # 
    arr_mean_dale_chall_readability_scores = np.mean(dale_chall_readability_scores)
    print('after_predict_:------arr_mean_dale_chall_readability_scores----------'+ str(arr_mean_dale_chall_readability_scores))

    # print(arr_mean_dale_chall_readability_scores)
    
    arr_mean_difficult_wordss = np.mean(difficult_wordss)
    print('after_predict_:------arr_mean_difficult_wordss----------'+ str(arr_mean_difficult_wordss))

    # print(arr_mean_difficult_wordss)
        
    arr_mean_linsear_write_formulas = np.mean(linsear_write_formulas)
    print('after_predict_:------arr_mean_linsear_write_formulas----------'+ str(arr_mean_linsear_write_formulas))

    # print(arr_mean_linsear_write_formulas)
    
    arr_mean_gunning_fogs = np.mean(gunning_fogs)
    print('after_predict_:------arr_mean_gunning_fogs----------'+ str(arr_mean_gunning_fogs))

    # print(arr_mean_gunning_fogs)    
        
    arr_mean_text_standards = np.mean(text_standards)
    print('after_predict_:------arr_mean_text_standards----------'+ str(arr_mean_text_standards))

    # print(arr_mean_text_standards) 
    print('after_predict_:------over')
    return  flesch_reading_eases, flesch_kincaid_grades, coleman_liau_indexs, automated_readability_indexs, dale_chall_readability_scores, difficult_wordss, linsear_write_formulas, gunning_fogs, text_standards
        
def before_predict_read(a):
    with open(f'D:\short_comment\step3 completion\codebert\\test_{a}.txt','r',encoding='utf-8')as f3:
        data=f3.readlines()
        comms=[]

        if a =='sub':
            for dat in data:
                comm=dat.split(',')[0].replace('@$',',')
                nee=comm.replace('<PLACE_HOLDER>','')
                nee=reverse(nee)
                comms.append(nee)
        else:
            for dat in data:
                comm=dat.split(',')[0].replace('@$',',')
                nee=comm.replace('<PLACE_HOLDER>','')
                comms.append(nee)
                

        # nees=[]
        flesch_reading_eases=[]
        # smog_indexs=[]
        flesch_kincaid_grades=[]
        coleman_liau_indexs=[]
        automated_readability_indexs=[]
        dale_chall_readability_scores=[]
        difficult_wordss=[]
        linsear_write_formulas=[]
        gunning_fogs=[]
        text_standards=[]
        for nee in comms:

        # for dat in data[1:]:
            # nee=dat.split(',')[0].replace('@&',',')
            #The Flesch Reading Ease formula
            flesch_reading_ease=textstat.flesch_reading_ease(nee)
            smog_index=textstat.smog_index(nee)
            # Flesch-Kincaid Grade Level 
            flesch_kincaid_grade=textstat.flesch_kincaid_grade(nee)
            coleman_liau_index=textstat.coleman_liau_index(nee)
            #Automated Readability Index
            automated_readability_index=textstat.automated_readability_index(nee)
            dale_chall_readability_score=textstat.dale_chall_readability_score(nee)
            difficult_words=textstat.difficult_words(nee)
            linsear_write_formula=textstat.linsear_write_formula(nee)
            #The Fog Scale (Gunning FOG Formula)
            gunning_fog=textstat.gunning_fog(nee)
    
            #所有可读性的一致性
            # text_standard=textstat.text_standard(nee)
            text_standar=textstat.text_standard(nee)
            text_standar1=text_standar.split('and')[0]
            text_standar2=text_standar.split('and')[1]
            text_standar1=re.sub("\D","",text_standar1)
            text_standar2=re.sub("\D","",text_standar2)
            # print(text_standar1,text_standar2)
            text_standard=(int(text_standar1)+int(text_standar2))/2

            flesch_reading_eases.append(flesch_reading_ease)
            # smog_indexs.append(smog_index)
            flesch_kincaid_grades.append(flesch_kincaid_grade)
            coleman_liau_indexs.append(coleman_liau_index)
            automated_readability_indexs.append(automated_readability_index)
            dale_chall_readability_scores.append(dale_chall_readability_score)
            difficult_wordss.append(difficult_words)
            linsear_write_formulas.append(linsear_write_formula)
            gunning_fogs.append(gunning_fog)
            text_standards.append(text_standard)
        # with open('result_for_buwanzheng_keduxing.csv','w',encoding='utf-8')as f1:
        # with open('result_if_buwanzheng_keduxing.csv','w',encoding='utf-8')as f1:
    with open(f'before_predict_{a}_read.csv','w',encoding='utf-8')as f4:
        # with open('result_state_buwanzheng_keduxing.csv','w',encoding='utf-8')as f1:
            for i in range(len(flesch_reading_eases)):
                f4.write(str(flesch_reading_eases[i])+','+str(flesch_kincaid_grades[i])+','+str(coleman_liau_indexs[i])+','+str(automated_readability_indexs[i])
                         +','+str(dale_chall_readability_scores[i])+','+str(difficult_wordss[i])+','+str(linsear_write_formulas[i])+','+
                         str(gunning_fogs[i])+','+str(text_standards[i])+'\n')

            # nees.append(nee)
    arr_mean_flesch_reading_eases = np.mean(flesch_reading_eases)
    print('before_predict_:------arr_mean_flesch_reading_eases----------'+ str(arr_mean_flesch_reading_eases))
    
    # arr_mean_smog_indexs = np.mean(smog_indexs)
    # print('ellipsis:------arr_mean_smog_indexs----------'+ str(arr_mean_smog_indexs))

    # print(arr_mean_smog_indexs)
    
    arr_mean_flesch_kincaid_grades = np.mean(flesch_kincaid_grades)
    print('before_predict_:------arr_mean_flesch_kincaid_grades----------'+ str(arr_mean_flesch_kincaid_grades))

    # print(arr_mean_flesch_kincaid_grades)
        
    arr_mean_coleman_liau_indexs = np.mean(coleman_liau_indexs)
    print('before_predict_:------arr_mean_coleman_liau_indexs----------'+ str(arr_mean_coleman_liau_indexs))

    # print(arr_mean_coleman_liau_indexs)
    
    arr_mean_automated_readability_indexs = np.mean(automated_readability_indexs)
    print('before_predict_:------arr_mean_automated_readability_indexs----------'+ str(arr_mean_automated_readability_indexs))

    # print(arr_mean_automated_readability_indexs)
    # 
    arr_mean_dale_chall_readability_scores = np.mean(dale_chall_readability_scores)
    print('before_predict_:------arr_mean_dale_chall_readability_scores----------'+ str(arr_mean_dale_chall_readability_scores))

    # print(arr_mean_dale_chall_readability_scores)
    
    arr_mean_difficult_wordss = np.mean(difficult_wordss)
    print('before_predict_:------arr_mean_difficult_wordss----------'+ str(arr_mean_difficult_wordss))

    # print(arr_mean_difficult_wordss)
        
    arr_mean_linsear_write_formulas = np.mean(linsear_write_formulas)
    print('before_predict_:------arr_mean_linsear_write_formulas----------'+ str(arr_mean_linsear_write_formulas))

    # print(arr_mean_linsear_write_formulas)
    
    arr_mean_gunning_fogs = np.mean(gunning_fogs)
    print('before_predict_:------arr_mean_gunning_fogs----------'+ str(arr_mean_gunning_fogs))

    # print(arr_mean_gunning_fogs)    
        
    arr_mean_text_standards = np.mean(text_standards)
    print('before_predict_:------arr_mean_text_standards----------'+ str(arr_mean_text_standards))

    # print(arr_mean_text_standards) 
    print('before_predict_:------over')
    return  flesch_reading_eases, flesch_kincaid_grades, coleman_liau_indexs, automated_readability_indexs, dale_chall_readability_scores, difficult_wordss, linsear_write_formulas, gunning_fogs, text_standards
def before_predict_read_pre(a):
    with open(f'D:\\short_comment\\step3 completion\\codebert\\result\\codebert_pre\\code\\model\\java\\del_dup\\test_{a}_deldup.txt','r',encoding='utf-8')as f3:
        data=f3.readlines()
        comms=[]

        if a =='sub':
            for dat in data:
                comm=dat.split(',')[0].replace('@$',',')
                nee=comm.replace('<PLACE_HOLDER>','')
                nee=reverse(nee)
                comms.append(nee)
        else:
            for dat in data:
                comm=dat.split(',')[0].replace('@$',',')
                nee=comm.replace('<PLACE_HOLDER>','')
                comms.append(nee)
                

        # nees=[]
        flesch_reading_eases=[]
        # smog_indexs=[]
        flesch_kincaid_grades=[]
        coleman_liau_indexs=[]
        automated_readability_indexs=[]
        dale_chall_readability_scores=[]
        difficult_wordss=[]
        linsear_write_formulas=[]
        gunning_fogs=[]
        text_standards=[]
        for nee in comms:

        # for dat in data[1:]:
            # nee=dat.split(',')[0].replace('@&',',')
            #The Flesch Reading Ease formula
            flesch_reading_ease=textstat.flesch_reading_ease(nee)
            smog_index=textstat.smog_index(nee)
            # Flesch-Kincaid Grade Level 
            flesch_kincaid_grade=textstat.flesch_kincaid_grade(nee)
            coleman_liau_index=textstat.coleman_liau_index(nee)
            #Automated Readability Index
            automated_readability_index=textstat.automated_readability_index(nee)
            dale_chall_readability_score=textstat.dale_chall_readability_score(nee)
            difficult_words=textstat.difficult_words(nee)
            linsear_write_formula=textstat.linsear_write_formula(nee)
            #The Fog Scale (Gunning FOG Formula)
            gunning_fog=textstat.gunning_fog(nee)
    
            #所有可读性的一致性
            # text_standard=textstat.text_standard(nee)
            text_standar=textstat.text_standard(nee)
            text_standar1=text_standar.split('and')[0]
            text_standar2=text_standar.split('and')[1]
            text_standar1=re.sub("\D","",text_standar1)
            text_standar2=re.sub("\D","",text_standar2)
            # print(text_standar1,text_standar2)
            text_standard=(int(text_standar1)+int(text_standar2))/2

            flesch_reading_eases.append(flesch_reading_ease)
            # smog_indexs.append(smog_index)
            flesch_kincaid_grades.append(flesch_kincaid_grade)
            coleman_liau_indexs.append(coleman_liau_index)
            automated_readability_indexs.append(automated_readability_index)
            dale_chall_readability_scores.append(dale_chall_readability_score)
            difficult_wordss.append(difficult_words)
            linsear_write_formulas.append(linsear_write_formula)
            gunning_fogs.append(gunning_fog)
            text_standards.append(text_standard)
        # with open('result_for_buwanzheng_keduxing.csv','w',encoding='utf-8')as f1:
        # with open('result_if_buwanzheng_keduxing.csv','w',encoding='utf-8')as f1:
    with open(f'before_predict_{a}_read.csv','w',encoding='utf-8')as f4:
        # with open('result_state_buwanzheng_keduxing.csv','w',encoding='utf-8')as f1:
            for i in range(len(flesch_reading_eases)):
                f4.write(str(flesch_reading_eases[i])+','+str(flesch_kincaid_grades[i])+','+str(coleman_liau_indexs[i])+','+str(automated_readability_indexs[i])
                         +','+str(dale_chall_readability_scores[i])+','+str(difficult_wordss[i])+','+str(linsear_write_formulas[i])+','+
                         str(gunning_fogs[i])+','+str(text_standards[i])+'\n')

            # nees.append(nee)
    arr_mean_flesch_reading_eases = np.mean(flesch_reading_eases)
    print('before_predict_:------arr_mean_flesch_reading_eases----------'+ str(arr_mean_flesch_reading_eases))
    
    # arr_mean_smog_indexs = np.mean(smog_indexs)
    # print('ellipsis:------arr_mean_smog_indexs----------'+ str(arr_mean_smog_indexs))

    # print(arr_mean_smog_indexs)
    
    arr_mean_flesch_kincaid_grades = np.mean(flesch_kincaid_grades)
    print('before_predict_:------arr_mean_flesch_kincaid_grades----------'+ str(arr_mean_flesch_kincaid_grades))

    # print(arr_mean_flesch_kincaid_grades)
        
    arr_mean_coleman_liau_indexs = np.mean(coleman_liau_indexs)
    print('before_predict_:------arr_mean_coleman_liau_indexs----------'+ str(arr_mean_coleman_liau_indexs))

    # print(arr_mean_coleman_liau_indexs)
    
    arr_mean_automated_readability_indexs = np.mean(automated_readability_indexs)
    print('before_predict_:------arr_mean_automated_readability_indexs----------'+ str(arr_mean_automated_readability_indexs))

    # print(arr_mean_automated_readability_indexs)
    # 
    arr_mean_dale_chall_readability_scores = np.mean(dale_chall_readability_scores)
    print('before_predict_:------arr_mean_dale_chall_readability_scores----------'+ str(arr_mean_dale_chall_readability_scores))

    # print(arr_mean_dale_chall_readability_scores)
    
    arr_mean_difficult_wordss = np.mean(difficult_wordss)
    print('before_predict_:------arr_mean_difficult_wordss----------'+ str(arr_mean_difficult_wordss))

    # print(arr_mean_difficult_wordss)
        
    arr_mean_linsear_write_formulas = np.mean(linsear_write_formulas)
    print('before_predict_:------arr_mean_linsear_write_formulas----------'+ str(arr_mean_linsear_write_formulas))

    # print(arr_mean_linsear_write_formulas)
    
    arr_mean_gunning_fogs = np.mean(gunning_fogs)
    print('before_predict_:------arr_mean_gunning_fogs----------'+ str(arr_mean_gunning_fogs))

    # print(arr_mean_gunning_fogs)    
        
    arr_mean_text_standards = np.mean(text_standards)
    print('before_predict_:------arr_mean_text_standards----------'+ str(arr_mean_text_standards))

    # print(arr_mean_text_standards) 
    print('before_predict_:------over')
    return  flesch_reading_eases, flesch_kincaid_grades, coleman_liau_indexs, automated_readability_indexs, dale_chall_readability_scores, difficult_wordss, linsear_write_formulas, gunning_fogs, text_standards
        
if __name__ =='__main__':
    # # name=['if','for','try','state','all']
    # # for a in name:
    # #     complete_read(a)
    # #     ellipsis_read(a)
    # name=['sub','obj']
    name=['pre']
    for a in name:
        after_predict_read(a)
        # before_predict_read(a)
        before_predict_read_pre(a)
