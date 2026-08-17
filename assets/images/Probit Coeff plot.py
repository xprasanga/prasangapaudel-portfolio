import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# MODEL 1: CURRENT PRICE (PROBIT)
# ============================================================

data1 = {

    "Variable": [
        "Geopolitical",
        "CC Harm",
        "Disaster",
        "Bid/Gas",
        "Age",
        "Male",
        "White",
        "Education",
        "Democrat",
        "Gas Income\nShare",
        "Risk Health",
        "Urban"
    ],

    "beta": [
        0.00992,
        -0.4024,
        0.1259,
        -0.0174,
        -0.1767,
        0.0435,
        0.00762,
        0.0235,
        0.1193,
        0.1337,
        0.2228,
        0.0956
    ],

    "se": [
        0.0485,
        0.0470,
        0.0487,
        0.0459,
        0.0464,
        0.0428,
        0.0455,
        0.0435,
        0.0448,
        0.0497,
        0.0467,
        0.0440
    ]
}


df1 = pd.DataFrame(data1)

df1["lower"] = (
    df1["beta"]
    - 1.96 * df1["se"]
)

df1["upper"] = (
    df1["beta"]
    + 1.96 * df1["se"]
)

df1["Model"] = "Current Price"


# ============================================================
# MODEL 2: $2.50 PRICE (PROBIT)
# ============================================================

data2 = {

    "Variable": [
        "Geopolitical",
        "CC Harm",
        "Disaster",
        "Bid/Gas",
        "Age",
        "Male",
        "White",
        "Education",
        "Democrat",
        "Gas Income\nShare",
        "Risk Health",
        "Urban"
    ],

    "beta": [
        -0.0846,
        -0.3208,
        -0.0385,
        -0.1536,
        -0.1384,
        -0.0114,
        0.00956,
        0.0105,
        0.1969,
        0.0145,
        0.1492,
        0.0399
    ],

    "se": [
        0.0498,
        0.0463,
        0.0501,
        0.0527,
        0.0478,
        0.0438,
        0.0472,
        0.0439,
        0.0473,
        0.0483,
        0.0485,
        0.0459
    ]
}


df2 = pd.DataFrame(data2)

df2["lower"] = (
    df2["beta"]
    - 1.96 * df2["se"]
)

df2["upper"] = (
    df2["beta"]
    + 1.96 * df2["se"]
)

df2["Model"] = "Price: $2.50"


# ============================================================
# COMBINE DATA
# ============================================================

df = pd.concat(
    [df1, df2],
    ignore_index=True
)


# ============================================================
# ORDER VARIABLES BY MODEL 1 COEFFICIENT
# ============================================================

order = (
    df1
    .sort_values("beta")["Variable"]
    .tolist()
)


df["Variable"] = pd.Categorical(
    df["Variable"],
    categories=order,
    ordered=True
)

df = df.sort_values(
    "Variable"
)


# ============================================================
# ELSEVIER SMALL-COLUMN SETTINGS
# ============================================================

# Elsevier small/single-column width:
#
# 90 mm = 3.5433 inches

FIG_WIDTH = 90 / 25.4


# Height is increased slightly because there are
# 12 control variables.

FIG_HEIGHT = 90 / 25.4


# TIFF resolution

DPI = 1200


# ============================================================
# PUBLICATION STYLE
# ============================================================

