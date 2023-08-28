import pandas as pd
import sys
arg = sys.argv
df = pd.read_csv("comp.csv")
req = df[(df["name"] == arg[1]) & (df["type"] == arg[2])]
print(req)
print(f"mark_avg: {req['mark'].mean()}")
print(f"mark_std: {req['mark'].std()}")
def comp_avg_loss(l):
    l_avg = 0
    for i in range(len(l)): l_avg+=40-l[i]
    return l_avg/len(l)
print(f"avg_loss: {comp_avg_loss(req['mark'].values)}")
