# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PNMTextGlyph(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A single glyph in a PNMTextMaker.
     */
    """
    def getAdvance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_advance(PNMTextGlyph self)
        
        /**
         * Returns the number of pixels by which the pen should be advanced after
         * rendering this glyph.
         */
        """
        pass

    def getBottom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bottom(PNMTextGlyph self)
        
        /**
         * Returns the y coordinate of the bottommost pixel in the glyph.
         */
        """
        pass

    def getHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_height(PNMTextGlyph self)
        
        /**
         * Returns the height of the glyph in pixels.
         */
        """
        pass

    def getInteriorFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_interior_flag(PNMTextGlyph self, int x, int y)
        
        /**
         * Returns true if the indicated pixel represents a pixel in the interior of a
         * hollow font, false otherwise.
         */
        """
        pass

    def getLeft(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_left(PNMTextGlyph self)
        
        /**
         * Returns the x coordinate of the leftmost pixel in the glyph.
         */
        """
        pass

    def getRight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right(PNMTextGlyph self)
        
        /**
         * Returns the x coordinate of the rightmost pixel in the glyph.
         */
        """
        pass

    def getTop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_top(PNMTextGlyph self)
        
        /**
         * Returns the y coordinate of the topmost pixel in the glyph.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(PNMTextGlyph self, int x, int y)
        
        /**
         * Returns the value of the indicated pixel of the glyph.  The result is in
         * the range [0, 1], where 0 indicates the pixel is not part of the glyph, and
         * 1 indicates it is.  Intermediate values are used to represent antialiasing.
         */
        """
        pass

    def getWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_width(PNMTextGlyph self)
        
        /**
         * Returns the width of the glyph in pixels.
         */
        """
        pass

    def get_advance(self, PNMTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_advance(PNMTextGlyph self)
        
        /**
         * Returns the number of pixels by which the pen should be advanced after
         * rendering this glyph.
         */
        """
        pass

    def get_bottom(self, PNMTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bottom(PNMTextGlyph self)
        
        /**
         * Returns the y coordinate of the bottommost pixel in the glyph.
         */
        """
        pass

    def get_height(self, PNMTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_height(PNMTextGlyph self)
        
        /**
         * Returns the height of the glyph in pixels.
         */
        """
        pass

    def get_interior_flag(self, PNMTextGlyph_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_interior_flag(PNMTextGlyph self, int x, int y)
        
        /**
         * Returns true if the indicated pixel represents a pixel in the interior of a
         * hollow font, false otherwise.
         */
        """
        pass

    def get_left(self, PNMTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_left(PNMTextGlyph self)
        
        /**
         * Returns the x coordinate of the leftmost pixel in the glyph.
         */
        """
        pass

    def get_right(self, PNMTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right(PNMTextGlyph self)
        
        /**
         * Returns the x coordinate of the rightmost pixel in the glyph.
         */
        """
        pass

    def get_top(self, PNMTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_top(PNMTextGlyph self)
        
        /**
         * Returns the y coordinate of the topmost pixel in the glyph.
         */
        """
        pass

    def get_value(self, PNMTextGlyph_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(PNMTextGlyph self, int x, int y)
        
        /**
         * Returns the value of the indicated pixel of the glyph.  The result is in
         * the range [0, 1], where 0 indicates the pixel is not part of the glyph, and
         * 1 indicates it is.  Intermediate values are used to represent antialiasing.
         */
        """
        pass

    def get_width(self, PNMTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_width(PNMTextGlyph self)
        
        /**
         * Returns the width of the glyph in pixels.
         */
        """
        pass

    def place(self, const_PNMTextGlyph_self, PNMImage_dest_image, int_xp, int_yp, const_LVecBase4f_fg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        place(const PNMTextGlyph self, PNMImage dest_image, int xp, int yp, const LVecBase4f fg)
        place(const PNMTextGlyph self, PNMImage dest_image, int xp, int yp, const LVecBase4f fg, const LVecBase4f interior)
        
        /**
         * Copies the glyph to the indicated destination image at the indicated
         * origin.  It colors the glyph pixels the indicated foreground color, blends
         * antialiased pixels with the appropriate amount of the foreground color and
         * the existing background color, and leaves other pixels alone.
         */
        
        /**
         * This flavor of place() also fills in the interior color.  This requires
         * that determine_interior was called earlier.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PNMTextGlyph' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PNMTextGlyph' objects>"
        '__doc__': '/**\n * A single glyph in a PNMTextMaker.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PNMTextGlyph' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE393BE0>'
        'getAdvance': None, # (!) real value is "<method 'getAdvance' of 'panda3d.core.PNMTextGlyph' objects>"
        'getBottom': None, # (!) real value is "<method 'getBottom' of 'panda3d.core.PNMTextGlyph' objects>"
        'getHeight': None, # (!) real value is "<method 'getHeight' of 'panda3d.core.PNMTextGlyph' objects>"
        'getInteriorFlag': None, # (!) real value is "<method 'getInteriorFlag' of 'panda3d.core.PNMTextGlyph' objects>"
        'getLeft': None, # (!) real value is "<method 'getLeft' of 'panda3d.core.PNMTextGlyph' objects>"
        'getRight': None, # (!) real value is "<method 'getRight' of 'panda3d.core.PNMTextGlyph' objects>"
        'getTop': None, # (!) real value is "<method 'getTop' of 'panda3d.core.PNMTextGlyph' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.core.PNMTextGlyph' objects>"
        'getWidth': None, # (!) real value is "<method 'getWidth' of 'panda3d.core.PNMTextGlyph' objects>"
        'get_advance': None, # (!) real value is "<method 'get_advance' of 'panda3d.core.PNMTextGlyph' objects>"
        'get_bottom': None, # (!) real value is "<method 'get_bottom' of 'panda3d.core.PNMTextGlyph' objects>"
        'get_height': None, # (!) real value is "<method 'get_height' of 'panda3d.core.PNMTextGlyph' objects>"
        'get_interior_flag': None, # (!) real value is "<method 'get_interior_flag' of 'panda3d.core.PNMTextGlyph' objects>"
        'get_left': None, # (!) real value is "<method 'get_left' of 'panda3d.core.PNMTextGlyph' objects>"
        'get_right': None, # (!) real value is "<method 'get_right' of 'panda3d.core.PNMTextGlyph' objects>"
        'get_top': None, # (!) real value is "<method 'get_top' of 'panda3d.core.PNMTextGlyph' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.core.PNMTextGlyph' objects>"
        'get_width': None, # (!) real value is "<method 'get_width' of 'panda3d.core.PNMTextGlyph' objects>"
        'place': None, # (!) real value is "<method 'place' of 'panda3d.core.PNMTextGlyph' objects>"
    }


