import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Let's create a simple calculator""")
    return


@app.cell
def _():
    from enum import StrEnum

    class Ops(StrEnum):
        Plus = "+"
        Minus = "-"
        Multiply = "×"
        Divide = "÷"

        def __call__(self, values):
            a, b = values
            match self:
                case Ops.Plus:
                    return a + b
                case Ops.Minus:
                    return a - b
                case Ops.Multiply:
                    return a * b
                case Ops.Divide:
                    return a / b
    return (Ops,)


@app.cell
def _(Ops):
    def calculate(*args: int | float | str):
        x, op, y = None, None, None
        for arg in args:
            if isinstance(arg, str):
                op = Ops(arg)
            elif x:
                y = arg
            else:
                x = arg
        if x and op and y:
            return op([x, y])
        else:
            raise Exception("Invalid Arguments!")
    return (calculate,)


@app.cell
def _(Ops, mo):
    prompt = mo.md("{a} {ops} {b}").batch(
        a=mo.ui.number(1), ops=mo.ui.dropdown(Ops, Ops.Plus), b=mo.ui.number(1)
    )
    prompt
    return (prompt,)


@app.cell
def _(calculate, prompt):
    calculate(*prompt.value.values())
    return


if __name__ == "__main__":
    app.run()
