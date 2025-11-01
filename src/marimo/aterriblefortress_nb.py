import marimo

__generated_with = "0.17.0"
app = marimo.App()


@app.function
# pylint: disable=missing-module-docstring

def aterriblefortress(n, l):
    """
    Compute the total number of blazes in a fortress.

    The function sums up the blaze counts for each section of the fortress.

    Parameters
    ----------
    n : int
        The number of sections in the fortress.
    l : list of int
        A list containing the blaze count for each section. The list
        length should be at least `n`.

    Returns
    -------
    int
        The total number of blazes across all sections.

    Examples
    --------
    >>> aterriblefortress(3, [2, 5, 1])
    8
    >>> aterriblefortress(4, [1, 1, 1, 1])
    4
    """
    total = 0
    for i in range(n):
        blaze_count = l[i]
        total += blaze_count
    return total


@app.cell
def _():
    import marimo as mo

    n = mo.ui.text(label="Number", value="3")
    l = mo.ui.text(label="list", value="2,5,1")
    return l, mo, n


@app.cell
def _(l, mo, n):
    l_val = [int(x) for x in l.value.split(',')]
    mo.md(f"Result : {aterriblefortress(int(n.value),  l_val)}")
    return


if __name__ == "__main__":
    app.run()
