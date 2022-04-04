# this for impoting the library pandas to read CSV file and some time need to install
import pandas
# this is a function inside the variable to read the file but need to insert the file path

event=pandas.read_csv("C:\\Users\Hussain\Dropbox\PC\Desktop\\2021_Events_Remot\\1_2020-12-05-20-49_5650(1).csv")
# to dispaly the code output
print(event)
# to know the column heading name then we can use it in particular
print(event.columns)
# this function an advance but timely will use two function for two columns print(event[['Timestamp', 'STATION_1:Freq']])
# we use .iloc[0:9000] after column1=event["Timestamp"] and column2=event["STATION_1:Freq"] to determine data limitation and without it the code will excued whole the column data
column1=event["Timestamp"].iloc[0:9000]
column2=event["STATION_1:Freq"].iloc[0:9000]
print(column1,column2)
#this library do the plot stuff
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# this function plot the figure but ned other function to show the plot (plt.show()) where axis=ax , figure=fig
fig,ax = plt.subplots(1,1, figsize=(12,6))
ax.plot(column1,column2)
ax.xaxis.set_major_locator(ticker.MaxNLocator(40))
ax.tick_params('x',labelrotation=90)
ax.yaxis.set_major_locator(ticker.MaxNLocator(10))
ax.tick_params('y',labelrotation=0)
ax.set_ylabel("Frequency (Hz)")
ax.set_xlabel("Timestamp")
plt.tight_layout()
plt.show()
# the column of the time show disorder data so we use other function
