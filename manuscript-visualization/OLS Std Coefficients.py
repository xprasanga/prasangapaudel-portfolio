import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# OLS coefficient visualization for the Energy Policy manuscript.
# The plot uses the reported standardized coefficients and 95% confidence intervals.

data1={"Variable":["Geopolitical","CC Harm","Disaster","Bid/Gas","Age","Male","White","Education","Democrat","Gas Income\nShare","Risk Health","Urban"],"beta":[0.01758,-0.06142,0.06570,-0.01250,-0.08381,0.03746,0.05111,0.08916,0.05642,0.03653,0.07366,0.05079],"lower":[-0.05142,-0.12650,-0.00321,-0.07266,-0.15006,-0.02332,-0.01337,0.02764,-0.00756,-0.02747,0.00766,-0.01178],"upper":[0.08657,0.00367,0.13461,0.04767,-0.01756,0.09824,0.11559,0.15068,0.12039,0.10054,0.13967,0.11336]}
data2={"Variable":["Geopolitical","CC Harm","Disaster","Bid/Gas","Age","Male","White","Education","Democrat","Gas Income\nShare","Risk Health","Urban"],"beta":[0.03170,-0.17898,0.04726,-0.02488,-0.11647,0.03702,0.02137,0.03154,0.10500,0.07643,0.19433,0.04724],"lower":[-0.03262,-0.23965,-0.01698,-0.08096,-0.17823,-0.01964,-0.03874,-0.02581,0.04537,0.01677,0.13281,-0.01109],"upper":[0.09602,-0.11830,0.11150,0.03120,-0.05472,0.09368,0.08148,0.08889,0.16464,0.13609,0.25586,0.10556]}
df1=pd.DataFrame(data1); df1["Model"]="Current Price"
df2=pd.DataFrame(data2); df2["Model"]="Price: $2.50"
df=pd.concat([df1,df2],ignore_index=True)
order=df1.sort_values("beta")["Variable"].tolist(); df["Variable"]=pd.Categorical(df["Variable"],categories=order,ordered=True); df=df.sort_values("Variable")
plt.rcParams.update({"font.family":"Times New Roman","font.size":6.5,"axes.labelsize":6.5,"xtick.labelsize":5.5,"ytick.labelsize":6.2,"legend.fontsize":5.8,"axes.linewidth":0.7,"figure.facecolor":"white","axes.facecolor":"white"})
fig,ax=plt.subplots(figsize=(90/25.4,90/25.4)); y_pos=np.arange(len(order)); offset=0.13
colors={"Current Price":"#1f77b4","Price: $2.50":"#d62728"}
for model,marker in [("Current Price","o"),("Price: $2.50","s")]:
    d=df[df["Model"]==model]
    ax.errorbar(d["beta"],y_pos+(-offset if model=="Current Price" else offset),xerr=[d["beta"]-d["lower"],d["upper"]-d["beta"]],fmt=marker,markersize=2,markeredgewidth=.5,markeredgecolor=colors[model],linewidth=.5,elinewidth=.5,capsize=2,capthick=.5,color=colors[model],label=model,zorder=4)
ax.axvline(0,color="black",linewidth=.5,linestyle="--"); ax.set_yticks(y_pos); ax.set_yticklabels(order,fontsize=6.2); ax.set_ylabel("Control Variables",fontsize=6.5,fontweight="bold",labelpad=5); ax.set_xlabel("Standardized OLS Coefficient",fontsize=6.5,fontweight="bold",labelpad=3); ax.grid(axis="x",color="0.88",linewidth=.15,alpha=.95,zorder=0); ax.grid(axis="y",visible=False); ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False); ax.set_ylim(-.65,len(order)-.35); ax.legend(frameon=False,loc="lower right",fontsize=5.8)
plt.subplots_adjust(left=.20,right=.98,bottom=.10,top=.98)
plt.show()
