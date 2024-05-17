# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class BamCacheRecord(TypedWritableReferenceCount):
    """
    /**
     * An instance of this class is written to the front of a Bam or Txo file to
     * make the file a cached instance of some other loadable resource.  This
     * record contains information needed to test the validity of the cache.
     */
    """
    def addDependentFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_dependent_file(const BamCacheRecord self, const VirtualFile file)
        
        /**
         * Adds the indicated file to the list of files that will be loaded to
         * generate the data in this record.  This should be called once for the
         * primary source file, and again for each secondary source file, if any.
         */
        
        /**
         * Variant of add_dependent_file that takes an already opened VirtualFile.
         */
        """
        pass

    def add_dependent_file(self, const_BamCacheRecord_self, const_VirtualFile_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_dependent_file(const BamCacheRecord self, const VirtualFile file)
        
        /**
         * Adds the indicated file to the list of files that will be loaded to
         * generate the data in this record.  This should be called once for the
         * primary source file, and again for each secondary source file, if any.
         */
        
        /**
         * Variant of add_dependent_file that takes an already opened VirtualFile.
         */
        """
        pass

    def clearData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_data(const BamCacheRecord self)
        
        /**
         * Removes the in-memory data object associated with this record, if any.
         * This does not affect the on-disk representation of the record.
         */
        """
        pass

    def clearDependentFiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_dependent_files(const BamCacheRecord self)
        
        /**
         * Empties the list of files that contribute to the data in this record.
         */
        """
        pass

    def clear_data(self, const_BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_data(const BamCacheRecord self)
        
        /**
         * Removes the in-memory data object associated with this record, if any.
         * This does not affect the on-disk representation of the record.
         */
        """
        pass

    def clear_dependent_files(self, const_BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_dependent_files(const BamCacheRecord self)
        
        /**
         * Empties the list of files that contribute to the data in this record.
         */
        """
        pass

    def dependentsUnchanged(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        dependents_unchanged(BamCacheRecord self)
        
        /**
         * Returns true if all of the dependent files are still the same as when the
         * cache was recorded, false otherwise.
         */
        """
        pass

    def dependents_unchanged(self, BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        dependents_unchanged(BamCacheRecord self)
        
        /**
         * Returns true if all of the dependent files are still the same as when the
         * cache was recorded, false otherwise.
         */
        """
        pass

    def getCacheFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cache_filename(BamCacheRecord self)
        
        /**
         * Returns the name of the cache file as hashed from the source_pathname.
         * This will be relative to the root of the cache directory, and it will not
         * include any suffixes that may be appended to resolve hash conflicts.
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
        get_data(BamCacheRecord self)
        
        /**
         * Returns a pointer to the data stored in the record, or NULL if there is no
         * data.  The pointer is not removed from the record.
         */
        """
        pass

    def getDependentPathname(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dependent_pathname(BamCacheRecord self, int n)
        
        /**
         * Returns the full pathname of the nth source files that contributes to the
         * cache.
         */
        """
        pass

    def getNumDependentFiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_dependent_files(BamCacheRecord self)
        
        /**
         * Returns the number of source files that contribute to the cache.
         */
        """
        pass

    def getRecordedTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_recorded_time(BamCacheRecord self)
        
        /**
         * Returns the time at which this particular record was recorded or updated.
         */
        """
        pass

    def getSourcePathname(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_source_pathname(BamCacheRecord self)
        
        /**
         * Returns the full pathname to the source file that originally generated this
         * cache request.  In some cases, for instance in the case of a of a multipage
         * texture like "cube_#.png", this may not not a true filename on disk.
         */
        """
        pass

    def getSourceTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_source_timestamp(BamCacheRecord self)
        
        /**
         * Returns the file timestamp of the original source file that generated this
         * cache record, if available.  In some cases the original file timestamp is
         * not available, and this will return 0.
         */
        """
        pass

    def get_cache_filename(self, BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cache_filename(BamCacheRecord self)
        
        /**
         * Returns the name of the cache file as hashed from the source_pathname.
         * This will be relative to the root of the cache directory, and it will not
         * include any suffixes that may be appended to resolve hash conflicts.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_data(self, BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data(BamCacheRecord self)
        
        /**
         * Returns a pointer to the data stored in the record, or NULL if there is no
         * data.  The pointer is not removed from the record.
         */
        """
        pass

    def get_dependent_pathname(self, BamCacheRecord_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dependent_pathname(BamCacheRecord self, int n)
        
        /**
         * Returns the full pathname of the nth source files that contributes to the
         * cache.
         */
        """
        pass

    def get_num_dependent_files(self, BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_dependent_files(BamCacheRecord self)
        
        /**
         * Returns the number of source files that contribute to the cache.
         */
        """
        pass

    def get_recorded_time(self, BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_recorded_time(BamCacheRecord self)
        
        /**
         * Returns the time at which this particular record was recorded or updated.
         */
        """
        pass

    def get_source_pathname(self, BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_source_pathname(BamCacheRecord self)
        
        /**
         * Returns the full pathname to the source file that originally generated this
         * cache request.  In some cases, for instance in the case of a of a multipage
         * texture like "cube_#.png", this may not not a true filename on disk.
         */
        """
        pass

    def get_source_timestamp(self, BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_source_timestamp(BamCacheRecord self)
        
        /**
         * Returns the file timestamp of the original source file that generated this
         * cache record, if available.  In some cases the original file timestamp is
         * not available, and this will return 0.
         */
        """
        pass

    def hasData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_data(BamCacheRecord self)
        
        /**
         * Returns true if this cache record has an in-memory data object associated--
         * that is, the object stored in the cache.
         */
        """
        pass

    def has_data(self, BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_data(BamCacheRecord self)
        
        /**
         * Returns true if this cache record has an in-memory data object associated--
         * that is, the object stored in the cache.
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(BamCacheRecord self)
        
        /**
         * Returns a duplicate of the BamCacheRecord.  The duplicate will not have a
         * data pointer set, even though one may have been assigned to the original
         * via set_data().
         */
        """
        pass

    def make_copy(self, BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(BamCacheRecord self)
        
        /**
         * Returns a duplicate of the BamCacheRecord.  The duplicate will not have a
         * data pointer set, even though one may have been assigned to the original
         * via set_data().
         */
        """
        pass

    def output(self, BamCacheRecord_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(BamCacheRecord self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_data(const BamCacheRecord self, TypedWritableReferenceCount ptr)
        set_data(const BamCacheRecord self, TypedWritable ptr)
        set_data(const BamCacheRecord self, TypedWritable ptr, ReferenceCount ref_ptr)
        set_data(const BamCacheRecord self, TypedWritable ptr, int dummy)
        
        /**
         * Stores a new data object on the record.  You should pass the same pointer
         * twice, to both parameters; this allows the C++ typecasting to automatically
         * convert the pointer into both a TypedWritable and a ReferenceCount pointer,
         * so that the BamCacheRecord object can reliably manage the reference counts.
         *
         * You may pass 0 or NULL as the second parameter.  If you do this, the
         * BamCacheRecord will not manage the object's reference count; it will be up
         * to you to ensure the object is not deleted during the lifetime of the
         * BamCacheRecord object.
         */
        
        /**
         * This variant on set_data() is provided to easily pass objects deriving from
         * TypedWritable.
         */
        
        /**
         * This variant on set_data() is provided to easily pass objects deriving from
         * TypedWritableReferenceCount.
         */
        
        /**
         * This variant on set_data() is provided just to allow Python code to pass a
         * 0 as the second parameter.
         */
        """
        pass

    def set_data(self, const_BamCacheRecord_self, TypedWritableReferenceCount_ptr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_data(const BamCacheRecord self, TypedWritableReferenceCount ptr)
        set_data(const BamCacheRecord self, TypedWritable ptr)
        set_data(const BamCacheRecord self, TypedWritable ptr, ReferenceCount ref_ptr)
        set_data(const BamCacheRecord self, TypedWritable ptr, int dummy)
        
        /**
         * Stores a new data object on the record.  You should pass the same pointer
         * twice, to both parameters; this allows the C++ typecasting to automatically
         * convert the pointer into both a TypedWritable and a ReferenceCount pointer,
         * so that the BamCacheRecord object can reliably manage the reference counts.
         *
         * You may pass 0 or NULL as the second parameter.  If you do this, the
         * BamCacheRecord will not manage the object's reference count; it will be up
         * to you to ensure the object is not deleted during the lifetime of the
         * BamCacheRecord object.
         */
        
        /**
         * This variant on set_data() is provided to easily pass objects deriving from
         * TypedWritable.
         */
        
        /**
         * This variant on set_data() is provided to easily pass objects deriving from
         * TypedWritableReferenceCount.
         */
        
        /**
         * This variant on set_data() is provided just to allow Python code to pass a
         * 0 as the second parameter.
         */
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const BamCacheRecord self)
        
        upcast from BamCacheRecord to TypedWritableReferenceCount
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_BamCacheRecord_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const BamCacheRecord self)
        
        upcast from BamCacheRecord to TypedWritableReferenceCount
        """
        pass

    def write(self, BamCacheRecord_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(BamCacheRecord self, ostream out, int indent_level)
        
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

    cache_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    recorded_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_pathname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.BamCacheRecord' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.BamCacheRecord' objects>"
        '__doc__': '/**\n * An instance of this class is written to the front of a Bam or Txo file to\n * make the file a cached instance of some other loadable resource.  This\n * record contains information needed to test the validity of the cache.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.BamCacheRecord' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.BamCacheRecord' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.BamCacheRecord' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.BamCacheRecord' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BamCacheRecord' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.BamCacheRecord' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.BamCacheRecord' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.BamCacheRecord' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE36F8D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.BamCacheRecord' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.BamCacheRecord' objects>"
        'addDependentFile': None, # (!) real value is "<method 'addDependentFile' of 'panda3d.core.BamCacheRecord' objects>"
        'add_dependent_file': None, # (!) real value is "<method 'add_dependent_file' of 'panda3d.core.BamCacheRecord' objects>"
        'cache_filename': None, # (!) real value is "<attribute 'cache_filename' of 'panda3d.core.BamCacheRecord' objects>"
        'clearData': None, # (!) real value is "<method 'clearData' of 'panda3d.core.BamCacheRecord' objects>"
        'clearDependentFiles': None, # (!) real value is "<method 'clearDependentFiles' of 'panda3d.core.BamCacheRecord' objects>"
        'clear_data': None, # (!) real value is "<method 'clear_data' of 'panda3d.core.BamCacheRecord' objects>"
        'clear_dependent_files': None, # (!) real value is "<method 'clear_dependent_files' of 'panda3d.core.BamCacheRecord' objects>"
        'data': None, # (!) real value is "<attribute 'data' of 'panda3d.core.BamCacheRecord' objects>"
        'dependentsUnchanged': None, # (!) real value is "<method 'dependentsUnchanged' of 'panda3d.core.BamCacheRecord' objects>"
        'dependents_unchanged': None, # (!) real value is "<method 'dependents_unchanged' of 'panda3d.core.BamCacheRecord' objects>"
        'getCacheFilename': None, # (!) real value is "<method 'getCacheFilename' of 'panda3d.core.BamCacheRecord' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE36F8D0>)>'
        'getData': None, # (!) real value is "<method 'getData' of 'panda3d.core.BamCacheRecord' objects>"
        'getDependentPathname': None, # (!) real value is "<method 'getDependentPathname' of 'panda3d.core.BamCacheRecord' objects>"
        'getNumDependentFiles': None, # (!) real value is "<method 'getNumDependentFiles' of 'panda3d.core.BamCacheRecord' objects>"
        'getRecordedTime': None, # (!) real value is "<method 'getRecordedTime' of 'panda3d.core.BamCacheRecord' objects>"
        'getSourcePathname': None, # (!) real value is "<method 'getSourcePathname' of 'panda3d.core.BamCacheRecord' objects>"
        'getSourceTimestamp': None, # (!) real value is "<method 'getSourceTimestamp' of 'panda3d.core.BamCacheRecord' objects>"
        'get_cache_filename': None, # (!) real value is "<method 'get_cache_filename' of 'panda3d.core.BamCacheRecord' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE36F8D0>)>'
        'get_data': None, # (!) real value is "<method 'get_data' of 'panda3d.core.BamCacheRecord' objects>"
        'get_dependent_pathname': None, # (!) real value is "<method 'get_dependent_pathname' of 'panda3d.core.BamCacheRecord' objects>"
        'get_num_dependent_files': None, # (!) real value is "<method 'get_num_dependent_files' of 'panda3d.core.BamCacheRecord' objects>"
        'get_recorded_time': None, # (!) real value is "<method 'get_recorded_time' of 'panda3d.core.BamCacheRecord' objects>"
        'get_source_pathname': None, # (!) real value is "<method 'get_source_pathname' of 'panda3d.core.BamCacheRecord' objects>"
        'get_source_timestamp': None, # (!) real value is "<method 'get_source_timestamp' of 'panda3d.core.BamCacheRecord' objects>"
        'hasData': None, # (!) real value is "<method 'hasData' of 'panda3d.core.BamCacheRecord' objects>"
        'has_data': None, # (!) real value is "<method 'has_data' of 'panda3d.core.BamCacheRecord' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.core.BamCacheRecord' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.core.BamCacheRecord' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.BamCacheRecord' objects>"
        'recorded_time': None, # (!) real value is "<attribute 'recorded_time' of 'panda3d.core.BamCacheRecord' objects>"
        'setData': None, # (!) real value is "<method 'setData' of 'panda3d.core.BamCacheRecord' objects>"
        'set_data': None, # (!) real value is "<method 'set_data' of 'panda3d.core.BamCacheRecord' objects>"
        'source_pathname': None, # (!) real value is "<attribute 'source_pathname' of 'panda3d.core.BamCacheRecord' objects>"
        'source_timestamp': None, # (!) real value is "<attribute 'source_timestamp' of 'panda3d.core.BamCacheRecord' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.BamCacheRecord' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.BamCacheRecord' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.BamCacheRecord' objects>"
    }


