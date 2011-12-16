from nose.tools import assert_equal

from sortedcollections import SortedSet

def test_sortedset():
    a = SortedSet([2, 3])
    a.add(1)
    a.discard(2)

    assert_equal(list(a), [1, 3])
