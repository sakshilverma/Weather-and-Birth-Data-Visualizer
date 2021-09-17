import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'tempYearly.csv')

#scatter plot between year and temperature
sns.set(rc={'figure.figsize':(12,6)})
sns.scatterplot(x='Year', y='Temperature', data=df)
plt.show()

#scatter plot between rainfall and temperature
sns.set(rc={'figure.figsize':(12,6)})
sns.scatterplot(x='Rainfall', y='Temperature', data=df)
plt.show()


#regression plot between year and temperature
sns.set(rc={'figure.figsize':(12,6)})
sns.regplot(x='Year', y='Temperature', data=df)
plt.show()

#regression plot between rainfall and temperature
sns.set(rc={'figure.figsize':(12,6)})
sns.regplot(x='Rainfall', y='Temperature', data=df)
plt.show()
