# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ostream import ostream

class MultiplexStream(ostream):
    """
    /**
     * This is a special ostream that forwards the data that is written to it to
     * any number of other sources, for instance other ostreams, or explicitly to
     * a disk file or to system logging utilities.  It's a very handy thing to set
     * Notify to refer to when running in batch mode.
     */
    """
    def addFile(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_file(const MultiplexStream self, Filename file)
        
        /**
         * Adds the given file to the multiplex output.  The file is opened in append
         * mode with line buffering.  Returns false if the file cannot be opened.
         */
        """
        pass

    def addOstream(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_ostream(const MultiplexStream self, ostream out, bool delete_later)
        
        /**
         * Adds the indicated generic ostream to the multiplex output.  The ostream
         * will receive whatever data is sent to the pipe.
         */
        """
        pass

    def addStandardOutput(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_standard_output(const MultiplexStream self)
        
        /**
         * Adds the standard output channel.
         */
        """
        pass

    def addSystemDebug(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_system_debug(const MultiplexStream self)
        
        /**
         * Adds the system debug output the the multiplex output.  This may map to a
         * syslog or some such os-specific output system.  It may do nothing on a
         * particular system.
         *
         * Presently, this maps only to OutputDebugString() on Windows.
         */
        """
        pass

    def add_file(self, const_MultiplexStream_self, Filename_file): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_file(const MultiplexStream self, Filename file)
        
        /**
         * Adds the given file to the multiplex output.  The file is opened in append
         * mode with line buffering.  Returns false if the file cannot be opened.
         */
        """
        pass

    def add_ostream(self, const_MultiplexStream_self, ostream_out, bool_delete_later): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_ostream(const MultiplexStream self, ostream out, bool delete_later)
        
        /**
         * Adds the indicated generic ostream to the multiplex output.  The ostream
         * will receive whatever data is sent to the pipe.
         */
        """
        pass

    def add_standard_output(self, const_MultiplexStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_standard_output(const MultiplexStream self)
        
        /**
         * Adds the standard output channel.
         */
        """
        pass

    def add_system_debug(self, const_MultiplexStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_system_debug(const MultiplexStream self)
        
        /**
         * Adds the system debug output the the multiplex output.  This may map to a
         * syslog or some such os-specific output system.  It may do nothing on a
         * particular system.
         *
         * Presently, this maps only to OutputDebugString() on Windows.
         */
        """
        pass

    def flush(self, const_MultiplexStream_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flush(const MultiplexStream self)
        
        /**
         * Forces out all output that hasn't yet been written.
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
        '__doc__': "/**\n * This is a special ostream that forwards the data that is written to it to\n * any number of other sources, for instance other ostreams, or explicitly to\n * a disk file or to system logging utilities.  It's a very handy thing to set\n * Notify to refer to when running in batch mode.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MultiplexStream' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE26D5C0>'
        'addFile': None, # (!) real value is "<method 'addFile' of 'panda3d.core.MultiplexStream' objects>"
        'addOstream': None, # (!) real value is "<method 'addOstream' of 'panda3d.core.MultiplexStream' objects>"
        'addStandardOutput': None, # (!) real value is "<method 'addStandardOutput' of 'panda3d.core.MultiplexStream' objects>"
        'addSystemDebug': None, # (!) real value is "<method 'addSystemDebug' of 'panda3d.core.MultiplexStream' objects>"
        'add_file': None, # (!) real value is "<method 'add_file' of 'panda3d.core.MultiplexStream' objects>"
        'add_ostream': None, # (!) real value is "<method 'add_ostream' of 'panda3d.core.MultiplexStream' objects>"
        'add_standard_output': None, # (!) real value is "<method 'add_standard_output' of 'panda3d.core.MultiplexStream' objects>"
        'add_system_debug': None, # (!) real value is "<method 'add_system_debug' of 'panda3d.core.MultiplexStream' objects>"
        'flush': None, # (!) real value is "<method 'flush' of 'panda3d.core.MultiplexStream' objects>"
    }


