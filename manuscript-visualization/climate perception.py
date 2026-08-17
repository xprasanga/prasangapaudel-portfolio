import matplotlib.pyplot as plt
import seaborn as sns
import textwrap
questions={
"Do you think the world's climate is changing?":{"labels":["Definitely\nchanging","Probably\nchanging","Not sure/\nNo opinion","Probably\nnot\nchanging","Definitely\nnot\nchanging"],"freq":[497,283,48,45,171]},
"How important is the issue of global warming to you personally?":{"labels":["Extremely\nimportant","Very\nimportant","Somewhat\nimportant","Not too\nimportant","Not at all\nimportant"],"freq":[295,281,268,125,75]},
"How worried are you about global warming?":{"labels":["Very\nworried","Somewhat\nworried","Not very\nworried","Not at all\nworried"],"freq":[304,430,200,110]},
"How much do you think global warming will harm you personally?":{"labels":["A great\ndeal","A moderate\namount","Only a\nlittle","Not at\nall","Don't\nknow"],"freq":[217,360,261,143,63]},
"How much do you think global warming will harm future generations?":{"labels":["A great\ndeal","A moderate\namount","Only a\nlittle","Not at\nall","Don't\nknow"],"freq":[456,280,160,87,61]},
"Do you favor increasing taxes on fossil fuels to reduce climate change?":{"labels":["Strongly\nfavor","Somewhat\nfavor","Neither\nfavor\nnor Against","Somewhat\nagainst","strongly\ndisagree"],"freq":[211,287,261,139,146]}}
sns.set_theme(style="whitegrid"); plt.rcParams.update({"font.family":"Times New Roman","font.size":6.5,"axes.titlesize":7,"axes.titleweight":"bold","xtick.labelsize":5,"ytick.labelsize":5.5,"axes.linewidth":.7,"figure.facecolor":"white","axes.facecolor":"white"})
fig,axes=plt.subplots(3,2,figsize=(90/25.4,6.6),sharey=True); axes=axes.flatten(); colors=sns.color_palette("Set2",6)
for i,(q,d) in enumerate(questions.items()):
    ax=axes[i]; x=range(len(d["freq"])); bars=ax.bar(x,d["freq"],color=colors[i],edgecolor="black",linewidth=.5,width=.7,zorder=3); ax.set_xticks(list(x)); ax.set_xticklabels(d["labels"],rotation=0,ha="center",va="top",fontsize=5,linespacing=.85); ax.set_xlim(-.55,len(d["freq"])-.45); ax.set_title(f"({chr(65+i)}) {textwrap.fill(q,width=28)}",fontsize=7,fontweight="bold",pad=4); ax.set_ylabel("Frequency",fontsize=6.5); ax.tick_params(axis="y",labelleft=False,length=0); ax.set_ylim(0,550); ax.set_yticks([0,100,200,300,400,500]); ax.grid(axis="y",color="0.85",linewidth=.4); ax.grid(axis="x",visible=False)
    for b in bars: ax.text(b.get_x()+b.get_width()/2,b.get_height()+8,str(int(b.get_height())),ha="center",va="bottom",fontsize=5.5,bbox=dict(facecolor="white",edgecolor="none",boxstyle="round,pad=.08"))
plt.subplots_adjust(left=.045,right=.985,bottom=.038,top=.94,wspace=.19,hspace=.35); plt.show()
