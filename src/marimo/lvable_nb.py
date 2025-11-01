import marimo

__generated_with = "0.17.0"
app = marimo.App()


@app.function
# pylint: disable=missing-module-docstring
def lvable(s):
    """
    Classify a string based on the presence of the letters 'l' and 'v'.

    The function returns:
        - 0 if both 'l' and 'v' appear consecutively as "lv" in the string.
        - 1 if the string contains either 'l' or 'v' (but not "lv").
        - 2 if neither 'l' nor 'v' appears in the string.

    Parameters
    ----------
    s : str
        The input string to check.

    Returns
    -------
    int
        Classification code:
        0 -> contains "lv"
        1 -> contains 'l' or 'v'
        2 -> contains neither 'l' nor 'v'

    Examples
    --------
    >>> lvable("love")
    0
    >>> lvable("lamp")
    1
    >>> lvable("cat")
    2
    """
    if "lv" in s:
        return 0
    if 'l' in s or 'v' in s:
        return 1
    return 2


@app.cell
def _():
    import marimo as mo

    a = mo.ui.text(label="string", value="love")
    return a, mo


@app.cell
def _(a, mo):
    mo.md(f"Result : {lvable(a.value)}")
    return


if __name__ == "__main__":
    app.run()
