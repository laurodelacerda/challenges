import pytest
import codility


binary_gap = [(1041, 5),
                    (15, 0),
                    (32, 0),
                    (328, 2),
                    (51712, 2),
                    (561892, 3),
                    (66561, 9)
                    ]
@pytest.mark.parametrize(['N', 'result'], binary_gap)
def test_binary_gap(N, result):
    assert codility.binary_gap(N) == result

parity_degree = [(24, 3),
                 (48, 4),
                 (97, 0),
                 (1, 0),
                 (0, 0),
                 (2, 1)]
@pytest.mark.parametrize(['N', 'result'], parity_degree)
def test_parity_degree(N, result):
    assert codility.parity_degree(N) == result