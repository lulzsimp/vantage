import pandas as pd
import plotly.express as px
import sys

df = pd.read_csv("./marks.csv")
# ops = input("\ncheck || analyze || compare? ")
# def_ops = ops.split(" ")
argv = sys.argv
if argv[1] == "check":
    reqd = df.loc[((df["type"]==argv[2]) & (df["year"]==int(argv[3])))]
    print("\n", reqd[["subj","mark"]])
elif argv[1] == "analyze":
    reqd = df.loc[((df["type"]==argv[2]) & (df["year"]==int(argv[3])))]
    print("\n", reqd[["subj", "mark"]],"\n")
    print(f"avg {reqd['mark'].mean()}\nstd {reqd['mark'].std()}\ncgpa {((reqd['mark'].sum()/240)*100)/9.5}\nmin/max {reqd['mark'].min()}/{reqd['mark'].max()}")
    if argv[2] == "ae" or argv[2] == "mt": print(reqd["mark"]*1.25)
    else: print(reqd["mark"]*2.5)