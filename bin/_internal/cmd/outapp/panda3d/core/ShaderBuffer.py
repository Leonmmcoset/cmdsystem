# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

from .Namable import Namable

from .GeomEnums import GeomEnums

class ShaderBuffer(TypedWritableReferenceCount, Namable, GeomEnums):
    """
    /**
     * This is a generic buffer object that lives in graphics memory.
     *
     * @since 1.10.0
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def isPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_prepared(ShaderBuffer self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the data has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def is_prepared(self, ShaderBuffer_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_prepared(ShaderBuffer self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the data has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def prepare(self, const_ShaderBuffer_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare(const ShaderBuffer self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Indicates that the data should be enqueued to be prepared in the indicated
         * prepared_objects at the beginning of the next frame.  This will ensure the
         * data is already loaded into the GSG if it is expected to be rendered soon.
         *
         * Use this function instead of prepare_now() to preload datas from a user
         * interface standpoint.
         */
        """
        pass

    def prepareNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_now(const ShaderBuffer self, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
        /**
         * Creates a context for the data on the particular GSG, if it does not
         * already exist.  Returns the new (or old) BufferContext.  This assumes
         * that the GraphicsStateGuardian is the currently active rendering context
         * and that it is ready to accept new datas.  If this is not necessarily the
         * case, you should use prepare() instead.
         *
         * Normally, this is not called directly except by the GraphicsStateGuardian;
         * a data does not need to be explicitly prepared by the user before it may be
         * rendered.
         */
        """
        pass

    def prepare_now(self, const_ShaderBuffer_self, PreparedGraphicsObjects_prepared_objects, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_now(const ShaderBuffer self, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
        /**
         * Creates a context for the data on the particular GSG, if it does not
         * already exist.  Returns the new (or old) BufferContext.  This assumes
         * that the GraphicsStateGuardian is the currently active rendering context
         * and that it is ready to accept new datas.  If this is not necessarily the
         * case, you should use prepare() instead.
         *
         * Normally, this is not called directly except by the GraphicsStateGuardian;
         * a data does not need to be explicitly prepared by the user before it may be
         * rendered.
         */
        """
        pass

    def release(self, const_ShaderBuffer_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(const ShaderBuffer self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Frees the data context only on the indicated object, if it exists there.
         * Returns true if it was released, false if it had not been prepared.
         */
        """
        pass

    def releaseAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all(const ShaderBuffer self)
        
        /**
         * Frees the context allocated on all objects for which the data has been
         * declared.  Returns the number of contexts which have been freed.
         */
        """
        pass

    def release_all(self, const_ShaderBuffer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all(const ShaderBuffer self)
        
        /**
         * Frees the context allocated on all objects for which the data has been
         * declared.  Returns the number of contexts which have been freed.
         */
        """
        pass

    def upcastToGeomEnums(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GeomEnums(const ShaderBuffer self)
        
        upcast from ShaderBuffer to GeomEnums
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const ShaderBuffer self)
        
        upcast from ShaderBuffer to Namable
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const ShaderBuffer self)
        
        upcast from ShaderBuffer to TypedWritableReferenceCount
        """
        pass

    def upcast_to_GeomEnums(self, const_ShaderBuffer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GeomEnums(const ShaderBuffer self)
        
        upcast from ShaderBuffer to GeomEnums
        """
        pass

    def upcast_to_Namable(self, const_ShaderBuffer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const ShaderBuffer self)
        
        upcast from ShaderBuffer to Namable
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_ShaderBuffer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const ShaderBuffer self)
        
        upcast from ShaderBuffer to TypedWritableReferenceCount
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

    data_size_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usage_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ShaderBuffer' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ShaderBuffer' objects>"
        '__doc__': '/**\n * This is a generic buffer object that lives in graphics memory.\n *\n * @since 1.10.0\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ShaderBuffer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FF0E0>'
        'data_size_bytes': None, # (!) real value is "<attribute 'data_size_bytes' of 'panda3d.core.ShaderBuffer' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FF0E0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FF0E0>)>'
        'isPrepared': None, # (!) real value is "<method 'isPrepared' of 'panda3d.core.ShaderBuffer' objects>"
        'is_prepared': None, # (!) real value is "<method 'is_prepared' of 'panda3d.core.ShaderBuffer' objects>"
        'prepare': None, # (!) real value is "<method 'prepare' of 'panda3d.core.ShaderBuffer' objects>"
        'prepareNow': None, # (!) real value is "<method 'prepareNow' of 'panda3d.core.ShaderBuffer' objects>"
        'prepare_now': None, # (!) real value is "<method 'prepare_now' of 'panda3d.core.ShaderBuffer' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.ShaderBuffer' objects>"
        'releaseAll': None, # (!) real value is "<method 'releaseAll' of 'panda3d.core.ShaderBuffer' objects>"
        'release_all': None, # (!) real value is "<method 'release_all' of 'panda3d.core.ShaderBuffer' objects>"
        'upcastToGeomEnums': None, # (!) real value is "<method 'upcastToGeomEnums' of 'panda3d.core.ShaderBuffer' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.ShaderBuffer' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.ShaderBuffer' objects>"
        'upcast_to_GeomEnums': None, # (!) real value is "<method 'upcast_to_GeomEnums' of 'panda3d.core.ShaderBuffer' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.ShaderBuffer' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.ShaderBuffer' objects>"
        'usage_hint': None, # (!) real value is "<attribute 'usage_hint' of 'panda3d.core.ShaderBuffer' objects>"
    }


