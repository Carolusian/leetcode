# Insert 'm' into 'n' between 'i' and 'j'
import unittest

def insertion(n, m, i, j):
    left_mask = ~0 << (j + 1)
    right_mask = ((1 << i) - 1)

    mask = left_mask | right_mask
    n_cleared = n & mask
    m_shifted = m << i

    return n_cleared | m_shifted
