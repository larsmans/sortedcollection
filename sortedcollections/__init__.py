from collections import Iterator, MutableSet
from .set import _SortedSet, _SetIterator

class SortedSetIterator(_SetIterator, Iterator):
    pass

class SortedSet(_SortedSet, MutableSet):
    """Dynamic set data structure with iteration in sorted order"""

    def __init__(self, data=()):
        super(SortedSet, self).__init__()
        for x in data:
            self.add(x)

    def __iter__(self):
        return SortedSetIterator(self)

    def __repr__(self):
        return "SortedSet(%r)" % list(self)
