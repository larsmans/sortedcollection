SRCD = sortedcollections

all:
	python setup.py build_ext

debug:
	python setup.py build_ext --inplace --pyrex-gdb

inplace:
	python setup.py build_ext --inplace

clean:
	rm -f $(SRCD)/*.cpp $(SRCD)/*.pyc $(SRCD)/*.so
	rm -rf cython_debug/
	python setup.py clean
