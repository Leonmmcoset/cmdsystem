# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class SubfileInfo(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class records a particular byte sub-range within an existing file on
     * disk.  Generally, the filename is understood as a physical file on disk,
     * and not to be looked up via the vfs.
     */
    """
    def assign(self, const_SubfileInfo_self, const_SubfileInfo_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const SubfileInfo self, const SubfileInfo copy)
        """
        pass

    def getFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_file(SubfileInfo self)
        
        /**
         * Returns the FileReference that represents this file.
         */
        """
        pass

    def getFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_filename(SubfileInfo self)
        
        /**
         * A shortcut to the filename.
         */
        """
        pass

    def getSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_size(SubfileInfo self)
        
        /**
         * Returns the number of consecutive bytes, beginning at get_start(), that
         * correspond to this file data.
         */
        """
        pass

    def getStart(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_start(SubfileInfo self)
        
        /**
         * Returns the offset within the file at which this file data begins.
         */
        """
        pass

    def get_file(self, SubfileInfo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_file(SubfileInfo self)
        
        /**
         * Returns the FileReference that represents this file.
         */
        """
        pass

    def get_filename(self, SubfileInfo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_filename(SubfileInfo self)
        
        /**
         * A shortcut to the filename.
         */
        """
        pass

    def get_size(self, SubfileInfo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_size(SubfileInfo self)
        
        /**
         * Returns the number of consecutive bytes, beginning at get_start(), that
         * correspond to this file data.
         */
        """
        pass

    def get_start(self, SubfileInfo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_start(SubfileInfo self)
        
        /**
         * Returns the offset within the file at which this file data begins.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(SubfileInfo self)
        
        /**
         * Returns true if this SubfileInfo doesn't define any file, false if it has
         * real data.
         */
        """
        pass

    def is_empty(self, SubfileInfo_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(SubfileInfo self)
        
        /**
         * Returns true if this SubfileInfo doesn't define any file, false if it has
         * real data.
         */
        """
        pass

    def output(self, SubfileInfo_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(SubfileInfo self, ostream out)
        
        /**
         *
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.SubfileInfo' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.SubfileInfo' objects>"
        '__doc__': '/**\n * This class records a particular byte sub-range within an existing file on\n * disk.  Generally, the filename is understood as a physical file on disk,\n * and not to be looked up via the vfs.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SubfileInfo' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE279480>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.SubfileInfo' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.SubfileInfo' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.SubfileInfo' objects>"
        'getFile': None, # (!) real value is "<method 'getFile' of 'panda3d.core.SubfileInfo' objects>"
        'getFilename': None, # (!) real value is "<method 'getFilename' of 'panda3d.core.SubfileInfo' objects>"
        'getSize': None, # (!) real value is "<method 'getSize' of 'panda3d.core.SubfileInfo' objects>"
        'getStart': None, # (!) real value is "<method 'getStart' of 'panda3d.core.SubfileInfo' objects>"
        'get_file': None, # (!) real value is "<method 'get_file' of 'panda3d.core.SubfileInfo' objects>"
        'get_filename': None, # (!) real value is "<method 'get_filename' of 'panda3d.core.SubfileInfo' objects>"
        'get_size': None, # (!) real value is "<method 'get_size' of 'panda3d.core.SubfileInfo' objects>"
        'get_start': None, # (!) real value is "<method 'get_start' of 'panda3d.core.SubfileInfo' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.SubfileInfo' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.SubfileInfo' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.SubfileInfo' objects>"
    }


