import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data1={"Variable":["Geopolitical","CC Harm","Disaster","Bid/Gas","Age","Male","White","Education","Democrat","Gas Income\nShare","Risk Health","Urban"],"beta":[0.00992,-0.4024,0.1259,-0.0174,-0.1767,0.0435,0.00762,0.0235,0.1193,0.1337,0.2228,0.0956],"se":[0.0485,0.0470,0.0487,0.0459,0.0464,0.0428,0.0455,0.0435,0.0448,0.0497,0.0467,0.0440]}
data2={"Variable":["Geopolitical","CC Harm","Disaster","Bid/Gas","Age","Male","White","Education","Democrat","Gas Income\nShare","Risk Health","Urban"],"beta":[-0.0846,-0.3208,-0.0385,-0.1536,-0.1384,-0.0114,0.00956,0.0105,0.1969,0.0145,0.1492,0.0399],"se":[0.0498,0.0463,0.0501,0.0527,0.0478,0.0438,0.0472,0.0439,0.0473,0.0483,0.0485,0.0459]}
for d,m in [(data1,"Current Price"),(data2,"Price: $2.50")]:
    x=pd.DataFrame(d); x["lower"]=x.beta-1.96*x.se; x["upper"]=x.beta+1.96*x.se; x["Model"]=m
    if m=="Current Price": df1=x
    else: df2=x
df=pd.concat([df1,df2],ignore_index=True); order=df1.sort_values("beta")["Variable"].tolist(); df["Variable"]=pd.Categorical(df.Variable,categories=order,ordered=True); df=df.sort_values("Variable")
plt.rcParams.update({"font.family":"Times New Roman","font.size":6.5,"axes.labelsize":6.5,"xtick.labelsize":5.5,"ytick.labelsize":6.2,"legend.fontsize":5.8,"axes.linewidth":.7,"figure.facecolor":"white","axes.facecolor":"white"})
fig,ax=plt.subplots(figsize=(90/25.4,90/25.4)); y=np.arange(len(order)); off=.13; colors={"Current Price":"#1f77b4","Price: $2.50":"#d62728"}
for model,marker in [("Current Price","o"),("Price: $2.50","s")]:
    d=df[df.Model==model]; ax.errorbar(d.beta,y+(-off if model=="Current Price" else off),xerr=[d.beta-d.lower,d.upper-d.beta],fmt=marker,markersize=2,markeredgewidth=.5,markeredgecolor=colors[model],linewidth=.5,elinewidth=.5,capsize=2,capthick=.5,color=colors[model],label=model,zorder=4)
ax.axvline(0,color="black",linewidth=.5,linestyle="--"); ax.set_yticks(y); ax.set_yticklabels(order,fontsize=6.2); ax.set_ylabel("Control Variables",fontsize=6.5,fontweight="bold"); ax.set_xlabel("Standardized Probit Coefficient",fontsize=6.5,fontweight="bold"); ax.grid(axis="x",color="0.88",linewidth=.15); ax.grid(axis="y",visible=False); ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False); ax.set_ylim(-.65,len(order)-.35); ax.legend(frameon=False,loc="lower right",fontsize=5.8); plt.subplots_adjust(left=.20,right=.98,bottom=.10,top=.98); plt.show()
