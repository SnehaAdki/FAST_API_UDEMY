import pytest


def test_equal_or_not_none() -> None:
    """Equal or not None."""
    assert 3 == 3
    assert 3 != 1

def test_is_instance() -> None:
    assert  isinstance(3,int)
    assert isinstance('string', str)
    assert not isinstance('string', int)


def test_boolean() -> None:
    val  = True
    assert True == True
    assert val is True
    assert ('12' == '23') is False

def test_validate_type() -> None:
    assert type('abc'is str)
    assert type(123 is int)

def test_gt_lt() -> None:
    assert 7 > 5
    assert 10 < 20

def test_list() -> None:
    num_list = [10,20,30]
    bool_list = [] # if list is empty then any will return False
    bool_list_val = [False,True,False]
    num_list_false = [0,10, 20, 30]
    assert 10 in num_list
    assert 50 not in num_list
    assert len(num_list) > 0
    assert all(num_list)
    assert any(num_list)
    assert not any(bool_list)
    assert any(bool_list_val)
    assert any(num_list_false)
    assert not all(num_list_false) # checks all values should be truth return false if we encounter any 0

@pytest.fixture
def test_default_details():
    return {'f_name':'Sneha','l_name':'Adki'}


def get_valid_details(test_default_details):
    assert test_default_details['f_name'] == 'Sneha'
    assert test_default_details['l_name'] == 'Adki'