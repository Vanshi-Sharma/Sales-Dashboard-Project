import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("students.csv")
df["Total"] = df[["Math","Science","English","Computer"]].sum(axis=1)
s=df["Total"]
print("The highest marks is:",np.max(s))
print("The lowest marks is:",np.min(s))
print("The average marks is:",np.average(s))
df["Result"]=np.where(df["Total"] < 285, "Fail", "Pass")
print(df)
fig,axs=plt.subplots(1,2,figsize=(15,5)) 
# bar chart
axs[0].bar(df["Name"],df["Total"],color="red")
axs[0].set_title("Bar Chart")
axs[0].set_xlabel("Name")
axs[0].set_ylabel("Total Marks of each students")
# pie chart
c=[np.max(s),np.min(s),np.average(s)]
labels=["Highest","Lowest","Average"]
axs[1].pie(c, labels=labels, autopct="%1.1f%%", explode=[0.1, 0, 0])
axs[1].set_title("Pie Chart")
plt.savefig("Graph.png")
plt.show()

#print(df.columns)
#print(df["Total"])
#print(df["Total"].dtype)

