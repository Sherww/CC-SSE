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
def fail_before():
    with open('all_comment_fail.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nees=[]
        for dat in data:
            nee=float(dat.split(',')[5].replace('\n',''))
            nees.append(nee)

        mean0= np.mean(nees)
        std0= np.std(nees)

        rel0= stats.kstest(nees, 'norm', (mean0, std0))
        if rel0[1]> 0.05:
            print('yes---flesch_reading_eases---norm')
        else:
            print('no---flesch_reading_eases---not_norm')
def fail_after():
    with open('all_comment_fail.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nees=[]
        for dat in data:
            nee=float(dat.split(',')[6].replace('\n',''))
            nees.append(nee)

        mean0= np.mean(nees)
        std0= np.std(nees)

        rel0= stats.kstest(nees, 'norm', (mean0, std0))
        if rel0[1]> 0.05:
            print('yes---flesch_reading_eases---norm')
        else:
            print('no---flesch_reading_eases---not_norm')
def succ_before():
    with open('all_comment_success.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nees=[]
        for dat in data:
            nee=float(dat.split(',')[5].replace('\n',''))
            nees.append(nee)

        mean0= np.mean(nees)
        std0= np.std(nees)

        rel0= stats.kstest(nees, 'norm', (mean0, std0))
        if rel0[1]> 0.05:
            print('yes---flesch_reading_eases---norm')
        else:
            print('no---flesch_reading_eases---not_norm')
def succ_after():
    with open('all_comment_success.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nees=[]
        for dat in data:
            nee=float(dat.split(',')[6].replace('\n',''))
            nees.append(nee)

        mean0= np.mean(nees)
        std0= np.std(nees)

        rel0= stats.kstest(nees, 'norm', (mean0, std0))
        if rel0[1]> 0.05:
            print('yes---flesch_reading_eases---norm')
        else:
            print('no---flesch_reading_eases---not_norm')
def all_delta():
    
        #检验p,delta,cllif
        # with open('before_after_result_new.csv','r',encoding='utf-8')as f:
        # with open('sub_all.csv','r',encoding='utf-8')as f:
        # with open('pre_all.csv','r',encoding='utf-8')as f:
        with open('obj_all.csv','r',encoding='utf-8')as f:

            befores=[]
            afters=[]
            data=f.readlines()
            for dat in data:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_success---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_success--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_success--'+str(quatile_complete))

def succ_delta():
    
        #检验p,delta,cllif
        # with open('all_comment_success.csv','r',encoding='utf-8')as f:
        # with open('sub_success.csv','r',encoding='utf-8')as f:
        # with open('pre_success.csv','r',encoding='utf-8')as f:
        with open('obj_success.csv','r',encoding='utf-8')as f:

            befores=[]
            afters=[]
            data=f.readlines()
            for dat in data:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_success---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_success--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_success--'+str(quatile_complete))

def fail_delta():
        # with open('all_comment_fail.csv','r',encoding='utf-8')as f:
        # with open('sub_fail.csv','r',encoding='utf-8')as f:
        # with open('pre_fail.csv','r',encoding='utf-8')as f:
        with open('obj_fail.csv','r',encoding='utf-8')as f:

            befores=[]
            afters=[]
            data=f.readlines()
            for dat in data:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
def java_experi():
        # with open('all_comment_fail.csv','r',encoding='utf-8')as f:
        # with open('sub_fail.csv','r',encoding='utf-8')as f:
        with open('java_experience.csv','r',encoding='utf-8')as f:

            befores=[]
            afters=[]
            data=f.readlines()
            for dat in data[0:162]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        with open('java_experience.csv','r',encoding='utf-8')as ff:

            befores=[]
            afters=[]
            data=ff.readlines()
            for dat in data[162:252]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        print('----------------------------------------------')
        with open('java_experience.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[252:316]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        with open('java_experience.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[316:348]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        print('----------------------------------------------')

        with open('java_experience.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[348:372]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        with open('java_experience.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[372:]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
def dev_experi():
        # with open('all_comment_fail.csv','r',encoding='utf-8')as f:
        # with open('sub_fail.csv','r',encoding='utf-8')as f:
        with open('develop_experience.csv','r',encoding='utf-8')as f:

            befores=[]
            afters=[]
            data=f.readlines()
            for dat in data[0:101]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        with open('develop_experience.csv','r',encoding='utf-8')as ff:

            befores=[]
            afters=[]
            data=ff.readlines()
            for dat in data[101:156]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        print('----------------------------------------------')
        with open('develop_experience.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[156:249]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        with open('develop_experience.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[249:300]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        print('----------------------------------------------')

        with open('develop_experience.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[300:356]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        with open('develop_experience.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[356:]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
def work_experi():
        with open('work_or_not.csv','r',encoding='utf-8')as ff:

            befores=[]
            afters=[]
            data=ff.readlines()
            for dat in data[0:84]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        # with open('all_comment_fail.csv','r',encoding='utf-8')as f:
        # with open('sub_fail.csv','r',encoding='utf-8')as f:
        with open('work_or_not.csv','r',encoding='utf-8')as f:

            befores=[]
            afters=[]
            data=f.readlines()
            for dat in data[0:53]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        with open('work_or_not.csv','r',encoding='utf-8')as ff:

            befores=[]
            afters=[]
            data=ff.readlines()
            for dat in data[53:84]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        

        
        print('----------------------------------------------')
        with open('work_or_not.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[84:]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
               
        
        with open('work_or_not.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[84:281]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        
        with open('work_or_not.csv','r',encoding='utf-8')as fff:

            befores=[]
            afters=[]
            data=fff.readlines()
            for dat in data[281:]:
                before=float(dat.split(',')[5].replace('\n',''))
                after=float(dat.split(',')[6].replace('\n',''))
                befores.append(before)
                afters.append(after)
        delta0, matrix0 = cliffsDelta(befores,afters)
        p0=stats.mannwhitneyu(befores,afters,alternative='two-sided')
        p0=p0[1]

        print('-----P_value--all_fail---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(befores,(0, 25, 50, 75, 100))
        print('---quatile-all_fail--' +str(quatile_ellipsis))
        quatile_complete = np.percentile(afters,(0, 25, 50, 75, 100))
        print('----quatile-all_fail--'+str(quatile_complete))
        

        
        print('----------------------------------------------')


if __name__=='__main__':

        # #检验是否是正态分布
        # fail_before()
        # fail_after()
        # succ_before()
        # succ_after()

        # 检验p,delta,cllif
        all_delta()
        succ_delta()
        fail_delta()
        
        # java_experi()
        
        # dev_experi()
        
        # work_experi()
        
        
        
        
        
        
        
        
        
        
        
        
        