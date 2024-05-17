# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class InputDeviceSet(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Manages a list of InputDevice objects, as returned by various
     * InputDeviceManager methods.  This is implemented like a set, meaning the
     * same device cannot occur more than once.
     */
    """
    def assign(self, const_InputDeviceSet_self, const_InputDeviceSet_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const InputDeviceSet self, const InputDeviceSet copy)
        """
        pass

    def clear(self, const_InputDeviceSet_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const InputDeviceSet self)
        
        /**
         * Removes all InputDevices from the collection.
         */
        """
        pass

    def output(self, InputDeviceSet_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(InputDeviceSet self, ostream out)
        
        /**
         * Writes a brief one-line description of the InputDeviceSet to the indicated
         * output stream.
         */
        """
        pass

    def reserve(self, const_InputDeviceSet_self, int_num): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reserve(const InputDeviceSet self, int num)
        
        /**
         * This is a hint to Panda to allocate enough memory to hold the given number
         * of InputDevices, if you know ahead of time how many you will be adding.
         */
        """
        pass

    def write(self, InputDeviceSet_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(InputDeviceSet self, ostream out, int indent_level)
        
        /**
         * Writes a complete multi-line description of the InputDeviceSet to the
         * indicated output stream.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.InputDeviceSet' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.InputDeviceSet' objects>"
        '__doc__': '/**\n * Manages a list of InputDevice objects, as returned by various\n * InputDeviceManager methods.  This is implemented like a set, meaning the\n * same device cannot occur more than once.\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.InputDeviceSet' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.InputDeviceSet' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.InputDeviceSet' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D6F80>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.InputDeviceSet' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.InputDeviceSet' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.InputDeviceSet' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.InputDeviceSet' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.InputDeviceSet' objects>"
        'reserve': None, # (!) real value is "<method 'reserve' of 'panda3d.core.InputDeviceSet' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.InputDeviceSet' objects>"
    }


