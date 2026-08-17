import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# ELSEVIER FIGURE SETTINGS
# ============================================================

# Elsevier full-width figure:
# 190 mm = 7.4803 inches
FIG_WIDTH = 190 / 25.4

# Figure height
# 5.2 inches = 132.1 mm
FIG_HEIGHT = 5.2

# ------------------------------------------------------------
# Global matplotlib style
# ------------------------------------------------------------

plt.rcParams.update({

    # Font sizes in points
    "font.size": 7.5,
    "axes.titlesize": 8.5,
    "axes.labelsize": 7.5,

    "xtick.labelsize": 7,
    "ytick.labelsize": 7,

    "axes.titleweight": "bold",
    "axes.labelweight": "normal",

    # Thin journal-style axes
    "axes.linewidth": 0.8,

    # Vector PDF fonts
    "pdf.fonttype": 42,
    "ps.fonttype": 42,

    # White background
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
    "mean": [0.7687075, 0.7860262, 0.7077626, 0.6486486, 0.5663717],
    "lcl":  [0.6997395, 0.7325093, 0.6470541, 0.5853620, 0.5012675],
    "ucl":  [0.8376755, 0.8395431, 0.7684710, 0.7119353, 0.6314758]
})


# ------------------------------------------------------------
# GENDER
# ------------------------------------------------------------

male = pd.DataFrame({
    "group": [0, 1],
    "mean": [0.6910420, 0.6881288],
    "lcl":  [0.6521986, 0.6472601],
    "ucl":  [0.7298855, 0.7289975]
})


# ------------------------------------------------------------
# EDUCATION
# ------------------------------------------------------------

educ = pd.DataFrame({
    "group": [1, 2, 3, 4, 5, 6, 7, 8],
    "mean": [
        0.5581395,
        0.69375,
        0.6619048,
        0.7423581,
        0.7113402,
        0.7857143,
        0.6349206,
        1.0
    ],
    "lcl": [
        0.4034973,
        0.6429758,
        0.5973966,
        0.6852882,
        0.6195380,
        0.5398558,
        0.5496948,
        1.0
    ],
    "ucl": [
        0.7127818,
        0.7445242,
        0.7264129,
        0.7994280,
        0.8031424,
        1.0,
        0.7201465,
        1.0
    ]
})

educ["ucl"] = educ["ucl"].clip(upper=1)
educ["lcl"] = educ["lcl"].clip(lower=0)


# ------------------------------------------------------------
# POLITICAL AFFILIATION
# ------------------------------------------------------------

dem = pd.DataFrame({
    "group": [0, 1],
    "mean": [0.6212121, 0.8072917],
    "lcl":  [0.5841080, 0.7676649],
    "ucl":  [0.6583162, 0.8469184]
})


# ------------------------------------------------------------
# BID
# ------------------------------------------------------------

bid = pd.DataFrame({
    "group": [0.05, 0.15, 0.25, 0.35],
    "mean": [0.7352941, 0.7427184, 0.6415094, 0.6904762],
    "lcl":  [0.6742408, 0.6825236, 0.5956781, 0.6274359],
    "ucl":  [0.7963474, 0.8029133, 0.6873408, 0.7535165]
})


# ------------------------------------------------------------
# RACE
# ------------------------------------------------------------

