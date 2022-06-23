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
def kstest_ellipsis():
    with open('ellipsis_384.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nees=[]
        for dat in data:
            nee=float(dat.split(',')[-1].replace('\n',''))
            nees.append(nee)

        mean0= np.mean(nees)

        std0= np.std(nees)

        rel0= stats.kstest(nees, 'norm', (mean0, std0))
        if rel0[1]> 0.05:
            print('yes---flesch_reading_eases---norm')
        else:
            print('no---flesch_reading_eases---not_norm')

def kstest_complete():
    with open('complete_383.csv','r',encoding='utf-8')as f:
        data=f.readlines()
        nees=[]
        for dat in data:
            nee=float(dat.split(',')[-1].replace('\n',''))
            nees.append(nee)

        mean0= np.mean(nees)
        std0= np.std(nees)

        rel0= stats.kstest(nees, 'norm', (mean0, std0))
        if rel0[1]> 0.05:
            print('yes---flesch_reading_eases---norm')
        else:
            print('no---flesch_reading_eases---not_norm')


if __name__=='__main__':

        #检验是否是正态分布
        kstest_ellipsis()
        kstest_complete()
        
        #检验p,delta,cllif
        with open('ellipsis_384.csv','r',encoding='utf-8')as f:

            nees=[]
            ellipsis=f.readlines()
            for dat in ellipsis:
                nee=float(dat.split(',')[-1].replace('\n',''))
                nees.append(nee)
        
        with open('complete_383.csv','r',encoding='utf-8')as ff:

            coms=[]
            complete=ff.readlines()
            for dat in complete:
                com=float(dat.split(',')[-1].replace('\n',''))
                coms.append(com)

        delta0, matrix0 = cliffsDelta(nees,coms)
        p0=stats.mannwhitneyu(nees,coms,alternative='two-sided')
        p0=p0[1]

        print('-----P_value---'+ str(p0))

        print(delta0,matrix0)
 
        quatile_ellipsis = np.percentile(nees,(0, 25, 50, 75, 100))
        print('---quatile_ellipsis---' +str(quatile_ellipsis))
        quatile_complete = np.percentile(coms,(0, 25, 50, 75, 100))
        print('----quatile_complete---'+str(quatile_complete))


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        