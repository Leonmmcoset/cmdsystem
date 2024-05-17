# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CollisionHandlerPhysical import CollisionHandlerPhysical

class CollisionHandlerPusher(CollisionHandlerPhysical):
    """
    /**
     * A specialized kind of CollisionHandler that simply pushes back on things
     * that attempt to move into solid walls.  This is the simplest kind of "real-
     * world" collisions you can have.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getHorizontal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_horizontal(CollisionHandlerPusher self)
        
        /**
         *
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_horizontal(self, CollisionHandlerPusher_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_horizontal(CollisionHandlerPusher self)
        
        /**
         *
         */
        """
        pass

    def readDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_datagram(const CollisionHandlerPusher self, DatagramIterator source)
        
        /**
         * Restores the object state from the given datagram, previously obtained using
         * __getstate__.
         */
        """
        pass

    def read_datagram(self, const_CollisionHandlerPusher_self, DatagramIterator_source): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_datagram(const CollisionHandlerPusher self, DatagramIterator source)
        
        /**
         * Restores the object state from the given datagram, previously obtained using
         * __getstate__.
         */
        """
        pass

    def setHorizontal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_horizontal(const CollisionHandlerPusher self, bool flag)
        
        /**
         *
         */
        """
        pass

    def set_horizontal(self, const_CollisionHandlerPusher_self, bool_flag): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_horizontal(const CollisionHandlerPusher self, bool flag)
        
        /**
         *
         */
        """
        pass

    def writeDatagram(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_datagram(CollisionHandlerPusher self, Datagram destination)
        
        /**
         * Serializes this object, to implement pickle support.
         */
        """
        pass

    def write_datagram(self, CollisionHandlerPusher_self, Datagram_destination): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_datagram(CollisionHandlerPusher self, Datagram destination)
        
        /**
         * Serializes this object, to implement pickle support.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    horizontal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A specialized kind of CollisionHandler that simply pushes back on things\n * that attempt to move into solid walls.  This is the simplest kind of "real-\n * world" collisions you can have.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CollisionHandlerPusher' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CF510>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CF510>)>'
        'getHorizontal': None, # (!) real value is "<method 'getHorizontal' of 'panda3d.core.CollisionHandlerPusher' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CF510>)>'
        'get_horizontal': None, # (!) real value is "<method 'get_horizontal' of 'panda3d.core.CollisionHandlerPusher' objects>"
        'horizontal': None, # (!) real value is "<attribute 'horizontal' of 'panda3d.core.CollisionHandlerPusher' objects>"
        'readDatagram': None, # (!) real value is "<method 'readDatagram' of 'panda3d.core.CollisionHandlerPusher' objects>"
        'read_datagram': None, # (!) real value is "<method 'read_datagram' of 'panda3d.core.CollisionHandlerPusher' objects>"
        'setHorizontal': None, # (!) real value is "<method 'setHorizontal' of 'panda3d.core.CollisionHandlerPusher' objects>"
        'set_horizontal': None, # (!) real value is "<method 'set_horizontal' of 'panda3d.core.CollisionHandlerPusher' objects>"
        'writeDatagram': None, # (!) real value is "<method 'writeDatagram' of 'panda3d.core.CollisionHandlerPusher' objects>"
        'write_datagram': None, # (!) real value is "<method 'write_datagram' of 'panda3d.core.CollisionHandlerPusher' objects>"
    }


