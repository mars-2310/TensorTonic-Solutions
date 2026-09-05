import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]

    angle = pos / (base ** (2 * (i // 2) / d_model))

    pe = np.zeros((seq_len, d_model), dtype=float)

    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])

    return pe
    pass