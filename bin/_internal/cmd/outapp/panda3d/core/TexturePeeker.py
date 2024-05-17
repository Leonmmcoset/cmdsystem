# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class TexturePeeker(ReferenceCount):
    """
    /**
     * An instance of this object is returned by Texture::peek().  This object
     * allows quick and easy inspection of a texture's texels by (u, v)
     * coordinates.
     */
    """
    def fetchPixel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        fetch_pixel(TexturePeeker self, LVecBase4f color, int x, int y)
        fetch_pixel(TexturePeeker self, LVecBase4f color, int x, int y, int z)
        
        /**
         * Works like TexturePeeker::lookup(), but instead of uv-coordinates, integer
         * coordinates are used.
         */
        
        /**
         * Works like TexturePeeker::lookup(), but instead of uv-coordinates, integer
         * coordinates are used.
         */
        """
        pass

    def fetch_pixel(self, TexturePeeker_self, LVecBase4f_color, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fetch_pixel(TexturePeeker self, LVecBase4f color, int x, int y)
        fetch_pixel(TexturePeeker self, LVecBase4f color, int x, int y, int z)
        
        /**
         * Works like TexturePeeker::lookup(), but instead of uv-coordinates, integer
         * coordinates are used.
         */
        
        /**
         * Works like TexturePeeker::lookup(), but instead of uv-coordinates, integer
         * coordinates are used.
         */
        """
        pass

    def filterRect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        filter_rect(TexturePeeker self, LVecBase4f color, float min_u, float min_v, float max_u, float max_v)
        filter_rect(TexturePeeker self, LVecBase4f color, float min_u, float min_v, float min_w, float max_u, float max_v, float max_w)
        
        /**
         * Fills "color" with the average RGBA color of the texels within the
         * rectangle defined by the specified coordinate range.
         *
         * The texel color is linearly filtered over the entire region.  u, v, and w
         * must be in the range [0, 1].
         */
        
        /**
         * Fills "color" with the average RGBA color of the texels within the
         * rectangle defined by the specified coordinate range.
         *
         * The texel color is linearly filtered over the entire region.  u, v, and w
         * must be in the range [0, 1].
         */
        """
        pass

    def filter_rect(self, TexturePeeker_self, LVecBase4f_color, float_min_u, float_min_v, float_max_u, float_max_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        filter_rect(TexturePeeker self, LVecBase4f color, float min_u, float min_v, float max_u, float max_v)
        filter_rect(TexturePeeker self, LVecBase4f color, float min_u, float min_v, float min_w, float max_u, float max_v, float max_w)
        
        /**
         * Fills "color" with the average RGBA color of the texels within the
         * rectangle defined by the specified coordinate range.
         *
         * The texel color is linearly filtered over the entire region.  u, v, and w
         * must be in the range [0, 1].
         */
        
        /**
         * Fills "color" with the average RGBA color of the texels within the
         * rectangle defined by the specified coordinate range.
         *
         * The texel color is linearly filtered over the entire region.  u, v, and w
         * must be in the range [0, 1].
         */
        """
        pass

    def getXSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x_size(TexturePeeker self)
        
        /**
         * Returns the width of the texture image that is contributing to the
         * TexturePeeker's information.  This may be either the Texture's full width,
         * or its simple ram image's width.
         */
        """
        pass

    def getYSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y_size(TexturePeeker self)
        
        /**
         * Returns the height of the texture image that is contributing to the
         * TexturePeeker's information.  This may be either the Texture's full height,
         * or its simple ram image's height.
         */
        """
        pass

    def getZSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_z_size(TexturePeeker self)
        
        /**
         * Returns the depth of the texture image that is contributing to the
         * TexturePeeker's information.
         */
        """
        pass

    def get_x_size(self, TexturePeeker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x_size(TexturePeeker self)
        
        /**
         * Returns the width of the texture image that is contributing to the
         * TexturePeeker's information.  This may be either the Texture's full width,
         * or its simple ram image's width.
         */
        """
        pass

    def get_y_size(self, TexturePeeker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y_size(TexturePeeker self)
        
        /**
         * Returns the height of the texture image that is contributing to the
         * TexturePeeker's information.  This may be either the Texture's full height,
         * or its simple ram image's height.
         */
        """
        pass

    def get_z_size(self, TexturePeeker_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_z_size(TexturePeeker self)
        
        /**
         * Returns the depth of the texture image that is contributing to the
         * TexturePeeker's information.
         */
        """
        pass

    def hasPixel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_pixel(TexturePeeker self, int x, int y)
        has_pixel(TexturePeeker self, int x, int y, int z)
        
        /**
         * Returns whether a given coordinate is inside of the texture dimensions.
         */
        
        /**
         * Returns whether a given coordinate is inside of the texture dimensions.
         */
        """
        pass

    def has_pixel(self, TexturePeeker_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_pixel(TexturePeeker self, int x, int y)
        has_pixel(TexturePeeker self, int x, int y, int z)
        
        /**
         * Returns whether a given coordinate is inside of the texture dimensions.
         */
        
        /**
         * Returns whether a given coordinate is inside of the texture dimensions.
         */
        """
        pass

    def lookup(self, TexturePeeker_self, LVecBase4f_color, float_u, float_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lookup(TexturePeeker self, LVecBase4f color, float u, float v)
        lookup(TexturePeeker self, LVecBase4f color, float u, float v, float w)
        
        /**
         * Fills "color" with the RGBA color of the texel at point (u, v).
         *
         * The texel color is determined via nearest-point sampling (no filtering of
         * adjacent pixels), regardless of the filter type associated with the
         * texture.  u, v, and w will wrap around regardless of the texture's wrap
         * mode.
         */
        
        /**
         * Fills "color" with the RGBA color of the texel at point (u, v, w).
         *
         * The texel color is determined via nearest-point sampling (no filtering of
         * adjacent pixels), regardless of the filter type associated with the
         * texture.  u, v, and w will wrap around regardless of the texture's wrap
         * mode.
         */
        """
        pass

    def lookupBilinear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        lookup_bilinear(TexturePeeker self, LVecBase4f color, float u, float v)
        
        /**
         * Performs a bilinear lookup to retrieve the color value stored at the uv
         * coordinate (u, v).
         *
         * In case the point is outside of the uv range, color is set to zero,
         * and false is returned.  Otherwise true is returned.
         */
        """
        pass

    def lookup_bilinear(self, TexturePeeker_self, LVecBase4f_color, float_u, float_v): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lookup_bilinear(TexturePeeker self, LVecBase4f color, float u, float v)
        
        /**
         * Performs a bilinear lookup to retrieve the color value stored at the uv
         * coordinate (u, v).
         *
         * In case the point is outside of the uv range, color is set to zero,
         * and false is returned.  Otherwise true is returned.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TexturePeeker' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TexturePeeker' objects>"
        '__doc__': "/**\n * An instance of this object is returned by Texture::peek().  This object\n * allows quick and easy inspection of a texture's texels by (u, v)\n * coordinates.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TexturePeeker' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE301520>'
        'fetchPixel': None, # (!) real value is "<method 'fetchPixel' of 'panda3d.core.TexturePeeker' objects>"
        'fetch_pixel': None, # (!) real value is "<method 'fetch_pixel' of 'panda3d.core.TexturePeeker' objects>"
        'filterRect': None, # (!) real value is "<method 'filterRect' of 'panda3d.core.TexturePeeker' objects>"
        'filter_rect': None, # (!) real value is "<method 'filter_rect' of 'panda3d.core.TexturePeeker' objects>"
        'getXSize': None, # (!) real value is "<method 'getXSize' of 'panda3d.core.TexturePeeker' objects>"
        'getYSize': None, # (!) real value is "<method 'getYSize' of 'panda3d.core.TexturePeeker' objects>"
        'getZSize': None, # (!) real value is "<method 'getZSize' of 'panda3d.core.TexturePeeker' objects>"
        'get_x_size': None, # (!) real value is "<method 'get_x_size' of 'panda3d.core.TexturePeeker' objects>"
        'get_y_size': None, # (!) real value is "<method 'get_y_size' of 'panda3d.core.TexturePeeker' objects>"
        'get_z_size': None, # (!) real value is "<method 'get_z_size' of 'panda3d.core.TexturePeeker' objects>"
        'hasPixel': None, # (!) real value is "<method 'hasPixel' of 'panda3d.core.TexturePeeker' objects>"
        'has_pixel': None, # (!) real value is "<method 'has_pixel' of 'panda3d.core.TexturePeeker' objects>"
        'lookup': None, # (!) real value is "<method 'lookup' of 'panda3d.core.TexturePeeker' objects>"
        'lookupBilinear': None, # (!) real value is "<method 'lookupBilinear' of 'panda3d.core.TexturePeeker' objects>"
        'lookup_bilinear': None, # (!) real value is "<method 'lookup_bilinear' of 'panda3d.core.TexturePeeker' objects>"
    }


