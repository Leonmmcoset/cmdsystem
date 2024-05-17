# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .SimpleAllocator import SimpleAllocator

class VertexDataSaveFile(SimpleAllocator):
    """
    /**
     * A temporary file to hold the vertex data that has been evicted from memory
     * and written to disk.  All vertex data arrays are written into one large
     * flat file.
     */
    """
    def getTotalFileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_total_file_size(VertexDataSaveFile self)
        
        /**
         * Returns the amount of space consumed by the save file, including unused
         * portions.
         */
        """
        pass

    def getUsedFileSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_used_file_size(VertexDataSaveFile self)
        
        /**
         * Returns the amount of space within the save file that is currently in use.
         */
        """
        pass

    def get_total_file_size(self, VertexDataSaveFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_total_file_size(VertexDataSaveFile self)
        
        /**
         * Returns the amount of space consumed by the save file, including unused
         * portions.
         */
        """
        pass

    def get_used_file_size(self, VertexDataSaveFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_used_file_size(VertexDataSaveFile self)
        
        /**
         * Returns the amount of space within the save file that is currently in use.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(VertexDataSaveFile self)
        
        /**
         * Returns true if the save file was successfully created and is ready for
         * use, false if there was an error.
         */
        """
        pass

    def is_valid(self, VertexDataSaveFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(VertexDataSaveFile self)
        
        /**
         * Returns true if the save file was successfully created and is ready for
         * use, false if there was an error.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A temporary file to hold the vertex data that has been evicted from memory\n * and written to disk.  All vertex data arrays are written into one large\n * flat file.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.VertexDataSaveFile' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FAC00>'
        'getTotalFileSize': None, # (!) real value is "<method 'getTotalFileSize' of 'panda3d.core.VertexDataSaveFile' objects>"
        'getUsedFileSize': None, # (!) real value is "<method 'getUsedFileSize' of 'panda3d.core.VertexDataSaveFile' objects>"
        'get_total_file_size': None, # (!) real value is "<method 'get_total_file_size' of 'panda3d.core.VertexDataSaveFile' objects>"
        'get_used_file_size': None, # (!) real value is "<method 'get_used_file_size' of 'panda3d.core.VertexDataSaveFile' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.VertexDataSaveFile' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.VertexDataSaveFile' objects>"
    }


