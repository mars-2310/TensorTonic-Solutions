import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    ans = []
    for el in x:
        if el <= 0:
            ans.append(alpha*(math.exp(el) - 1))
        else:
            ans.append(el)

    return ans
    pass