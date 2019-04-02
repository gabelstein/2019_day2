from maxima import find_maxima
import numpy as np
import pytest	

test_cases = [

([1,2,3,2,1],[2]),
([1,2,1,2,1],[1,3])

]


@pytest.mark.parametrize("inp, exp", test_cases)
def test_maxima(inp, exp):
	out = find_maxima(inp)
	assert out == exp



