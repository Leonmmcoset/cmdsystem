# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class CullBinAttrib(RenderAttrib):
    """
    /**
     * Assigns geometry to a particular bin by name.  The bins must be created
     * separately via the CullBinManager interface.
     */
    """
    def getBinName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bin_name(CullBinAttrib self)
        
        /**
         * Returns the name of the bin this attribute specifies.  If this is the empty
         * string, it refers to the default bin.
         */
        """
        pass

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

    def getDrawOrder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_draw_order(CullBinAttrib self)
        
        /**
         * Returns the draw order this attribute specifies.  Some bins (in particular,
         * CullBinFixed bins) use this to further specify the order in which objects
         * should be rendered.
         */
        """
        pass

    def get_bin_name(self, CullBinAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bin_name(CullBinAttrib self)
        
        /**
         * Returns the name of the bin this attribute specifies.  If this is the empty
         * string, it refers to the default bin.
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

    def get_draw_order(self, CullBinAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_draw_order(CullBinAttrib self)
        
        /**
         * Returns the draw order this attribute specifies.  Some bins (in particular,
         * CullBinFixed bins) use this to further specify the order in which objects
         * should be rendered.
         */
        """
        pass

    def make(self, str_bin_name, int_draw_order): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(str bin_name, int draw_order)
        
        /**
         * Constructs a new CullBinAttrib assigning geometry into the named bin.  If
         * the bin name is the empty string, the default bin is used.
         *
         * The draw_order specifies further ordering information which is relevant
         * only to certain kinds of bins (in particular CullBinFixed type bins).
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

    bin_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 11
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * Assigns geometry to a particular bin by name.  The bins must be created\n * separately via the CullBinManager interface.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CullBinAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE295EB0>'
        'bin_name': None, # (!) real value is "<attribute 'bin_name' of 'panda3d.core.CullBinAttrib' objects>"
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.CullBinAttrib'>"
        'draw_order': None, # (!) real value is "<attribute 'draw_order' of 'panda3d.core.CullBinAttrib' objects>"
        'getBinName': None, # (!) real value is "<method 'getBinName' of 'panda3d.core.CullBinAttrib' objects>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE295EB0>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE295EB0>)>'
        'getDrawOrder': None, # (!) real value is "<method 'getDrawOrder' of 'panda3d.core.CullBinAttrib' objects>"
        'get_bin_name': None, # (!) real value is "<method 'get_bin_name' of 'panda3d.core.CullBinAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE295EB0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE295EB0>)>'
        'get_draw_order': None, # (!) real value is "<method 'get_draw_order' of 'panda3d.core.CullBinAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE295EB0>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE295EB0>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE295EB0>)>'
    }


