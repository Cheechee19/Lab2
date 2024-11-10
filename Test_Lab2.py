from Lab2 import calc_min_temperature, calc_max_temperature, calc_average_temperature,calc_median_temperature


def test_calc_average_temperature():
    assert calc_average_temperature([5, 10, 15]) == 10.0

def test_calc_min_temperature():
    assert calc_min_temperature([5, 10, 15]) == 5

def test_calc_max_temperature():
    assert calc_max_temperature([5, 10, 15]) == 15

def test_calc_median_temperature():
    assert calc_median_temperature([5, 10, 15]) == 10
    assert calc_median_temperature([5, 10, 15, 20]) == 12.5

