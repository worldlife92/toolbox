from toolbox.sum_of_three import sum3

def test_numbers_0_0_0():
    assert sum3(1, 2, 0) == 3

def test_with_negative_numbers():
    assert sum3(-1, 1, 0) == 0
