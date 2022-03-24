import pytest
import foobar

tests_braille = [
    ("code", "100100101010100110100010"),
    ("Braille", "000001110000111010100000010100111000111000100010"),
    ("The quick brown fox jumps over the lazy dog", "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110")
]
@pytest.mark.parametrize(["sentence", "result"], tests_braille)
def test_braille_translation(sentence, result):
    assert foobar.braille_translation(sentence) == result


tests_maxProductSubset = [
    ([2, 0, 2, 2, 0], "8"),
    ([-2, -3, 4, -5], "60"),
    ([-1, -1, -2, 4, 3], "24"),
    ([-1, 0], "0"),
    ([-1], "-1"),
    ([696, 254, 707, 730, 252, 144, 18, -678, 921, 681, -665, 421, -501, 204, 742, -609, 672, -72, 339, -555, -736,
      230, -450, 375, 941, 50, 897, -192, -912, -915, 609, 100, -933, 458, -893, 932, -590, -209, 107, 473, -311, 73,
      68, -229, 480, 41, -235, 558, -615, -289, -643],
     "112783193423281396421025291063982496313759557506029207349556366834514274891010648892576460433185005069070271452630069726538629120")
]
@pytest.mark.parametrize(["list_numbers", "result"], tests_maxProductSubset)
def test_maxProductSubset(list_numbers, result):
    assert foobar.maxProductSubset_naive(list_numbers) == result


test_salute = [
    ("--->-><-><-->-", 10),
    (">----<", 2),
    ("<<>><", 4),
]
@pytest.mark.parametrize(["hallway", "result"], test_salute)
def test_route_salute(hallway, result):
    assert foobar.route_salute(hallway) == result


@pytest.mark.parametrize(["hallway", "result"], test_salute)
def test_route_salute_2(hallway, result):
    assert foobar.route_salute_2(hallway) == result