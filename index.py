import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Index of Pages

    1. [Calculator](/calculator.html)
    """
    )
    return


if __name__ == "__main__":
    app.run()
