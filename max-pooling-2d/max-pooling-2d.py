def max_pooling_2d(X: list, pool_size: int) -> list:
    """
    Returns non-overlapping maximum-pooled windows.
    """
    # Write code here
    h_out, w_out = len(X) // pool_size, len(X[0]) // pool_size
    output = []

    for i in range(h_out):
        row = []
        for j in range(w_out):
            maxi = float("-inf")

            for r in range(i * pool_size, (i+1) * pool_size):
                for c in range(j * pool_size, (j+1) * pool_size):
                    maxi = max(maxi, X[r][c])

            row.append(maxi)
        output.append(row)

    return output
    pass