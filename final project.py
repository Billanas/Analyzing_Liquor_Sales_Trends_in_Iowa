import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/home/billys/Documents/workearly/Python/Final-Assignment-main/DATA FINAL ASSIGNMENT.csv")
item = df.groupby('zip_code').bottles_sold.max()

print(item)


plt.figure(figsize=(12,4),dpi=200)
sns.scatterplot(x=item.index, y=item, data=item, hue='zip_code', size=item.index)

plt.title("bottles sold")
plt.show()