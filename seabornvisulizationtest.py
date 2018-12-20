import pandas as pd
import krakenex
import sys
import datetime
import calendar
import time
import getopt
from decimal import Decimal as D
import matplotlib.pyplot as plt
import seaborn as sns

def date_str(nix_time):
	return datetime.datetime.fromtimestamp(nix_time).strftime('%m, %d, %Y %H:%M:%S')

k = krakenex.API()
k.load_key('kraken.key.txt')


OHLC_1 = k.query_public('OHLC', {'pair': 'XXRPZUSD','interval':240})
if 'result' in OHLC_1:
	OHLC1 = (OHLC_1['result']['XXRPZUSD'])
	print ([date_str(OHLC1[-1][0]),float(OHLC1[-1][4])])

timelist = []
for i in OHLC1[-20:]:
	timelist.append([date_str(i[0]),float(i[4])])


sns.set(style='darkgrid',color_codes=True)
#initialize the data frame its row header and column
df  = pd.DataFrame(timelist,columns=['x','y'])

#start appending to the df
print (df)
plt.xticks(rotation=90)
g = sns.lineplot(x='x',y='y',data=df)

#g = sns.regplot('x','y',data=df, fit_reg=False)
#g = g.map(plt.scatter, 'x','y',edgecolor='w')
plt.show()