white = pd.DataFrame({
    "group": [0, 1],
    "mean": [0.7382920, 0.6637298],
    "lcl":  [0.6928591, 0.6281579],
    "ucl":  [0.7837249, 0.6993017]
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
    # Confidence interval lengths
    # --------------------------------------------------------

    lower = df["mean"] - df["lcl"]
    upper = df["ucl"] - df["mean"]

    # --------------------------------------------------------
    # X positions
    # --------------------------------------------------------

    if binary:

        # Give binary categories equal visual spacing
        x = [0.45, 0.55]

    else:

        x = df["group"].values

    # --------------------------------------------------------
    # Main line + points + confidence intervals
    # --------------------------------------------------------

    ax.errorbar(

        x,
        df["mean"].values,

        yerr=[
            lower.values,
            upper.values
        ],

        # Line joining points
        fmt="o-",
        color="black",

        # Slightly thinner connecting line
        linewidth=0.6,

        # Point
        markersize=3.5,
        markerfacecolor="#1f77b4",
        markeredgecolor="black",
        markeredgewidth=0.7,

        # Confidence intervals
        elinewidth=1.0,
        capsize=3,
        capthick=1.0,

        zorder=3
    )

    # --------------------------------------------------------
    # Y-axis
    # --------------------------------------------------------

    ax.set_ylim(0, 100)

    # Y-axis ticks
    ax.set_yticks([0, 20, 40, 60, 80, 100])

    # Only show "Support (%)" for A and D
    if show_ylabel:

        ax.set_ylabel(
            "Support (%)",
            fontsize=7.5,
            fontweight="normal",
            labelpad=3
        )

    else:

        ax.set_ylabel("")

    # --------------------------------------------------------
    # X-axis label
    # --------------------------------------------------------

    ax.set_xlabel(
        xlabel,
        fontsize=7.5,
        fontweight="normal",
        labelpad=3
    )

    # --------------------------------------------------------
    # Explicit x-axis ticks
    # --------------------------------------------------------

    if xticks is not None:

        ax.set_xticks(xticks)

    # --------------------------------------------------------
    # Binary variables
    # --------------------------------------------------------

    if binary:

        ax.set_xlim(0.35, 0.65)

        ax.set_xticks([0.45, 0.55])

        ax.set_xticklabels(
            labels,
            fontsize=7
        )

    # --------------------------------------------------------
    # User-defined x limits
    # --------------------------------------------------------

    if xlim is not None:

        ax.set_xlim(xlim)

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    ax.set_title(
        title,
        fontsize=8.5,
        fontweight="bold",
        pad=4
    )

    # --------------------------------------------------------
    # Panel label
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # Grid
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # Spines
    # --------------------------------------------------------

    for spine in ax.spines.values():

        spine.set_linewidth(0.8)
        spine.set_color("black")

    # --------------------------------------------------------
    # Ticks
    # --------------------------------------------------------

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
    figsize=(FIG_WIDTH, FIG_HEIGHT)
)


# ============================================================
# (A) AGE
# ============================================================

plot_ci(
    axs[0, 0],
    age,
    xlabel="Age Group",
    title="Age",
    panel_label="A",
    show_ylabel=True,
    xticks=[2, 3, 4, 5, 6],
    xlim=(1.5, 6.5)
)

# Explicitly force ALL age categories
axs[0, 0].set_xticks([2, 3, 4, 5, 6])
axs[0, 0].set_xticklabels(
    ["2", "3", "4", "5", "6"]
)


# ============================================================
# (B) GENDER
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
# (C) EDUCATION
# ============================================================

plot_ci(
    axs[0, 2],
    educ,
    xlabel="Education Level",
    title="Education",
    panel_label="C",
    show_ylabel=False,
    xticks=[1, 2, 3, 4, 5, 6, 7, 8],
    xlim=(0.5, 8.5)
)

# ------------------------------------------------------------
# IMPORTANT:
# Explicitly force ALL eight education categories
# ------------------------------------------------------------

axs[0, 2].set_xlim(0.5, 8.5)

axs[0, 2].set_xticks(
    [1, 2, 3, 4, 5, 6, 7, 8]
)

axs[0, 2].set_xticklabels(
    ["1", "2", "3", "4", "5", "6", "7", "8"]
)


# ============================================================
# (D) POLITICAL AFFILIATION
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
# (E) BID AMOUNT
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
    xlim=(0.02, 0.38)
)

# ------------------------------------------------------------
# Explicitly force ALL four bid categories
# ------------------------------------------------------------

axs[1, 1].set_xlim(0.02, 0.38)

axs[1, 1].set_xticks(
    [0.05, 0.15, 0.25, 0.35]
)

axs[1, 1].set_xticklabels(
    ["0.05", "0.15", "0.25", "0.35"]
)


# ============================================================
# (F) RACE
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

# IMPORTANT:
# Do NOT use bbox_inches="tight".
#
# This preserves the exact 190-mm figure width.
#
# hspace creates the visible gap between the upper and lower
# rows of panels.

plt.subplots_adjust(
    left=0.075,
    right=0.985,
    bottom=0.14,
    top=0.91,
    wspace=0.30,
    hspace=0.70
)


# ============================================================
# OUTPUT PATH
# ============================================================

output_base = (
    "/Users/freebird/Library/CloudStorage/"
    "OneDrive-TexasTechUniversity/VS Code/python/"
    "support_250_gas_tax_groups"
)


# ============================================================
# SAVE VECTOR PDF
# ============================================================

pdf_path = output_base + ".pdf"

fig.savefig(
    pdf_path,
    format="pdf",
    bbox_inches=None,
    pad_inches=0
)


# ============================================================
# SAVE 300-DPI PNG PREVIEW
# ============================================================

# This PNG has the SAME physical dimensions as the PDF:
# 190 mm wide × 132.1 mm high
#
# 300 dpi is used here only for the raster preview.

png_path = output_base + "_preview_1200dpi.tiff"

fig.savefig(
    png_path,
    format="tiff",
    dpi=1200,
    bbox_inches=None,
    pad_inches=0
)


# ============================================================
# DISPLAY
# ============================================================

plt.show()


# ============================================================
# PRINT FILE INFORMATION
# ============================================================

print("--------------------------------------------")
print("Figure created successfully.")
print("--------------------------------------------")
print(f"PDF: {pdf_path}")
print(f"PNG preview: {png_path}")
print("--------------------------------------------")
print(f"Figure width : {FIG_WIDTH:.4f} inches")
print(f"Figure width : 190.0 mm")
print(f"Figure height: {FIG_HEIGHT:.2f} inches")
print(f"Figure height: {FIG_HEIGHT * 25.4:.1f} mm")
print("--------------------------------------------")
print("PDF is vector format.")
print("PNG preview is 300 DPI.")
print("--------------------------------------------")