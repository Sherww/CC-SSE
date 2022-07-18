from __future__ import division
import numpy as np
from scipy import stats

def cliffsDelta(lst1, lst2, **dull):

    """Returns delta and true if there are more than 'dull' differences"""
    if not dull:
        dull = {'small': 0.147, 'medium': 0.33, 'large': 0.474} # effect sizes from (Hess and Kromrey, 2004)
    m, n = len(lst1), len(lst2)
    lst2 = sorted(lst2)
    j = more = less = 0
    for repeats, x in runs(sorted(lst1)):
        while j <= (n - 1) and lst2[j] < x:
            j += 1
        more += j*repeats
        while j <= (n - 1) and lst2[j] == x:
            j += 1
        less += (n - j)*repeats
    d = (more - less) / (m*n)
    size = lookup_size(d, dull)
    return d, size


def lookup_size(delta: float, dull: dict) -> str:
    """
    :type delta: float
    :type dull: dict, a dictionary of small, medium, large thresholds.
    """
    delta = abs(delta)
    if delta < dull['small']:
        return 'negligible'
    if dull['small'] <= delta < dull['medium']:
        return 'small'
    if dull['medium'] <= delta < dull['large']:
        return 'medium'
    if delta >= dull['large']:
        return 'large'


def runs(lst):
    """Iterator, chunks repeated values"""
    for j, two in enumerate(lst):
        if j == 0:
            one, i = two, 0
        if one != two:
            yield j - i, one
            i = j
        one = two
    yield j - i + 1, two 
