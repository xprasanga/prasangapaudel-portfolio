import matplotlib.pyplot as plt
import seaborn as sns
risk_questions={"Risk (General)":{"freq":[58,94,95,114,157,251,108,76,42,49]},"Health Risk":{"freq":[140,140,109,108,130,180,88,61,35,53]},"Family Risk":{"freq":[250,175,98,86,88,123,57,58,40,69]},"Financial Risk":{"freq":[118,144,136,108,111,176,76,70,49,56]},"Driving Risk":{"freq":[187,152,110,89,102,180,80,59,41,44]},"Sports Risk":{"freq":[163,98,87,101,131,190,84,77,53,60]},"Job Risk":{"freq":[150,100,81,105,125,180,87,93,40,83]}}
sns.set_theme(style="whitegrid"); plt.rcParams.update({"font.family":"Times New Roman","font.size":6.5,"axes.titlesize":7,"axes.titleweight":"bold","axes.labelsize":6.5,"xtick.labelsize":6,"ytick.labelsize":6,"axes.linewidth":.7,"figure.facecolor":"white","axes.facecolor":"white"})
colors=sns.color_palette("Set2",len(risk_questions)); fig,axes=plt.subplots(4,2,figsize=(90/25.4,7.8),sharey=True); axes=axes.flatten()
for i,(title,d) in enumerate(risk_questions.items()):
    ax=axes[i]; scales=list(range(1,11)); bars=ax.bar(scales,d["freq"],color=colors[i],edgecolor="black",linewidth=.5,width=.72,zorder=3); ax.set_xticks(scales); ax.set_xticklabels([str(x) for x in scales],fontsize=6); ax.set_xlim(.4,10.6); ax.set_xlabel(f"({chr(65+i)}) {title}",fontsize=6.5,fontweight="bold",labelpad=3); ax.set_ylabel("Frequency",fontsize=6.5); ax.set_ylim(0,280); ax.set_yticks([0,50,100,150,200,250]); ax.grid(axis="y",color="0.85",linewidth=.4); ax.grid(axis="x",visible=False)
    for b in bars: ax.text(b.get_x()+b.get_width()/2,b.get_height()+3,str(int(b.get_height())),ha="center",va="bottom",fontsize=5.5,bbox=dict(facecolor="white",edgecolor="none",boxstyle="round,pad=.08"))
fig.delaxes(axes[7]); plt.subplots_adjust(left=.12,right=.95,bottom=.06,top=.985,wspace=.30,hspace=.70); plt.show()
