# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

from .GeomEnums import GeomEnums

class GeomVertexArrayDataHandle(ReferenceCount, GeomEnums):
    """
    /**
     * This data object is returned by GeomVertexArrayData::get_handle() or
     * modify_handle(). As long as it exists, the data is locked; when the last of
     * these destructs, the data is unlocked.
     *
     * Only one thread at a time may lock the data; other threads attempting to
     * lock the data will block.  A given thread may simultaneously lock the data
     * multiple times.
     *
     * This class serves in lieu of a pair of GeomVertexArrayDataPipelineReader
     * and GeomVertexArrayDataPipelineWriter classes
     */
    """
    def clearRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_rows(const GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def clear_rows(self, const_GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_rows(const GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def copyDataFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_data_from(const GeomVertexArrayDataHandle self, const GeomVertexArrayDataHandle other)
        copy_data_from(const GeomVertexArrayDataHandle self, object buffer)
        
        /**
         * Copies the entire data array from the other object.
         */
        
        /**
         * Copies the entire data array from the buffer.
         */
        """
        pass

    def copySubdataFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_subdata_from(const GeomVertexArrayDataHandle self, int to_start, int to_size, object buffer)
        copy_subdata_from(const GeomVertexArrayDataHandle self, int to_start, int to_size, const GeomVertexArrayDataHandle other, int from_start, int from_size)
        copy_subdata_from(const GeomVertexArrayDataHandle self, int to_start, int to_size, object buffer, int from_start, int from_size)
        
        /**
         * Copies a portion of the data array from the other object into a portion of
         * the data array of this object.  If to_size != from_size, the size of this
         * data array is adjusted accordingly.
         */
        
        /**
         * Copies a portion of the data array from the buffer into a portion of the
         * data array of this object.  If to_size != from_size, the size of this data
         * array is adjusted accordingly.
         */
        """
        pass

    def copy_data_from(self, const_GeomVertexArrayDataHandle_self, const_GeomVertexArrayDataHandle_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_data_from(const GeomVertexArrayDataHandle self, const GeomVertexArrayDataHandle other)
        copy_data_from(const GeomVertexArrayDataHandle self, object buffer)
        
        /**
         * Copies the entire data array from the other object.
         */
        
        /**
         * Copies the entire data array from the buffer.
         */
        """
        pass

    def copy_subdata_from(self, const_GeomVertexArrayDataHandle_self, int_to_start, int_to_size, object_buffer): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_subdata_from(const GeomVertexArrayDataHandle self, int to_start, int to_size, object buffer)
        copy_subdata_from(const GeomVertexArrayDataHandle self, int to_start, int to_size, const GeomVertexArrayDataHandle other, int from_start, int from_size)
        copy_subdata_from(const GeomVertexArrayDataHandle self, int to_start, int to_size, object buffer, int from_start, int from_size)
        
        /**
         * Copies a portion of the data array from the other object into a portion of
         * the data array of this object.  If to_size != from_size, the size of this
         * data array is adjusted accordingly.
         */
        
        /**
         * Copies a portion of the data array from the buffer into a portion of the
         * data array of this object.  If to_size != from_size, the size of this data
         * array is adjusted accordingly.
         */
        """
        pass

    def getArrayFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_format(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data(GeomVertexArrayDataHandle self)
        
        /**
         * Returns the entire raw data of the GeomVertexArrayData object, formatted as
         * a string.  This is primarily for the benefit of high-level languages such
         * as Python.
         */
        """
        pass

    def getDataSizeBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data_size_bytes(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def getModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modified(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def getNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_rows(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def getObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_object(const GeomVertexArrayDataHandle self)
        get_object(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def getSubdata(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_subdata(GeomVertexArrayDataHandle self, int start, int size)
        
        /**
         * Returns a subset of the raw data of the GeomVertexArrayData object,
         * formatted as a string.  This is primarily for the benefit of high-level
         * languages such as Python.
         */
        """
        pass

    def getUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_usage_hint(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def get_array_format(self, GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_format(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_data(self, GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data(GeomVertexArrayDataHandle self)
        
        /**
         * Returns the entire raw data of the GeomVertexArrayData object, formatted as
         * a string.  This is primarily for the benefit of high-level languages such
         * as Python.
         */
        """
        pass

    def get_data_size_bytes(self, GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data_size_bytes(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def get_modified(self, GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def get_num_rows(self, GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_rows(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def get_object(self, const_GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_object(const GeomVertexArrayDataHandle self)
        get_object(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def get_subdata(self, GeomVertexArrayDataHandle_self, int_start, int_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_subdata(GeomVertexArrayDataHandle self, int start, int size)
        
        /**
         * Returns a subset of the raw data of the GeomVertexArrayData object,
         * formatted as a string.  This is primarily for the benefit of high-level
         * languages such as Python.
         */
        """
        pass

    def get_usage_hint(self, GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_usage_hint(GeomVertexArrayDataHandle self)
        
        /**
         *
         */
        """
        pass

    def markUsed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        mark_used(GeomVertexArrayDataHandle self)
        
        /**
         * Marks the array data recently-used.
         */
        """
        pass

    def mark_used(self, GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        mark_used(GeomVertexArrayDataHandle self)
        
        /**
         * Marks the array data recently-used.
         */
        """
        pass

    def prepareNow(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        prepare_now(GeomVertexArrayDataHandle self, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
        /**
         * Creates a context for the data on the particular GSG, if it does not
         * already exist.  Returns the new (or old) VertexBufferContext.  This assumes
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

    def prepare_now(self, GeomVertexArrayDataHandle_self, PreparedGraphicsObjects_prepared_objects, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_now(GeomVertexArrayDataHandle self, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
        /**
         * Creates a context for the data on the particular GSG, if it does not
         * already exist.  Returns the new (or old) VertexBufferContext.  This assumes
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

    def requestResident(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        request_resident(GeomVertexArrayDataHandle self)
        
        /**
         * Returns true if the vertex data is currently resident in memory.  If this
         * returns true, the next call to get_handle()->get_read_pointer() will
         * probably not block.  If this returns false, the vertex data will be brought
         * back into memory shortly; try again later.
         */
        """
        pass

    def request_resident(self, GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        request_resident(GeomVertexArrayDataHandle self)
        
        /**
         * Returns true if the vertex data is currently resident in memory.  If this
         * returns true, the next call to get_handle()->get_read_pointer() will
         * probably not block.  If this returns false, the vertex data will be brought
         * back into memory shortly; try again later.
         */
        """
        pass

    def reserveNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reserve_num_rows(const GeomVertexArrayDataHandle self, int n)
        
        /**
         *
         */
        """
        pass

    def reserve_num_rows(self, const_GeomVertexArrayDataHandle_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reserve_num_rows(const GeomVertexArrayDataHandle self, int n)
        
        /**
         *
         */
        """
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data(const GeomVertexArrayDataHandle self, bytes data)
        
        /**
         * Replaces the entire raw data array with the contents of the indicated
         * string.  This is primarily for the benefit of high-level languages like
         * Python.
         */
        """
        pass

    def setNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_rows(const GeomVertexArrayDataHandle self, int n)
        
        /**
         *
         */
        """
        pass

    def setSubdata(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_subdata(const GeomVertexArrayDataHandle self, int start, int size, bytes data)
        
        /**
         * Replaces a portion of the data array from the indicated string.  If size !=
         * data.size(), the size of this data array is adjusted accordingly.
         *
         * This is primarily for the benefit of high-level languages like Python.
         */
        """
        pass

    def set_data(self, const_GeomVertexArrayDataHandle_self, bytes_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data(const GeomVertexArrayDataHandle self, bytes data)
        
        /**
         * Replaces the entire raw data array with the contents of the indicated
         * string.  This is primarily for the benefit of high-level languages like
         * Python.
         */
        """
        pass

    def set_num_rows(self, const_GeomVertexArrayDataHandle_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_rows(const GeomVertexArrayDataHandle self, int n)
        
        /**
         *
         */
        """
        pass

    def set_subdata(self, const_GeomVertexArrayDataHandle_self, int_start, int_size, bytes_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_subdata(const GeomVertexArrayDataHandle self, int start, int size, bytes data)
        
        /**
         * Replaces a portion of the data array from the indicated string.  If size !=
         * data.size(), the size of this data array is adjusted accordingly.
         *
         * This is primarily for the benefit of high-level languages like Python.
         */
        """
        pass

    def uncleanSetNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unclean_set_num_rows(const GeomVertexArrayDataHandle self, int n)
        
        /**
         *
         */
        """
        pass

    def unclean_set_num_rows(self, const_GeomVertexArrayDataHandle_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unclean_set_num_rows(const GeomVertexArrayDataHandle self, int n)
        
        /**
         *
         */
        """
        pass

    def upcastToGeomEnums(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomVertexArrayDataHandle self)
        
        upcast from GeomVertexArrayDataHandle to GeomEnums
        """
        pass

    def upcastToReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_ReferenceCount(const GeomVertexArrayDataHandle self)
        
        upcast from GeomVertexArrayDataHandle to ReferenceCount
        """
        pass

    def upcast_to_GeomEnums(self, const_GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomVertexArrayDataHandle self)
        
        upcast from GeomVertexArrayDataHandle to GeomEnums
        """
        pass

    def upcast_to_ReferenceCount(self, const_GeomVertexArrayDataHandle_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_ReferenceCount(const GeomVertexArrayDataHandle self)
        
        upcast from GeomVertexArrayDataHandle to ReferenceCount
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    array_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_size_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usage_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This data object is returned by GeomVertexArrayData::get_handle() or\n * modify_handle(). As long as it exists, the data is locked; when the last of\n * these destructs, the data is unlocked.\n *\n * Only one thread at a time may lock the data; other threads attempting to\n * lock the data will block.  A given thread may simultaneously lock the data\n * multiple times.\n *\n * This class serves in lieu of a pair of GeomVertexArrayDataPipelineReader\n * and GeomVertexArrayDataPipelineWriter classes\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FB510>'
        'array_format': None, # (!) real value is "<attribute 'array_format' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'clearRows': None, # (!) real value is "<method 'clearRows' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'clear_rows': None, # (!) real value is "<method 'clear_rows' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'copyDataFrom': None, # (!) real value is "<method 'copyDataFrom' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'copySubdataFrom': None, # (!) real value is "<method 'copySubdataFrom' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'copy_data_from': None, # (!) real value is "<method 'copy_data_from' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'copy_subdata_from': None, # (!) real value is "<method 'copy_subdata_from' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'data_size_bytes': None, # (!) real value is "<attribute 'data_size_bytes' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'getArrayFormat': None, # (!) real value is "<method 'getArrayFormat' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FB510>)>'
        'getData': None, # (!) real value is "<method 'getData' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'getDataSizeBytes': None, # (!) real value is "<method 'getDataSizeBytes' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'getNumRows': None, # (!) real value is "<method 'getNumRows' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'getObject': None, # (!) real value is "<method 'getObject' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'getSubdata': None, # (!) real value is "<method 'getSubdata' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'getUsageHint': None, # (!) real value is "<method 'getUsageHint' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'get_array_format': None, # (!) real value is "<method 'get_array_format' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FB510>)>'
        'get_data': None, # (!) real value is "<method 'get_data' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'get_data_size_bytes': None, # (!) real value is "<method 'get_data_size_bytes' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'get_num_rows': None, # (!) real value is "<method 'get_num_rows' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'get_object': None, # (!) real value is "<method 'get_object' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'get_subdata': None, # (!) real value is "<method 'get_subdata' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'get_usage_hint': None, # (!) real value is "<method 'get_usage_hint' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'markUsed': None, # (!) real value is "<method 'markUsed' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'mark_used': None, # (!) real value is "<method 'mark_used' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'object': None, # (!) real value is "<attribute 'object' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'prepareNow': None, # (!) real value is "<method 'prepareNow' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'prepare_now': None, # (!) real value is "<method 'prepare_now' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'requestResident': None, # (!) real value is "<method 'requestResident' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'request_resident': None, # (!) real value is "<method 'request_resident' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'reserveNumRows': None, # (!) real value is "<method 'reserveNumRows' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'reserve_num_rows': None, # (!) real value is "<method 'reserve_num_rows' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'setData': None, # (!) real value is "<method 'setData' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'setNumRows': None, # (!) real value is "<method 'setNumRows' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'setSubdata': None, # (!) real value is "<method 'setSubdata' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'set_data': None, # (!) real value is "<method 'set_data' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'set_num_rows': None, # (!) real value is "<method 'set_num_rows' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'set_subdata': None, # (!) real value is "<method 'set_subdata' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'uncleanSetNumRows': None, # (!) real value is "<method 'uncleanSetNumRows' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'unclean_set_num_rows': None, # (!) real value is "<method 'unclean_set_num_rows' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'upcastToGeomEnums': None, # (!) real value is "<method 'upcastToGeomEnums' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'upcastToReferenceCount': None, # (!) real value is "<method 'upcastToReferenceCount' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'upcast_to_GeomEnums': None, # (!) real value is "<method 'upcast_to_GeomEnums' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'upcast_to_ReferenceCount': None, # (!) real value is "<method 'upcast_to_ReferenceCount' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
        'usage_hint': None, # (!) real value is "<attribute 'usage_hint' of 'panda3d.core.GeomVertexArrayDataHandle' objects>"
    }


