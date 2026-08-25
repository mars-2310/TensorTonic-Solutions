def linear_layer_forward(X: list, W: list, b: list) -> list:
    """
    Returns the affine transformation for every input row.
    """
    # Write code here
    n, d_in, d_out = len(X), len(W), len(b)
    res = []
    for i in range(n):
        row = []
        for j in range(d_out):
            y = 0
            for k in range(d_in):
                y += X[i][k]*W[k][j]
            y += b[j]
            row.append(y)
            
        res.append(row)

    return res         
    pass