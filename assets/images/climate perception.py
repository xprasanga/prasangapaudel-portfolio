import matplotlib.pyplot as plt
import seaborn as sns
import textwrap


# ============================================================
# CLIMATE CHANGE PERCEPTION FREQUENCY DATA
# ============================================================

questions = {

    "Do you think the world's climate is changing?":
    {
        "labels": [
            "Definitely\nchanging",
            "Probably\nchanging",
            "Not sure/\nNo opinion",
            "Probably\nnot\nchanging",
            "Definitely\nnot\nchanging"
        ],

        "freq": [
            497,
            283,
            48,
            45,
            171
        ]
    },


    "How important is the issue of global warming to you personally?":
    {
        "labels": [
            "Extremely\nimportant",
            "Very\nimportant",
            "Somewhat\nimportant",
            "Not too\nimportant",
            "Not at all\nimportant"
        ],

        "freq": [
            295,
            281,
            268,
            125,
            75
        ]
    },


    "How worried are you about global warming?":
    {
        "labels": [
            "Very\nworried",
            "Somewhat\nworried",
            "Not very\nworried",
            "Not at all\nworried"
        ],

        "freq": [
            304,
            430,
            200,
            110
        ]
    },


    "How much do you think global warming will harm you personally?":
    {
        "labels": [
            "A great\ndeal",
            "A moderate\namount",
            "Only a\nlittle",
            "Not at\nall",
            "Don't\nknow"
        ],

        "freq": [
            217,
            360,
            261,
            143,
            63
        ]
    },


    "How much do you think global warming will harm future generations?":
    {
        "labels": [
            "A great\ndeal",
            "A moderate\namount",
            "Only a\nlittle",
            "Not at\nall",
            "Don't\nknow"
        ],

        "freq": [
            456,
            280,
            160,
            87,
            61
        ]
    },


    "Do you favor increasing taxes on fossil fuels to reduce climate change?":
    {
        "labels": [
            "Strongly\nfavor",
            "Somewhat\nfavor",
            "Neither\nfavor\nnor Against",
            "Somewhat\nagainst",
            "strongly\ndisagree"
        ],

        "freq": [
            211,
            287,
            261,
            139,
            146
        ]
    }
}


# ============================================================
# ELSEVIER SMALL-COLUMN SETTINGS
# ============================================================

# Elsevier small/single-column width:
#
# 90 mm = 3.5433 inches

FIG_WIDTH = 90 / 25.4


# Six panels:
#
# A B
# C D
# E F

FIG_HEIGHT = 6.6


# TIFF resolution

DPI = 1200


# ============================================================
# PUBLICATION STYLE
# ============================================================

sns.set_theme(
    style="whitegrid"
)


plt.rcParams.update({

    # --------------------------------------------------------
    # Font
    # --------------------------------------------------------

    "font.family": "Times New Roman",

    "font.size": 6.5,

    "axes.titlesize": 7,
    "axes.titleweight": "bold",

    "axes.labelsize": 6.5,

    # Small enough for 90-mm column
    "xtick.labelsize": 5,
    "ytick.labelsize": 5.5,

    # --------------------------------------------------------
    # Axes
    # --------------------------------------------------------

    "axes.linewidth": 0.7,

    # --------------------------------------------------------
    # Ticks
    # --------------------------------------------------------

    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,

    # --------------------------------------------------------
    # Background
    # --------------------------------------------------------

    "figure.facecolor": "white",
    "axes.facecolor": "white"
})


# ============================================================
# COLORS
# ============================================================

colors = sns.color_palette(
    "Set2",
    6
)


# ============================================================
# CREATE FIGURE
# ============================================================

fig, axes = plt.subplots(

    3,
    2,

    figsize=(
        FIG_WIDTH,
        FIG_HEIGHT
    ),

    sharey=True
)


axes = axes.flatten()


# ============================================================
# PANEL LETTERS
# ============================================================

letters = [
    "(A)",
    "(B)",
    "(C)",
    "(D)",
    "(E)",
    "(F)"
]


# ============================================================
# CREATE EACH PANEL
# ============================================================

