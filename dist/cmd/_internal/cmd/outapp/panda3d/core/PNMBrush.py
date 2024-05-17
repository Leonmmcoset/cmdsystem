# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class PNMBrush(ReferenceCount):
    """
    /**
     * This class is used to control the shape and color of the drawing operations
     * performed by a PNMPainter object.
     *
     * Normally, you don't create a PNMBrush directly; instead, use one of the
     * static PNMBrush::make_*() methods provided here.
     *
     * A PNMBrush is used to draw the border of a polygon or rectangle, as well as
     * for filling its interior.  When it is used to draw a border, the brush is
     * "smeared" over the border; when it is used to fill the interior, it is
     * tiled through the interior.
     */
    """
    def makeImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_image(const PNMImage image, float xc, float yc, int effect)
        
        /**
         * Returns a new brush that paints with the indicated image.  xc and yc
         * indicate the pixel in the center of the brush.
         *
         * The brush makes a copy of the image; it is safe to deallocate or modify the
         * image after making this call.
         */
        """
        pass

    def makePixel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_pixel(const LVecBase4f color, int effect)
        
        /**
         * Returns a new brush that paints a single pixel of the indicated color on a
         * border, or paints a solid color in an interior.
         */
        """
        pass

    def makeSpot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_spot(const LVecBase4f color, float radius, bool fuzzy, int effect)
        
        /**
         * Returns a new brush that paints a spot of the indicated color and radius.
         * If fuzzy is true, the spot is fuzzy; otherwise, it is hard-edged.
         */
        """
        pass

    def makeTransparent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_transparent()
        
        /**
         * Returns a new brush that does not paint anything.  Can be used as either a
         * pen or a fill brush to make borderless or unfilled shapes, respectively.
         */
        """
        pass

    def make_image(self, const_PNMImage_image, float_xc, float_yc, int_effect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_image(const PNMImage image, float xc, float yc, int effect)
        
        /**
         * Returns a new brush that paints with the indicated image.  xc and yc
         * indicate the pixel in the center of the brush.
         *
         * The brush makes a copy of the image; it is safe to deallocate or modify the
         * image after making this call.
         */
        """
        pass

    def make_pixel(self, const_LVecBase4f_color, int_effect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_pixel(const LVecBase4f color, int effect)
        
        /**
         * Returns a new brush that paints a single pixel of the indicated color on a
         * border, or paints a solid color in an interior.
         */
        """
        pass

    def make_spot(self, const_LVecBase4f_color, float_radius, bool_fuzzy, int_effect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_spot(const LVecBase4f color, float radius, bool fuzzy, int effect)
        
        /**
         * Returns a new brush that paints a spot of the indicated color and radius.
         * If fuzzy is true, the spot is fuzzy; otherwise, it is hard-edged.
         */
        """
        pass

    def make_transparent(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_transparent()
        
        /**
         * Returns a new brush that does not paint anything.  Can be used as either a
         * pen or a fill brush to make borderless or unfilled shapes, respectively.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    BEBlend = 1
    BEDarken = 2
    BELighten = 3
    BESet = 0
    BE_blend = 1
    BE_darken = 2
    BE_lighten = 3
    BE_set = 0
    DtoolClassDict = {
        'BEBlend': 1,
        'BEDarken': 2,
        'BELighten': 3,
        'BESet': 0,
        'BE_blend': 1,
        'BE_darken': 2,
        'BE_lighten': 3,
        'BE_set': 0,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This class is used to control the shape and color of the drawing operations\n * performed by a PNMPainter object.\n *\n * Normally, you don\'t create a PNMBrush directly; instead, use one of the\n * static PNMBrush::make_*() methods provided here.\n *\n * A PNMBrush is used to draw the border of a polygon or rectangle, as well as\n * for filling its interior.  When it is used to draw a border, the brush is\n * "smeared" over the border; when it is used to fill the interior, it is\n * tiled through the interior.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PNMBrush' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE356260>'
        'makeImage': None, # (!) real value is '<staticmethod(<built-in method makeImage of type object at 0x00007FFCFE356260>)>'
        'makePixel': None, # (!) real value is '<staticmethod(<built-in method makePixel of type object at 0x00007FFCFE356260>)>'
        'makeSpot': None, # (!) real value is '<staticmethod(<built-in method makeSpot of type object at 0x00007FFCFE356260>)>'
        'makeTransparent': None, # (!) real value is '<staticmethod(<built-in method makeTransparent of type object at 0x00007FFCFE356260>)>'
        'make_image': None, # (!) real value is '<staticmethod(<built-in method make_image of type object at 0x00007FFCFE356260>)>'
        'make_pixel': None, # (!) real value is '<staticmethod(<built-in method make_pixel of type object at 0x00007FFCFE356260>)>'
        'make_spot': None, # (!) real value is '<staticmethod(<built-in method make_spot of type object at 0x00007FFCFE356260>)>'
        'make_transparent': None, # (!) real value is '<staticmethod(<built-in method make_transparent of type object at 0x00007FFCFE356260>)>'
    }


