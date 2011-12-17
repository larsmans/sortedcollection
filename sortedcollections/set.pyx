cdef extern from "set.hpp":
    cdef cppclass sorted_set:
        void add(object)
        bint contains(object)
        void discard(object)
        size_t size()

    cdef struct sorted_set_iterator:
        pass

    cdef bint iterator_at_end(sorted_set_iterator &, sorted_set *)
    cdef object get_and_increment(sorted_set_iterator &)
    cdef void make_iterator(sorted_set *, sorted_set_iterator &)

cdef class _SortedSet(object):
    cdef sorted_set *_set

    def __cinit__(self):
        self._set = new sorted_set()

    def __dealloc__(self):
        del self._set

    def __contains__(self, x):
        return self._set.contains(x)

    def __iter__(self):
        return _SetIterator(self)

    def __len__(self):
        return self._set.size()

    def add(self, x):
        """Add element x to the set

        Complexity: O(lg n)
        """
        self._set.add(x)

    def discard(self, x):
        """Remove element x from the set, if present (else no-op)

        Complexity: O(lg n)
        """
        self._set.discard(x)

cdef class _SetIterator(object):
    cdef _SortedSet _set
    cdef sorted_set_iterator _iter

    def __cinit__(self, _SortedSet s):
        self._set = s
        make_iterator(s._set, self._iter)

    def __iter__(self):
        return self

    def next(self):
        if iterator_at_end(self._iter, self._set._set):
            raise StopIteration
        else:
            return get_and_increment(self._iter)
