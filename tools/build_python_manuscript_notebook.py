from pathlib import Path
import ast
import nbformat as nbf
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "manuscript-visualization"
OUT = PROJECT / "python_analysis.ipynb"

# One notebook, one published webpage. The .py files remain the source files;
# this script turns them into genuine Jupyter code cells and captures their
# real matplotlib outputs.
SCRIPTS = [
    ("climate perception.py", "Climate Perception"),
    ("risk2.py", "Risk Perception"),
    ("support across group 250.py", "Support Across Groups — $2.50 Gasoline Price"),
    ("support across groups current.py", "Support Across Groups — Current Gasoline Price"),
    ("OLS Std Coefficients.py", "OLS Coefficients"),
    ("Probit Coeff plot.py", "Probit Coefficients"),
]


def split_into_cells(source: str):
    """Split valid Python source at top-level statement boundaries.

    This keeps imports, data definitions, plotting setup, loops, and display
    statements executable in their original order. It deliberately avoids
    `%run` and avoids turning the notebook into a fake HTML code viewer.
    """
    tree = ast.parse(source)
    lines = source.splitlines()
    cells = []

    for start in range(0, len(tree.body), 3):
        nodes = tree.body[start:start + 3]
        first = min(node.lineno for node in nodes) - 1
        last = max(getattr(node, "end_lineno", node.lineno) for node in nodes)
        code = "\n".join(lines[first:last]).strip()
        if code:
            cells.append(code + "\n")
    return cells


def describe_cell(code: str, index: int) -> str:
    text = code.lower()
    if index == 0:
        return "Setup and inputs"
    if any(x in text for x in ["questions", "data1", "data2", "risk_questions"]):
        return "Define the analysis inputs"
    if any(x in text for x in ["subplots", "rcparams", "set_theme", "color_palette"]):
        return "Set up the visualization"
    if any(x in text for x in ["bar(", "errorbar(", "plot(", "ax.", "for i,"]):
        return "Create the visualization"
    if "show()" in text or "savefig" in text:
        return "Display the result"
    return f"Analysis step {index + 1}"


nb = nbf.v4.new_notebook()
nb.metadata.update({
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.x"},
    "quarto": {
        "title": "Python Data Analysis",
        "author": "Prasanga Paudel",
        "jupyter": "python3",
        "format": {
            "html": {
                "code-fold": False,
                "code-tools": True,
                "toc": True,
                "page-layout": "article",
            }
        },
    },
})

nb.cells.append(nbf.v4.new_markdown_cell(
    "# Python Data Analysis\n\n"
    "This page presents the Python analyses in a single executable Jupyter notebook. "
    "Each section contains explanatory text, the underlying Python code, and the actual output produced by running that code.\n\n"
    "The original `.py` files are retained as reusable source files; this notebook is the presentation version published through Quarto."
))

for number, (filename, title) in enumerate(SCRIPTS, 1):
    source = (PROJECT / filename).read_text(encoding="utf-8")
    nb.cells.append(nbf.v4.new_markdown_cell(
        f"## {number}. {title}\n\n"
        f"The analysis below is based on `{filename}`."
    ))

    for i, code in enumerate(split_into_cells(source)):
        nb.cells.append(nbf.v4.new_markdown_cell(f"### {describe_cell(code, i)}"))
        nb.cells.append(nbf.v4.new_code_cell(code))

nb.cells.append(nbf.v4.new_markdown_cell(
    "## Reproducibility\n\n"
    "The notebook is generated from the Python source files and executed during the website build. "
    "Quarto then renders this same notebook as the published webpage, so the code and figures shown here are the actual notebook cells and outputs."
))

client = NotebookClient(
    nb,
    timeout=600,
    kernel_name="python3",
    resources={"metadata": {"path": str(PROJECT)}},
    allow_errors=False,
)
client.execute()
nbf.write(nb, OUT)
print(f"Built and executed {OUT}")
