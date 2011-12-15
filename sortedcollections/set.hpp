#ifndef _SET_HPP
#define _SET_HPP

#include <set>
#include "py_obj.hpp"

// Note: public inheritance from a baseclass without virtual dtor;
// a mortal sin in some C++ programmers' circles.
class sorted_set : public std::set<py_object>
{
  public:
    void add(PyObject *obj)
    {
        insert(py_object(obj));
    }

    bool contains(PyObject *obj)
    {
        return find(py_object(obj)) != end();
    }

    void discard(PyObject *obj)
    {
        erase(py_object(obj));
    }
};

// Cython doesn't grok :: in a cdef extern type
struct sorted_set_iterator : public sorted_set::const_iterator
{
    sorted_set_iterator(sorted_set::const_iterator const &other)
      : sorted_set::const_iterator(other)
    {
    }
};

inline PyObject *get_and_increment(sorted_set_iterator &i)
{
    return (*i++).obj;
}

inline bool iterator_at_end(sorted_set_iterator const &i, sorted_set const *s)
{
    return i == s->end();
}

inline void make_iterator(sorted_set const *s, sorted_set_iterator &i)
{
    i = s->begin();
}

#endif
