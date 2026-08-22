from pathlib import Path
import ast
import nbformat as nbf
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
M = ROOT / "manuscript-visualization"
OUT = M / "manuscript_visualization.ipynb"

SCRIPTS = [
    ("OLS Std Coefficients.py", "Regression coefficients: OLS"),
    ("Probit Coeff plot.py", "Regression coefficients: Probit"),
    ("climate perception.py", "Climate-change perceptions"),
    ("risk2.py", "Risk perceptions"),
    ("support across group 250.py", "Support under the $2.50 gasoline-price scenario"),
    ("support across groups current.py", "Support under the current gasoline-price scenario"),
]


def top_level_chunks(source: str, max_nodes: int = 3):
    """Split real Python source into executable notebook cells without replacing it with %run calls.

    The source text is preserved exactly; cells are grouped at top-level Python
    statement boundaries so the presentation reads like a Jupyter/Colab analysis.
    """
    tree = ast.parse(source)
    nodes = tree.body
    if not nodes:
        return []

    chunks = []
    for i in range(0, len(nodes), max_nodes):
        group = nodes[i : i + max_nodes]
        start = min(n.lineno for n in group) - 1
        end = max(getattr(n, "end_lineno", n.lineno) for n in group)
        text = "\n".join(source.splitlines()[start:end]).strip()
        if text:
            chunks.append(text + "\n")
    return chunks


def purpose(text: str, index: int, total: int) -> str:
    lower = text.lower()
    if index == 0:
        return "Imports and initial setup"
    if any(k in lower for k in ["dataframe", "data1", "data2", "questions", "risk_questions"]):
        return "Data and analytical inputs"
    if any(k in lower for k in ["rcparams", "set_theme", "colors", "fig,", "subplots"]):
        return "Figure and publication settings"
    if any(k in lower for k in ["errorbar", "bar(", "plot(", "set_title", "set_xticks", "ax.", "for i,"]):
        return "Create the figure"
    if any(k in lower for k in ["show()", "savefig"]):
        return "Render and display the result"
    return f"Analysis step {index + 1}"


nb = nbf.v4.new_notebook()
nb.metadata = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python"},
}

# Quarto reads this first raw cell as document metadata. The notebook is
# executed below by nbclient, then Quarto renders the saved outputs as a
# normal notebook-style web page.
nb.cells.append(nbf.v4.new_raw_cell(
    "---\n"
    "title: \"Public Support for Gasoline Taxes to Finance Renewable Energy\"\n"
    "subtitle: \"The Role of Informational Framing and Fuel Prices\"\n"
    "author: \"Prasanga Paudel\"\n"
    "jupyter: python3\n"
    "format:\n"
    "  html:\n"
    "    code-fold: false\n"
    "    code-tools: true\n"
    "    toc: true\n"
    "    page-layout: article\n"
    "execute:\n"
    "  enabled: false\n"
    "---"
))

nb.cells.append(nbf.v4.new_markdown_cell(
    "# Manuscript Visualization Notebook\n\n"
    "This is the executed Python presentation of the manuscript visualizations. "
    "Each project is organized as a research notebook: **explanation → actual Python code → actual output → next code cell → next output**. "
    "The code shown below is the source contained in the corresponding `.py` files; there are no `%run` or placeholder cells."
))

for section, (filename, title) in enumerate(SCRIPTS, 1):
    path = M / filename
    source = path.read_text(encoding="utf-8")
    chunks = top_level_chunks(source)

    nb.cells.append(nbf.v4.new_markdown_cell(
        f"## {section}. {title}\n\n"
        f"**Source:** `{filename}`\n\n"
        "The following cells preserve the executable Python source and the output produced by running it. "
        "This section is intentionally formatted like a Google Colab/Jupyter research notebook rather than a single block of code."
    ))

    for i, chunk in enumerate(chunks):
        nb.cells.append(nbf.v4.new_markdown_cell(f"### {purpose(chunk, i, len(chunks))}"))
        nb.cells.append(nbf.v4.new_code_cell(chunk))

nb.cells.append(nbf.v4.new_markdown_cell(
    "## Reproducibility notes\n\n"
    "The `.py` files remain the reusable source files. This `.ipynb` is the presentation and execution record. "
    "The GitHub Actions workflow executes the notebook and Quarto renders the saved notebook as the published HTML page."
))

# Execute from the manuscript directory so relative file references behave naturally.
client = NotebookClient(nb, timeout=600, kernel_name="python3", resources={"metadata": {"path": str(M)}})
client.execute()
nbf.write(nb, OUT)
