import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    n=int(round(m*ppy))
    time=np.arange(1,n+1)
    r=y/ppy
    c=face*couponRate/ppy
    cf=np.full(n,c,dtype=float)+face*(time==n)
    df=(1+r)**(-time)
    pvcf=cf*df
    price=pvcf.sum()
    t=time/ppy
    return float((t*pvcf).sum()/price)

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
