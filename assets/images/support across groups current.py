import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# ELSEVIER FIGURE SETTINGS
# ============================================================

# Full-width Elsevier figure
# 190 mm = 7.4803 inches
FIG_WIDTH = 190 / 25.4

# Figure height
FIG_HEIGHT = 5.2

# TIFF resolution
# Elsevier guideline for combination artwork = 500 DPI
# 600 DPI gives additional safety/quality.
DPI = 1200


# ============================================================
# GLOBAL STYLE
# ============================================================

plt.rcParams.update({

    # --------------------------------------------------------
    # Fonts
    # --------------------------------------------------------

    "font.size": 7.5,

    "axes.titlesize": 8.5,
    "axes.labelsize": 7.5,

    "axes.titleweight": "bold",
    "axes.labelweight": "normal",

    "xtick.labelsize": 7,
    "ytick.labelsize": 7,

    # --------------------------------------------------------
    # Axes
    # --------------------------------------------------------

    "axes.linewidth": 0.8,

    # --------------------------------------------------------
    # Tick widths
    # --------------------------------------------------------

    "xtick.major.width": 0.7,
    "ytick.major.width": 0.7,

    # --------------------------------------------------------
    # White background
    # --------------------------------------------------------

    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


# ============================================================
# DATA
# ============================================================


# ------------------------------------------------------------
# AGE
# ------------------------------------------------------------

age = pd.DataFrame({
    "group": [2, 3, 4, 5, 6],
    "mean": [
        0.6258503,
        0.6812227,
        0.6027397,
        0.4864865,
        0.3230088
    ],
    "lcl": [
        0.5467015,
        0.6204120,
        0.5374206,
        0.4202270,
        0.2615764
    ],
    "ucl": [
        0.7049992,
        0.7420335,
        0.6680588,
        0.5527460,
        0.3844413
    ]
})


# ------------------------------------------------------------
# GENDER
# ------------------------------------------------------------

male = pd.DataFrame({
    "group": [0, 1],
    "mean": [
        0.5191956,
        0.5573441
    ],
    "lcl": [
        0.4771941,
        0.5135250
    ],
    "ucl": [
        0.5611972,
        0.6011631
    ]
})


# ------------------------------------------------------------
# EDUCATION
# ------------------------------------------------------------

educ = pd.DataFrame({
    "group": [1, 2, 3, 4, 5, 6, 7, 8],

    "mean": [
        0.4418605,
        0.55625,
        0.4857143,
        0.6026201,
        0.5567010,
        0.5,
        0.4682540,
        0.8
    ],

    "lcl": [
        0.2872182,
        0.5015222,
        0.4175605,
        0.5387619,
        0.4560587,
        0.2004108,
        0.3799234,
        0.2447110
    ],

    "ucl": [
        0.5965027,
        0.6109778,
        0.5538680,
        0.6664783,
        0.6573434,
        0.7995892,
        0.5565845,
        1.0
    ]
})


# ------------------------------------------------------------
# POLITICAL AFFILIATION
# ------------------------------------------------------------

dem = pd.DataFrame({
    "group": [0, 1],

    "mean": [
        0.4772727,
        0.6406250
    ],

    "lcl": [
        0.4390673,
        0.5924192
    ],

    "ucl": [
        0.5154781,
        0.6888308
    ]
})


# ------------------------------------------------------------
# BID
# ------------------------------------------------------------

bid = pd.DataFrame({
    "group": [
        0.05,
        0.15,
        0.25,
        0.35
    ],

    "mean": [
        0.5735294,
        0.5291262,
        0.5141509,
        0.5571429
    ],

    "lcl": [
        0.5050879,
        0.4603918,
        0.4663850,
        0.4894080
    ],

    "ucl": [
        0.6419709,
        0.5978607,
        0.5619169,
        0.6248777
    ]
})


# ------------------------------------------------------------
# RACE
# ------------------------------------------------------------

white = pd.DataFrame({
    "group": [0, 1],

    "mean": [
        0.6143251,
        0.4963289
    ],

    "lcl": [
        0.5640146,
        0.4586823
    ],

    "ucl": [
        0.6646355,
        0.5339755
    ]
})


# ============================================================
# PLOT FUNCTION
# ============================================================

def plot_ci(
    ax,
    df,
    xlabel,
    title,
    panel_label,
    binary=False,
    labels=None,
    show_ylabel=False,
    xticks=None,
    xlim=None
):

    df = df.copy()


    # --------------------------------------------------------
    # Convert proportions to percentages
    # --------------------------------------------------------

    for col in ["mean", "lcl", "ucl"]:
        df[col] = df[col] * 100


    # --------------------------------------------------------
    # Calculate confidence interval distances
    # --------------------------------------------------------

    lower = df["mean"] - df["lcl"]
    upper = df["ucl"] - df["mean"]


    # --------------------------------------------------------
    # X positions
    # --------------------------------------------------------

    if binary:

        x = [0.45, 0.55]

    else:

        x = df["group"].values


    # ========================================================
    # MAIN PLOT
    # ========================================================

    ax.errorbar(

        x,
        df["mean"].values,

        yerr=[
            lower.values,
            upper.values
        ],

        # ----------------------------------------------------
        # Connecting line
        # ----------------------------------------------------

        fmt="o-",
        color="black",

        # THINNER connecting line
        linewidth=0.6,

        # ----------------------------------------------------
        # Markers
        # ----------------------------------------------------

        markersize=4.5,

        markerfacecolor="#1f77b4",
        markeredgecolor="black",
        markeredgewidth=0.7,

        # ----------------------------------------------------
        # Confidence intervals
        # ----------------------------------------------------

        elinewidth=0.8,
        capsize=3,
        capthick=0.8,

        zorder=3
    )


    # ========================================================
    # Y AXIS
    # ========================================================

    ax.set_ylim(0, 100)

    ax.set_yticks(
        [0, 20, 40, 60, 80, 100]
    )


    # --------------------------------------------------------
    # Show Support (%) only on A and D
    # --------------------------------------------------------

    if show_ylabel:

        ax.set_ylabel(
            "Support (%)",
            fontsize=7.5,
            fontweight="normal",
            labelpad=3
        )

    else:

        ax.set_ylabel("")


    # ========================================================
    # X AXIS
    # ========================================================

    ax.set_xlabel(
        xlabel,
        fontsize=7.5,
        fontweight="normal",
        labelpad=3
    )


    # --------------------------------------------------------
    # Explicit x ticks
    # --------------------------------------------------------

    if xticks is not None:

        ax.set_xticks(xticks)


    # ========================================================
    # BINARY VARIABLES
    # ========================================================

    if binary:

        ax.set_xlim(
            0.35,
            0.65
        )

        ax.set_xticks(
            [0.45, 0.55]
        )

        ax.set_xticklabels(
            labels,
            fontsize=7
        )


    # ========================================================
    # CUSTOM X LIMIT
    # ========================================================

    if xlim is not None:

        ax.set_xlim(xlim)


    # ========================================================
    # TITLE
    # ========================================================

    ax.set_title(
        title,
        fontsize=8.5,
        fontweight="bold",
        pad=4
    )


    # ========================================================
    # PANEL LABEL
    # ========================================================

    ax.text(
        -0.12,
        1.06,
        f"({panel_label})",

        transform=ax.transAxes,

        fontsize=8.5,
        fontweight="bold",

        va="bottom",
        ha="left"
    )


    # ========================================================
    # GRID
    # ========================================================

    ax.grid(
        axis="y",
        color="0.85",
        linewidth=0.5,
        alpha=0.8
    )

    ax.grid(
        axis="x",
        visible=False
    )


    # ========================================================
    # SPINES
    # ========================================================

    for spine in ax.spines.values():

        spine.set_linewidth(0.8)
        spine.set_color("black")


    # ========================================================
    # TICKS
    # ========================================================

    ax.tick_params(
        axis="both",
        which="major",

        width=0.7,
        length=3,

        pad=2
    )


# ============================================================
# CREATE FIGURE
# ============================================================

fig, axs = plt.subplots(
    2,
    3,

    figsize=(
        FIG_WIDTH,
        FIG_HEIGHT
    )
)


# ============================================================
# PANEL A — AGE
# ============================================================

plot_ci(
    axs[0, 0],

    age,

    xlabel="Age Group",
    title="Age",

    panel_label="A",

    show_ylabel=True,

    xticks=[
        2, 3, 4, 5, 6
    ],

    xlim=(
        1.5,
        6.5
    )
)


# Explicitly force all Age categories
axs[0, 0].set_xticks(
    [2, 3, 4, 5, 6]
)

axs[0, 0].set_xticklabels(
    ["2", "3", "4", "5", "6"]
)


# ============================================================
# PANEL B — GENDER
# ============================================================

plot_ci(
    axs[0, 1],

    male,

    xlabel="Gender",
    title="Gender",

    panel_label="B",

    binary=True,

    labels=[
        "Non-Male",
        "Male"
    ],

    show_ylabel=False
)


# ============================================================
# PANEL C — EDUCATION
# ============================================================

plot_ci(
    axs[0, 2],

    educ,

    xlabel="Education Level",
    title="Education",

    panel_label="C",

    show_ylabel=False,

    xticks=[
        1, 2, 3, 4,
        5, 6, 7, 8
    ],

    xlim=(
        0.5,
        8.5
    )
)


# Explicitly force ALL education categories
axs[0, 2].set_xlim(
    0.5,
    8.5
)

axs[0, 2].set_xticks(
    [1, 2, 3, 4, 5, 6, 7, 8]
)

axs[0, 2].set_xticklabels(
    ["1", "2", "3", "4", "5", "6", "7", "8"]
)


# ============================================================
# PANEL D — POLITICAL AFFILIATION
# ============================================================

plot_ci(
    axs[1, 0],

    dem,

    xlabel="Political Affiliation",
    title="Political Affiliation",

    panel_label="D",

    binary=True,

    labels=[
        "Non-Democrat",
        "Democrat"
    ],

    show_ylabel=True
)


# ============================================================
# PANEL E — BID AMOUNT
# ============================================================

plot_ci(
    axs[1, 1],

    bid,

    xlabel="Bid Amount ($)",
    title="Bid Amount",

    panel_label="E",

    show_ylabel=False,

    xticks=[
        0.05,
        0.15,
        0.25,
        0.35
    ],

    xlim=(
        0.02,
        0.38
    )
)


# Explicitly force all Bid categories
axs[1, 1].set_xlim(
    0.02,
    0.38
)

axs[1, 1].set_xticks(
    [
        0.05,
        0.15,
        0.25,
        0.35
    ]
)

axs[1, 1].set_xticklabels(
    [
        "0.05",
        "0.15",
        "0.25",
        "0.35"
    ]
)


# ============================================================
# PANEL F — RACE
# ============================================================

plot_ci(
    axs[1, 2],

    white,

    xlabel="Race",
    title="Race",

    panel_label="F",

    binary=True,

    labels=[
        "Non-White",
        "White"
    ],

    show_ylabel=False
)


# ============================================================
# FINAL LAYOUT
# ============================================================

# Do NOT use tight_layout().
#
# Do NOT use bbox_inches="tight".
#
# This preserves the exact 190-mm physical width.

plt.subplots_adjust(

    left=0.075,
    right=0.985,

    bottom=0.14,
    top=0.91,

    # Horizontal space between columns
    wspace=0.30,

    # Larger vertical gap between rows
    hspace=0.70
)


# ============================================================
# OUTPUT PATH
# ============================================================

output_base = (
    "/Users/freebird/Library/CloudStorage/"
    "OneDrive-TexasTechUniversity/VS Code/python/"
    "current_support_by_groups"
)


# ============================================================
# SAVE TIFF
# ============================================================

tiff_path = (
    output_base +
    "_1200dpi.tiff"
)


fig.savefig(

    tiff_path,

    format="tiff",

    # 600 DPI
    dpi=DPI,

    # IMPORTANT:
    # Do not crop the canvas.
    bbox_inches=None,

    pad_inches=0,

    # White background
    facecolor="white",

    edgecolor="white"
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
# PRINT INFORMATION
# ============================================================

print()
print("--------------------------------------------")
print("Figure created successfully")
print("--------------------------------------------")
print()
print("Submission TIFF:")
print(tiff_path)
print()
print("Preview PNG:")
print(png_path)
print()
print("--------------------------------------------")
print(f"Figure width : {FIG_WIDTH:.4f} inches")
print("Figure width : 190.0 mm")
print()
print(f"Figure height: {FIG_HEIGHT:.2f} inches")
print(
    f"Figure height: "
    f"{FIG_HEIGHT * 25.4:.1f} mm"
)
print()
print(f"TIFF resolution: {DPI} DPI")
print("--------------------------------------------")
print()
