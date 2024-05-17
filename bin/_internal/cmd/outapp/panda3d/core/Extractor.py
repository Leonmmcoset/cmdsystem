# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Extractor(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class automatically extracts the contents of a Multifile to the
     * current directory (or to a specified directory) in the background.
     *
     * It is designed to limit its use of system resources and run unobtrusively
     * in the background.  After specifying the files you wish to extract via
     * repeated calls to request_subfile(), begin the process by calling run()
     * repeatedly.  Each call to run() extracts another small portion of the
     * Multifile.  Call run() whenever you have spare cycles until run() returns
     * EU_success.
     */
    """
    def getProgress(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_progress(Extractor self)
        
        /**
         * Returns the fraction of the Multifile extracted so far.
         */
        """
        pass

    def get_progress(self, Extractor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_progress(Extractor self)
        
        /**
         * Returns the fraction of the Multifile extracted so far.
         */
        """
        pass

    def requestAllSubfiles(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        request_all_subfiles(const Extractor self)
        
        /**
         * Requests all subfiles in the Multifile to be extracted.  Returns the number
         * requested.
         */
        """
        pass

    def requestSubfile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        request_subfile(const Extractor self, const Filename subfile_name)
        
        /**
         * Requests a particular subfile to be extracted when step() or run() is
         * called.  Returns true if the subfile exists, false otherwise.
         */
        """
        pass

    def request_all_subfiles(self, const_Extractor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        request_all_subfiles(const Extractor self)
        
        /**
         * Requests all subfiles in the Multifile to be extracted.  Returns the number
         * requested.
         */
        """
        pass

    def request_subfile(self, const_Extractor_self, const_Filename_subfile_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        request_subfile(const Extractor self, const Filename subfile_name)
        
        /**
         * Requests a particular subfile to be extracted when step() or run() is
         * called.  Returns true if the subfile exists, false otherwise.
         */
        """
        pass

    def reset(self, const_Extractor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset(const Extractor self)
        
        /**
         * Interrupts the Extractor in the middle of its business and makes it ready
         * to accept a new list of subfiles to extract.
         */
        """
        pass

    def run(self, const_Extractor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        run(const Extractor self)
        
        /**
         * A convenience function to extract the Multifile all at once, when you don't
         * care about doing it in the background.
         *
         * First, call request_file() or request_all_files() to specify the files you
         * would like to extract, then call run() to do the extraction.  Also see
         * step() for when you would like the extraction to happen as a background
         * task.
         */
        """
        pass

    def setExtractDir(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_extract_dir(const Extractor self, const Filename extract_dir)
        
        /**
         * Specifies the directory into which all extracted subfiles will be written.
         * Relative paths of subfiles within the Multifile will be written as relative
         * paths to this directory.
         */
        """
        pass

    def setMultifile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_multifile(const Extractor self, const Filename multifile_name)
        
        /**
         * Specifies the filename of the Multifile that the Extractor will read.
         * Returns true on success, false if the mulifile name is invalid.
         */
        """
        pass

    def set_extract_dir(self, const_Extractor_self, const_Filename_extract_dir): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_extract_dir(const Extractor self, const Filename extract_dir)
        
        /**
         * Specifies the directory into which all extracted subfiles will be written.
         * Relative paths of subfiles within the Multifile will be written as relative
         * paths to this directory.
         */
        """
        pass

    def set_multifile(self, const_Extractor_self, const_Filename_multifile_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_multifile(const Extractor self, const Filename multifile_name)
        
        /**
         * Specifies the filename of the Multifile that the Extractor will read.
         * Returns true on success, false if the mulifile name is invalid.
         */
        """
        pass

    def step(self, const_Extractor_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        step(const Extractor self)
        
        /**
         * After all of the requests have been made via request_file() or
         * request_all_subfiles(), call step() repeatedly until it stops returning
         * EU_ok.
         *
         * step() extracts the next small unit of data from the Multifile.  Returns
         * EU_ok if progress is continuing, EU_error_abort if there is a problem, or
         * EU_success when the last piece has been extracted.
         *
         * Also see run().
         */
        """
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
        '__doc__': '/**\n * This class automatically extracts the contents of a Multifile to the\n * current directory (or to a specified directory) in the background.\n *\n * It is designed to limit its use of system resources and run unobtrusively\n * in the background.  After specifying the files you wish to extract via\n * repeated calls to request_subfile(), begin the process by calling run()\n * repeatedly.  Each call to run() extracts another small portion of the\n * Multifile.  Call run() whenever you have spare cycles until run() returns\n * EU_success.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Extractor' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26D3F0>'
        'getProgress': None, # (!) real value is "<method 'getProgress' of 'panda3d.core.Extractor' objects>"
        'get_progress': None, # (!) real value is "<method 'get_progress' of 'panda3d.core.Extractor' objects>"
        'progress': None, # (!) real value is "<attribute 'progress' of 'panda3d.core.Extractor' objects>"
        'requestAllSubfiles': None, # (!) real value is "<method 'requestAllSubfiles' of 'panda3d.core.Extractor' objects>"
        'requestSubfile': None, # (!) real value is "<method 'requestSubfile' of 'panda3d.core.Extractor' objects>"
        'request_all_subfiles': None, # (!) real value is "<method 'request_all_subfiles' of 'panda3d.core.Extractor' objects>"
        'request_subfile': None, # (!) real value is "<method 'request_subfile' of 'panda3d.core.Extractor' objects>"
        'reset': None, # (!) real value is "<method 'reset' of 'panda3d.core.Extractor' objects>"
        'run': None, # (!) real value is "<method 'run' of 'panda3d.core.Extractor' objects>"
        'setExtractDir': None, # (!) real value is "<method 'setExtractDir' of 'panda3d.core.Extractor' objects>"
        'setMultifile': None, # (!) real value is "<method 'setMultifile' of 'panda3d.core.Extractor' objects>"
        'set_extract_dir': None, # (!) real value is "<method 'set_extract_dir' of 'panda3d.core.Extractor' objects>"
        'set_multifile': None, # (!) real value is "<method 'set_multifile' of 'panda3d.core.Extractor' objects>"
        'step': None, # (!) real value is "<method 'step' of 'panda3d.core.Extractor' objects>"
    }


