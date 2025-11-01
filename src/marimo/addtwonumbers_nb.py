import marimo

__generated_with = "0.17.0"
app = marimo.App()


@app.function
# pylint: disable=missing-module-docstring
def addtwonumbers(a, b):
    """
    Return the sum of two numbers.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    int or float
        The sum of `a` and `b`.

    Examples
    --------
    >>> addtwonumbers(2, 3)
    5
    >>> addtwonumbers(1.5, 2.5)
    4.0
    """
    return a + b


@app.cell
def _():
    import marimo as mo

    a = mo.ui.text(label="Number1", value="7")
    b = mo.ui.text(label="Number2", value="12")
    return a, b, mo


@app.cell
def _(a, b, mo):
    mo.md(f"Result : {addtwonumbers(int(a.value),  int(b.value))}")
    return


if __name__ == "__main__":
    app.run()
