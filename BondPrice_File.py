import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(round(m * ppy))
    time = np.arange(1, n + 1)
    r = y / ppy
    c = face * couponRate / ppy
    df = (1.0 + r) ** (-time)
    return float(c * df.sum() + face * df[-1])


y = 0.03
face = 2000000
couponRate = 0.04
m = 10

