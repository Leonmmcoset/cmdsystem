# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PGFrameStyle(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     *
     */
    """
    def assign(self, const_PGFrameStyle_self, const_PGFrameStyle_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PGFrameStyle self, const PGFrameStyle copy)
        """
        pass

    def clearTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_texture(const PGFrameStyle self)
        
        /**
         * Removes the texture from the frame.
         */
        """
        pass

    def clear_texture(self, const_PGFrameStyle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_texture(const PGFrameStyle self)
        
        /**
         * Removes the texture from the frame.
         */
        """
        pass

    def getColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color(PGFrameStyle self)
        
        /**
         * Returns the dominant color of the frame.
         */
        """
        pass

    def getInternalFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_internal_frame(PGFrameStyle self, const LVecBase4f frame)
        
        /**
         * Computes the size of the internal frame, given the indicated external
         * frame, appropriate for this kind of frame style.  This simply subtracts the
         * border width for those frame styles that include a border.
         */
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(PGFrameStyle self)
        
        /**
         * Returns the texture that has been applied to the frame, or NULL if no
         * texture has been applied.
         */
        """
        pass

    def getType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_type(PGFrameStyle self)
        
        /**
         * Returns the basic type of frame.
         */
        """
        pass

    def getUvWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_uv_width(PGFrameStyle self)
        
        /**
         * See set_uv_width().
         */
        """
        pass

    def getVisibleScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_visible_scale(PGFrameStyle self)
        
        /**
         * Returns the scale factor on the visible representation of the frame, in the
         * X and Y directions.  If this scale factor is other than 1, it will affect
         * the size of the visible frame representation within the actual frame
         * border.
         */
        """
        pass

    def getWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_width(PGFrameStyle self)
        
        /**
         * Returns the width parameter, which has meaning only for certain frame
         * types.  For instance, this is the width of the bevel for T_bevel_in or
         * T_bevel_out.  The units are in screen units.
         */
        """
        pass

    def get_color(self, PGFrameStyle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(PGFrameStyle self)
        
        /**
         * Returns the dominant color of the frame.
         */
        """
        pass

    def get_internal_frame(self, PGFrameStyle_self, const_LVecBase4f_frame): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_internal_frame(PGFrameStyle self, const LVecBase4f frame)
        
        /**
         * Computes the size of the internal frame, given the indicated external
         * frame, appropriate for this kind of frame style.  This simply subtracts the
         * border width for those frame styles that include a border.
         */
        """
        pass

    def get_texture(self, PGFrameStyle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(PGFrameStyle self)
        
        /**
         * Returns the texture that has been applied to the frame, or NULL if no
         * texture has been applied.
         */
        """
        pass

    def get_type(self, PGFrameStyle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_type(PGFrameStyle self)
        
        /**
         * Returns the basic type of frame.
         */
        """
        pass

    def get_uv_width(self, PGFrameStyle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_uv_width(PGFrameStyle self)
        
        /**
         * See set_uv_width().
         */
        """
        pass

    def get_visible_scale(self, PGFrameStyle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_visible_scale(PGFrameStyle self)
        
        /**
         * Returns the scale factor on the visible representation of the frame, in the
         * X and Y directions.  If this scale factor is other than 1, it will affect
         * the size of the visible frame representation within the actual frame
         * border.
         */
        """
        pass

    def get_width(self, PGFrameStyle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_width(PGFrameStyle self)
        
        /**
         * Returns the width parameter, which has meaning only for certain frame
         * types.  For instance, this is the width of the bevel for T_bevel_in or
         * T_bevel_out.  The units are in screen units.
         */
        """
        pass

    def hasTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_texture(PGFrameStyle self)
        
        /**
         * Returns true if a texture has been applied to the frame.
         */
        """
        pass

    def has_texture(self, PGFrameStyle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_texture(PGFrameStyle self)
        
        /**
         * Returns true if a texture has been applied to the frame.
         */
        """
        pass

    def output(self, PGFrameStyle_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PGFrameStyle self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const PGFrameStyle self, const LVecBase4f color)
        set_color(const PGFrameStyle self, float r, float g, float b, float a)
        
        /**
         * Sets the dominant color of the frame.
         */
        
        /**
         * Sets the dominant color of the frame.
         */
        """
        pass

    def setTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture(const PGFrameStyle self, Texture texture)
        
        /**
         * Specifies a texture that should be applied to the frame.
         */
        """
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_type(const PGFrameStyle self, int type)
        
        /**
         * Sets the basic type of frame.
         */
        """
        pass

    def setUvWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_uv_width(const PGFrameStyle self, const LVecBase2f uv_width)
        set_uv_width(const PGFrameStyle self, float u, float v)
        
        /**
         * Sets the uv_width parameter, which indicates the amount of the texture that
         * is consumed by the inner bevel--the width in texture space of the amount
         * indicated by set_width.
         */
        
        /**
         * Sets the uv_width parameter, which indicates the amount of the texture that
         * is consumed by the inner bevel--the width in texture space of the amount
         * indicated by set_width.
         */
        """
        pass

    def setVisibleScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_visible_scale(const PGFrameStyle self, const LVecBase2f visible_scale)
        set_visible_scale(const PGFrameStyle self, float x, float y)
        
        /**
         * Sets a scale factor on the visible representation of the frame, in the X
         * and Y directions.  If this scale factor is other than 1, it will affect the
         * size of the visible frame representation within the actual frame border.
         */
        
        /**
         * Sets a scale factor on the visible representation of the frame, in the X
         * and Y directions.  If this scale factor is other than 1, it will affect the
         * size of the visible frame representation within the actual frame border.
         */
        """
        pass

    def setWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_width(const PGFrameStyle self, const LVecBase2f width)
        set_width(const PGFrameStyle self, float x, float y)
        
        /**
         * Sets the width parameter, which has meaning only for certain frame types.
         * For instance, this is the width of the bevel for T_bevel_in or T_bevel_out.
         * The units are in screen units.
         */
        
        /**
         * Sets the width parameter, which has meaning only for certain frame types.
         * For instance, this is the width of the bevel for T_bevel_in or T_bevel_out.
         * The units are in screen units.
         */
        """
        pass

    def set_color(self, const_PGFrameStyle_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const PGFrameStyle self, const LVecBase4f color)
        set_color(const PGFrameStyle self, float r, float g, float b, float a)
        
        /**
         * Sets the dominant color of the frame.
         */
        
        /**
         * Sets the dominant color of the frame.
         */
        """
        pass

    def set_texture(self, const_PGFrameStyle_self, Texture_texture): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture(const PGFrameStyle self, Texture texture)
        
        /**
         * Specifies a texture that should be applied to the frame.
         */
        """
        pass

    def set_type(self, const_PGFrameStyle_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_type(const PGFrameStyle self, int type)
        
        /**
         * Sets the basic type of frame.
         */
        """
        pass

    def set_uv_width(self, const_PGFrameStyle_self, const_LVecBase2f_uv_width): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_uv_width(const PGFrameStyle self, const LVecBase2f uv_width)
        set_uv_width(const PGFrameStyle self, float u, float v)
        
        /**
         * Sets the uv_width parameter, which indicates the amount of the texture that
         * is consumed by the inner bevel--the width in texture space of the amount
         * indicated by set_width.
         */
        
        /**
         * Sets the uv_width parameter, which indicates the amount of the texture that
         * is consumed by the inner bevel--the width in texture space of the amount
         * indicated by set_width.
         */
        """
        pass

    def set_visible_scale(self, const_PGFrameStyle_self, const_LVecBase2f_visible_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_visible_scale(const PGFrameStyle self, const LVecBase2f visible_scale)
        set_visible_scale(const PGFrameStyle self, float x, float y)
        
        /**
         * Sets a scale factor on the visible representation of the frame, in the X
         * and Y directions.  If this scale factor is other than 1, it will affect the
         * size of the visible frame representation within the actual frame border.
         */
        
        /**
         * Sets a scale factor on the visible representation of the frame, in the X
         * and Y directions.  If this scale factor is other than 1, it will affect the
         * size of the visible frame representation within the actual frame border.
         */
        """
        pass

    def set_width(self, const_PGFrameStyle_self, const_LVecBase2f_width): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_width(const PGFrameStyle self, const LVecBase2f width)
        set_width(const PGFrameStyle self, float x, float y)
        
        /**
         * Sets the width parameter, which has meaning only for certain frame types.
         * For instance, this is the width of the bevel for T_bevel_in or T_bevel_out.
         * The units are in screen units.
         */
        
        /**
         * Sets the width parameter, which has meaning only for certain frame types.
         * For instance, this is the width of the bevel for T_bevel_in or T_bevel_out.
         * The units are in screen units.
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'TBevelIn': 3,
        'TBevelOut': 2,
        'TFlat': 1,
        'TGroove': 4,
        'TNone': 0,
        'TRidge': 5,
        'TTextureBorder': 6,
        'T_bevel_in': 3,
        'T_bevel_out': 2,
        'T_flat': 1,
        'T_groove': 4,
        'T_none': 0,
        'T_ridge': 5,
        'T_texture_border': 6,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PGFrameStyle' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PGFrameStyle' objects>"
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PGFrameStyle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE383DF0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.PGFrameStyle' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.PGFrameStyle' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.PGFrameStyle' objects>"
        'clearTexture': None, # (!) real value is "<method 'clearTexture' of 'panda3d.core.PGFrameStyle' objects>"
        'clear_texture': None, # (!) real value is "<method 'clear_texture' of 'panda3d.core.PGFrameStyle' objects>"
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d.core.PGFrameStyle' objects>"
        'getInternalFrame': None, # (!) real value is "<method 'getInternalFrame' of 'panda3d.core.PGFrameStyle' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.core.PGFrameStyle' objects>"
        'getType': None, # (!) real value is "<method 'getType' of 'panda3d.core.PGFrameStyle' objects>"
        'getUvWidth': None, # (!) real value is "<method 'getUvWidth' of 'panda3d.core.PGFrameStyle' objects>"
        'getVisibleScale': None, # (!) real value is "<method 'getVisibleScale' of 'panda3d.core.PGFrameStyle' objects>"
        'getWidth': None, # (!) real value is "<method 'getWidth' of 'panda3d.core.PGFrameStyle' objects>"
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d.core.PGFrameStyle' objects>"
        'get_internal_frame': None, # (!) real value is "<method 'get_internal_frame' of 'panda3d.core.PGFrameStyle' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.core.PGFrameStyle' objects>"
        'get_type': None, # (!) real value is "<method 'get_type' of 'panda3d.core.PGFrameStyle' objects>"
        'get_uv_width': None, # (!) real value is "<method 'get_uv_width' of 'panda3d.core.PGFrameStyle' objects>"
        'get_visible_scale': None, # (!) real value is "<method 'get_visible_scale' of 'panda3d.core.PGFrameStyle' objects>"
        'get_width': None, # (!) real value is "<method 'get_width' of 'panda3d.core.PGFrameStyle' objects>"
        'hasTexture': None, # (!) real value is "<method 'hasTexture' of 'panda3d.core.PGFrameStyle' objects>"
        'has_texture': None, # (!) real value is "<method 'has_texture' of 'panda3d.core.PGFrameStyle' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.PGFrameStyle' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.core.PGFrameStyle' objects>"
        'setTexture': None, # (!) real value is "<method 'setTexture' of 'panda3d.core.PGFrameStyle' objects>"
        'setType': None, # (!) real value is "<method 'setType' of 'panda3d.core.PGFrameStyle' objects>"
        'setUvWidth': None, # (!) real value is "<method 'setUvWidth' of 'panda3d.core.PGFrameStyle' objects>"
        'setVisibleScale': None, # (!) real value is "<method 'setVisibleScale' of 'panda3d.core.PGFrameStyle' objects>"
        'setWidth': None, # (!) real value is "<method 'setWidth' of 'panda3d.core.PGFrameStyle' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.core.PGFrameStyle' objects>"
        'set_texture': None, # (!) real value is "<method 'set_texture' of 'panda3d.core.PGFrameStyle' objects>"
        'set_type': None, # (!) real value is "<method 'set_type' of 'panda3d.core.PGFrameStyle' objects>"
        'set_uv_width': None, # (!) real value is "<method 'set_uv_width' of 'panda3d.core.PGFrameStyle' objects>"
        'set_visible_scale': None, # (!) real value is "<method 'set_visible_scale' of 'panda3d.core.PGFrameStyle' objects>"
        'set_width': None, # (!) real value is "<method 'set_width' of 'panda3d.core.PGFrameStyle' objects>"
    }
    TBevelIn = 3
    TBevelOut = 2
    TFlat = 1
    TGroove = 4
    TNone = 0
    TRidge = 5
    TTextureBorder = 6
    T_bevel_in = 3
    T_bevel_out = 2
    T_flat = 1
    T_groove = 4
    T_none = 0
    T_ridge = 5
    T_texture_border = 6


