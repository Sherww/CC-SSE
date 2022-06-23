import textstat
import re
import numpy as np 

def classify():
    # with open('comment_code_for_final_result.csv','r',encoding='utf-8')as f:
    with open('comment_code_if_final_result.csv','r',encoding='utf-8')as f:
    # with open('comment_code_try_final_result.csv','r',encoding='utf-8')as f:
    # with open('comment_code_state_final_result.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        ellipsis1s=[]
        ellipsis2s=[]
        others=[]
        completes=[]
        for dat in data[1:]:
            ellipsis1=dat.split(',')[12]
            ellipsis12=dat.split(',')[13]
            ellipsis2=dat.split(',')[10]
            ellipsis22=dat.split(',')[11]
            if (ellipsis1 != '0' or ellipsis12 != '0' ) and (ellipsis2  =='0' and ellipsis22 =='0'):
                ellipsis1s.append(dat)
            elif (ellipsis1  != '0' or ellipsis12 != '0') and (ellipsis2 != '0' or ellipsis22 != '0'):
                completes.append(dat)
            elif (ellipsis2 != '0' or ellipsis22 != '0') and (ellipsis1 == '0' and ellipsis12 == '0'):
                ellipsis2s.append(dat)
            else:
                others.append(dat)
        print('none ellipsis:', len(completes))
        print('ellipsis of subject:',len(ellipsis2s))
        print('ellipsi of object:',len(ellipsis1s))
        print('ellipsi of predicate:',len(others))
    # with open('for_complete.csv','w',encoding='utf-8')as ff:
    with open('if_complete.csv','w',encoding='utf-8')as ff:
    # with open('try_complete.csv','w',encoding='utf-8')as ff:
    # with open('state_complete.csv','w',encoding='utf-8')as ff:

        for j in range(len(completes)):
            ff.write(completes[j])
            
            
    # with open('for_ellipsis.csv','w',encoding='utf-8')as fff:
    with open('if_ellipsis.csv','w',encoding='utf-8')as fff:
    # with open('try_ellipsis.csv','w',encoding='utf-8')as fff:
    # with open('state_ellipsis.csv','w',encoding='utf-8')as fff:
        for i in range(len(ellipsis1s)):
            fff.write(ellipsis1s[i])
        for k in range(len(ellipsis2s)):
            fff.write(ellipsis2s[k])
        for z in range(len(others)):
            fff.write(others[z])
    return ellipsis2s,ellipsis1s,completes,others
    
    
def complete_read(a):
    
    with open(f'D:\\short_comment\\step2 dependency parser\\statistics\\all_if_try_for\\complete_{a}.csv','r',encoding='utf-8')as f1:
        data=f1.readlines()
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
        for dat in data:
        # for dat in data[1:]:
            nee=dat.split(',')[0].replace('@$',',')
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
            #Consistency of all readability
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
        # with open('result_for_complete_keduxing.csv','w',encoding='utf-8')as f2:
        # with open('result_if_complete_keduxing.csv','w',encoding='utf-8')as f2:      
    with open(f'complete_{a}_read.csv','w',encoding='utf-8')as f2:       
        # with open('result_state_complete_keduxing.csv','w',encoding='utf-8')as f2:       

            for i in range(len(flesch_reading_eases)):
                f2.write(str(flesch_reading_eases[i])+','+str(flesch_kincaid_grades[i])+','+str(coleman_liau_indexs[i])+','+str(automated_readability_indexs[i])
                         +','+str(dale_chall_readability_scores[i])+','+str(difficult_wordss[i])+','+str(linsear_write_formulas[i])+','+
                         str(gunning_fogs[i])+','+str(text_standards[i])+'\n')  
            # nees.append(nee)
    arr_mean_flesch_reading_eases = np.mean(flesch_reading_eases)
    print('complete:------arr_mean_flesch_reading_eases----------'+ str(arr_mean_flesch_reading_eases))
    
    # arr_mean_smog_indexs = np.mean(smog_indexs)
    # print('complete:------arr_mean_smog_indexs----------'+ str(arr_mean_smog_indexs))

    # print(arr_mean_smog_indexs)
    
    arr_mean_flesch_kincaid_grades = np.mean(flesch_kincaid_grades)
    print('complete:------arr_mean_flesch_kincaid_grades----------'+ str(arr_mean_flesch_kincaid_grades))

    # print(arr_mean_flesch_kincaid_grades)
        
    arr_mean_coleman_liau_indexs = np.mean(coleman_liau_indexs)
    print('complete:------arr_mean_coleman_liau_indexs----------'+ str(arr_mean_coleman_liau_indexs))

    # print(arr_mean_coleman_liau_indexs)
    
    arr_mean_automated_readability_indexs = np.mean(automated_readability_indexs)
    print('complete:------arr_mean_automated_readability_indexs----------'+ str(arr_mean_automated_readability_indexs))

    # print(arr_mean_automated_readability_indexs)
    # 
    arr_mean_dale_chall_readability_scores = np.mean(dale_chall_readability_scores)
    print('complete:------arr_mean_dale_chall_readability_scores----------'+ str(arr_mean_dale_chall_readability_scores))

    # print(arr_mean_dale_chall_readability_scores)
    
    arr_mean_difficult_wordss = np.mean(difficult_wordss)
    print('complete:------arr_mean_difficult_wordss----------'+ str(arr_mean_difficult_wordss))

    # print(arr_mean_difficult_wordss)
        
    arr_mean_linsear_write_formulas = np.mean(linsear_write_formulas)
    print('complete:------arr_mean_linsear_write_formulas----------'+ str(arr_mean_linsear_write_formulas))

    # print(arr_mean_linsear_write_formulas)
    
    arr_mean_gunning_fogs = np.mean(gunning_fogs)
    print('complete:------arr_mean_gunning_fogs----------'+ str(arr_mean_gunning_fogs))

    # print(arr_mean_gunning_fogs)    
        
    arr_mean_text_standards = np.mean(text_standards)
    print('complete:------arr_mean_text_standards----------'+ str(arr_mean_text_standards))

    # print(arr_mean_text_standards) 
    print('complete:------over')
    return  flesch_reading_eases, flesch_kincaid_grades, coleman_liau_indexs, automated_readability_indexs, dale_chall_readability_scores, difficult_wordss, linsear_write_formulas, gunning_fogs, text_standards
        
