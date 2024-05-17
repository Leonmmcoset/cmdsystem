# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .MouseInterfaceNode import MouseInterfaceNode

class MouseSubregion(MouseInterfaceNode):
    """
    /**
     * The MouseSubregion object scales the mouse inputs from within a rectangular
     * region of the screen, as if they were the full-screen inputs.
     *
     * If you choose your MouseSubregion coordinates to exactly match a
     * DisplayRegion within your window, you end up with a virtual mouse within
     * your DisplayRegion.
     */
    """
    def getBottom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bottom(MouseSubregion self)
        
        /**
         * Retrieves the y coordinate of the bottom edge of the rectangle within the
         * window.  This number will be in the range [0..1].
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getLeft(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_left(MouseSubregion self)
        
        /**
         * Retrieves the x coordinate of the left edge of the rectangle within the
         * window.  This number will be in the range [0..1].
         */
        """
        pass

    def getRight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right(MouseSubregion self)
        
        /**
         * Retrieves the x coordinate of the right edge of the rectangle within the
         * window.  This number will be in the range [0..1].
         */
        """
        pass

    def getTop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_top(MouseSubregion self)
        
        /**
         * Retrieves the y coordinate of the top edge of the rectangle within the
         * window.  This number will be in the range [0..1].
         */
        """
        pass

    def get_bottom(self, MouseSubregion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bottom(MouseSubregion self)
        
        /**
         * Retrieves the y coordinate of the bottom edge of the rectangle within the
         * window.  This number will be in the range [0..1].
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_left(self, MouseSubregion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_left(MouseSubregion self)
        
        /**
         * Retrieves the x coordinate of the left edge of the rectangle within the
         * window.  This number will be in the range [0..1].
         */
        """
        pass

    def get_right(self, MouseSubregion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right(MouseSubregion self)
        
        /**
         * Retrieves the x coordinate of the right edge of the rectangle within the
         * window.  This number will be in the range [0..1].
         */
        """
        pass

    def get_top(self, MouseSubregion_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_top(MouseSubregion self)
        
        /**
         * Retrieves the y coordinate of the top edge of the rectangle within the
         * window.  This number will be in the range [0..1].
         */
        """
        pass

    def setDimensions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_dimensions(const MouseSubregion self, float l, float r, float b, float t)
        
        /**
         * Changes the region of the window in which the mouse is considered to be
         * active.  The parameters are identical to those for a DisplayRegion: they
         * range from 0 to 1, where 0,0 is the lower left corner and 1,1 is the upper
         * right; (0, 1, 0, 1) represents the whole window.
         */
        """
        pass

    def set_dimensions(self, const_MouseSubregion_self, float_l, float_r, float_b, float_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_dimensions(const MouseSubregion self, float l, float r, float b, float t)
        
        /**
         * Changes the region of the window in which the mouse is considered to be
         * active.  The parameters are identical to those for a DisplayRegion: they
         * range from 0 to 1, where 0,0 is the lower left corner and 1,1 is the upper
         * right; (0, 1, 0, 1) represents the whole window.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MouseSubregion' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MouseSubregion' objects>"
        '__doc__': '/**\n * The MouseSubregion object scales the mouse inputs from within a rectangular\n * region of the screen, as if they were the full-screen inputs.\n *\n * If you choose your MouseSubregion coordinates to exactly match a\n * DisplayRegion within your window, you end up with a virtual mouse within\n * your DisplayRegion.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MouseSubregion' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE366470>'
        'getBottom': None, # (!) real value is "<method 'getBottom' of 'panda3d.core.MouseSubregion' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE366470>)>'
        'getLeft': None, # (!) real value is "<method 'getLeft' of 'panda3d.core.MouseSubregion' objects>"
        'getRight': None, # (!) real value is "<method 'getRight' of 'panda3d.core.MouseSubregion' objects>"
        'getTop': None, # (!) real value is "<method 'getTop' of 'panda3d.core.MouseSubregion' objects>"
        'get_bottom': None, # (!) real value is "<method 'get_bottom' of 'panda3d.core.MouseSubregion' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE366470>)>'
        'get_left': None, # (!) real value is "<method 'get_left' of 'panda3d.core.MouseSubregion' objects>"
        'get_right': None, # (!) real value is "<method 'get_right' of 'panda3d.core.MouseSubregion' objects>"
        'get_top': None, # (!) real value is "<method 'get_top' of 'panda3d.core.MouseSubregion' objects>"
        'setDimensions': None, # (!) real value is "<method 'setDimensions' of 'panda3d.core.MouseSubregion' objects>"
        'set_dimensions': None, # (!) real value is "<method 'set_dimensions' of 'panda3d.core.MouseSubregion' objects>"
    }


