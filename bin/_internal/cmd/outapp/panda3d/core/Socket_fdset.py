# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Socket_fdset(__dtoolconfig.DTOOL_SUPER_BASE):
    # no doc
    def clear(self, const_Socket_fdset_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const Socket_fdset self)
        
        /**
         * Marks the content as empty
         */
        """
        pass

    def IsSetFor(self, Socket_fdset_self, const_Socket_IP_incon): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        IsSetFor(Socket_fdset self, const Socket_IP incon)
        
        /**
         * check to see if a socket object has been marked for reading
         */
        """
        pass

    def setForSocket(self, const_Socket_fdset_self, const_Socket_IP_incon): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setForSocket(const Socket_fdset self, const Socket_IP incon)
        
        /**
         *
         */
        """
        pass

    def WaitForError(self, const_Socket_fdset_self, bool_zeroFds, int_sleep_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        WaitForError(const Socket_fdset self, bool zeroFds, int sleep_time)
        
        /**
         * This is the function that will wait till one of the sockets is in error
         * state
         */
        """
        pass

    def WaitForRead(self, const_Socket_fdset_self, bool_zeroFds, int_sleep_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        WaitForRead(const Socket_fdset self, bool zeroFds, int sleep_time)
        
        /**
         *
         */
        
        /**
         *
         */
        """
        pass

    def WaitForWrite(self, const_Socket_fdset_self, bool_zeroFds, int_sleep_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        WaitForWrite(const Socket_fdset self, bool zeroFds, int sleep_time)
        
        /**
         * This is the function that will wait till one of the sockets is ready for
         * writing
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'IsSetFor': None, # (!) real value is "<method 'IsSetFor' of 'panda3d.core.Socket_fdset' objects>"
        'WaitForError': None, # (!) real value is "<method 'WaitForError' of 'panda3d.core.Socket_fdset' objects>"
        'WaitForRead': None, # (!) real value is "<method 'WaitForRead' of 'panda3d.core.Socket_fdset' objects>"
        'WaitForWrite': None, # (!) real value is "<method 'WaitForWrite' of 'panda3d.core.Socket_fdset' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Socket_fdset' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Socket_fdset' objects>"
        '__doc__': None,
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Socket_fdset' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38EDA0>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.Socket_fdset' objects>"
        'setForSocket': None, # (!) real value is "<method 'setForSocket' of 'panda3d.core.Socket_fdset' objects>"
    }


