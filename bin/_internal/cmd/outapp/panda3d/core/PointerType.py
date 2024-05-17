# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PointerType(__enum.Enum):
    # no doc
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initial start value or None
                count: the number of existing members
                last_values: the list of values assigned
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    eraser = None # (!) real value is '<PointerType.eraser: 4>'
    finger = None # (!) real value is '<PointerType.finger: 2>'
    mouse = None # (!) real value is '<PointerType.mouse: 1>'
    stylus = None # (!) real value is '<PointerType.stylus: 3>'
    unknown = None # (!) real value is '<PointerType.unknown: 0>'
    _member_map_ = {
        'eraser': None, # (!) real value is '<PointerType.eraser: 4>'
        'finger': None, # (!) real value is '<PointerType.finger: 2>'
        'mouse': None, # (!) real value is '<PointerType.mouse: 1>'
        'stylus': None, # (!) real value is '<PointerType.stylus: 3>'
        'unknown': None, # (!) real value is '<PointerType.unknown: 0>'
    }
    _member_names_ = [
        'unknown',
        'mouse',
        'finger',
        'stylus',
        'eraser',
    ]
    _member_type_ = object
    _unhashable_values_ = []
    _use_args_ = False
    _value2member_map_ = {
        0: None, # (!) real value is '<PointerType.unknown: 0>'
        1: None, # (!) real value is '<PointerType.mouse: 1>'
        2: None, # (!) real value is '<PointerType.finger: 2>'
        3: None, # (!) real value is '<PointerType.stylus: 3>'
        4: None, # (!) real value is '<PointerType.eraser: 4>'
    }
    _value_repr_ = None


