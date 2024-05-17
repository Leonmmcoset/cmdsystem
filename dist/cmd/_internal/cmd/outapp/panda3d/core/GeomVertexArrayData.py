# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CopyOnWriteObject import CopyOnWriteObject

from .SimpleLruPage import SimpleLruPage

from .GeomEnums import GeomEnums

class GeomVertexArrayData(CopyOnWriteObject, SimpleLruPage, GeomEnums):
    """
    /**
     * This is the data for one array of a GeomVertexData structure.  Many
     * GeomVertexData structures will only define one array, with all data
     * elements interleaved (DirectX 8.0 and before insisted on this format); some
     * will define multiple arrays.
     *
     * DirectX calls this concept of one array a "stream". It also closely
     * correlates with the concept of a vertex buffer.
     *
     * This object is just a block of data.  In general, you should not be
     * directly messing with this object from application code.  See
     * GeomVertexData for the organizing structure, and see
     * GeomVertexReader/Writer/Rewriter for high-level tools to manipulate the
     * actual vertex data.
     */
    """
    def assign(self, const_GeomVertexArrayData_self, const_GeomVertexArrayData_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GeomVertexArrayData self, const GeomVertexArrayData copy)
        """
        pass

    def clearRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_rows(const GeomVertexArrayData self)
        
        /**
         * Removes all of the rows in the array.  Functionally equivalent to
         * set_num_rows(0).
         */
        """
        pass

    def clear_rows(self, const_GeomVertexArrayData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_rows(const GeomVertexArrayData self)
        
        /**
         * Removes all of the rows in the array.  Functionally equivalent to
         * set_num_rows(0).
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(GeomVertexArrayData self, const GeomVertexArrayData other)
        
        /**
         * Returns 0 if the two arrays are equivalent, even if they are not the same
         * pointer.
         */
        """
        pass

    def compare_to(self, GeomVertexArrayData_self, const_GeomVertexArrayData_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(GeomVertexArrayData self, const GeomVertexArrayData other)
        
        /**
         * Returns 0 if the two arrays are equivalent, even if they are not the same
         * pointer.
         */
        """
        pass

    def getArrayFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_format(GeomVertexArrayData self)
        
        /**
         * Returns the format object that describes this array.
         */
        """
        pass

    def getBook(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_book()
        
        /**
         * Returns the global VertexDataBook that will be used to allocate vertex data
         * buffers.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDataSizeBytes(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data_size_bytes(GeomVertexArrayData self)
        
        /**
         * Returns the number of bytes stored in the array.
         */
        """
        pass

    def getHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_handle(GeomVertexArrayData self, Thread current_thread)
        
        /**
         * Returns an object that can be used to read the actual data bytes stored in
         * the array.  Calling this method locks the data, and will block any other
         * threads attempting to read or write the data, until the returned object
         * destructs.
         */
        """
        pass

    def getIndependentLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_independent_lru()
        
        /**
         * Returns a pointer to the global LRU object that manages the
         * GeomVertexArrayData's that have not (yet) been paged out.
         */
        """
        pass

    def getModified(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_modified(GeomVertexArrayData self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the array vertex data is modified.
         */
        """
        pass

    def getNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_rows(GeomVertexArrayData self)
        
        /**
         * Returns the number of rows stored in the array, based on the number of
         * bytes and the stride.  This should be the same for all arrays within a
         * given GeomVertexData object.
         */
        """
        pass

    def getSmallLru(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_small_lru()
        
        /**
         * Returns a pointer to the global LRU object that manages the
         * GeomVertexArrayData's that are deemed too small to be paged out.
         */
        """
        pass

    def getUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_usage_hint(GeomVertexArrayData self)
        
        /**
         * Returns the usage hint that describes to the rendering backend how often
         * the vertex data will be modified and/or rendered.  See geomEnums.h.
         */
        """
        pass

    def get_array_format(self, GeomVertexArrayData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_format(GeomVertexArrayData self)
        
        /**
         * Returns the format object that describes this array.
         */
        """
        pass

    def get_book(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_book()
        
        /**
         * Returns the global VertexDataBook that will be used to allocate vertex data
         * buffers.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_data_size_bytes(self, GeomVertexArrayData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data_size_bytes(GeomVertexArrayData self)
        
        /**
         * Returns the number of bytes stored in the array.
         */
        """
        pass

    def get_handle(self, GeomVertexArrayData_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_handle(GeomVertexArrayData self, Thread current_thread)
        
        /**
         * Returns an object that can be used to read the actual data bytes stored in
         * the array.  Calling this method locks the data, and will block any other
         * threads attempting to read or write the data, until the returned object
         * destructs.
         */
        """
        pass

    def get_independent_lru(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_independent_lru()
        
        /**
         * Returns a pointer to the global LRU object that manages the
         * GeomVertexArrayData's that have not (yet) been paged out.
         */
        """
        pass

    def get_modified(self, GeomVertexArrayData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_modified(GeomVertexArrayData self)
        
        /**
         * Returns a sequence number which is guaranteed to change at least every time
         * the array vertex data is modified.
         */
        """
        pass

    def get_num_rows(self, GeomVertexArrayData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_rows(GeomVertexArrayData self)
        
        /**
         * Returns the number of rows stored in the array, based on the number of
         * bytes and the stride.  This should be the same for all arrays within a
         * given GeomVertexData object.
         */
        """
        pass

    def get_small_lru(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_small_lru()
        
        /**
         * Returns a pointer to the global LRU object that manages the
         * GeomVertexArrayData's that are deemed too small to be paged out.
         */
        """
        pass

    def get_usage_hint(self, GeomVertexArrayData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_usage_hint(GeomVertexArrayData self)
        
        /**
         * Returns the usage hint that describes to the rendering backend how often
         * the vertex data will be modified and/or rendered.  See geomEnums.h.
         */
        """
        pass

    def hasColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_column(GeomVertexArrayData self, const InternalName name)
        
        /**
         * Returns true if the array has the named column, false otherwise.  This is
         * really just a shortcut for asking the same thing from the format.
         */
        """
        pass

    def has_column(self, GeomVertexArrayData_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_column(GeomVertexArrayData self, const InternalName name)
        
        /**
         * Returns true if the array has the named column, false otherwise.  This is
         * really just a shortcut for asking the same thing from the format.
         */
        """
        pass

    def isPrepared(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_prepared(GeomVertexArrayData self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the data has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def is_prepared(self, GeomVertexArrayData_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_prepared(GeomVertexArrayData self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Returns true if the data has already been prepared or enqueued for
         * preparation on the indicated GSG, false otherwise.
         */
        """
        pass

    def lruEpoch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        lru_epoch()
        
        /**
         * Marks that an epoch has passed in each LRU.  Asks the LRU's to consider
         * whether they should perform evictions.
         */
        """
        pass

    def lru_epoch(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        lru_epoch()
        
        /**
         * Marks that an epoch has passed in each LRU.  Asks the LRU's to consider
         * whether they should perform evictions.
         */
        """
        pass

    def modifyHandle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_handle(const GeomVertexArrayData self, Thread current_thread)
        
        /**
         * Returns an object that can be used to read or write the actual data bytes
         * stored in the array.  Calling this method locks the data, and will block
         * any other threads attempting to read or write the data, until the returned
         * object destructs.
         */
        """
        pass

    def modify_handle(self, const_GeomVertexArrayData_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_handle(const GeomVertexArrayData self, Thread current_thread)
        
        /**
         * Returns an object that can be used to read or write the actual data bytes
         * stored in the array.  Calling this method locks the data, and will block
         * any other threads attempting to read or write the data, until the returned
         * object destructs.
         */
        """
        pass

    def output(self, GeomVertexArrayData_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GeomVertexArrayData self, ostream out)
        
        /**
         *
         */
        """
        pass

    def prepare(self, const_GeomVertexArrayData_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare(const GeomVertexArrayData self, PreparedGraphicsObjects prepared_objects)
        
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
        prepare_now(const GeomVertexArrayData self, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
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

    def prepare_now(self, const_GeomVertexArrayData_self, PreparedGraphicsObjects_prepared_objects, GraphicsStateGuardianBase_gsg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        prepare_now(const GeomVertexArrayData self, PreparedGraphicsObjects prepared_objects, GraphicsStateGuardianBase gsg)
        
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

    def release(self, const_GeomVertexArrayData_self, PreparedGraphicsObjects_prepared_objects): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release(const GeomVertexArrayData self, PreparedGraphicsObjects prepared_objects)
        
        /**
         * Frees the data context only on the indicated object, if it exists there.
         * Returns true if it was released, false if it had not been prepared.
         */
        """
        pass

    def releaseAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        release_all(const GeomVertexArrayData self)
        
        /**
         * Frees the context allocated on all objects for which the data has been
         * declared.  Returns the number of contexts which have been freed.
         */
        """
        pass

    def release_all(self, const_GeomVertexArrayData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        release_all(const GeomVertexArrayData self)
        
        /**
         * Frees the context allocated on all objects for which the data has been
         * declared.  Returns the number of contexts which have been freed.
         */
        """
        pass

    def requestResident(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        request_resident(GeomVertexArrayData self, Thread current_thread)
        
        /**
         * Returns true if the vertex data is currently resident in memory.  If this
         * returns true, the next call to get_handle()->get_read_pointer() will
         * probably not block.  If this returns false, the vertex data will be brought
         * back into memory shortly; try again later.
         */
        """
        pass

    def request_resident(self, GeomVertexArrayData_self, Thread_current_thread): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        request_resident(GeomVertexArrayData self, Thread current_thread)
        
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
        reserve_num_rows(const GeomVertexArrayData self, int n)
        
        /**
         * This ensures that enough memory space for n rows is allocated, so that you
         * may increase the number of rows to n without causing a new memory
         * allocation.  This is a performance optimization only; it is especially
         * useful when you know ahead of time that you will be adding n rows to the
         * data.
         */
        """
        pass

    def reserve_num_rows(self, const_GeomVertexArrayData_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reserve_num_rows(const GeomVertexArrayData self, int n)
        
        /**
         * This ensures that enough memory space for n rows is allocated, so that you
         * may increase the number of rows to n without causing a new memory
         * allocation.  This is a performance optimization only; it is especially
         * useful when you know ahead of time that you will be adding n rows to the
         * data.
         */
        """
        pass

    def setNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_num_rows(const GeomVertexArrayData self, int n)
        
        /**
         * Sets the length of the array to n rows.
         *
         * Normally, you would not call this directly, since all of the arrays in a
         * particular GeomVertexData must have the same number of rows; instead, call
         * GeomVertexData::set_num_rows().
         *
         * The return value is true if the number of rows was changed, false if the
         * object already contained n rows (or if there was some error).
         *
         * The new vertex data is initialized to 0, including the "color" column (but
         * see GeomVertexData::set_num_rows()).
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def setUsageHint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_usage_hint(const GeomVertexArrayData self, int usage_hint)
        
        /**
         * Changes the UsageHint hint for this array.  See get_usage_hint().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_num_rows(self, const_GeomVertexArrayData_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_num_rows(const GeomVertexArrayData self, int n)
        
        /**
         * Sets the length of the array to n rows.
         *
         * Normally, you would not call this directly, since all of the arrays in a
         * particular GeomVertexData must have the same number of rows; instead, call
         * GeomVertexData::set_num_rows().
         *
         * The return value is true if the number of rows was changed, false if the
         * object already contained n rows (or if there was some error).
         *
         * The new vertex data is initialized to 0, including the "color" column (but
         * see GeomVertexData::set_num_rows()).
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def set_usage_hint(self, const_GeomVertexArrayData_self, int_usage_hint): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_usage_hint(const GeomVertexArrayData self, int usage_hint)
        
        /**
         * Changes the UsageHint hint for this array.  See get_usage_hint().
         *
         * Don't call this in a downstream thread unless you don't mind it blowing
         * away other changes you might have recently made in an upstream thread.
         */
        """
        pass

    def uncleanSetNumRows(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        unclean_set_num_rows(const GeomVertexArrayData self, int n)
        
        /**
         * This method behaves like set_num_rows(), except the new data is not
         * initialized.  Furthermore, after this call, *any* of the data in the
         * GeomVertexArrayData may be uninitialized, including the earlier rows.
         *
         * Normally, you would not call this directly, since all of the arrays in a
         * particular GeomVertexData must have the same number of rows; instead, call
         * GeomVertexData::unclean_set_num_rows().
         */
        """
        pass

    def unclean_set_num_rows(self, const_GeomVertexArrayData_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unclean_set_num_rows(const GeomVertexArrayData self, int n)
        
        /**
         * This method behaves like set_num_rows(), except the new data is not
         * initialized.  Furthermore, after this call, *any* of the data in the
         * GeomVertexArrayData may be uninitialized, including the earlier rows.
         *
         * Normally, you would not call this directly, since all of the arrays in a
         * particular GeomVertexData must have the same number of rows; instead, call
         * GeomVertexData::unclean_set_num_rows().
         */
        """
        pass

    def upcastToCopyOnWriteObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_CopyOnWriteObject(const GeomVertexArrayData self)
        
        upcast from GeomVertexArrayData to CopyOnWriteObject
        """
        pass

    def upcastToGeomEnums(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomVertexArrayData self)
        
        upcast from GeomVertexArrayData to GeomEnums
        """
        pass

    def upcastToSimpleLruPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_SimpleLruPage(const GeomVertexArrayData self)
        
        upcast from GeomVertexArrayData to SimpleLruPage
        """
        pass

    def upcast_to_CopyOnWriteObject(self, const_GeomVertexArrayData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_CopyOnWriteObject(const GeomVertexArrayData self)
        
        upcast from GeomVertexArrayData to CopyOnWriteObject
        """
        pass

    def upcast_to_GeomEnums(self, const_GeomVertexArrayData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomVertexArrayData self)
        
        upcast from GeomVertexArrayData to GeomEnums
        """
        pass

    def upcast_to_SimpleLruPage(self, const_GeomVertexArrayData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_SimpleLruPage(const GeomVertexArrayData self)
        
        upcast from GeomVertexArrayData to SimpleLruPage
        """
        pass

    def write(self, GeomVertexArrayData_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(GeomVertexArrayData self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    array_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_size_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usage_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__doc__': '/**\n * This is the data for one array of a GeomVertexData structure.  Many\n * GeomVertexData structures will only define one array, with all data\n * elements interleaved (DirectX 8.0 and before insisted on this format); some\n * will define multiple arrays.\n *\n * DirectX calls this concept of one array a "stream". It also closely\n * correlates with the concept of a vertex buffer.\n *\n * This object is just a block of data.  In general, you should not be\n * directly messing with this object from application code.  See\n * GeomVertexData for the organizing structure, and see\n * GeomVertexReader/Writer/Rewriter for high-level tools to manipulate the\n * actual vertex data.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FB340>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GeomVertexArrayData' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GeomVertexArrayData' objects>"
        'array_format': None, # (!) real value is "<attribute 'array_format' of 'panda3d.core.GeomVertexArrayData' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GeomVertexArrayData' objects>"
        'clearRows': None, # (!) real value is "<method 'clearRows' of 'panda3d.core.GeomVertexArrayData' objects>"
        'clear_rows': None, # (!) real value is "<method 'clear_rows' of 'panda3d.core.GeomVertexArrayData' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.GeomVertexArrayData' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.GeomVertexArrayData' objects>"
        'data_size_bytes': None, # (!) real value is "<attribute 'data_size_bytes' of 'panda3d.core.GeomVertexArrayData' objects>"
        'getArrayFormat': None, # (!) real value is "<method 'getArrayFormat' of 'panda3d.core.GeomVertexArrayData' objects>"
        'getBook': None, # (!) real value is '<staticmethod(<built-in method getBook of type object at 0x00007FFCFE2FB340>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FB340>)>'
        'getDataSizeBytes': None, # (!) real value is "<method 'getDataSizeBytes' of 'panda3d.core.GeomVertexArrayData' objects>"
        'getHandle': None, # (!) real value is "<method 'getHandle' of 'panda3d.core.GeomVertexArrayData' objects>"
        'getIndependentLru': None, # (!) real value is '<staticmethod(<built-in method getIndependentLru of type object at 0x00007FFCFE2FB340>)>'
        'getModified': None, # (!) real value is "<method 'getModified' of 'panda3d.core.GeomVertexArrayData' objects>"
        'getNumRows': None, # (!) real value is "<method 'getNumRows' of 'panda3d.core.GeomVertexArrayData' objects>"
        'getSmallLru': None, # (!) real value is '<staticmethod(<built-in method getSmallLru of type object at 0x00007FFCFE2FB340>)>'
        'getUsageHint': None, # (!) real value is "<method 'getUsageHint' of 'panda3d.core.GeomVertexArrayData' objects>"
        'get_array_format': None, # (!) real value is "<method 'get_array_format' of 'panda3d.core.GeomVertexArrayData' objects>"
        'get_book': None, # (!) real value is '<staticmethod(<built-in method get_book of type object at 0x00007FFCFE2FB340>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FB340>)>'
        'get_data_size_bytes': None, # (!) real value is "<method 'get_data_size_bytes' of 'panda3d.core.GeomVertexArrayData' objects>"
        'get_handle': None, # (!) real value is "<method 'get_handle' of 'panda3d.core.GeomVertexArrayData' objects>"
        'get_independent_lru': None, # (!) real value is '<staticmethod(<built-in method get_independent_lru of type object at 0x00007FFCFE2FB340>)>'
        'get_modified': None, # (!) real value is "<method 'get_modified' of 'panda3d.core.GeomVertexArrayData' objects>"
        'get_num_rows': None, # (!) real value is "<method 'get_num_rows' of 'panda3d.core.GeomVertexArrayData' objects>"
        'get_small_lru': None, # (!) real value is '<staticmethod(<built-in method get_small_lru of type object at 0x00007FFCFE2FB340>)>'
        'get_usage_hint': None, # (!) real value is "<method 'get_usage_hint' of 'panda3d.core.GeomVertexArrayData' objects>"
        'hasColumn': None, # (!) real value is "<method 'hasColumn' of 'panda3d.core.GeomVertexArrayData' objects>"
        'has_column': None, # (!) real value is "<method 'has_column' of 'panda3d.core.GeomVertexArrayData' objects>"
        'isPrepared': None, # (!) real value is "<method 'isPrepared' of 'panda3d.core.GeomVertexArrayData' objects>"
        'is_prepared': None, # (!) real value is "<method 'is_prepared' of 'panda3d.core.GeomVertexArrayData' objects>"
        'lruEpoch': None, # (!) real value is '<staticmethod(<built-in method lruEpoch of type object at 0x00007FFCFE2FB340>)>'
        'lru_epoch': None, # (!) real value is '<staticmethod(<built-in method lru_epoch of type object at 0x00007FFCFE2FB340>)>'
        'modified': None, # (!) real value is "<attribute 'modified' of 'panda3d.core.GeomVertexArrayData' objects>"
        'modifyHandle': None, # (!) real value is "<method 'modifyHandle' of 'panda3d.core.GeomVertexArrayData' objects>"
        'modify_handle': None, # (!) real value is "<method 'modify_handle' of 'panda3d.core.GeomVertexArrayData' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GeomVertexArrayData' objects>"
        'prepare': None, # (!) real value is "<method 'prepare' of 'panda3d.core.GeomVertexArrayData' objects>"
        'prepareNow': None, # (!) real value is "<method 'prepareNow' of 'panda3d.core.GeomVertexArrayData' objects>"
        'prepare_now': None, # (!) real value is "<method 'prepare_now' of 'panda3d.core.GeomVertexArrayData' objects>"
        'release': None, # (!) real value is "<method 'release' of 'panda3d.core.GeomVertexArrayData' objects>"
        'releaseAll': None, # (!) real value is "<method 'releaseAll' of 'panda3d.core.GeomVertexArrayData' objects>"
        'release_all': None, # (!) real value is "<method 'release_all' of 'panda3d.core.GeomVertexArrayData' objects>"
        'requestResident': None, # (!) real value is "<method 'requestResident' of 'panda3d.core.GeomVertexArrayData' objects>"
        'request_resident': None, # (!) real value is "<method 'request_resident' of 'panda3d.core.GeomVertexArrayData' objects>"
        'reserveNumRows': None, # (!) real value is "<method 'reserveNumRows' of 'panda3d.core.GeomVertexArrayData' objects>"
        'reserve_num_rows': None, # (!) real value is "<method 'reserve_num_rows' of 'panda3d.core.GeomVertexArrayData' objects>"
        'setNumRows': None, # (!) real value is "<method 'setNumRows' of 'panda3d.core.GeomVertexArrayData' objects>"
        'setUsageHint': None, # (!) real value is "<method 'setUsageHint' of 'panda3d.core.GeomVertexArrayData' objects>"
        'set_num_rows': None, # (!) real value is "<method 'set_num_rows' of 'panda3d.core.GeomVertexArrayData' objects>"
        'set_usage_hint': None, # (!) real value is "<method 'set_usage_hint' of 'panda3d.core.GeomVertexArrayData' objects>"
        'uncleanSetNumRows': None, # (!) real value is "<method 'uncleanSetNumRows' of 'panda3d.core.GeomVertexArrayData' objects>"
        'unclean_set_num_rows': None, # (!) real value is "<method 'unclean_set_num_rows' of 'panda3d.core.GeomVertexArrayData' objects>"
        'upcastToCopyOnWriteObject': None, # (!) real value is "<method 'upcastToCopyOnWriteObject' of 'panda3d.core.GeomVertexArrayData' objects>"
        'upcastToGeomEnums': None, # (!) real value is "<method 'upcastToGeomEnums' of 'panda3d.core.GeomVertexArrayData' objects>"
        'upcastToSimpleLruPage': None, # (!) real value is "<method 'upcastToSimpleLruPage' of 'panda3d.core.GeomVertexArrayData' objects>"
        'upcast_to_CopyOnWriteObject': None, # (!) real value is "<method 'upcast_to_CopyOnWriteObject' of 'panda3d.core.GeomVertexArrayData' objects>"
        'upcast_to_GeomEnums': None, # (!) real value is "<method 'upcast_to_GeomEnums' of 'panda3d.core.GeomVertexArrayData' objects>"
        'upcast_to_SimpleLruPage': None, # (!) real value is "<method 'upcast_to_SimpleLruPage' of 'panda3d.core.GeomVertexArrayData' objects>"
        'usage_hint': None, # (!) real value is "<attribute 'usage_hint' of 'panda3d.core.GeomVertexArrayData' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.GeomVertexArrayData' objects>"
    }