plt.rcParams.update({

    # --------------------------------------------------------
    # Font
    # --------------------------------------------------------

    "font.family": "Times New Roman",

    "font.size": 6.5,

    "axes.labelsize": 6.5,

    "xtick.labelsize": 5.5,

    "ytick.labelsize": 6.2,

    "legend.fontsize": 5.8,

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
# CREATE FIGURE
# ============================================================

fig, ax = plt.subplots(

    figsize=(
        FIG_WIDTH,
        FIG_HEIGHT
    )
)


# ============================================================
# Y POSITIONS
# ============================================================

y_pos = np.arange(
    len(order)
)


# Distance between the two model estimates

offset = 0.13


# ============================================================
# COLORS
# ============================================================

colors = {

    "Current Price": "#1f77b4",

    "Price: $2.50": "#d62728"
}


# ============================================================
# MODEL 1: CURRENT PRICE
# ============================================================

df_m1 = df[
    df["Model"] == "Current Price"
]


ax.errorbar(

    df_m1["beta"],

    y_pos - offset,

    xerr=[
        df_m1["beta"] - df_m1["lower"],
        df_m1["upper"] - df_m1["beta"]
    ],

    # Circle marker
    fmt="o",

    # Slightly smaller marker for 90-mm figure
    markersize=2,

    markeredgewidth=0.5,

    markeredgecolor=colors["Current Price"],

    # THINNER CI LINE
    linewidth=0.5,

    elinewidth=0.5,

    capsize=2.5,

    capthick=0.5,

    color=colors["Current Price"],

    label="Current Price",

    zorder=4
)


# ============================================================
# MODEL 2: $2.50 PRICE
# ============================================================

df_m2 = df[
    df["Model"] == "Price: $2.50"
]


ax.errorbar(

    df_m2["beta"],

    y_pos + offset,

    xerr=[
        df_m2["beta"] - df_m2["lower"],
        df_m2["upper"] - df_m2["beta"]
    ],

    # Square marker
    fmt="s",

    markersize=2,

    markeredgewidth=0.5,

    markeredgecolor=colors["Price: $2.50"],

    # THINNER CI LINE
    linewidth=0.5,

    elinewidth=0.5,

    capsize=2,

    capthick=0.5,

    color=colors["Price: $2.50"],

    label="Price: $2.50",

    zorder=4
)


# ============================================================
# ZERO REFERENCE LINE
# ============================================================

ax.axvline(

    0,

    color="black",

    linewidth=0.5,

    linestyle="--",

    zorder=1
)


# ============================================================
# Y AXIS
# ============================================================

ax.set_yticks(
    y_pos
)


ax.set_yticklabels(

    order,

    fontsize=6.2
)


# ------------------------------------------------------------
# Y-AXIS TITLE
# ------------------------------------------------------------

ax.set_ylabel(

    "Control Variables",

    fontsize=6.5,

    fontweight="bold",

    labelpad=5
)


# ============================================================
# X AXIS
# ============================================================

ax.set_xlabel(

    "Standardized Probit Coefficient",

    fontsize=6.5,

    fontweight="bold",

    labelpad=3
)


# ============================================================
# X-AXIS TICK LABEL SIZE
# ============================================================

ax.tick_params(

    axis="x",

    which="major",

    width=0.6,

    length=2.5,

    pad=2,

    labelsize=5.5
)


# ============================================================
# Y-AXIS TICKS
# ============================================================

ax.tick_params(

    axis="y",

    which="major",

    width=0.6,

    length=2.5,

    pad=2,

    labelsize=6.2
)


# ============================================================
# GRID
# ============================================================

# Very light vertical gridlines help read coefficients.

ax.grid(

    axis="x",

    color="0.88",

    linewidth=0.15,

    alpha=0.95,

    zorder=0
)


ax.grid(

    axis="y",

    visible=False
)


# ============================================================
# SPINES
# ============================================================

ax.spines["top"].set_visible(False)

ax.spines["right"].set_visible(False)

ax.spines["left"].set_linewidth(0.7)

ax.spines["bottom"].set_linewidth(0.7)


# ============================================================
# Y LIMITS
# ============================================================

# Small padding above and below the first/last variable.

ax.set_ylim(

    -0.65,

    len(order) - 0.35
)


# ============================================================
# LEGEND
# ============================================================

ax.legend(

    frameon=False,

    loc="lower right",

    fontsize=5.8,

    handlelength=1.8,

    handletextpad=0.4,

    borderaxespad=0.2
)


# ============================================================
# LAYOUT
# ============================================================

# Use the full 90-mm width.
#
# The left margin is kept relatively small because the
# variable names are short enough to fit.
#
# The right margin is also small to maximize plotting area.

plt.subplots_adjust(

    left=0.20,

    right=0.98,

    bottom=0.10,

    top=0.98
)


# ============================================================
# OUTPUT LOCATION
# ============================================================

output_base = (

    "/Users/freebird/Library/CloudStorage/"
    "OneDrive-TexasTechUniversity/VS Code/python/"
    "EnergyPolicy_Probit_Coefficients_90mm"
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
    # Do not crop the figure.
    #
    # This preserves the exact 90-mm physical width.

    bbox_inches=None,

    pad_inches=0,

    facecolor="white",

    edgecolor="white"
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
print("Probit coefficient figure created")
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
