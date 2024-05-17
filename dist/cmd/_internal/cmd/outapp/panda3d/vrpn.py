# encoding: utf-8
# module panda3d.vrpn
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\vrpn.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import panda3d.core as __panda3d_core


# Variables with simple values

Dtool_PyNativeInterface = 1

# functions

def Dtool_BorrowThisReference(*args, **kwargs): # real signature unknown
    """
    Used to borrow 'this' pointer (to, from)
    Assumes no ownership.
    """
    pass

# classes

class VrpnClient(__panda3d_core.ClientBase):
    """
    /**
     * A specific ClientBase that connects to a VRPN server and records
     * information on the connected VRPN devices.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getServerName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_server_name(VrpnClient self)
        
        /**
         * Returns the name of the server as passed to the VrpnClient constructor.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_server_name(self, VrpnClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_server_name(VrpnClient self)
        
        /**
         * Returns the name of the server as passed to the VrpnClient constructor.
         */
        """
        pass

    def isConnected(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_connected(VrpnClient self)
        
        /**
         * Returns true if the connection is established successfully, false
         * otherwise.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(VrpnClient self)
        
        /**
         * Returns true if everything seems to be kosher with the server (even if
         * there is no connection), or false otherwise.
         */
        """
        pass

    def is_connected(self, VrpnClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_connected(VrpnClient self)
        
        /**
         * Returns true if the connection is established successfully, false
         * otherwise.
         */
        """
        pass

    def is_valid(self, VrpnClient_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(VrpnClient self)
        
        /**
         * Returns true if everything seems to be kosher with the server (even if
         * there is no connection), or false otherwise.
         */
        """
        pass

    def write(self, VrpnClient_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(VrpnClient self, ostream out, int indent_level)
        
        /**
         * Writes a list of the active devices that the VrpnClient is currently
         * polling each frame.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A specific ClientBase that connects to a VRPN server and records\n * information on the connected VRPN devices.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.vrpn.VrpnClient' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDEA10B200>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.vrpn.VrpnClient' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDEA10B200>)>'
        'getServerName': None, # (!) real value is "<method 'getServerName' of 'panda3d.vrpn.VrpnClient' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDEA10B200>)>'
        'get_server_name': None, # (!) real value is "<method 'get_server_name' of 'panda3d.vrpn.VrpnClient' objects>"
        'isConnected': None, # (!) real value is "<method 'isConnected' of 'panda3d.vrpn.VrpnClient' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.vrpn.VrpnClient' objects>"
        'is_connected': None, # (!) real value is "<method 'is_connected' of 'panda3d.vrpn.VrpnClient' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.vrpn.VrpnClient' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.vrpn.VrpnClient' objects>"
    }


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001520E959D50>'

__spec__ = None # (!) real value is "ModuleSpec(name='panda3d.vrpn', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001520E959D50>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\panda3d\\\\vrpn.cp311-win_amd64.pyd')"

