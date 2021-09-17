import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create the dataframes using the json file..
df=pd.read_json(r'./rain.json')

#plot temperature and month
plt.figure(figsize=(17,5))
plt.plot(df['Month'], df['Temperature'], label='Temperature')
plt.show()

#plot rainfall and month
plt.figure(figsize=(17,5))
plt.plot(df['Month'], df['Rainfall'], label='Rainfall')
plt.show()

#plot rainfall and temperature together
plt.figure(figsize=(17,5))
plt.plot(df['Month'], df['Rainfall'], label='Rainfall')
plt.plot(df['Month'], df['Temperature'], label='Temperature')
plt.legend()
plt.show()