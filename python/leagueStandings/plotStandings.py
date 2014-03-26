from pandas import Series, DataFrame
import pandas as pd

df = pd.read_csv('fullIdStandings.csv', index_col='Unnamed: 0.1')

df1 = df.drop(['Unnamed: 0', 'Record 2009', 'Record 2010', 'Record 2011', 'Record 2012', 'Record 2013'], axis=1)

#df1.to_csv('js_IDplot.csv', encoding='utf-8')

df2 = df1.T

#df1.to_csv('standsIdPlot.csv', encoding='utf-8')

fig = plt.figure(figsize=(12, 8))

ax1 = fig.add_subplot(1, 1, 1)

box = ax1.get_position()
ax1.set_position([box.x0 - 0.05, box.y0, box.width * 0.95, box.height])

df2.plot(ax=ax1, marker='o', linewidth=1, label='Default')

ax1.legend(loc='center right', bbox_to_anchor=(1.25, 0.5))

plt.savefig('IDwinPCT.eps')

