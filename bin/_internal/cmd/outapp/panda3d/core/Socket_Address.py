# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Socket_Address(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A simple place to store and manipulate tcp and port address for
     * communication layer
     */
    """
    def clear(self, const_Socket_Address_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const Socket_Address self)
        
        /**
         * Set the internal values to a suitable known value
         */
        """
        pass

    def getFamily(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_family(Socket_Address self)
        
        /**
         * Returns AF_INET if this is an IPv4 address, or AF_INET6 if this is an IPv6
         * address.
         */
        """
        pass

    def getIp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ip(Socket_Address self)
        
        /**
         * Return the IP address portion in dot notation string.
         */
        """
        pass

    def GetIPAddressRaw(self, Socket_Address_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        GetIPAddressRaw(Socket_Address self)
        
        /**
         * Returns a raw 32-bit unsigned integer representing the IPv4 address.
         * @deprecated  Does not work with IPv6 addresses.
         */
        """
        pass

    def getIpPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ip_port(Socket_Address self)
        
        /**
         * Return the ip address/port in dot notation string.  If this is an IPv6
         * address, it will be enclosed in square brackets.
         */
        """
        pass

    def getPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_port(Socket_Address self)
        
        /**
         * Get the port portion as an integer
         */
        """
        pass

    def get_family(self, Socket_Address_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_family(Socket_Address self)
        
        /**
         * Returns AF_INET if this is an IPv4 address, or AF_INET6 if this is an IPv6
         * address.
         */
        """
        pass

    def get_ip(self, Socket_Address_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ip(Socket_Address self)
        
        /**
         * Return the IP address portion in dot notation string.
         */
        """
        pass

    def get_ip_port(self, Socket_Address_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ip_port(Socket_Address self)
        
        /**
         * Return the ip address/port in dot notation string.  If this is an IPv6
         * address, it will be enclosed in square brackets.
         */
        """
        pass

    def get_port(self, Socket_Address_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_port(Socket_Address self)
        
        /**
         * Get the port portion as an integer
         */
        """
        pass

    def isAny(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_any(Socket_Address self)
        
        /**
         * True if the address is zero.
         */
        """
        pass

    def isMcastRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_mcast_range(Socket_Address self)
        
        /**
         * True if the address is in the multicast range.
         */
        """
        pass

    def is_any(self, Socket_Address_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_any(Socket_Address self)
        
        /**
         * True if the address is zero.
         */
        """
        pass

    def is_mcast_range(self, Socket_Address_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_mcast_range(Socket_Address self)
        
        /**
         * True if the address is in the multicast range.
         */
        """
        pass

    def setAnyIP(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_any_IP(const Socket_Address self, int port)
        
        /**
         * Set to any address and a specified port
         */
        """
        pass

    def setAnyIPv6(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_any_IPv6(const Socket_Address self, int port)
        
        /**
         * Set to any IPv6 address and a specified port.
         */
        """
        pass

    def setBroadcast(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_broadcast(const Socket_Address self, int port)
        
        /**
         * Set to the broadcast address and a specified port
         */
        """
        pass

    def setHost(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_host(const Socket_Address self, str hostname)
        set_host(const Socket_Address self, str hostname, int port)
        set_host(const Socket_Address self, int ip4addr, int port)
        
        /**
         *
         */
        
        /**
         * This function will take a port and string-based TCP address and initialize
         * the address with this information.  Returns true on success; on failure, it
         * returns false and the address may be undefined.
         */
        
        /**
         * Initializes the address from a string specifying both the address and port,
         * separated by a colon.  An IPv6 address must be enclosed in brackets.
         */
        """
        pass

    def setPort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_port(const Socket_Address self, int port)
        
        /**
         * Set to a specified port
         */
        """
        pass

    def set_any_IP(self, const_Socket_Address_self, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_any_IP(const Socket_Address self, int port)
        
        /**
         * Set to any address and a specified port
         */
        """
        pass

    def set_any_IPv6(self, const_Socket_Address_self, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_any_IPv6(const Socket_Address self, int port)
        
        /**
         * Set to any IPv6 address and a specified port.
         */
        """
        pass

    def set_broadcast(self, const_Socket_Address_self, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_broadcast(const Socket_Address self, int port)
        
        /**
         * Set to the broadcast address and a specified port
         */
        """
        pass

    def set_host(self, const_Socket_Address_self, str_hostname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_host(const Socket_Address self, str hostname)
        set_host(const Socket_Address self, str hostname, int port)
        set_host(const Socket_Address self, int ip4addr, int port)
        
        /**
         *
         */
        
        /**
         * This function will take a port and string-based TCP address and initialize
         * the address with this information.  Returns true on success; on failure, it
         * returns false and the address may be undefined.
         */
        
        /**
         * Initializes the address from a string specifying both the address and port,
         * separated by a colon.  An IPv6 address must be enclosed in brackets.
         */
        """
        pass

    def set_port(self, const_Socket_Address_self, int_port): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_port(const Socket_Address self, int port)
        
        /**
         * Set to a specified port
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'GetIPAddressRaw': None, # (!) real value is "<method 'GetIPAddressRaw' of 'panda3d.core.Socket_Address' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Socket_Address' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Socket_Address' objects>"
        '__doc__': '/**\n * A simple place to store and manipulate tcp and port address for\n * communication layer\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.Socket_Address' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.Socket_Address' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.Socket_Address' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.Socket_Address' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Socket_Address' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.Socket_Address' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.Socket_Address' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.Socket_Address' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE38E2B0>'
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.Socket_Address' objects>"
        'getFamily': None, # (!) real value is "<method 'getFamily' of 'panda3d.core.Socket_Address' objects>"
        'getIp': None, # (!) real value is "<method 'getIp' of 'panda3d.core.Socket_Address' objects>"
        'getIpPort': None, # (!) real value is "<method 'getIpPort' of 'panda3d.core.Socket_Address' objects>"
        'getPort': None, # (!) real value is "<method 'getPort' of 'panda3d.core.Socket_Address' objects>"
        'get_family': None, # (!) real value is "<method 'get_family' of 'panda3d.core.Socket_Address' objects>"
        'get_ip': None, # (!) real value is "<method 'get_ip' of 'panda3d.core.Socket_Address' objects>"
        'get_ip_port': None, # (!) real value is "<method 'get_ip_port' of 'panda3d.core.Socket_Address' objects>"
        'get_port': None, # (!) real value is "<method 'get_port' of 'panda3d.core.Socket_Address' objects>"
        'isAny': None, # (!) real value is "<method 'isAny' of 'panda3d.core.Socket_Address' objects>"
        'isMcastRange': None, # (!) real value is "<method 'isMcastRange' of 'panda3d.core.Socket_Address' objects>"
        'is_any': None, # (!) real value is "<method 'is_any' of 'panda3d.core.Socket_Address' objects>"
        'is_mcast_range': None, # (!) real value is "<method 'is_mcast_range' of 'panda3d.core.Socket_Address' objects>"
        'setAnyIP': None, # (!) real value is "<method 'setAnyIP' of 'panda3d.core.Socket_Address' objects>"
        'setAnyIPv6': None, # (!) real value is "<method 'setAnyIPv6' of 'panda3d.core.Socket_Address' objects>"
        'setBroadcast': None, # (!) real value is "<method 'setBroadcast' of 'panda3d.core.Socket_Address' objects>"
        'setHost': None, # (!) real value is "<method 'setHost' of 'panda3d.core.Socket_Address' objects>"
        'setPort': None, # (!) real value is "<method 'setPort' of 'panda3d.core.Socket_Address' objects>"
        'set_any_IP': None, # (!) real value is "<method 'set_any_IP' of 'panda3d.core.Socket_Address' objects>"
        'set_any_IPv6': None, # (!) real value is "<method 'set_any_IPv6' of 'panda3d.core.Socket_Address' objects>"
        'set_broadcast': None, # (!) real value is "<method 'set_broadcast' of 'panda3d.core.Socket_Address' objects>"
        'set_host': None, # (!) real value is "<method 'set_host' of 'panda3d.core.Socket_Address' objects>"
        'set_port': None, # (!) real value is "<method 'set_port' of 'panda3d.core.Socket_Address' objects>"
    }


