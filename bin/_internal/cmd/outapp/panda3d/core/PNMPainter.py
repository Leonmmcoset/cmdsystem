# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PNMPainter(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class provides a number of convenient methods for painting drawings
     * directly into a PNMImage.
     *
     * It stores a pointer to the PNMImage you pass it, but it does not take
     * ownership of the object; you are responsible for ensuring that the PNMImage
     * does not destruct during the lifetime of the PNMPainter object.
     */
    """
    def drawLine(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        draw_line(const PNMPainter self, float xa, float ya, float xb, float yb)
        
        /**
         * Draws an antialiased line on the PNMImage, using the current pen.
         */
        """
        pass

    def drawPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        draw_point(const PNMPainter self, float x, float y)
        
        /**
         * Draws an antialiased point on the PNMImage, using the current pen.
         */
        """
        pass

    def drawRectangle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        draw_rectangle(const PNMPainter self, float xa, float ya, float xb, float yb)
        
        /**
         * Draws a filled rectangule on the PNMImage, using the current pen for the
         * outline, and the current fill brush for the interior.
         *
         * The two coordinates specify any two diagonally opposite corners.
         */
        """
        pass

    def draw_line(self, const_PNMPainter_self, float_xa, float_ya, float_xb, float_yb): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        draw_line(const PNMPainter self, float xa, float ya, float xb, float yb)
        
        /**
         * Draws an antialiased line on the PNMImage, using the current pen.
         */
        """
        pass

    def draw_point(self, const_PNMPainter_self, float_x, float_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        draw_point(const PNMPainter self, float x, float y)
        
        /**
         * Draws an antialiased point on the PNMImage, using the current pen.
         */
        """
        pass

    def draw_rectangle(self, const_PNMPainter_self, float_xa, float_ya, float_xb, float_yb): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        draw_rectangle(const PNMPainter self, float xa, float ya, float xb, float yb)
        
        /**
         * Draws a filled rectangule on the PNMImage, using the current pen for the
         * outline, and the current fill brush for the interior.
         *
         * The two coordinates specify any two diagonally opposite corners.
         */
        """
        pass

    def getFill(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fill(PNMPainter self)
        
        /**
         * Returns the current fill brush.  See set_fill().
         */
        """
        pass

    def getPen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pen(PNMPainter self)
        
        /**
         * Returns the current pen.  See set_pen().
         */
        """
        pass

    def get_fill(self, PNMPainter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fill(PNMPainter self)
        
        /**
         * Returns the current fill brush.  See set_fill().
         */
        """
        pass

    def get_pen(self, PNMPainter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pen(PNMPainter self)
        
        /**
         * Returns the current pen.  See set_pen().
         */
        """
        pass

    def setFill(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fill(const PNMPainter self, PNMBrush fill)
        
        /**
         * Specifies a PNMBrush that will be used for filling in the interiors of
         * objects.  If the brush is a bitmap brush, its image will be tiled
         * throughout the space.
         *
         * Unlike the PNMImage passed to the constructor, the PNMPainter will take
         * ownership of the fill brush.  It is not necessary to keep a separate
         * pointer to it.
         */
        """
        pass

    def setPen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pen(const PNMPainter self, PNMBrush pen)
        
        /**
         * Specifies a PNMBrush that will be used for drawing lines and edges.  If the
         * brush is a bitmap brush, its image will be smeared pixelwise along the
         * line.
         *
         * Unlike the PNMImage passed to the constructor, the PNMPainter will take
         * ownership of the pen.  It is not necessary to keep a separate pointer to
         * it.
         */
        """
        pass

    def set_fill(self, const_PNMPainter_self, PNMBrush_fill): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fill(const PNMPainter self, PNMBrush fill)
        
        /**
         * Specifies a PNMBrush that will be used for filling in the interiors of
         * objects.  If the brush is a bitmap brush, its image will be tiled
         * throughout the space.
         *
         * Unlike the PNMImage passed to the constructor, the PNMPainter will take
         * ownership of the fill brush.  It is not necessary to keep a separate
         * pointer to it.
         */
        """
        pass

    def set_pen(self, const_PNMPainter_self, PNMBrush_pen): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pen(const PNMPainter self, PNMBrush pen)
        
        /**
         * Specifies a PNMBrush that will be used for drawing lines and edges.  If the
         * brush is a bitmap brush, its image will be smeared pixelwise along the
         * line.
         *
         * Unlike the PNMImage passed to the constructor, the PNMPainter will take
         * ownership of the pen.  It is not necessary to keep a separate pointer to
         * it.
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

    fill = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PNMPainter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PNMPainter' objects>"
        '__doc__': '/**\n * This class provides a number of convenient methods for painting drawings\n * directly into a PNMImage.\n *\n * It stores a pointer to the PNMImage you pass it, but it does not take\n * ownership of the object; you are responsible for ensuring that the PNMImage\n * does not destruct during the lifetime of the PNMPainter object.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PNMPainter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3569A0>'
        'drawLine': None, # (!) real value is "<method 'drawLine' of 'panda3d.core.PNMPainter' objects>"
        'drawPoint': None, # (!) real value is "<method 'drawPoint' of 'panda3d.core.PNMPainter' objects>"
        'drawRectangle': None, # (!) real value is "<method 'drawRectangle' of 'panda3d.core.PNMPainter' objects>"
        'draw_line': None, # (!) real value is "<method 'draw_line' of 'panda3d.core.PNMPainter' objects>"
        'draw_point': None, # (!) real value is "<method 'draw_point' of 'panda3d.core.PNMPainter' objects>"
        'draw_rectangle': None, # (!) real value is "<method 'draw_rectangle' of 'panda3d.core.PNMPainter' objects>"
        'fill': None, # (!) real value is "<attribute 'fill' of 'panda3d.core.PNMPainter' objects>"
        'getFill': None, # (!) real value is "<method 'getFill' of 'panda3d.core.PNMPainter' objects>"
        'getPen': None, # (!) real value is "<method 'getPen' of 'panda3d.core.PNMPainter' objects>"
        'get_fill': None, # (!) real value is "<method 'get_fill' of 'panda3d.core.PNMPainter' objects>"
        'get_pen': None, # (!) real value is "<method 'get_pen' of 'panda3d.core.PNMPainter' objects>"
        'pen': None, # (!) real value is "<attribute 'pen' of 'panda3d.core.PNMPainter' objects>"
        'setFill': None, # (!) real value is "<method 'setFill' of 'panda3d.core.PNMPainter' objects>"
        'setPen': None, # (!) real value is "<method 'setPen' of 'panda3d.core.PNMPainter' objects>"
        'set_fill': None, # (!) real value is "<method 'set_fill' of 'panda3d.core.PNMPainter' objects>"
        'set_pen': None, # (!) real value is "<method 'set_pen' of 'panda3d.core.PNMPainter' objects>"
    }


