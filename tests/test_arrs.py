from utils import arrs
import pytest


@pytest.fixture
def testing_list():
    return [1, 2, 3, 4]


def test_get(testing_list):
    assert arrs.get(testing_list, 1, "test") == 2
    assert arrs.get([], -2, "test") == "test"


def test_slice(testing_list):
    assert arrs.my_slice(testing_list, 1, 3) == [2, 3]
    assert arrs.my_slice(testing_list, 1) == [2, 3, 4]


def test_slice_empty():
    assert arrs.my_slice([], 1, 3) == []


def test_slice_negative_index(testing_list):
    assert arrs.my_slice(testing_list, -10, 2) == [1, 2]
    assert arrs.my_slice(testing_list, -3, -1) == [2, 3]
