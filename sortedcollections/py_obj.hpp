#ifndef _PY_OBJ_HPP
#define _PY_OBJ_HPP

#include <Python.h>

// RAII wrapper for PyObject *
struct py_object
{
    PyObject mutable *obj;

    py_object(PyObject *o) : obj(o)
    {
        Py_INCREF(obj);
    }

    py_object(py_object const &other) : obj(other.obj)
    {
        Py_INCREF(obj);
    }

    ~py_object()
    {
        Py_DECREF(obj);
    }
};

bool operator<(py_object const &x, py_object const &y)
{
    return PyObject_RichCompareBool(x.obj, y.obj, Py_LT) == 1;
}

#endif
