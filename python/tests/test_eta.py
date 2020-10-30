import numpy as np
from numpy.testing import assert_allclose

from light_curve_pure import Eta


def test_eta():
    a = np.array([1, 2, 3, 3, 3, 4, 4])
    feature = Eta()
    actual = feature(a, a, None)
    desired = 0.43750000000000006
    assert_allclose(actual, desired)