def ellipsis_read(a):
    with open(f'D:\\short_comment\\step2 dependency parser\\statistics\\all_if_try_for\\ellipsis_{a}.csv','r',encoding='utf-8')as f3:
    # with open('state_ellipsis.csv','r',encoding='utf-8')as ff:
        data=f3.readlines()
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
        for dat in data:

        # for dat in data[1:]:
            nee=dat.split(',')[0].replace('@&',',')
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
            #Consistency of all readability
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
        # with open('result_for_ellipsis_keduxing.csv','w',encoding='utf-8')as f1:
        # with open('result_if_ellipsis_keduxing.csv','w',encoding='utf-8')as f1:
    with open(f'ellipsis_{a}_read.csv','w',encoding='utf-8')as f4:
        # with open('result_state_ellipsis_keduxing.csv','w',encoding='utf-8')as f1:
            for i in range(len(flesch_reading_eases)):
                f4.write(str(flesch_reading_eases[i])+','+str(flesch_kincaid_grades[i])+','+str(coleman_liau_indexs[i])+','+str(automated_readability_indexs[i])
                         +','+str(dale_chall_readability_scores[i])+','+str(difficult_wordss[i])+','+str(linsear_write_formulas[i])+','+
                         str(gunning_fogs[i])+','+str(text_standards[i])+'\n')

            # nees.append(nee)
    arr_mean_flesch_reading_eases = np.mean(flesch_reading_eases)
    print('ellipsis:------arr_mean_flesch_reading_eases----------'+ str(arr_mean_flesch_reading_eases))
    
    # arr_mean_smog_indexs = np.mean(smog_indexs)
    # print('ellipsis:------arr_mean_smog_indexs----------'+ str(arr_mean_smog_indexs))

    # print(arr_mean_smog_indexs)
    
    arr_mean_flesch_kincaid_grades = np.mean(flesch_kincaid_grades)
    print('ellipsis:------arr_mean_flesch_kincaid_grades----------'+ str(arr_mean_flesch_kincaid_grades))

    # print(arr_mean_flesch_kincaid_grades)
        
    arr_mean_coleman_liau_indexs = np.mean(coleman_liau_indexs)
    print('ellipsis:------arr_mean_coleman_liau_indexs----------'+ str(arr_mean_coleman_liau_indexs))

    # print(arr_mean_coleman_liau_indexs)
    
    arr_mean_automated_readability_indexs = np.mean(automated_readability_indexs)
    print('ellipsis:------arr_mean_automated_readability_indexs----------'+ str(arr_mean_automated_readability_indexs))

    # print(arr_mean_automated_readability_indexs)
    # 
    arr_mean_dale_chall_readability_scores = np.mean(dale_chall_readability_scores)
    print('ellipsis:------arr_mean_dale_chall_readability_scores----------'+ str(arr_mean_dale_chall_readability_scores))

    # print(arr_mean_dale_chall_readability_scores)
    
    arr_mean_difficult_wordss = np.mean(difficult_wordss)
    print('ellipsis:------arr_mean_difficult_wordss----------'+ str(arr_mean_difficult_wordss))

    # print(arr_mean_difficult_wordss)
        
    arr_mean_linsear_write_formulas = np.mean(linsear_write_formulas)
    print('ellipsis:------arr_mean_linsear_write_formulas----------'+ str(arr_mean_linsear_write_formulas))

    # print(arr_mean_linsear_write_formulas)
    
    arr_mean_gunning_fogs = np.mean(gunning_fogs)
    print('ellipsis:------arr_mean_gunning_fogs----------'+ str(arr_mean_gunning_fogs))

    # print(arr_mean_gunning_fogs)    
        
    arr_mean_text_standards = np.mean(text_standards)
    print('ellipsis:------arr_mean_text_standards----------'+ str(arr_mean_text_standards))

    # print(arr_mean_text_standards) 
    print('ellipsis:------over')
    return  flesch_reading_eases, flesch_kincaid_grades, coleman_liau_indexs, automated_readability_indexs, dale_chall_readability_scores, difficult_wordss, linsear_write_formulas, gunning_fogs, text_standards
    
if __name__ =='__main__':
    # name=['if','for','try','state','all']
    # for a in name:
    #     complete_read(a)
    #     ellipsis_read(a)

        complete_read('all')
        ellipsis_read('all')
