# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Light import Light

from .Camera import Camera

class LightLensNode(Light, Camera):
    """
    /**
     * A derivative of Light and of Camera.  The name might be misleading: it does
     * not directly derive from LensNode, but through the Camera class.  The
     * Camera serves no purpose unless shadows are enabled.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getShadowBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shadow_buffer(const LightLensNode self, GraphicsStateGuardianBase gsg)
        
        /**
         * Returns the buffer that has been constructed for a given GSG, or NULL if no
         * such buffer has (yet) been constructed.  This should be used for debugging
         * only, you will not need to call this normally.
         */
        """
        pass

    def getShadowBufferSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shadow_buffer_size(LightLensNode self)
        
        /**
         * Returns the size of the shadow buffer to be created for this light source.
         */
        """
        pass

    def getShadowBufferSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shadow_buffer_sort(LightLensNode self)
        
        /**
         * Returns the sort of the shadow buffer to be created for this light source.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_shadow_buffer(self, const_LightLensNode_self, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shadow_buffer(const LightLensNode self, GraphicsStateGuardianBase gsg)
        
        /**
         * Returns the buffer that has been constructed for a given GSG, or NULL if no
         * such buffer has (yet) been constructed.  This should be used for debugging
         * only, you will not need to call this normally.
         */
        """
        pass

    def get_shadow_buffer_size(self, LightLensNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shadow_buffer_size(LightLensNode self)
        
        /**
         * Returns the size of the shadow buffer to be created for this light source.
         */
        """
        pass

    def get_shadow_buffer_sort(self, LightLensNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shadow_buffer_sort(LightLensNode self)
        
        /**
         * Returns the sort of the shadow buffer to be created for this light source.
         */
        """
        pass

    def hasSpecularColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_specular_color(LightLensNode self)
        
        /**
         * Returns true if this light defines a specular color, false if the specular
         * color is derived automatically from the light color.
         */
        """
        pass

    def has_specular_color(self, LightLensNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_specular_color(LightLensNode self)
        
        /**
         * Returns true if this light defines a specular color, false if the specular
         * color is derived automatically from the light color.
         */
        """
        pass

    def isShadowCaster(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_shadow_caster(LightLensNode self)
        
        /**
         * Returns whether this light is configured to cast shadows or not.
         */
        """
        pass

    def is_shadow_caster(self, LightLensNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_shadow_caster(LightLensNode self)
        
        /**
         * Returns whether this light is configured to cast shadows or not.
         */
        """
        pass

    def output(self, LightLensNode_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(LightLensNode self, ostream out)
        
        // We have to explicitly publish these because they resolve the multiple
        // inheritance.
        
        /**
         *
         */
        """
        pass

    def setShadowBufferSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shadow_buffer_size(const LightLensNode self, const LVecBase2i size)
        
        /**
         * Sets the size of the shadow buffer to be created for this light source.
         */
        """
        pass

    def setShadowCaster(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shadow_caster(const LightLensNode self, bool caster)
        set_shadow_caster(const LightLensNode self, bool caster, int buffer_xsize, int buffer_ysize, int sort)
        
        /**
         * Sets the flag indicating whether this light should cast shadows or not.
         * This is the variant without buffer size, meaning that the current buffer
         * size will be kept (512x512 is the default). Note that enabling shadows will
         * require the shader generator to be enabled on the scene.
         */
        
        /**
         * Sets the flag indicating whether this light should cast shadows or not.
         * The xsize and ysize parameters specify the size of the shadow buffer that
         * will be set up, the sort parameter specifies the sort.  Note that enabling
         * shadows will require the shader generator to be enabled on the scene.
         */
        """
        pass

    def set_shadow_buffer_size(self, const_LightLensNode_self, const_LVecBase2i_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shadow_buffer_size(const LightLensNode self, const LVecBase2i size)
        
        /**
         * Sets the size of the shadow buffer to be created for this light source.
         */
        """
        pass

    def set_shadow_caster(self, const_LightLensNode_self, bool_caster): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shadow_caster(const LightLensNode self, bool caster)
        set_shadow_caster(const LightLensNode self, bool caster, int buffer_xsize, int buffer_ysize, int sort)
        
        /**
         * Sets the flag indicating whether this light should cast shadows or not.
         * This is the variant without buffer size, meaning that the current buffer
         * size will be kept (512x512 is the default). Note that enabling shadows will
         * require the shader generator to be enabled on the scene.
         */
        
        /**
         * Sets the flag indicating whether this light should cast shadows or not.
         * The xsize and ysize parameters specify the size of the shadow buffer that
         * will be set up, the sort parameter specifies the sort.  Note that enabling
         * shadows will require the shader generator to be enabled on the scene.
         */
        """
        pass

    def upcastToCamera(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Camera(const LightLensNode self)
        
        upcast from LightLensNode to Camera
        """
        pass

    def upcastToLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Light(const LightLensNode self)
        
        upcast from LightLensNode to Light
        """
        pass

    def upcast_to_Camera(self, const_LightLensNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Camera(const LightLensNode self)
        
        upcast from LightLensNode to Camera
        """
        pass

    def upcast_to_Light(self, const_LightLensNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Light(const LightLensNode self)
        
        upcast from LightLensNode to Light
        """
        pass

    def write(self, LightLensNode_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(LightLensNode self, ostream out, int indent_level)
        
        /**
         *
         */
        """
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

    shadow_buffer_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shadow_caster = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A derivative of Light and of Camera.  The name might be misleading: it does\n * not directly derive from LensNode, but through the Camera class.  The\n * Camera serves no purpose unless shadows are enabled.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LightLensNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE287530>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.LightLensNode' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.LightLensNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE287530>)>'
        'getShadowBuffer': None, # (!) real value is "<method 'getShadowBuffer' of 'panda3d.core.LightLensNode' objects>"
        'getShadowBufferSize': None, # (!) real value is "<method 'getShadowBufferSize' of 'panda3d.core.LightLensNode' objects>"
        'getShadowBufferSort': None, # (!) real value is "<method 'getShadowBufferSort' of 'panda3d.core.LightLensNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE287530>)>'
        'get_shadow_buffer': None, # (!) real value is "<method 'get_shadow_buffer' of 'panda3d.core.LightLensNode' objects>"
        'get_shadow_buffer_size': None, # (!) real value is "<method 'get_shadow_buffer_size' of 'panda3d.core.LightLensNode' objects>"
        'get_shadow_buffer_sort': None, # (!) real value is "<method 'get_shadow_buffer_sort' of 'panda3d.core.LightLensNode' objects>"
        'hasSpecularColor': None, # (!) real value is "<method 'hasSpecularColor' of 'panda3d.core.LightLensNode' objects>"
        'has_specular_color': None, # (!) real value is "<method 'has_specular_color' of 'panda3d.core.LightLensNode' objects>"
        'isShadowCaster': None, # (!) real value is "<method 'isShadowCaster' of 'panda3d.core.LightLensNode' objects>"
        'is_shadow_caster': None, # (!) real value is "<method 'is_shadow_caster' of 'panda3d.core.LightLensNode' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.LightLensNode' objects>"
        'setShadowBufferSize': None, # (!) real value is "<method 'setShadowBufferSize' of 'panda3d.core.LightLensNode' objects>"
        'setShadowCaster': None, # (!) real value is "<method 'setShadowCaster' of 'panda3d.core.LightLensNode' objects>"
        'set_shadow_buffer_size': None, # (!) real value is "<method 'set_shadow_buffer_size' of 'panda3d.core.LightLensNode' objects>"
        'set_shadow_caster': None, # (!) real value is "<method 'set_shadow_caster' of 'panda3d.core.LightLensNode' objects>"
        'shadow_buffer_size': None, # (!) real value is "<attribute 'shadow_buffer_size' of 'panda3d.core.LightLensNode' objects>"
        'shadow_caster': None, # (!) real value is "<attribute 'shadow_caster' of 'panda3d.core.LightLensNode' objects>"
        'upcastToCamera': None, # (!) real value is "<method 'upcastToCamera' of 'panda3d.core.LightLensNode' objects>"
        'upcastToLight': None, # (!) real value is "<method 'upcastToLight' of 'panda3d.core.LightLensNode' objects>"
        'upcast_to_Camera': None, # (!) real value is "<method 'upcast_to_Camera' of 'panda3d.core.LightLensNode' objects>"
        'upcast_to_Light': None, # (!) real value is "<method 'upcast_to_Light' of 'panda3d.core.LightLensNode' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.LightLensNode' objects>"
    }


