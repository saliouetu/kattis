import marimo

__generated_with = "0.17.0"
app = marimo.App()


@app.cell
def _():
    # pylint: disable=missing-module-docstring
    import math

    def area(a):
        """
        Compute the perimeter of a square given its area.

        The area `a` is assumed to be the area of a square. The perimeter
        of a square is calculated as 4 times the side length, where the
        side length is the square root of the area.

        Parameters
        ----------
        a : float
            The area of the square.

        Returns
        -------
        float
            The perimeter of the square.

        Examples
        --------
        >>> area(16)
        16.0
        >>> area(25)
        20.0
        """
        perimeter = 4 * math.sqrt(a)
        return perimeter
    return (area,)


@app.cell
def _():
    import marimo as mo

    a = mo.ui.text(label="area", value="25")
    return a, mo


@app.cell
def _(a, area, mo):
    mo.md(f"Result : {area(int(a.value))}")
    return


if __name__ == "__main__":
    app.run()
