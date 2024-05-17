# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .DataNode import DataNode

class DialNode(DataNode):
    """
    /**
     * This is the primary interface to infinite dial type devices associated with
     * a ClientBase.  This creates a node that connects to the named dial device,
     * if it exists, and provides hooks to the user to read the state of any of
     * the sequentially numbered dial controls associated with that device.
     *
     * A dial is a rotating device that does not have stops--it can keep rotating
     * any number of times.  Therefore it does not have a specific position at any
     * given time, unlike an AnalogDevice.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumDials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_dials(DialNode self)
        
        /**
         * Returns the number of dial dials known to the DialNode.  This number may
         * change as more dials are discovered.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_dials(self, DialNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_dials(DialNode self)
        
        /**
         * Returns the number of dial dials known to the DialNode.  This number may
         * change as more dials are discovered.
         */
        """
        pass

    def isDialKnown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_dial_known(DialNode self, int index)
        
        /**
         * Returns true if the state of the indicated dial dial is known, or false if
         * we have never heard anything about this particular dial.
         */
        """
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_valid(DialNode self)
        
        /**
         * Returns true if the DialNode is valid and connected to a server, false
         * otherwise.
         */
        """
        pass

    def is_dial_known(self, DialNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_dial_known(DialNode self, int index)
        
        /**
         * Returns true if the state of the indicated dial dial is known, or false if
         * we have never heard anything about this particular dial.
         */
        """
        pass

    def is_valid(self, DialNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_valid(DialNode self)
        
        /**
         * Returns true if the DialNode is valid and connected to a server, false
         * otherwise.
         */
        """
        pass

    def readDial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_dial(const DialNode self, int index)
        
        /**
         * Returns the number of complete revolutions of the dial since the last time
         * read_dial() was called.  This is a destructive operation; it is not
         * possible to read the dial without resetting the counter.
         */
        """
        pass

    def read_dial(self, const_DialNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_dial(const DialNode self, int index)
        
        /**
         * Returns the number of complete revolutions of the dial since the last time
         * read_dial() was called.  This is a destructive operation; it is not
         * possible to read the dial without resetting the counter.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.DialNode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.DialNode' objects>"
        '__doc__': '/**\n * This is the primary interface to infinite dial type devices associated with\n * a ClientBase.  This creates a node that connects to the named dial device,\n * if it exists, and provides hooks to the user to read the state of any of\n * the sequentially numbered dial controls associated with that device.\n *\n * A dial is a rotating device that does not have stops--it can keep rotating\n * any number of times.  Therefore it does not have a specific position at any\n * given time, unlike an AnalogDevice.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.DialNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D6DB0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D6DB0>)>'
        'getNumDials': None, # (!) real value is "<method 'getNumDials' of 'panda3d.core.DialNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D6DB0>)>'
        'get_num_dials': None, # (!) real value is "<method 'get_num_dials' of 'panda3d.core.DialNode' objects>"
        'isDialKnown': None, # (!) real value is "<method 'isDialKnown' of 'panda3d.core.DialNode' objects>"
        'isValid': None, # (!) real value is "<method 'isValid' of 'panda3d.core.DialNode' objects>"
        'is_dial_known': None, # (!) real value is "<method 'is_dial_known' of 'panda3d.core.DialNode' objects>"
        'is_valid': None, # (!) real value is "<method 'is_valid' of 'panda3d.core.DialNode' objects>"
        'readDial': None, # (!) real value is "<method 'readDial' of 'panda3d.core.DialNode' objects>"
        'read_dial': None, # (!) real value is "<method 'read_dial' of 'panda3d.core.DialNode' objects>"
    }


