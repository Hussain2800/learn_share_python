
import pandas
from scipy.signal import savgol_filter as Filter
event=pandas.read_csv("C:\\Users\Hussain\Dropbox\PC\Desktop\\2021_Events_Remot\\6_2021-03-07-19-20_1590.csv")

print(event)
print(event.columns)

column1=event["Timestamp"]#.iloc[0:9000]
column2=event["STATION_1:Freq"]#.iloc[0:9000]

print(column1,column2)
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
fig,ax = plt.subplots(1,1, figsize=(12,6))

orig = column2.to_numpy()#filter
x = Filter(orig,500,2)#filter
ax.plot(column1,orig)#filter

ax.plot(column1,x,label='Event')
ax.xaxis.set_major_locator(ticker.MaxNLocator(40))
ax.tick_params('x',labelrotation=90)
ax.set_xlim([min(column1),max(column1)])
ax.yaxis.set_major_locator(ticker.MaxNLocator(10))
ax.tick_params('y',labelrotation=0)
ax.set_ylabel("Frequency (Hz)")
ax.set_xlabel("Timestamp")
ax.set_title("2021 file", weight = 'bold')# set title
plt.tight_layout()
plt.legend()
plt.show()