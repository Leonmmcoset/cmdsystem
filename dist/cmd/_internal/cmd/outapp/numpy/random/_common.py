# encoding: utf-8
# module numpy.random._common
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\numpy\random\_common.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sys as sys # <module 'sys' (built-in)>
import numpy as np # C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\numpy\__init__.py

# functions

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

# classes

class interface(tuple):
    """ interface(state_address, state, next_uint64, next_uint32, next_double, bit_generator) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new interface object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new interface object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, state_address, state, next_uint64, next_uint32, next_double, bit_generator): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, state_address, state, next_uint64, next_uint32, next_double, bit_generator): # reliably restored by inspect
        """ Create new instance of interface(state_address, state, next_uint64, next_uint32, next_double, bit_generator) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    bit_generator = _tuplegetter(5, 'Alias for field number 5')
    next_double = _tuplegetter(4, 'Alias for field number 4')
    next_uint32 = _tuplegetter(3, 'Alias for field number 3')
    next_uint64 = _tuplegetter(2, 'Alias for field number 2')
    state = _tuplegetter(1, 'Alias for field number 1')
    state_address = _tuplegetter(0, 'Alias for field number 0')
    _fields = (
        'state_address',
        'state',
        'next_uint64',
        'next_uint32',
        'next_double',
        'bit_generator',
    )
    _field_defaults = {}
    __match_args__ = (
        'state_address',
        'state',
        'next_uint64',
        'next_uint32',
        'next_double',
        'bit_generator',
    )
    __slots__ = ()


# variables with complex values

__all__ = [
    'interface',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DED0AD5D90>'

__pyx_capi__ = {
    'LEGACY_POISSON_LAM_MAX': None, # (!) real value is '<capsule object "double" at 0x000001DED0AD8300>'
    'MAXSIZE': None, # (!) real value is '<capsule object "uint64_t" at 0x000001DED0AD8330>'
    'POISSON_LAM_MAX': None, # (!) real value is '<capsule object "double" at 0x000001DED0AD82D0>'
    'benchmark': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *, PyObject *, Py_ssize_t, PyObject *)" at 0x000001DED0AD8360>'
    'check_array_constraint': None, # (!) real value is '<capsule object "int (PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x000001DED0AD8450>'
    'check_constraint': None, # (!) real value is '<capsule object "int (double, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x000001DED0AD8420>'
    'cont': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, int, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *)" at 0x000001DED0AD85D0>'
    'cont_broadcast_3': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x000001DED0AD8660>'
    'cont_f': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *)" at 0x000001DED0AD8630>'
    'disc': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, int, int, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x000001DED0AD8600>'
    'discrete_broadcast_iii': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x000001DED0AD8690>'
    'double_fill': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x000001DED0AD84B0>'
    'float_fill': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x000001DED0AD84E0>'
    'float_fill_from_double': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x000001DED0AD8510>'
    'int_to_array': None, # (!) real value is '<capsule object "PyArrayObject *(PyObject *, PyObject *, PyObject *, PyObject *)" at 0x000001DED0AD8570>'
    'kahan_sum': None, # (!) real value is '<capsule object "double (double *, npy_intp)" at 0x000001DED0AD8480>'
    'prepare_cffi': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *)" at 0x000001DED0AD83C0>'
    'prepare_ctypes': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *)" at 0x000001DED0AD83F0>'
    'random_raw': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x000001DED0AD8390>'
    'validate_output_shape': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyArrayObject *)" at 0x000001DED0AD85A0>'
    'wrap_int': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x000001DED0AD8540>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='numpy.random._common', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DED0AD5D90>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\numpy\\\\random\\\\_common.cp311-win_amd64.pyd')"

__test__ = {}

