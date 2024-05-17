# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Decompressor(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This manages run-time decompression of a zlib-compressed stream, as a
     * background or foreground task.
     */
    """
    def decompress(self, const_Decompressor_self, Ramfile_source_and_dest_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        decompress(const Decompressor self, Ramfile source_and_dest_file)
        
        /**
         * Performs a foreground decompression of the named file; does not return
         * until the decompression is complete.
         */
        
        /**
         * Does an in-memory decompression of the indicated Ramfile.  The decompressed
         * contents are written back into the same Ramfile on completion.
         */
        """
        pass

    def getProgress(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_progress(Decompressor self)
        
        /**
         * Returns the ratio through the decompression step in the background.
         */
        """
        pass

    def get_progress(self, Decompressor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_progress(Decompressor self)
        
        /**
         * Returns the ratio through the decompression step in the background.
         */
        """
        pass

    def initiate(self, const_Decompressor_self, const_Filename_source_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        initiate(const Decompressor self, const Filename source_file)
        initiate(const Decompressor self, const Filename source_file, const Filename dest_file)
        
        /**
         * Begins a background decompression of the named file (whose filename must
         * end in ".pz") to a new file without the .pz extension.  The source file is
         * removed after successful completion.
         */
        
        /**
         * Begins a background decompression from the named source file to the named
         * destination file.  The source file is removed after successful completion.
         */
        """
        pass

    def run(self, const_Decompressor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        run(const Decompressor self)
        
        /**
         * Called each frame to do the next bit of work in the background task.
         * Returns EU_ok if a chunk is completed but there is more to go, or
         * EU_success when we're all done.  Any other return value indicates an error.
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

    progress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Decompressor' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Decompressor' objects>"
        '__doc__': '/**\n * This manages run-time decompression of a zlib-compressed stream, as a\n * background or foreground task.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Decompressor' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26D050>'
        'decompress': None, # (!) real value is "<method 'decompress' of 'panda3d.core.Decompressor' objects>"
        'getProgress': None, # (!) real value is "<method 'getProgress' of 'panda3d.core.Decompressor' objects>"
        'get_progress': None, # (!) real value is "<method 'get_progress' of 'panda3d.core.Decompressor' objects>"
        'initiate': None, # (!) real value is "<method 'initiate' of 'panda3d.core.Decompressor' objects>"
        'progress': None, # (!) real value is "<attribute 'progress' of 'panda3d.core.Decompressor' objects>"
        'run': None, # (!) real value is "<method 'run' of 'panda3d.core.Decompressor' objects>"
    }


