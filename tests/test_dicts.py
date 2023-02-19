import pytest
from utils import dicts


@pytest.fixture
def testing_dict():
    return {1: "one", "two": 2, "name": {"name": "Marat", "surname": "Shainurov"}}


def test_dicts_normal_dict(testing_dict):
    assert dicts.get_val(testing_dict, "two", "git") == 2
    assert dicts.get_val(testing_dict, "name") == {"name": "Marat", "surname": "Shainurov"}
    assert dicts.get_val(testing_dict, 1) == "one"


def test_dicts_empty_dict(testing_dict):
    assert dicts.get_val({}, "two", "git") == "git"


def test_dicts_no_key(testing_dict):
    assert dicts.get_val(testing_dict, "three", default="pytest") == "pytest"
