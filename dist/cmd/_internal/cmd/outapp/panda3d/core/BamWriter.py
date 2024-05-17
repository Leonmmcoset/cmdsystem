# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .BamEnums import BamEnums

class BamWriter(BamEnums):
    """
    /**
     * This is the fundamental interface for writing binary objects to a Bam file,
     * to be extracted later by a BamReader.
     *
     * A Bam file can be thought of as a linear collection of objects.  Each
     * object is an instance of a class that inherits, directly or indirectly,
     * from TypedWritable.  The objects may include pointers to other objects; the
     * BamWriter automatically manages these (with help from code within each
     * class) and writes all referenced objects to the file in such a way that the
     * pointers may be correctly restored later.
     *
     * This is the abstract interface and does not specifically deal with disk
     * files, but rather with a DatagramSink of some kind, which simply accepts a
     * linear stream of Datagrams.  It is probably written to a disk file, but it
     * might conceivably be streamed directly to a network or some such nonsense.
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
    def flush(self, const_BamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const BamWriter self)
        
        /**
         * Ensures that all data written thus far is manifested on the output stream.
         */
        """
        pass

    def getFileEndian(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_endian(BamWriter self)
        
        /**
         * Returns the endian preference indicated by the Bam file currently being
         * written.  This does not imply that every number is stored using the
         * indicated convention, but individual objects may choose to respect this
         * flag when recording data.
         */
        """
        pass

    def getFileMajorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_major_ver(BamWriter self)
        
        /**
         * Returns the major version number of the Bam file currently being written.
         */
        """
        pass

    def getFileMinorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_minor_ver(BamWriter self)
        
        /**
         * Returns the minor version number of the Bam file currently being written.
         */
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(BamWriter self)
        
        /**
         * If a BAM is a file, then the BamWriter should contain the name of the file.
         * This enables the writer to convert pathnames in the BAM to relative to the
         * directory containing the BAM.
         */
        """
        pass

    def getFileStdfloatDouble(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_stdfloat_double(BamWriter self)
        
        /**
         * Returns true if the file will store all "standard" floats as 64-bit
         * doubles, or false if they are 32-bit floats.  This isn't runtime settable;
         * it's based on the compilation flags of the version of Panda that generated
         * this file.
         */
        """
        pass

    def getFileTextureMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file_texture_mode(BamWriter self)
        
        /**
         * Returns the BamTextureMode preference indicated by the Bam file currently
         * being written.  Texture objects written to this Bam file will be encoded
         * according to the specified mode.
         */
        """
        pass

    def getRootNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_root_node(BamWriter self)
        
        /**
         * Returns the root node of the part of the scene graph we are currently
         * writing out.  This is used for determining what to make NodePaths relative
         * to.
         */
        """
        pass

    def getTarget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_target(const BamWriter self)
        
        /**
         * Returns the current target of the BamWriter as set by set_target() or the
         * constructor.
         */
        """
        pass

    def get_filename(self, BamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(BamWriter self)
        
        /**
         * If a BAM is a file, then the BamWriter should contain the name of the file.
         * This enables the writer to convert pathnames in the BAM to relative to the
         * directory containing the BAM.
         */
        """
        pass

    def get_file_endian(self, BamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_endian(BamWriter self)
        
        /**
         * Returns the endian preference indicated by the Bam file currently being
         * written.  This does not imply that every number is stored using the
         * indicated convention, but individual objects may choose to respect this
         * flag when recording data.
         */
        """
        pass

    def get_file_major_ver(self, BamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_major_ver(BamWriter self)
        
        /**
         * Returns the major version number of the Bam file currently being written.
         */
        """
        pass

    def get_file_minor_ver(self, BamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_minor_ver(BamWriter self)
        
        /**
         * Returns the minor version number of the Bam file currently being written.
         */
        """
        pass

    def get_file_stdfloat_double(self, BamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_stdfloat_double(BamWriter self)
        
        /**
         * Returns true if the file will store all "standard" floats as 64-bit
         * doubles, or false if they are 32-bit floats.  This isn't runtime settable;
         * it's based on the compilation flags of the version of Panda that generated
         * this file.
         */
        """
        pass

    def get_file_texture_mode(self, BamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file_texture_mode(BamWriter self)
        
        /**
         * Returns the BamTextureMode preference indicated by the Bam file currently
         * being written.  Texture objects written to this Bam file will be encoded
         * according to the specified mode.
         */
        """
        pass

    def get_root_node(self, BamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_root_node(BamWriter self)
        
        /**
         * Returns the root node of the part of the scene graph we are currently
         * writing out.  This is used for determining what to make NodePaths relative
         * to.
         */
        """
        pass

    def get_target(self, const_BamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_target(const BamWriter self)
        
        /**
         * Returns the current target of the BamWriter as set by set_target() or the
         * constructor.
         */
        """
        pass

    def hasObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_object(BamWriter self, const TypedWritable obj)
        
        /**
         * Returns true if the object has previously been written (or at least
         * requested to be written) to the bam file, or false if we've never heard of
         * it before.
         */
        """
        pass

    def has_object(self, BamWriter_self, const_TypedWritable_obj): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_object(BamWriter self, const TypedWritable obj)
        
        /**
         * Returns true if the object has previously been written (or at least
         * requested to be written) to the bam file, or false if we've never heard of
         * it before.
         */
        """
        pass

    def init(self, const_BamWriter_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        init(const BamWriter self)
        
        /**
         * Initializes the BamWriter prior to writing any objects to its output
         * stream.  This includes writing out the Bam header.
         *
         * This returns true if the BamWriter successfully initialized, false
         * otherwise.
         */
        """
        pass

    def setFileMinorVer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_file_minor_ver(const BamWriter self, int minor_ver)
        
        /**
         * Changes the minor .bam version to write.  This should be called before
         * init().  Each Panda version has only a fairly narrow range of versions it
         * is able to write; consult the .bam documentation for more information.
         */
        """
        pass

    def setFileTextureMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_file_texture_mode(const BamWriter self, int file_texture_mode)
        
        /**
         * Changes the BamTextureMode preference for the Bam file currently being
         * written.  Texture objects written to this Bam file will be encoded
         * according to the specified mode.
         */
        """
        pass

    def setRootNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_root_node(const BamWriter self, TypedWritable root_node)
        
        /**
         * Sets the root node of the part of the scene graph we are currently writing
         * out.  NodePaths written to this bam file will be relative to this node.
         */
        """
        pass

    def setTarget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_target(const BamWriter self, DatagramSink target)
        
        /**
         * Changes the destination of future datagrams written by the BamWriter.  This
         * also implicitly calls init() if it has not already been called.
         */
        """
        pass

    def set_file_minor_ver(self, const_BamWriter_self, int_minor_ver): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_file_minor_ver(const BamWriter self, int minor_ver)
        
        /**
         * Changes the minor .bam version to write.  This should be called before
         * init().  Each Panda version has only a fairly narrow range of versions it
         * is able to write; consult the .bam documentation for more information.
         */
        """
        pass

    def set_file_texture_mode(self, const_BamWriter_self, int_file_texture_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_file_texture_mode(const BamWriter self, int file_texture_mode)
        
        /**
         * Changes the BamTextureMode preference for the Bam file currently being
         * written.  Texture objects written to this Bam file will be encoded
         * according to the specified mode.
         */
        """
        pass

    def set_root_node(self, const_BamWriter_self, TypedWritable_root_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_root_node(const BamWriter self, TypedWritable root_node)
        
        /**
         * Sets the root node of the part of the scene graph we are currently writing
         * out.  NodePaths written to this bam file will be relative to this node.
         */
        """
        pass

    def set_target(self, const_BamWriter_self, DatagramSink_target): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_target(const BamWriter self, DatagramSink target)
        
        /**
         * Changes the destination of future datagrams written by the BamWriter.  This
         * also implicitly calls init() if it has not already been called.
         */
        """
        pass

    def writeObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_object(const BamWriter self, const TypedWritable obj)
        
        /**
         * Writes a single object to the Bam file, so that the
         * BamReader::read_object() can later correctly restore the object and all its
         * pointers.
         *
         * This implicitly also writes any additional objects this object references
         * (if they haven't already been written), so that pointers may be fully
         * resolved.
         *
         * This may be called repeatedly to write a sequence of objects to the Bam
         * file, but typically (especially for scene graph files, indicated with the
         * .bam extension), only one object is written directly from the Bam file: the
         * root of the scene graph.  The remaining objects will all be written
         * recursively by the first object.
         *
         * Returns true if the object is successfully written, false otherwise.
         */
        """
        pass

    def write_object(self, const_BamWriter_self, const_TypedWritable_obj): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_object(const BamWriter self, const TypedWritable obj)
        
        /**
         * Writes a single object to the Bam file, so that the
         * BamReader::read_object() can later correctly restore the object and all its
         * pointers.
         *
         * This implicitly also writes any additional objects this object references
         * (if they haven't already been written), so that pointers may be fully
         * resolved.
         *
         * This may be called repeatedly to write a sequence of objects to the Bam
         * file, but typically (especially for scene graph files, indicated with the
         * .bam extension), only one object is written directly from the Bam file: the
         * root of the scene graph.  The remaining objects will all be written
         * recursively by the first object.
         *
         * Returns true if the object is successfully written, false otherwise.
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

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_endian = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_stdfloat_double = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_texture_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    root_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.BamWriter' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.BamWriter' objects>"
        '__doc__': '/**\n * This is the fundamental interface for writing binary objects to a Bam file,\n * to be extracted later by a BamReader.\n *\n * A Bam file can be thought of as a linear collection of objects.  Each\n * object is an instance of a class that inherits, directly or indirectly,\n * from TypedWritable.  The objects may include pointers to other objects; the\n * BamWriter automatically manages these (with help from code within each\n * class) and writes all referenced objects to the file in such a way that the\n * pointers may be correctly restored later.\n *\n * This is the abstract interface and does not specifically deal with disk\n * files, but rather with a DatagramSink of some kind, which simply accepts a\n * linear stream of Datagrams.  It is probably written to a disk file, but it\n * might conceivably be streamed directly to a network or some such nonsense.\n *\n * Bam files are most often used to store scene graphs or subgraphs, and by\n * convention they are given filenames ending in the extension ".bam" when\n * they are used for this purpose.  However, a Bam file may store any\n * arbitrary list of TypedWritable objects; in this more general usage, they\n * are given filenames ending in ".boo" to differentiate them from the more\n * common scene graph files.\n *\n * See also BamFile, which defines a higher-level interface to read and write\n * Bam files on disk.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.BamWriter' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE3701E0>'
        'file_endian': None, # (!) real value is "<attribute 'file_endian' of 'panda3d.core.BamWriter' objects>"
        'file_stdfloat_double': None, # (!) real value is "<attribute 'file_stdfloat_double' of 'panda3d.core.BamWriter' objects>"
        'file_texture_mode': None, # (!) real value is "<attribute 'file_texture_mode' of 'panda3d.core.BamWriter' objects>"
        'file_version': None, # (!) real value is "<attribute 'file_version' of 'panda3d.core.BamWriter' objects>"
        'filename': None, # (!) real value is "<attribute 'filename' of 'panda3d.core.BamWriter' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.BamWriter' objects>"
        'getFileEndian': None, # (!) real value is "<method 'getFileEndian' of 'panda3d.core.BamWriter' objects>"
        'getFileMajorVer': None, # (!) real value is "<method 'getFileMajorVer' of 'panda3d.core.BamWriter' objects>"
        'getFileMinorVer': None, # (!) real value is "<method 'getFileMinorVer' of 'panda3d.core.BamWriter' objects>"
        'getFileStdfloatDouble': None, # (!) real value is "<method 'getFileStdfloatDouble' of 'panda3d.core.BamWriter' objects>"
        'getFileTextureMode': None, # (!) real value is "<method 'getFileTextureMode' of 'panda3d.core.BamWriter' objects>"
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.BamWriter' objects>"
        'getRootNode': None, # (!) real value is "<method 'getRootNode' of 'panda3d.core.BamWriter' objects>"
        'getTarget': None, # (!) real value is "<method 'getTarget' of 'panda3d.core.BamWriter' objects>"
        'get_file_endian': None, # (!) real value is "<method 'get_file_endian' of 'panda3d.core.BamWriter' objects>"
        'get_file_major_ver': None, # (!) real value is "<method 'get_file_major_ver' of 'panda3d.core.BamWriter' objects>"
        'get_file_minor_ver': None, # (!) real value is "<method 'get_file_minor_ver' of 'panda3d.core.BamWriter' objects>"
        'get_file_stdfloat_double': None, # (!) real value is "<method 'get_file_stdfloat_double' of 'panda3d.core.BamWriter' objects>"
        'get_file_texture_mode': None, # (!) real value is "<method 'get_file_texture_mode' of 'panda3d.core.BamWriter' objects>"
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.BamWriter' objects>"
        'get_root_node': None, # (!) real value is "<method 'get_root_node' of 'panda3d.core.BamWriter' objects>"
        'get_target': None, # (!) real value is "<method 'get_target' of 'panda3d.core.BamWriter' objects>"
        'hasObject': None, # (!) real value is "<method 'hasObject' of 'panda3d.core.BamWriter' objects>"
        'has_object': None, # (!) real value is "<method 'has_object' of 'panda3d.core.BamWriter' objects>"
        'init': None, # (!) real value is "<method 'init' of 'panda3d.core.BamWriter' objects>"
        'root_node': None, # (!) real value is "<attribute 'root_node' of 'panda3d.core.BamWriter' objects>"
        'setFileMinorVer': None, # (!) real value is "<method 'setFileMinorVer' of 'panda3d.core.BamWriter' objects>"
        'setFileTextureMode': None, # (!) real value is "<method 'setFileTextureMode' of 'panda3d.core.BamWriter' objects>"
        'setRootNode': None, # (!) real value is "<method 'setRootNode' of 'panda3d.core.BamWriter' objects>"
        'setTarget': None, # (!) real value is "<method 'setTarget' of 'panda3d.core.BamWriter' objects>"
        'set_file_minor_ver': None, # (!) real value is "<method 'set_file_minor_ver' of 'panda3d.core.BamWriter' objects>"
        'set_file_texture_mode': None, # (!) real value is "<method 'set_file_texture_mode' of 'panda3d.core.BamWriter' objects>"
        'set_root_node': None, # (!) real value is "<method 'set_root_node' of 'panda3d.core.BamWriter' objects>"
        'set_target': None, # (!) real value is "<method 'set_target' of 'panda3d.core.BamWriter' objects>"
        'target': None, # (!) real value is "<attribute 'target' of 'panda3d.core.BamWriter' objects>"
        'writeObject': None, # (!) real value is "<method 'writeObject' of 'panda3d.core.BamWriter' objects>"
        'write_object': None, # (!) real value is "<method 'write_object' of 'panda3d.core.BamWriter' objects>"
    }


