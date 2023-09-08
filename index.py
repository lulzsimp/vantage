import pandas as pd
df = pd.read_csv('comp.csv')
def ind_get_rec(typ, name):
  _df = df[df['name'] == name]
  _df = _df[_df['type'] == typ]
  return _df.to_dict('records')

# compute
def comp_avg_loss(l, typ):
  l_avg = 0
  fin = 0
  if typ=="pt1": fin = 40
  else: fin = 80
  for i in range(len(l)): l_avg+=fin-l[i]
  return l_avg/len(l)

# compare
def comp_recs(comp1, comp2, typ):
  df1 = pd.DataFrame.from_dict(ind_get_rec(typ, comp1))["mark"]
  df2 = pd.DataFrame.from_dict(ind_get_rec(typ, comp2))["mark"]
  avl1 = comp_avg_loss(df1, typ)
  avl2 = comp_avg_loss(df2, typ)
  return [dict(max=df1.max(), min=df1.min(), std=df1.std(), avg_loss=avl1, avg=df1.mean()),
          dict(max=df2.max(), min=df2.min(), std=df2.std(), avg_loss=avl2, avg=df2.mean())]
print(comp_recs("joshua", "harish", "pt1"))


