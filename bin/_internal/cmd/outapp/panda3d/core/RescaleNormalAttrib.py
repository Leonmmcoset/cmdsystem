# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class RescaleNormalAttrib(RenderAttrib):
    """
    /**
     * Specifies how polygons are to be drawn.
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
        get_mode(RescaleNormalAttrib self)
        
        /**
         * Returns the render mode.
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

    def get_mode(self, RescaleNormalAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(RescaleNormalAttrib self)
        
        /**
         * Returns the render mode.
         */
        """
        pass

    def make(self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(int mode)
        
        /**
         * Constructs a new RescaleNormalAttrib object that specifies whether to
         * rescale normals to compensate for transform scales or incorrectly defined
         * normals.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Constructs a RescaleNormalAttrib object that's suitable for putting at the
         * top of a scene graph.  This will contain whatever attrib was suggested by
         * the user's rescale-normals Config variable.
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Constructs a RescaleNormalAttrib object that's suitable for putting at the
         * top of a scene graph.  This will contain whatever attrib was suggested by
         * the user's rescale-normals Config variable.
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


    class_slot = 21
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MAuto': 3,
        'MNone': 0,
        'MNormalize': 2,
        'MRescale': 1,
        'M_auto': 3,
        'M_none': 0,
        'M_normalize': 2,
        'M_rescale': 1,
        '__doc__': '/**\n * Specifies how polygons are to be drawn.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RescaleNormalAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2970D0>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.RescaleNormalAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE2970D0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2970D0>)>'
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.RescaleNormalAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE2970D0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2970D0>)>'
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.RescaleNormalAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2970D0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE2970D0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE2970D0>)>'
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.RescaleNormalAttrib' objects>"
    }
    MAuto = 3
    MNone = 0
    MNormalize = 2
    MRescale = 1
    M_auto = 3
    M_none = 0
    M_normalize = 2
    M_rescale = 1


