from _sorted import _SortedSet

a = _SortedSet()
a.add(2)
a.add(3)
a.add('foo')
a.add(1)
a.discard(2)
a.discard('bar')

print list(a)
