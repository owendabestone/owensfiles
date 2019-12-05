from find_pos import *
from openloc import *

def test_find_pos1():
    assert find_pos1('What day is today? Today is Monday', 'day') == [5,14,21,31]
    assert find_pos1('123451234512345','5') == [4,9,14]
    
def test_openloc():
    assert open_loc([1,2,3,4,5],[1,2],[3,4]) == [5]
    assert open_loc([1,2,4,5],[1,2],[5,4]) == []