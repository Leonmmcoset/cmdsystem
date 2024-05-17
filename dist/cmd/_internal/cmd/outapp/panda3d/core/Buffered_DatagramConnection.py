# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Socket_TCP import Socket_TCP

class Buffered_DatagramConnection(Socket_TCP):
    """
    // there are 3 states 1. Socket not even assigned,,,, 2. Socket Assigned and
    // trying to get a active connect open 3. Socket is open and  writable.. (
    // Fully powered up )...
    """
    def AddAddress(self, const_Buffered_DatagramConnection_self, Socket_Address_inadr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        AddAddress(const Buffered_DatagramConnection self, Socket_Address inadr)
        
        /**
         * must be called to set value to the server
         */
        """
        pass

    def AddressQueueSize(self, const_Buffered_DatagramConnection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        AddressQueueSize(const Buffered_DatagramConnection self)
        
        // address queue stuff
        """
        pass

    def ClearAddresses(self, const_Buffered_DatagramConnection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ClearAddresses(const Buffered_DatagramConnection self)
        """
        pass

    def DoConnect(self, const_Buffered_DatagramConnection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        DoConnect(const Buffered_DatagramConnection self)
        
        // all the real state magic is in here
        """
        pass

    def Flush(self, const_Buffered_DatagramConnection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Flush(const Buffered_DatagramConnection self)
        
        /**
         * Flush all writes.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def GetMessage(self, const_Buffered_DatagramConnection_self, Datagram_val): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        GetMessage(const Buffered_DatagramConnection self, Datagram val)
        
        /**
         * Reads a message.  Returns false on failure.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def IsConnected(self, const_Buffered_DatagramConnection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        IsConnected(const Buffered_DatagramConnection self)
        
        // all the real state magic is in here
        """
        pass

    def Reset(self, const_Buffered_DatagramConnection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        Reset(const Buffered_DatagramConnection self)
        
        /**
         * Reset
         */
        """
        pass

    def SendMessage(self, const_Buffered_DatagramConnection_self, const_Datagram_msg): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        SendMessage(const Buffered_DatagramConnection self, const Datagram msg)
        
        // the reason thsi all exists
        
        /**
         * send the message
         */
        """
        pass

    def WaitForNetworkReadEvent(self, const_Buffered_DatagramConnection_self, float_MaxTime): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        WaitForNetworkReadEvent(const Buffered_DatagramConnection self, float MaxTime)
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'AddAddress': None, # (!) real value is "<method 'AddAddress' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        'AddressQueueSize': None, # (!) real value is "<method 'AddressQueueSize' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        'ClearAddresses': None, # (!) real value is "<method 'ClearAddresses' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        'DoConnect': None, # (!) real value is "<method 'DoConnect' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Flush': None, # (!) real value is "<method 'Flush' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        'GetMessage': None, # (!) real value is "<method 'GetMessage' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        'IsConnected': None, # (!) real value is "<method 'IsConnected' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        'Reset': None, # (!) real value is "<method 'Reset' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        'SendMessage': None, # (!) real value is "<method 'SendMessage' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        'WaitForNetworkReadEvent': None, # (!) real value is "<method 'WaitForNetworkReadEvent' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        '__doc__': '// there are 3 states 1. Socket not even assigned,,,, 2. Socket Assigned and\n// trying to get a active connect open 3. Socket is open and  writable.. (\n// Fully powered up )...',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Buffered_DatagramConnection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38EF70>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE38EF70>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE38EF70>)>'
    }


