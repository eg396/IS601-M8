## operations_test.py
## IS 601, Module 8
## Evan Garvey

import pytest
from app.operations import add, subtract, multiply, divide

def test_add():

    ## test_add
    ## tests the addition capability of the add() function

    ## Inputs:
    ## 2
    ## 3

    ## Expected outcome:
    ## 5

    assert add(2, 3) == 5

def test_subtract():

    ## test_subtract
    ## tests the subtraction capability of the subtract() function

    ## Inputs:
    ## 5
    ## 3

    ## Expected outcome:
    ## 2

    assert subtract(5, 3) == 2

def test_multiply():

    ## test_multiply
    ## tests the multiplication capability of the multiply() function

    ## Inputs:
    ## 2
    ## 3

    ## Expected outcome:
    ## 6

    assert multiply(2, 3) == 6

def test_divide():

    ## test_divide
    ## tests the division capability of the divide() function

    ## Inputs:
    ## 10
    ## 2

    ## Expected outcome:
    ## 5

    assert divide(10, 2) == 5

def test_divide_by_zero():

    ## test_divide_by_zero
    ## tests if a ValueError is raised when dividing by zero

    ## Inputs:
    ## 5
    ## 0

    with pytest.raises(ValueError):
        divide(5, 0)