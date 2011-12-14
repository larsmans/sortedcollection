from collections import MutableSet
from _sorted import _SortedSet

class SortedSet(_SortedSet, MutableSet):
    def __init__(self, data):
        super(SortedSet, self).__init__()
        for x in data:
            self.add(x)

    def __repr__(self):
        return "SortedSet(%r)" % list(self)