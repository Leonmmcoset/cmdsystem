# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class NetAddress(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Represents a network address to which UDP packets may be sent or to which a
     * TCP socket may be bound.
     */
    """
    def clear(self, const_NetAddress_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const NetAddress self)
        
        /**
         * Resets the NetAddress to its initial state.
         */
        """
        pass

    def getAddr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_addr(NetAddress self)
        
        /**
         * Returns the Socket_Address for this address.
         */
        """
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(NetAddress self)
        
        /**
         *
         */
        """
        pass

    def getIp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ip(NetAddress self)
        
        /**
         * Returns the IP address to which this address refers, as a 32-bit integer,
         * in host byte order.
         * @deprecated  Does not work with IPv6 addresses.
         */
        """
        pass

    def getIpComponent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ip_component(NetAddress self, int n)
        
        /**
         * Returns the nth 8-bit component of the IP address.  An IP address has four
         * components; component 0 is the first (leftmost), and component 3 is the
         * last (rightmost) in the dotted number convention.
         */
        """
        pass

    def getIpString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ip_string(NetAddress self)
        
        /**
         * Returns the IP address to which this address refers, formatted as a string.
         */
        """
        pass

    def getPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_port(NetAddress self)
        
        /**
         * Returns the port number to which this address refers.
         */
        """
        pass

    def get_addr(self, NetAddress_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_addr(NetAddress self)
        
        /**
         * Returns the Socket_Address for this address.
         */
        """
        pass

    def get_hash(self, NetAddress_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(NetAddress self)
        
        /**
         *
         */
        """
        pass

    def get_ip(self, NetAddress_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ip(NetAddress self)
        
        /**
         * Returns the IP address to which this address refers, as a 32-bit integer,
         * in host byte order.
         * @deprecated  Does not work with IPv6 addresses.
         */
        """
        pass

    def get_ip_component(self, NetAddress_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ip_component(NetAddress self, int n)
        
        /**
         * Returns the nth 8-bit component of the IP address.  An IP address has four
         * components; component 0 is the first (leftmost), and component 3 is the
         * last (rightmost) in the dotted number convention.
         */
        """
        pass

    def get_ip_string(self, NetAddress_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ip_string(NetAddress self)
        
        /**
         * Returns the IP address to which this address refers, formatted as a string.
         */
        """
        pass

    def get_port(self, NetAddress_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_port(NetAddress self)
        
        /**
         * Returns the port number to which this address refers.
         */
        """
        pass

    def isAny(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_any(NetAddress self)
        
        /**
         * Returns true if the IP address has only zeroes.
         */
        """
        pass

    def is_any(self, NetAddress_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_any(NetAddress self)
        
        /**
         * Returns true if the IP address has only zeroes.
         */
        """
        pass

    def output(self, NetAddress_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(NetAddress self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setAny(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_any(const NetAddress self, int port)
        
        /**
         * Sets the address up to refer to a particular port, but not to any
         * particular IP.  Returns true if successful, false otherwise (currently,
         * this only returns true).
         */
        """
        pass

    def setBroadcast(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_broadcast(const NetAddress self, int port)
        
        /**
         * Sets the address to the broadcast address.
         */
        """
        pass

    def setHost(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_host(const NetAddress self, str hostname, int port)
        
        /**
         * Sets the address up to refer to a particular port on a particular host.
         * Returns true if the hostname is known, false otherwise.
         */
        """
        pass

    def setLocalhost(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_localhost(const NetAddress self, int port)
        
        /**
         * Sets the address up to refer to a particular port, on this host.
         */
        """
        pass

    def setPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_port(const NetAddress self, int port)
        
        /**
         * Resets the port number without otherwise changing the address.
         */
        """
        pass

    def set_any(self, const_NetAddress_self, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_any(const NetAddress self, int port)
        
        /**
         * Sets the address up to refer to a particular port, but not to any
         * particular IP.  Returns true if successful, false otherwise (currently,
         * this only returns true).
         */
        """
        pass

    def set_broadcast(self, const_NetAddress_self, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_broadcast(const NetAddress self, int port)
        
        /**
         * Sets the address to the broadcast address.
         */
        """
        pass

    def set_host(self, const_NetAddress_self, str_hostname, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_host(const NetAddress self, str hostname, int port)
        
        /**
         * Sets the address up to refer to a particular port on a particular host.
         * Returns true if the hostname is known, false otherwise.
         */
        """
        pass

    def set_localhost(self, const_NetAddress_self, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_localhost(const NetAddress self, int port)
        
        /**
         * Sets the address up to refer to a particular port, on this host.
         */
        """
        pass

    def set_port(self, const_NetAddress_self, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_port(const NetAddress self, int port)
        
        /**
         * Resets the port number without otherwise changing the address.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.NetAddress' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.NetAddress' objects>"
        '__doc__': '/**\n * Represents a network address to which UDP packets may be sent or to which a\n * TCP socket may be bound.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.NetAddress' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.NetAddress' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.NetAddress' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.NetAddress' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NetAddress' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.NetAddress' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.NetAddress' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.NetAddress' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE389720>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.NetAddress' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.NetAddress' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.NetAddress' objects>"
        'getAddr': None, # (!) real value is "<method 'getAddr' of 'panda3d.core.NetAddress' objects>"
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.core.NetAddress' objects>"
        'getIp': None, # (!) real value is "<method 'getIp' of 'panda3d.core.NetAddress' objects>"
        'getIpComponent': None, # (!) real value is "<method 'getIpComponent' of 'panda3d.core.NetAddress' objects>"
        'getIpString': None, # (!) real value is "<method 'getIpString' of 'panda3d.core.NetAddress' objects>"
        'getPort': None, # (!) real value is "<method 'getPort' of 'panda3d.core.NetAddress' objects>"
        'get_addr': None, # (!) real value is "<method 'get_addr' of 'panda3d.core.NetAddress' objects>"
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.core.NetAddress' objects>"
        'get_ip': None, # (!) real value is "<method 'get_ip' of 'panda3d.core.NetAddress' objects>"
        'get_ip_component': None, # (!) real value is "<method 'get_ip_component' of 'panda3d.core.NetAddress' objects>"
        'get_ip_string': None, # (!) real value is "<method 'get_ip_string' of 'panda3d.core.NetAddress' objects>"
        'get_port': None, # (!) real value is "<method 'get_port' of 'panda3d.core.NetAddress' objects>"
        'isAny': None, # (!) real value is "<method 'isAny' of 'panda3d.core.NetAddress' objects>"
        'is_any': None, # (!) real value is "<method 'is_any' of 'panda3d.core.NetAddress' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.NetAddress' objects>"
        'setAny': None, # (!) real value is "<method 'setAny' of 'panda3d.core.NetAddress' objects>"
        'setBroadcast': None, # (!) real value is "<method 'setBroadcast' of 'panda3d.core.NetAddress' objects>"
        'setHost': None, # (!) real value is "<method 'setHost' of 'panda3d.core.NetAddress' objects>"
        'setLocalhost': None, # (!) real value is "<method 'setLocalhost' of 'panda3d.core.NetAddress' objects>"
        'setPort': None, # (!) real value is "<method 'setPort' of 'panda3d.core.NetAddress' objects>"
        'set_any': None, # (!) real value is "<method 'set_any' of 'panda3d.core.NetAddress' objects>"
        'set_broadcast': None, # (!) real value is "<method 'set_broadcast' of 'panda3d.core.NetAddress' objects>"
        'set_host': None, # (!) real value is "<method 'set_host' of 'panda3d.core.NetAddress' objects>"
        'set_localhost': None, # (!) real value is "<method 'set_localhost' of 'panda3d.core.NetAddress' objects>"
        'set_port': None, # (!) real value is "<method 'set_port' of 'panda3d.core.NetAddress' objects>"
    }


