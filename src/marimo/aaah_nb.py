import marimo

__generated_with = "0.17.0"
app = marimo.App()


@app.function
# pylint: disable=missing-module-docstring
def aaah(jonah, doctorah):
    """
    Determine whether Jonah can say "aaah" long enough for the doctor.

    The doctor requires a certain length of "aaah" (represented by the 
    number of 'a' characters). Jonah succeeds if his "aaah" has at least 
    as many 'a's as the doctor's.

    Parameters
    ----------
    jonah : str
        The string representing Jonah's "aaah".
    doctorah : str
        The string representing the doctor's required "aaah".

    Returns
    -------
    str
        "go" if Jonah's "aaah" is long enough, otherwise "no".

    Examples
    --------
    >>> aaah("aaah", "ah")
    'go'
    >>> aaah("aaah", "aaaaah")
    'no'
    """
    if jonah.count('a') >= doctorah.count('a'):
        return "go"
    return "no"


@app.cell
def _():
    import marimo as mo

    jon = mo.ui.text(label="Jonah", value="aaah")
    dr = mo.ui.text(label="Doctor", value="ah")
    return dr, jon, mo


@app.cell
def _(dr, jon, mo):
    mo.md(f"""Result: {aaah(jon.value, dr.value)}""")
    return


if __name__ == "__main__":
    app.run()