def kstest_ellipsis(a):
    with open(f'before_predict_{a}_read.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        flesch_reading_eases=[]
        flesch_kincaid_grades=[]
        coleman_liau_indexs=[]
        automated_readability_indexs=[]
        dale_chall_readability_scores=[]
        difficult_wordss=[]
        linsear_write_formulas=[]
        gunning_fogs=[]
        text_standards=[]
        for dat in data:
            nee=dat.split(',')
            flesch_reading_eases.append(float(nee[0]))
            flesch_kincaid_grades.append(float(nee[1]))
            coleman_liau_indexs.append(float(nee[2]))
            automated_readability_indexs.append(float(nee[3]))
            dale_chall_readability_scores.append(float(nee[4]))
            difficult_wordss.append(float(nee[5]))
            linsear_write_formulas.append(float(nee[6]))
            gunning_fogs.append(float(nee[7])) 
            text_standards.append(float(nee[8]))
        mean0= np.mean(flesch_reading_eases)
        mean1= np.mean(flesch_kincaid_grades)
        mean2= np.mean(coleman_liau_indexs)
        mean3= np.mean(automated_readability_indexs)        
        mean4= np.mean(dale_chall_readability_scores)
        mean5= np.mean(difficult_wordss)        
        mean6= np.mean(linsear_write_formulas)
        mean7= np.mean(gunning_fogs)
        mean8= np.mean(text_standards)
        
        std0= np.std(flesch_reading_eases)
        std1= np.std(flesch_kincaid_grades)
        std2= np.std(coleman_liau_indexs)
        std3= np.std(automated_readability_indexs)        
        std4= np.std(dale_chall_readability_scores)
        std5= np.std(difficult_wordss)        
        std6= np.std(linsear_write_formulas)
        std7= np.std(gunning_fogs)
        std8= np.std(text_standards)

        rel0= stats.kstest(flesch_reading_eases, 'norm', (mean0, std0))
        if rel0[1]> 0.05:
            print('yes---flesch_reading_eases---norm')
        else:
            print('no---flesch_reading_eases---not_norm')
        rel1= stats.kstest(flesch_kincaid_grades, 'norm', (mean1, std1))
        if rel1[1]> 0.05:
            print('yes---flesch_kincaid_grades---norm')
        else:
            print('no---flesch_kincaid_grades---not_norm')
        rel2= stats.kstest(coleman_liau_indexs, 'norm', (mean2, std2))
        if rel2[1]> 0.05:
            print('yes--coleman_liau_indexs---norm')
        else:
            print('no---coleman_liau_indexs---not_norm')        
        rel3= stats.kstest(automated_readability_indexs, 'norm', (mean3, std3))
        if rel3[1]> 0.05:
            print('yes--automated_readability_indexs---norm')
        else:
            print('no---automated_readability_indexs---not_norm')
        rel4= stats.kstest(dale_chall_readability_scores, 'norm', (mean4, std4))
        if rel4[1]> 0.05:
            print('yes--dale_chall_readability_scores---norm')
        else:
            print('no---dale_chall_readability_scores---not_norm')
        rel5= stats.kstest(difficult_wordss, 'norm', (mean5, std5))
        if rel5[1]> 0.05:
            print('yes--difficult_wordss---norm')
        else:
            print('no---difficult_wordss---not_norm')
        rel6= stats.kstest(linsear_write_formulas, 'norm', (mean6, std6))
        if rel6[1]> 0.05:
            print('yes--linsear_write_formulas---norm')
        else:
            print('no---linsear_write_formulas---not_norm')
        rel7= stats.kstest(text_standards, 'norm', (mean7, std7))
        if rel7[1]> 0.05:
            print('yes--text_standards---norm')
        else:
            print('no--text_standards----not_norm')
        rel8= stats.kstest(gunning_fogs, 'norm', (mean8, std8))
        if rel8[1]> 0.05:
            print('yes---gunning_fogs--norm')
        else:
            print('no---gunning_fogs---not_norm')

def kstest_complete(a):
    with open(f'after_predict_{a}_read.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        flesch_reading_eases=[]
        flesch_kincaid_grades=[]
        coleman_liau_indexs=[]
        automated_readability_indexs=[]
        dale_chall_readability_scores=[]
        difficult_wordss=[]
        linsear_write_formulas=[]
        gunning_fogs=[]
        text_standards=[]
        for dat in data:
            nee=dat.split(',')
            flesch_reading_eases.append(float(nee[0]))
            flesch_kincaid_grades.append(float(nee[1]))
            coleman_liau_indexs.append(float(nee[2]))
            automated_readability_indexs.append(float(nee[3]))
            dale_chall_readability_scores.append(float(nee[4]))
            difficult_wordss.append(float(nee[5]))
            linsear_write_formulas.append(float(nee[6]))
            gunning_fogs.append(float(nee[7])) 
            text_standards.append(float(nee[8]))
        mean0= np.mean(flesch_reading_eases)
        mean1= np.mean(flesch_kincaid_grades)
        mean2= np.mean(coleman_liau_indexs)
        mean3= np.mean(automated_readability_indexs)        
        mean4= np.mean(dale_chall_readability_scores)
        mean5= np.mean(difficult_wordss)        
        mean6= np.mean(linsear_write_formulas)
        mean7= np.mean(gunning_fogs)
        mean8= np.mean(text_standards)
        
        std0= np.std(flesch_reading_eases)
        std1= np.std(flesch_kincaid_grades)
        std2= np.std(coleman_liau_indexs)
        std3= np.std(automated_readability_indexs)        
        std4= np.std(dale_chall_readability_scores)
        std5= np.std(difficult_wordss)        
        std6= np.std(linsear_write_formulas)
        std7= np.std(gunning_fogs)
        std8= np.std(text_standards)

        rel0= stats.kstest(flesch_reading_eases, 'norm', (mean0, std0))
        if rel0[1]> 0.05:
            print('yes---flesch_reading_eases---norm')
        else:
            print('no---flesch_reading_eases---not_norm')
        rel1= stats.kstest(flesch_kincaid_grades, 'norm', (mean1, std1))
        if rel1[1]> 0.05:
            print('yes---flesch_kincaid_grades---norm')
        else:
            print('no---flesch_kincaid_grades---not_norm')
        rel2= stats.kstest(coleman_liau_indexs, 'norm', (mean2, std2))
        if rel2[1]> 0.05:
            print('yes--coleman_liau_indexs---norm')
        else:
            print('no---coleman_liau_indexs---not_norm')        
        rel3= stats.kstest(automated_readability_indexs, 'norm', (mean3, std3))
        if rel3[1]> 0.05:
            print('yes--automated_readability_indexs---norm')
        else:
            print('no---automated_readability_indexs---not_norm')
        rel4= stats.kstest(dale_chall_readability_scores, 'norm', (mean4, std4))
        if rel4[1]> 0.05:
            print('yes--dale_chall_readability_scores---norm')
        else:
            print('no---dale_chall_readability_scores---not_norm')
        rel5= stats.kstest(difficult_wordss, 'norm', (mean5, std5))
        if rel5[1]> 0.05:
            print('yes--difficult_wordss---norm')
        else:
            print('no---difficult_wordss---not_norm')
        rel6= stats.kstest(linsear_write_formulas, 'norm', (mean6, std6))
        if rel6[1]> 0.05:
            print('yes--linsear_write_formulas---norm')
        else:
            print('no---linsear_write_formulas---not_norm')
        rel7= stats.kstest(gunning_fogs, 'norm', (mean7, std7))
        if rel7[1]> 0.05:
            print('yes--gunning_fogs---norm')
        else:
            print('no--gunning_fogs----not_norm')
        rel8= stats.kstest(text_standards, 'norm', (mean8, std8))
        if rel8[1]> 0.05:
            print('yes---text_standards--norm')
        else:
            print('no---text_standards---not_norm')


if __name__=='__main__':
    # name=['sub','obj']
    name=['pre']
    for a in name:
        # #检验是否是正态分布
        # kstest_ellipsis(a)
        # kstest_complete(a)
        
        
        #检验p,delta,cllif
        with open(f'before_predict_{a}_read.csv','r',encoding='utf-8')as f:
            rel0s=[]
            rel1s=[]
            rel2s=[]
            rel3s=[]
            rel4s=[]
            rel5s=[]
            rel6s=[]
            rel7s=[]
            rel8s=[]
            ellipsis=f.readlines()
            for dat in ellipsis:
                nee=dat.split(',')
                rel0=float(nee[0])
                rel0s.append(rel0)
                rel1=float(nee[1])
                rel1s.append(rel1)
                rel2=float(nee[2])
                rel2s.append(rel2)
                rel3=float(nee[3])
                rel3s.append(rel3)
                rel4=float(nee[4])
                rel4s.append(rel4)
                rel5=float(nee[5])
                rel5s.append(rel5)
                rel6=float(nee[6])
                rel6s.append(rel6)
                rel7=float(nee[7])
                rel7s.append(rel7)
                rel8=float(nee[8])
                rel8s.append(rel8)
    
        with open(f'after_predict_{a}_read.csv','r',encoding='utf-8')as ff:
            wrel0s=[]
            wrel1s=[]
            wrel2s=[]
            wrel3s=[]
            wrel4s=[]
            wrel5s=[]
            wrel6s=[]
            wrel7s=[]
            wrel8s=[]
            complete=ff.readlines()
            for dat in complete:
                nee=dat.split(',')
                rel0=float(nee[0])
                wrel0s.append(rel0)
                rel1=float(nee[1])
                wrel1s.append(rel1)
                rel2=float(nee[2])
                wrel2s.append(rel2)
                rel3=float(nee[3])
                wrel3s.append(rel3)
                rel4=float(nee[4])
                wrel4s.append(rel4)
                rel5=float(nee[5])
                wrel5s.append(rel5)
                rel6=float(nee[6])
                wrel6s.append(rel6)
                rel7=float(nee[7])
                wrel7s.append(rel7)
                rel8=float(nee[8])
                wrel8s.append(rel8)
        delta0, matrix0 = cliffsDelta(rel0s,wrel0s)
        p0=stats.mannwhitneyu(rel0s,wrel0s,alternative='two-sided')
        p0=p0[1]
        delta1, matrix1 = cliffsDelta(rel1s,wrel1s)
        p1=stats.mannwhitneyu(rel1s,wrel1s,alternative='two-sided')
        p1=p1[1]
        delta2, matrix2 = cliffsDelta(rel2s,wrel2s)
        p2=stats.mannwhitneyu(rel2s,wrel2s,alternative='two-sided')
        p2=p2[1]
        delta3, matrix3 = cliffsDelta(rel3s,wrel3s)
        p3=stats.mannwhitneyu(rel3s,wrel3s,alternative='two-sided')
        p3=p3[1]
        delta4, matrix4 = cliffsDelta(rel4s,wrel4s)
        p4=stats.mannwhitneyu(rel4s,wrel4s,alternative='two-sided')
        p4=p4[1]
        delta5, matrix5 = cliffsDelta(rel5s,wrel5s)
        p5=stats.mannwhitneyu(rel5s,wrel5s,alternative='two-sided')
        p5=p5[1]
        delta6, matrix6 = cliffsDelta(rel6s,wrel6s)
        p6=stats.mannwhitneyu(rel6s,wrel6s,alternative='two-sided')
        p6=p6[1]
        delta7, matrix7 = cliffsDelta(rel7s,wrel7s)
        p7=stats.mannwhitneyu(rel7s,wrel7s,alternative='two-sided')
        p7=p7[1]
        delta8, matrix8 = cliffsDelta(rel8s,wrel8s)
        p8=stats.mannwhitneyu(rel8s,wrel8s,alternative='two-sided')
        p8=p8[1]
        print(f'{a}----flesch_reading_eases---P_value---'+ str(p0))
        # p1=round(p1,)
        # delta1, matrix1 = cliffDelta(wanzhengif,buwanzhengif)
        print(delta0,matrix0)
        print(f'{a}----flesch_kincaid_grades---P_value---'+ str(p1))

        # print(p1)
        print(delta1,matrix1)
        print(f'{a}----coleman_liau_indexs---P_value---'+ str(p2))

        # print(p2)
        print(delta2,matrix2)
        print(f'{a}----automated_readability_indexs---P_value---'+ str(p3))

        # print(p3)
        print(delta3,matrix3)
        print(f'{a}----dale_chall_readability_scores---P_value---'+ str(p4))

        # print(p4)
        print(delta4,matrix4)
        print(f'{a}----difficult_wordss---P_value---'+ str(p5))

        # print(p5)
        print(delta5,matrix5)
        print(f'{a}----linsear_write_formulas---P_value---'+ str(p6))

        # print(p6)
        print(delta6,matrix6)
        print(f'{a}----gunning_fogs---P_value---'+ str(p7))

        # print(p7)
        print(delta7,matrix7)
        print(f'{a}----text_standards---P_value---'+ str(p8))

        # print(p8)
        print(delta8,matrix8)    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        