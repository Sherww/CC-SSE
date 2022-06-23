import aspell

def get_abbr_extension():
    s=aspell.Speller('lang','en')
    with open('abbr_nees_deldup.txt','r',encoding='utf-8')as f:
        data=f.readlines()
        nees=[]
        for dat in data:
            dat=dat.replace('\n','')
            nee=s.suggest(dat)
            nees.append(nee)
    with open('abbr_aspell_result.csv','w',encoding='utf-8')as ff:
        for i in range(len(data)):
            ff.write(data[i].replace('\n','')+  ','+ str(nees[i]).replace('[','').replace(']','')+'\n')
if __name__=='__main__':
    # get_abbr_extension()
    get_abbr_extension()