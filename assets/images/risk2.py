import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# RISK PERCEPTION FREQUENCY DATA
# ============================================================

risk_questions = {

    "Risk (General)": {
        "freq": [58, 94, 95, 114, 157, 251, 108, 76, 42, 49]
    },

    "Health Risk": {
        "freq": [140, 140, 109, 108, 130, 180, 88, 61, 35, 53]
    },

    "Family Risk": {
        "freq": [250, 175, 98, 86, 88, 123, 57, 58, 40, 69]
    },

    "Financial Risk": {
        "freq": [118, 144, 136, 108, 111, 176, 76, 70, 49, 56]
    },

    "Driving Risk": {
        "freq": [187, 152, 110, 89, 102, 180, 80, 59, 41, 44]
    },

    "Sports Risk": {
        "freq": [163, 98, 87, 101, 131, 190, 84, 77, 53, 60]
    },

    "Job Risk": {
        "freq": [150, 100, 81, 105, 125, 180, 87, 93, 40, 83]
    }
}


# ============================================================
# ELSEVIER SMALL-COLUMN SETTINGS
# ============================================================

# Elsevier small/single-column width:
#
# 90 mm = 3.5433 inches
#
FIG_WIDTH = 90 / 25.4


# 7 panels arranged as:
#
# A B
# C D
# E F
# G
#
# A height of 7.8 inches gives enough vertical space for
# four rows while keeping the 90-mm width fixed.

FIG_HEIGHT = 7.8


# TIFF resolution
#
# Elsevier recommendation:
# combination artwork = 500 DPI
#
# 600 DPI provides a little extra safety.

DPI = 1200


# ============================================================
# PUBLICATION STYLE
# ============================================================

sns.set_theme(style="whitegrid")


plt.rcParams.update({

    # --------------------------------------------------------
    # Font
    # --------------------------------------------------------

    "font.family": "Times New Roman",

    # Finished-size lettering
    "font.size": 6.5,

    "axes.titlesize": 7,
    "axes.titleweight": "bold",

    "axes.labelsize": 6.5,

    "xtick.labelsize": 6,
    "ytick.labelsize": 6,

    # --------------------------------------------------------
    # Axes
    # --------------------------------------------------------

    "axes.linewidth": 0.7,

    # --------------------------------------------------------
    # Tick widths
    # --------------------------------------------------------

    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,

    # --------------------------------------------------------
    # White background
    # --------------------------------------------------------

    "figure.facecolor": "white",
    "axes.facecolor": "white"
})


# ============================================================
# COLORS
# ============================================================

colors = sns.color_palette(
    "Set2",
    len(risk_questions)
)


# ============================================================
# CREATE FIGURE
# ============================================================

fig, axes = plt.subplots(

    4,
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
    "(F)",
    "(G)"
]


# ============================================================
# CREATE PANELS
# ============================================================

for i, (title, data) in enumerate(
    risk_questions.items()
):

    ax = axes[i]


    # --------------------------------------------------------
    # Likert scale
    # --------------------------------------------------------

    scales = list(
        range(1, 11)
    )


    # --------------------------------------------------------
    # BAR CHART
    # --------------------------------------------------------

    bars = ax.bar(

        scales,

        data["freq"],

        color=colors[i],

        edgecolor="black",

        # Thin borders
        linewidth=0.5,

        width=0.72,

        zorder=3
    )


    # ========================================================
    # X AXIS
    # ========================================================

    ax.set_xticks(
        scales
    )

    ax.set_xticklabels(
        [
            "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "10"
        ],

        fontsize=6
    )


    # Keep all bars comfortably inside axes
    ax.set_xlim(
        0.4,
        10.6
    )


    # ========================================================
    # X AXIS LABEL
    # ========================================================

    ax.set_xlabel(

        f"{letters[i]} {title}",

        fontsize=6.5,

        fontweight="bold",

        labelpad=3
    )


    # ========================================================
    # Y AXIS
    # ========================================================

    ax.set_ylabel(

        "Frequency",

        fontsize=6.5,

        fontweight="normal",

        labelpad=2
    )


    # ========================================================
    # Y AXIS LIMIT
    # ========================================================

    ax.set_ylim(
        0,
        280
    )


    # ========================================================
    # Y AXIS TICKS
    # ========================================================

    ax.set_yticks(
        [
            0,
            50,
            100,
            150,
            200,
            250
        ]
    )


    # ========================================================
    # FREQUENCY NUMBERS ABOVE BARS
    # ========================================================

    for bar in bars:

        height = bar.get_height()

        ax.text(

            bar.get_x()
            + bar.get_width() / 2,

            height + 3,

            str(int(height)),

            ha="center",

            va="bottom",

            fontsize=5.5,

            color="black",

            # White background makes numbers readable
            # even when bars are tall.

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
    # TICKS
    # ========================================================

    ax.tick_params(

        axis="both",

        which="major",

        width=0.6,

        length=2.5,

        pad=1.5
    )


# ============================================================
# REMOVE UNUSED 8TH PANEL
# ============================================================

# There are 7 plots and 8 available positions.
#
# The last position is removed.

fig.delaxes(
    axes[7]
)


# ============================================================
# LAYOUT
# ============================================================

# IMPORTANT:
#
# Do not use tight_layout().
#
# Do not use bbox_inches="tight".
#
# This preserves the exact 90-mm figure width.

plt.subplots_adjust(

    # Left margin
    left=0.12,

    # Right margin
    right=0.95,

    # Bottom margin
    bottom=0.06,

    # Top margin
    top=0.985,

    # Horizontal gap between the two columns
    wspace=0.30,

    # Vertical gap between rows
    hspace=0.70
)


# ============================================================
# OUTPUT LOCATION
# ============================================================

output_base = (

    "/Users/freebird/Library/CloudStorage/"
    "OneDrive-TexasTechUniversity/VS Code/python/"
    "Risk_Perception_Combined_90mm"
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
    # This keeps the figure canvas exactly 90 mm wide.

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

    # 600 DPI
    dpi=DPI,

    # IMPORTANT:
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
print("Risk perception figure created")
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
