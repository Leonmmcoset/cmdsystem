# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TextGlyph import TextGlyph

class DynamicTextGlyph(TextGlyph):
    """
    /**
     * A specialization on TextGlyph that is generated and stored by a
     * DynamicTextFont.  This keeps some additional information, such as where the
     * glyph appears on a texture map.
     */
    """
    def getBottom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bottom(DynamicTextGlyph self)
        
        /**
         * Returns the vertex coordinates that can be used when creating a custom text
         * renderer.
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
        get_left(DynamicTextGlyph self)
        
        /**
         * Returns the vertex coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def getPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page(DynamicTextGlyph self)
        
        /**
         * Returns the DynamicTextPage that this glyph is on.
         */
        """
        pass

    def getRight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right(DynamicTextGlyph self)
        
        /**
         * Returns the vertex coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def getTop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_top(DynamicTextGlyph self)
        
        /**
         * Returns the vertex coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def getUvBottom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv_bottom(DynamicTextGlyph self)
        
        /**
         * Returns the UV coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def getUvLeft(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv_left(DynamicTextGlyph self)
        
        /**
         * Returns the UV coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def getUvRight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv_right(DynamicTextGlyph self)
        
        /**
         * Returns the UV coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def getUvTop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv_top(DynamicTextGlyph self)
        
        /**
         * Returns the UV coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def get_bottom(self, DynamicTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bottom(DynamicTextGlyph self)
        
        /**
         * Returns the vertex coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_left(self, DynamicTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_left(DynamicTextGlyph self)
        
        /**
         * Returns the vertex coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def get_page(self, DynamicTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page(DynamicTextGlyph self)
        
        /**
         * Returns the DynamicTextPage that this glyph is on.
         */
        """
        pass

    def get_right(self, DynamicTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right(DynamicTextGlyph self)
        
        /**
         * Returns the vertex coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def get_top(self, DynamicTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_top(DynamicTextGlyph self)
        
        /**
         * Returns the vertex coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def get_uv_bottom(self, DynamicTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv_bottom(DynamicTextGlyph self)
        
        /**
         * Returns the UV coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def get_uv_left(self, DynamicTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv_left(DynamicTextGlyph self)
        
        /**
         * Returns the UV coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def get_uv_right(self, DynamicTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv_right(DynamicTextGlyph self)
        
        /**
         * Returns the UV coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def get_uv_top(self, DynamicTextGlyph_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv_top(DynamicTextGlyph self)
        
        /**
         * Returns the UV coordinates that can be used when creating a custom text
         * renderer.
         */
        """
        pass

    def intersects(self, DynamicTextGlyph_self, int_x, int_y, int_x_size, int_y_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        intersects(DynamicTextGlyph self, int x, int y, int x_size, int y_size)
        
        /**
         * Returns true if the particular position this glyph has been assigned to
         * overlaps the rectangle whose top left corner is at x, y and whose size is
         * given by x_size, y_size, or false otherwise.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A specialization on TextGlyph that is generated and stored by a\n * DynamicTextFont.  This keeps some additional information, such as where the\n * glyph appears on a texture map.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DynamicTextGlyph' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE35E1B0>'
        'getBottom': None, # (!) real value is "<method 'getBottom' of 'panda3d.core.DynamicTextGlyph' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE35E1B0>)>'
        'getLeft': None, # (!) real value is "<method 'getLeft' of 'panda3d.core.DynamicTextGlyph' objects>"
        'getPage': None, # (!) real value is "<method 'getPage' of 'panda3d.core.DynamicTextGlyph' objects>"
        'getRight': None, # (!) real value is "<method 'getRight' of 'panda3d.core.DynamicTextGlyph' objects>"
        'getTop': None, # (!) real value is "<method 'getTop' of 'panda3d.core.DynamicTextGlyph' objects>"
        'getUvBottom': None, # (!) real value is "<method 'getUvBottom' of 'panda3d.core.DynamicTextGlyph' objects>"
        'getUvLeft': None, # (!) real value is "<method 'getUvLeft' of 'panda3d.core.DynamicTextGlyph' objects>"
        'getUvRight': None, # (!) real value is "<method 'getUvRight' of 'panda3d.core.DynamicTextGlyph' objects>"
        'getUvTop': None, # (!) real value is "<method 'getUvTop' of 'panda3d.core.DynamicTextGlyph' objects>"
        'get_bottom': None, # (!) real value is "<method 'get_bottom' of 'panda3d.core.DynamicTextGlyph' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE35E1B0>)>'
        'get_left': None, # (!) real value is "<method 'get_left' of 'panda3d.core.DynamicTextGlyph' objects>"
        'get_page': None, # (!) real value is "<method 'get_page' of 'panda3d.core.DynamicTextGlyph' objects>"
        'get_right': None, # (!) real value is "<method 'get_right' of 'panda3d.core.DynamicTextGlyph' objects>"
        'get_top': None, # (!) real value is "<method 'get_top' of 'panda3d.core.DynamicTextGlyph' objects>"
        'get_uv_bottom': None, # (!) real value is "<method 'get_uv_bottom' of 'panda3d.core.DynamicTextGlyph' objects>"
        'get_uv_left': None, # (!) real value is "<method 'get_uv_left' of 'panda3d.core.DynamicTextGlyph' objects>"
        'get_uv_right': None, # (!) real value is "<method 'get_uv_right' of 'panda3d.core.DynamicTextGlyph' objects>"
        'get_uv_top': None, # (!) real value is "<method 'get_uv_top' of 'panda3d.core.DynamicTextGlyph' objects>"
        'intersects': None, # (!) real value is "<method 'intersects' of 'panda3d.core.DynamicTextGlyph' objects>"
        'page': None, # (!) real value is "<attribute 'page' of 'panda3d.core.DynamicTextGlyph' objects>"
    }


