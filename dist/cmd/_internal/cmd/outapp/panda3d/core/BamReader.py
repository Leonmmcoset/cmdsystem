# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .BamEnums import BamEnums

class BamReader(BamEnums):
    """
    /**
     * This is the fundamental interface for extracting binary objects from a Bam
     * file, as generated by a BamWriter.
     *
     * A Bam file can be thought of as a linear collection of objects.  Each
     * object is an instance of a class that inherits, directly or indirectly,
     * from TypedWritable.  The objects may include pointers to other objects
     * within the Bam file; the BamReader automatically manages these (with help
     * from code within each class) and restores the pointers correctly.
     *
     * This is the abstract interface and does not specifically deal with disk
     * files, but rather with a DatagramGenerator of some kind, which is simply a
     * linear source of Datagrams.  It is probably from a disk file, but it might
     * conceivably be streamed directly from a network or some such nonsense.
     *
     * Bam files are most often used to store scene graphs or subgraphs, and by
     * convention they are given filenames ending in the extension ".bam" when
     * they are used for this purpose.  However, a Bam file may store any
     * arbitrary list of TypedWritable objects; in this more general usage, they
     * are given filenames ending in ".boo" to differentiate them from the more
     * common scene graph files.
     *
     * See also BamFile, which defines a higher-level interface to read and write
     * Bam files on disk.
     */
    """
    def changePointer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        change_pointer(const BamReader self, const TypedWritable orig_pointer, const TypedWritable new_pointer)
        
        /**
         * Indicates that an object recently read from the bam stream should be
         * replaced with a new object.  Any future occurrences of the original object
         * in the stream will henceforth return the new object instead.
         *
         * The return value is true if the replacement was successfully made, or false
         * if the object was not read from the stream (or if change_pointer had
         * already been called on it).
         */
        """
        pass

    def change_pointer(self, const_BamReader_self, const_TypedWritable_orig_pointer, const_TypedWritable_new_pointer): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        change_pointer(const BamReader self, const TypedWritable orig_pointer, const TypedWritable new_pointer)
        
        /**
         * Indicates that an object recently read from the bam stream should be
         * replaced with a new object.  Any future occurrences of the original object
         * in the stream will henceforth return the new object instead.
         *
         * The return value is true if the replacement was successfully made, or false
         * if the object was not read from the stream (or if change_pointer had
         * already been called on it).
         */
        """
        pass

    def getCurrentMajorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_major_ver(BamReader self)
        
        /**
         * Returns the major version number of Bam files supported by the current code
         * base.  This must match get_file_major_ver() in order to successfully read a
         * file.
         */
        """
        pass

    def getCurrentMinorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_current_minor_ver(BamReader self)
        
        /**
         * Returns the minor version number of Bam files supported by the current code
         * base.  This must match or exceed get_file_minor_ver() in order to
         * successfully read a file.
         */
        """
        pass

    def getFileEndian(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_endian(BamReader self)
        
        /**
         * Returns the endian preference indicated by the Bam file currently being
         * read.  This does not imply that every number is stored using the indicated
         * convention, but individual objects may choose to respect this flag when
         * recording data.
         */
        """
        pass

    def getFileMajorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_major_ver(BamReader self)
        
        /**
         * Returns the major version number of the Bam file currently being read.
         */
        """
        pass

    def getFileMinorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_minor_ver(BamReader self)
        
        /**
         * Returns the minor version number of the Bam file currently being read.
         */
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(BamReader self)
        
        /**
         * If a BAM is a file, then the BamReader should contain the name of the file.
         * This enables the reader to interpret pathnames in the BAM as relative to
         * the directory containing the BAM.
         */
        """
        pass

    def getFileStdfloatDouble(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_stdfloat_double(BamReader self)
        
        /**
         * Returns true if the file stores all "standard" floats as 64-bit doubles, or
         * false if they are 32-bit floats.  This is determined by the compilation
         * flags of the version of Panda that generated this file.
         */
        """
        pass

    def getFileVersion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_version(BamReader self)
        """
        pass

    def getLoaderOptions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_loader_options(BamReader self)
        
        /**
         * Returns the LoaderOptions passed to the loader when the model was
         * requested, if any.
         */
        """
        pass

    def getSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_source(const BamReader self)
        
        /**
         * Returns the current source of the BamReader as set by set_source() or the
         * constructor.
         */
        """
        pass

    def get_current_major_ver(self, BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_major_ver(BamReader self)
        
        /**
         * Returns the major version number of Bam files supported by the current code
         * base.  This must match get_file_major_ver() in order to successfully read a
         * file.
         */
        """
        pass

    def get_current_minor_ver(self, BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_current_minor_ver(BamReader self)
        
        /**
         * Returns the minor version number of Bam files supported by the current code
         * base.  This must match or exceed get_file_minor_ver() in order to
         * successfully read a file.
         */
        """
        pass

    def get_filename(self, BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(BamReader self)
        
        /**
         * If a BAM is a file, then the BamReader should contain the name of the file.
         * This enables the reader to interpret pathnames in the BAM as relative to
         * the directory containing the BAM.
         */
        """
        pass

    def get_file_endian(self, BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_endian(BamReader self)
        
        /**
         * Returns the endian preference indicated by the Bam file currently being
         * read.  This does not imply that every number is stored using the indicated
         * convention, but individual objects may choose to respect this flag when
         * recording data.
         */
        """
        pass

    def get_file_major_ver(self, BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_major_ver(BamReader self)
        
        /**
         * Returns the major version number of the Bam file currently being read.
         */
        """
        pass

    def get_file_minor_ver(self, BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_minor_ver(BamReader self)
        
        /**
         * Returns the minor version number of the Bam file currently being read.
         */
        """
        pass

    def get_file_stdfloat_double(self, BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_stdfloat_double(BamReader self)
        
        /**
         * Returns true if the file stores all "standard" floats as 64-bit doubles, or
         * false if they are 32-bit floats.  This is determined by the compilation
         * flags of the version of Panda that generated this file.
         */
        """
        pass

    def get_file_version(self, BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_version(BamReader self)
        """
        pass

    def get_loader_options(self, BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_loader_options(BamReader self)
        
        /**
         * Returns the LoaderOptions passed to the loader when the model was
         * requested, if any.
         */
        """
        pass

    def get_source(self, const_BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_source(const BamReader self)
        
        /**
         * Returns the current source of the BamReader as set by set_source() or the
         * constructor.
         */
        """
        pass

    def init(self, const_BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        init(const BamReader self)
        
        /**
         * Initializes the BamReader prior to reading any objects from its source.
         * This includes reading the Bam header.
         *
         * This returns true if the BamReader successfully initialized, false
         * otherwise.
         */
        """
        pass

    def isEof(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_eof(BamReader self)
        
        /**
         * Returns true if the reader has reached end-of-file, false otherwise.  This
         * call is only valid after a call to read_object().
         */
        """
        pass

    def is_eof(self, BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_eof(BamReader self)
        
        /**
         * Returns true if the reader has reached end-of-file, false otherwise.  This
         * call is only valid after a call to read_object().
         */
        """
        pass

    def readObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_object(const BamReader self)
        
        /**
         * Reads a single object from the Bam file.  If the object type is known, a
         * new object of the appropriate type is created and returned; otherwise, NULL
         * is returned.  NULL is also returned when the end of the file is reached.
         * is_eof() may be called to differentiate between these two cases.
         *
         * This may be called repeatedly to extract out all the objects in the Bam
         * file, but typically (especially for scene graph files, indicated with the
         * .bam extension), only one object is retrieved directly from the Bam file:
         * the root of the scene graph.  The remaining objects will all be retrieved
         * recursively by the first object.
         *
         * Note that the object returned may not yet be complete.  In particular, some
         * of its pointers may not be filled in; you must call resolve() to fill in
         * all the available pointers before you can safely use any objects returned
         * by read_object().
         *
         * This flavor of read_object() requires the caller to know what type of
         * object it has received in order to properly manage the reference counts.
         */
        
        /**
         * Reads a single object from the Bam file.
         *
         * This flavor of read_object() returns both a TypedWritable and a
         * ReferenceCount pointer to the same object, so the reference count may be
         * tracked reliably, without having to know precisely what type of object we
         * have.
         * @return true on success, or false on failure.
         */
        """
        pass

    def read_object(self, const_BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_object(const BamReader self)
        
        /**
         * Reads a single object from the Bam file.  If the object type is known, a
         * new object of the appropriate type is created and returned; otherwise, NULL
         * is returned.  NULL is also returned when the end of the file is reached.
         * is_eof() may be called to differentiate between these two cases.
         *
         * This may be called repeatedly to extract out all the objects in the Bam
         * file, but typically (especially for scene graph files, indicated with the
         * .bam extension), only one object is retrieved directly from the Bam file:
         * the root of the scene graph.  The remaining objects will all be retrieved
         * recursively by the first object.
         *
         * Note that the object returned may not yet be complete.  In particular, some
         * of its pointers may not be filled in; you must call resolve() to fill in
         * all the available pointers before you can safely use any objects returned
         * by read_object().
         *
         * This flavor of read_object() requires the caller to know what type of
         * object it has received in order to properly manage the reference counts.
         */
        
        /**
         * Reads a single object from the Bam file.
         *
         * This flavor of read_object() returns both a TypedWritable and a
         * ReferenceCount pointer to the same object, so the reference count may be
         * tracked reliably, without having to know precisely what type of object we
         * have.
         * @return true on success, or false on failure.
         */
        """
        pass

    def registerFactory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        register_factory(TypeHandle handle, object func)
        
        /**
         * Registers a factory function that is called when an object of the given
         * type is encountered within the .bam stream.
         *
         * @param user_data an optional pointer to be passed along to the function.
         */
        """
        pass

    def register_factory(self, TypeHandle_handle, object_func): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        register_factory(TypeHandle handle, object func)
        
        /**
         * Registers a factory function that is called when an object of the given
         * type is encountered within the .bam stream.
         *
         * @param user_data an optional pointer to be passed along to the function.
         */
        """
        pass

    def resolve(self, const_BamReader_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resolve(const BamReader self)
        
        /**
         * This may be called at any time during processing of the Bam file to resolve
         * all the known pointers so far.  It is usually called at the end of the
         * processing, after all objects have been read, which is generally the best
         * time to call it.
         *
         * This must be called at least once after reading a particular object via
         * read_object() in order to validate that object.
         *
         * The return value is true if all objects have been resolved, or false if
         * some objects are still outstanding (in which case you will need to call
         * resolve() again later).
         */
        """
        pass

    def setLoaderOptions(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_loader_options(const BamReader self, const LoaderOptions options)
        
        /**
         * Specifies the LoaderOptions for this BamReader.
         */
        """
        pass

    def setSource(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_source(const BamReader self, DatagramGenerator source)
        
        /**
         * Changes the source of future datagrams for this BamReader.  This also
         * implicitly calls init() if it has not already been called.
         */
        """
        pass

    def set_loader_options(self, const_BamReader_self, const_LoaderOptions_options): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_loader_options(const BamReader self, const LoaderOptions options)
        
        /**
         * Specifies the LoaderOptions for this BamReader.
         */
        """
        pass

    def set_source(self, const_BamReader_self, DatagramGenerator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_source(const BamReader self, DatagramGenerator source)
        
        /**
         * Changes the source of future datagrams for this BamReader.  This also
         * implicitly calls init() if it has not already been called.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_endian = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_stdfloat_double = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loader_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This is the fundamental interface for extracting binary objects from a Bam\n * file, as generated by a BamWriter.\n *\n * A Bam file can be thought of as a linear collection of objects.  Each\n * object is an instance of a class that inherits, directly or indirectly,\n * from TypedWritable.  The objects may include pointers to other objects\n * within the Bam file; the BamReader automatically manages these (with help\n * from code within each class) and restores the pointers correctly.\n *\n * This is the abstract interface and does not specifically deal with disk\n * files, but rather with a DatagramGenerator of some kind, which is simply a\n * linear source of Datagrams.  It is probably from a disk file, but it might\n * conceivably be streamed directly from a network or some such nonsense.\n *\n * Bam files are most often used to store scene graphs or subgraphs, and by\n * convention they are given filenames ending in the extension ".bam" when\n * they are used for this purpose.  However, a Bam file may store any\n * arbitrary list of TypedWritable objects; in this more general usage, they\n * are given filenames ending in ".boo" to differentiate them from the more\n * common scene graph files.\n *\n * See also BamFile, which defines a higher-level interface to read and write\n * Bam files on disk.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BamReader' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE370010>'
        'changePointer': None, # (!) real value is "<method 'changePointer' of 'panda3d.core.BamReader' objects>"
        'change_pointer': None, # (!) real value is "<method 'change_pointer' of 'panda3d.core.BamReader' objects>"
        'file_endian': None, # (!) real value is "<attribute 'file_endian' of 'panda3d.core.BamReader' objects>"
        'file_stdfloat_double': None, # (!) real value is "<attribute 'file_stdfloat_double' of 'panda3d.core.BamReader' objects>"
        'file_version': None, # (!) real value is "<attribute 'file_version' of 'panda3d.core.BamReader' objects>"
        'filename': None, # (!) real value is "<attribute 'filename' of 'panda3d.core.BamReader' objects>"
        'getCurrentMajorVer': None, # (!) real value is "<method 'getCurrentMajorVer' of 'panda3d.core.BamReader' objects>"
        'getCurrentMinorVer': None, # (!) real value is "<method 'getCurrentMinorVer' of 'panda3d.core.BamReader' objects>"
        'getFileEndian': None, # (!) real value is "<method 'getFileEndian' of 'panda3d.core.BamReader' objects>"
        'getFileMajorVer': None, # (!) real value is "<method 'getFileMajorVer' of 'panda3d.core.BamReader' objects>"
        'getFileMinorVer': None, # (!) real value is "<method 'getFileMinorVer' of 'panda3d.core.BamReader' objects>"
        'getFileStdfloatDouble': None, # (!) real value is "<method 'getFileStdfloatDouble' of 'panda3d.core.BamReader' objects>"
        'getFileVersion': None, # (!) real value is "<method 'getFileVersion' of 'panda3d.core.BamReader' objects>"
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.BamReader' objects>"
        'getLoaderOptions': None, # (!) real value is "<method 'getLoaderOptions' of 'panda3d.core.BamReader' objects>"
        'getSource': None, # (!) real value is "<method 'getSource' of 'panda3d.core.BamReader' objects>"
        'get_current_major_ver': None, # (!) real value is "<method 'get_current_major_ver' of 'panda3d.core.BamReader' objects>"
        'get_current_minor_ver': None, # (!) real value is "<method 'get_current_minor_ver' of 'panda3d.core.BamReader' objects>"
        'get_file_endian': None, # (!) real value is "<method 'get_file_endian' of 'panda3d.core.BamReader' objects>"
        'get_file_major_ver': None, # (!) real value is "<method 'get_file_major_ver' of 'panda3d.core.BamReader' objects>"
        'get_file_minor_ver': None, # (!) real value is "<method 'get_file_minor_ver' of 'panda3d.core.BamReader' objects>"
        'get_file_stdfloat_double': None, # (!) real value is "<method 'get_file_stdfloat_double' of 'panda3d.core.BamReader' objects>"
        'get_file_version': None, # (!) real value is "<method 'get_file_version' of 'panda3d.core.BamReader' objects>"
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.BamReader' objects>"
        'get_loader_options': None, # (!) real value is "<method 'get_loader_options' of 'panda3d.core.BamReader' objects>"
        'get_source': None, # (!) real value is "<method 'get_source' of 'panda3d.core.BamReader' objects>"
        'init': None, # (!) real value is "<method 'init' of 'panda3d.core.BamReader' objects>"
        'isEof': None, # (!) real value is "<method 'isEof' of 'panda3d.core.BamReader' objects>"
        'is_eof': None, # (!) real value is "<method 'is_eof' of 'panda3d.core.BamReader' objects>"
        'loader_options': None, # (!) real value is "<attribute 'loader_options' of 'panda3d.core.BamReader' objects>"
        'readObject': None, # (!) real value is "<method 'readObject' of 'panda3d.core.BamReader' objects>"
        'read_object': None, # (!) real value is "<method 'read_object' of 'panda3d.core.BamReader' objects>"
        'registerFactory': None, # (!) real value is '<staticmethod(<built-in method registerFactory of type object at 0x00007FFCFE370010>)>'
        'register_factory': None, # (!) real value is '<staticmethod(<built-in method register_factory of type object at 0x00007FFCFE370010>)>'
        'resolve': None, # (!) real value is "<method 'resolve' of 'panda3d.core.BamReader' objects>"
        'setLoaderOptions': None, # (!) real value is "<method 'setLoaderOptions' of 'panda3d.core.BamReader' objects>"
        'setSource': None, # (!) real value is "<method 'setSource' of 'panda3d.core.BamReader' objects>"
        'set_loader_options': None, # (!) real value is "<method 'set_loader_options' of 'panda3d.core.BamReader' objects>"
        'set_source': None, # (!) real value is "<method 'set_source' of 'panda3d.core.BamReader' objects>"
        'source': None, # (!) real value is "<attribute 'source' of 'panda3d.core.BamReader' objects>"
    }


