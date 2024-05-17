# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class TransparencyAttrib(RenderAttrib):
    """
    /**
     * This controls the enabling of transparency.  Simply setting an alpha
     * component to non-1 does not in itself make an object transparent; you must
     * also enable transparency mode with a suitable TransparencyAttrib.
     * Similarly, it is wasteful to render an object with a TransparencyAttrib in
     * effect unless you actually want it to be at least partially transparent
     * (and it has alpha components less than 1).
     */
    """
    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode(TransparencyAttrib self)
        
        /**
         * Returns the transparency mode.
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_mode(self, TransparencyAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(TransparencyAttrib self)
        
        /**
         * Returns the transparency mode.
         */
        """
        pass

    def make(self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(int mode)
        
        /**
         * Constructs a new TransparencyAttrib object.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 29
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MAlpha': 1,
        'MBinary': 5,
        'MDual': 6,
        'MMultisample': 3,
        'MMultisampleMask': 4,
        'MNone': 0,
        'MPremultipliedAlpha': 2,
        'M_alpha': 1,
        'M_binary': 5,
        'M_dual': 6,
        'M_multisample': 3,
        'M_multisample_mask': 4,
        'M_none': 0,
        'M_premultiplied_alpha': 2,
        '__doc__': '/**\n * This controls the enabling of transparency.  Simply setting an alpha\n * component to non-1 does not in itself make an object transparent; you must\n * also enable transparency mode with a suitable TransparencyAttrib.\n * Similarly, it is wasteful to render an object with a TransparencyAttrib in\n * effect unless you actually want it to be at least partially transparent\n * (and it has alpha components less than 1).\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TransparencyAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE292F90>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.TransparencyAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE292F90>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE292F90>)>'
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.TransparencyAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE292F90>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE292F90>)>'
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.TransparencyAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE292F90>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE292F90>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE292F90>)>'
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.TransparencyAttrib' objects>"
    }
    MAlpha = 1
    MBinary = 5
    MDual = 6
    MMultisample = 3
    MMultisampleMask = 4
    MNone = 0
    MPremultipliedAlpha = 2
    M_alpha = 1
    M_binary = 5
    M_dual = 6
    M_multisample = 3
    M_multisample_mask = 4
    M_none = 0
    M_premultiplied_alpha = 2


