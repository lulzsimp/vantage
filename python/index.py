import pandas as pd
import plotly.express as px
import sys

pd.set_option("display.precision", 3)
df = pd.read_csv("../marks.csv")
# ops = input("\ncheck || analyze || compare? ")
# def_ops = ops.split(" ")
argv = sys.argv
if argv[1] == "check":
    reqd = df.loc[((df["type"] == argv[2]) & (df["year"] == int(argv[3])))]
    print("\n", reqd[["subj", "mark"]])
elif argv[1] == "analyze":
    reqd = df.loc[((df["type"] == argv[2]) & (df["year"] == int(argv[3])))]
    print("\n", reqd[["subj", "mark"]], "\n")
    print(
        f"avg {reqd['mark'].mean()}\n\nstd {reqd['mark'].std()}\n\ncgpa {((reqd['mark'].sum()/240)*100)/9.5}\n\nmin/max {reqd['mark'].min()}/{reqd['mark'].max()}\n"
    )
    if argv[2] == "pb1" or argv[2] == "pb2" or argv[2] == "ae" or argv[2] == "mt":
        print(reqd["mark"] * 1.25)
    else:
        print(reqd["mark"] * 2.5)
    if argv[2] == "pb1" or argv[2] == "pb2" or argv[2] == "ae" or argv[2] == "mt":
        print(reqd["mark"].sum() * 1.25)
    else:
        print(reqd["mark"].sum() * 2.5)
