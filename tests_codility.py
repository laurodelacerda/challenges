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


smallest_positive = [([1, 3, 6, 4, 1, 2], 5),
                     ([1, 2, 3], 4),
                     ([-1, 1, 5], 2),
                     ([-1, -3], 1)]
@pytest.mark.parametrize(['A', 'result'], smallest_positive)
def test_smallest_positive(A, result):
    assert codility.smallest_positive(A) == result



multiple_4 = [([0, 4, 8], 12),
              ([-6, -91, 1011, -100, 84, -22, 0, 1, 473], -16)]
@pytest.mark.parametrize(['A', 'result'], multiple_4)
def test_sum_multiple_4(A, result):
    assert codility.sum_multiple_4(A) == result



flip_heads_or_tails = [([0, 1, 0, 1, 1], 1),
                       ([1, 1, 0, 1, 1], 2),
                       ([0, 1, 0], 0),
                       ([0, 1, 1, 0], 2)]
@pytest.mark.parametrize(['A', 'result'], flip_heads_or_tails)
def test_flip_heads_or_tails(A, result):
    assert codility.flip_heads_or_tails(A) == result

