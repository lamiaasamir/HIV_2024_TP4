def test_find_closest_elements(find_closest_elements):
    assert find_closest_elements(numbers) == (3.9, 4.0)
    assert find_closest_elements(numbers) == (5.0, 5.9)
    assert find_closest_elements(numbers) == (5.0, 5.9)
    assert find_closest_elements(numbers) == (5.0, 5.9)
    assert find_closest_elements(numbers) == (5.0, 5.9)
    assert find_closest_elements(numbers) == (5.0, 5.9)
    assert find_closest_elements(numbers) == (5.0, 5.9)
    assert find_closest_elements(numbers) == (5.0, 5.9)
    assert find_closest_elements(numbers) == (5.0, 5.9)
    assert find_closest_elements(numbers) == (5.0, 5.9)
def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
