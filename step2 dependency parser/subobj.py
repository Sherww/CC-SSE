# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 11:45:43 2019

@author: njdx
"""
import time
from tqdm import trange,tqdm

from nltk.parse.stanford import StanfordDependencyParser
def dependencyparser():
    #we load Stanford parser
    eng_parser = StanfordDependencyParser(r"D:\\remote_download\\sher\\parser\\stanford-parser-full-2018-10-17\\stanford-parser-full-2018-10-17\\stanford-parser.jar",r"D:\\remote_download\\sher\\parser\\stanford-parser-full-2018-10-17\\stanford-parser-full-2018-10-17\\stanford-parser-3.9.2-models.jar",r"D:\\remote_download\\sher\\parser\\stanford-english-corenlp-2018-10-05-models\\edu\\stanford\\nlp\\models\\lexparser\\englishPCFG.ser.gz")
    with open ('comment_code.txt','r',encoding='utf-8')as f:

        comments = f.readlines()
        # j=400000
        j=0
        completes=[]
        completepasss=[]
        ellipsis1s=[]
        ellipsis1passs=[]
        ellipsis2s=[]

        # to get parser result
        for i in trange(len(comments[0:100000])):

            ne=comments[j].split('\",\"')
            nee=ne[0]
            nees=nee.replace("\"",'').split()
            if len(nees)>=200:
                nee_final=nees[0:200]
            else:
                nee_final=nees
            res = list(eng_parser.parse(nee_final))
            nsub=[]
            dobj=[]
            nsubpass=[]
            onlydobj=[]
            # nt=[]
            dobjpass=[]
            for row in res[0].triples():
#                print(row)
                if row[1] =='nsubj':
                    nsub.append( row[2]+row[0])
                        
                if row[1] =='dobj' and len(nsub) != 0 :
                    dobj.append(row[0]+row[2])
                if row[1] =='dobj' and len(nsub) == 0 :
                    onlydobj.append(row[0]+row[2])
                else:
                    pass
            for row in res[0].triples():                      
                if row[1] =='nsubjpass':
                        nsubpass.append(row[2]+row[0])
                if row[1] =='dobjpass' and len(nsubpass) != 0 :
                    dobjpass.append(row[0]+row[2])
                else:
                    pass
            if len(nsub) != 0 and len(dobj) != 0:      #to get complete data
                # print(nsub,dobj)    
                for k in range(len(nsub)):
                    for m in range(len(dobj)):
                        if nsub[k][2]==dobj[m][0]:
                            complete=nsub[k][0]+' '+nsub[k][2]+' '+dobj[m][2]+','+str(j)+'\n'
                            completes.append(complete)
                        else:
                            pass
            if len(nsubpass)!= 0 and len( dobjpass) !=0:     #to get complete data   
                for k in range(len(nsubpass)):
                    for m in range(len(dobj)):
                        if nsubpass[k][2]==dobj[m][0]:    
                            completepass=nsubpass[k][0]+' '+nsubpass[k][2]+' '+dobj[k][2]+','+str(j)+'\n'
                            completes.append(completepass)
                        else:
                            pass
            if len(nsub) !=0 and len(dobj) ==0:      #to get ellipsis1 data
                for k in range(len(nsub)):
                    ellipsis1=nsub[k][0]+' '+nsub[k][2]+','+str(j)+'\n'
                    ellipsis1s.append(ellipsis1)
            if len(nsubpass) !=0  and len(dobjpass) ==0:     #to get ellipsis1 data
                for k in range(len(nsubpass)):
                    ellipsis1pass=nsubpass[k][0]+' '+nsubpass[k][2]+','+str(j)+'\n'
                    ellipsis1s.append(ellipsis1pass)
            if len(onlydobj) !=0:      # to get ellipsis2 data
                for k in range(len(onlydobj)):
                    ellipsis2=onlydobj[k][0]+' '+onlydobj[k][2]+','+str(j)+'\n'
                    ellipsis2s.append(ellipsis2)
            else:
                    pass
            nsub=[]
            dobj=[]
            nsubpass=[]
            onlydobj=[]
            dobjpass=[]
            j+=1            
            time.sleep(0.01)
        return completes, ellipsis1s, ellipsis2s
                  
def write(completes, ellipsis1s, ellipsis2s):                
        with open('complete_1.csv','w',encoding='utf-8')as f:
            for i in range(len(completes)):
                f.write(completes[i])
        with open('ellipsis1_1.csv','w',encoding='utf-8')as ff:
            for i in range(len(ellipsis1s)):
                ff.write(ellipsis1s[i])                
        with open('ellipsis2_1.csv','w',encoding='utf-8')as fff:
            for i in range(len(ellipsis2s)):
                fff.write(ellipsis2s[i])
            
            
if __name__ == "__main__":
    #Data splitting, otherwise it will be slow
    completes, ellipsis1s, ellipsis2s = dependencyparser()
    write(completes, ellipsis1s, ellipsis2s)
#    links()