for i, (question, data) in enumerate(
    questions.items()
):

    ax = axes[i]


    # ========================================================
    # BAR POSITIONS
    # ========================================================

    x = list(
        range(
            len(data["freq"])
        )
    )


    # ========================================================
    # BAR CHART
    # ========================================================

    bars = ax.bar(

        x,

        data["freq"],

        color=colors[i],

        edgecolor="black",

        linewidth=0.5,

        width=0.70,

        zorder=3
    )


    # ========================================================
    # X AXIS
    # ========================================================

    ax.set_xticks(
        x
    )


    # --------------------------------------------------------
    # KEEP ALL LABELS HORIZONTAL
    # --------------------------------------------------------

    ax.set_xticklabels(

        data["labels"],

        rotation=0,

        ha="center",

        va="top",

        fontsize=5,

        linespacing=0.85
    )


    # Give the bars a little room at the edges

    ax.set_xlim(
        -0.55,
        len(x) - 0.45
    )


    # ========================================================
    # QUESTION TITLE
    # ========================================================

    # Narrow wrapping keeps long questions inside each panel.

    title = textwrap.fill(
        question,
        width=28
    )


    ax.set_title(

        f"{letters[i]} {title}",

        fontsize=7,

        fontweight="bold",

        pad=4,

        loc="center"
    )


    # ========================================================
    # Y AXIS LABEL
    # ========================================================

    ax.set_ylabel(

        "Frequency",

        fontsize=6.5,

        fontweight="normal",

        labelpad=2
    )


    # ========================================================
    # REMOVE NUMERICAL Y-AXIS LABELS
    # ========================================================

    # The actual frequencies are already printed above
    # the bars, so numbers such as 100, 200, 300 are removed.

    ax.tick_params(

        axis="y",

        which="both",

        labelleft=False,

        length=0
    )


    # ========================================================
    # Y AXIS RANGE
    # ========================================================

    ax.set_ylim(
        0,
        550
    )


    # ========================================================
    # KEEP GRIDLINES WITHOUT NUMBERS
    # ========================================================

    ax.set_yticks(

        [
            0,
            100,
            200,
            300,
            400,
            500
        ]
    )


    # ========================================================
    # FREQUENCY VALUES ABOVE BARS
    # ========================================================

    for bar in bars:

        height = bar.get_height()


        ax.text(

            bar.get_x()
            + bar.get_width() / 2,

            height + 8,

            str(int(height)),

            ha="center",

            va="bottom",

            fontsize=5.5,

            color="black",

            bbox=dict(

                facecolor="white",

                edgecolor="none",

                boxstyle="round,pad=0.08"
            ),

            zorder=5
        )


    # ========================================================
    # GRID
    # ========================================================

    ax.grid(

        axis="y",

        color="0.85",

        linewidth=0.4,

        alpha=0.8,

        zorder=0
    )


    ax.grid(

        axis="x",

        visible=False
    )


    # ========================================================
    # SPINES
    # ========================================================

    for spine in ax.spines.values():

        spine.set_linewidth(0.7)

        spine.set_color("black")


    # ========================================================
    # X-AXIS TICKS
    # ========================================================

    ax.tick_params(

        axis="x",

        which="major",

        width=0.6,

        length=2.5,

        pad=2
    )


# ============================================================
# LAYOUT
# ============================================================

# The plotting area is deliberately moved LEFT.
#
# This makes better use of the available 90-mm width.
#
# Horizontal x-axis labels are retained.
#
# The vertical gap between rows is kept relatively small.

plt.subplots_adjust(

    # MOVE EVERYTHING TO THE LEFT
    left=0.045,

    # Use almost all available width
    right=0.985,

    # Enough room for the bottom x-axis labels
    bottom=0.038,

    # Enough room for the first-row question titles
    top=0.94,

    # Small gap between the two columns
    wspace=0.19,

    # Reduced vertical gap between rows
    hspace=0.35
)


# ============================================================
# OUTPUT LOCATION
# ============================================================

output_base = (

    "/Users/freebird/Library/CloudStorage/"
    "OneDrive-TexasTechUniversity/VS Code/python/"
    "ClimateChange_Perceptions_90mm"
)


# ============================================================
# SAVE VECTOR PDF
# ============================================================

pdf_path = (

    output_base +
    ".pdf"
)


fig.savefig(

    pdf_path,

    format="pdf",

    # IMPORTANT:
    # No cropping.
    #
    # Keeps physical width exactly 90 mm.

    bbox_inches=None,

    pad_inches=0,

    facecolor="white",

    edgecolor="white"
)


# ============================================================
# SAVE 600-DPI TIFF
# ============================================================

tiff_path = (

    output_base +
    "_1200dpi.tiff"
)


fig.savefig(

    tiff_path,

    format="tiff",

    dpi=DPI,

    # Preserve exact 90-mm canvas.

    bbox_inches=None,

    pad_inches=0,

    facecolor="white",

    edgecolor="white"
)


# ============================================================
# DISPLAY
# ============================================================

plt.show()


# ============================================================
# PRINT OUTPUT INFORMATION
# ============================================================

print()
print("--------------------------------------------")
print("Climate perception figure created")
print("--------------------------------------------")
print()

print("PDF:")
print(pdf_path)

print()

print("TIFF:")
print(tiff_path)

print()

print("--------------------------------------------")

print(
    f"Figure width: "
    f"{FIG_WIDTH:.4f} inches"
)

print(
    "Figure width: 90.0 mm"
)

print()

print(
    f"Figure height: "
    f"{FIG_HEIGHT:.2f} inches"
)

print(
    f"Figure height: "
    f"{FIG_HEIGHT * 25.4:.1f} mm"
)

print()

print(
    f"TIFF resolution: "
    f"{DPI} DPI"
)

print(
    "PDF: Vector format"
)

print("--------------------------------------------")
