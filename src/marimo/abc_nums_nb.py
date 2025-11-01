import marimo

__generated_with = "0.17.0"
app = marimo.App()


@app.function
# pylint: disable=missing-module-docstring
def abc(nums, order):
    """
    Arrange three numbers according to a specified letter order.

    - The input list `nums` contains exactly three numbers.
    - They are sorted in ascending order and then mapped to letters:
      'A' = smallest, 'B' = middle, 'C' = largest.
    - The string `order` specifies the sequence of letters to output.
    - The function returns the corresponding numbers as a space-separated string.

    Parameters
    ----------
    nums : list of int
        A list containing exactly three integers.
    order : str
        A string consisting of the letters 'A', 'B', and 'C' in some order.

    Returns
    -------
    str
        A space-separated string of numbers arranged according to `order`.

    Examples
    --------
    >>> abc([1, 5, 3], "ABC")
    '1 3 5'
    >>> abc([1, 5, 3], "CBA")
    '5 3 1'
    >>> abc([10, 30, 20], "BAC")
    '20 10 30'
    """
    nums.sort()
    mapping = {'A': nums[0], 'B': nums[1], 'C': nums[2]}
    result = [str(mapping[ch]) for ch in order]
    return " ".join(result)


@app.cell
def _():
    import marimo as mo

    nums = mo.ui.text(label="Number", value="1,5,3")
    order = mo.ui.text(label="Order", value="ABC")
    return mo, nums, order


@app.cell
def _(mo, nums, order):
    nums_value = [int(x.strip()) for x in nums.value.split(',')]
    mo.md(f"Result : {abc(nums_value,order.value)}")
    return


if __name__ == "__main__":
    app.run()
