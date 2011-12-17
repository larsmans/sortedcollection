from nose.tools import assert_equal

from sortedcollections import SortedSet


def test_sortedset():
    a = SortedSet([2, 3])
    a.add(1)
    a.discard(2)

    assert_equal(list(a), [1, 3])


def test_set_iterator():
    l = "foo bar baz".split()
    a = SortedSet(l)
    assert_equal(sum(1 for x in a), len(l))


def test_set_union():
    a = SortedSet([1, 2])
    b = set([2, 3])

    assert_equal(list(a | b), [1, 2, 3])

    a |= b
    assert_equal(list(a), [1, 2, 3])
