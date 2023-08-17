def analyze_scores(sansu,kokugo,rika,syakai,eigo=None,*others):
    ls=[sansu,kokugo,rika,syakai]
    if eigo != None:
        ls.append(eigo)
    ls=ls+list(others)
    max_score=max(ls)
    min_score=min(ls)
    avg_score=sum(ls)/len(ls)

    return [max_score,min_score,avg_score]
x,n,g=analyze_scores(1,2,3,4,5,6,7)
print(x,n,g)

