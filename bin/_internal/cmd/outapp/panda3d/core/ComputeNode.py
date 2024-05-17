# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class ComputeNode(PandaNode):
    """
    /**
     * A special node, the sole purpose of which is to invoke a dispatch operation
     * on the assigned compute shader.
     */
    """
    def addDispatch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_dispatch(const ComputeNode self, const LVecBase3i num_groups)
        add_dispatch(const ComputeNode self, int num_groups_x, int num_groups_y, int num_groups_z)
        
        /**
         * Adds a dispatch command with the given number of work groups in the X, Y,
         * and Z dimensions.  Any of these values may be set to 1 if the respective
         * dimension should not be used.
         */
        
        /**
         * Adds a dispatch command with the given number of work groups in the X, Y,
         * and Z dimensions.  Any of these values may be set to 1 if the respective
         * dimension should not be used.
         */
        """
        pass

    def add_dispatch(self, const_ComputeNode_self, const_LVecBase3i_num_groups): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_dispatch(const ComputeNode self, const LVecBase3i num_groups)
        add_dispatch(const ComputeNode self, int num_groups_x, int num_groups_y, int num_groups_z)
        
        /**
         * Adds a dispatch command with the given number of work groups in the X, Y,
         * and Z dimensions.  Any of these values may be set to 1 if the respective
         * dimension should not be used.
         */
        
        /**
         * Adds a dispatch command with the given number of work groups in the X, Y,
         * and Z dimensions.  Any of these values may be set to 1 if the respective
         * dimension should not be used.
         */
        """
        pass

    def clearDispatches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_dispatches(const ComputeNode self)
        
        /**
         * Removes all dispatch commands.
         */
        """
        pass

    def clear_dispatches(self, const_ComputeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_dispatches(const ComputeNode self)
        
        /**
         * Removes all dispatch commands.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDispatch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dispatch(ComputeNode self, int i)
        
        /**
         * Returns the group counts of the nth dispatch associated with this object.
         */
        """
        pass

    def getDispatches(self, *args, **kwargs): # real signature unknown
        pass

    def getNumDispatches(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_dispatches(ComputeNode self)
        
        /**
         * Returns the number of times add_dispatch has been called on this object.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_dispatch(self, ComputeNode_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dispatch(ComputeNode self, int i)
        
        /**
         * Returns the group counts of the nth dispatch associated with this object.
         */
        """
        pass

    def get_dispatches(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_dispatches(self, ComputeNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_dispatches(ComputeNode self)
        
        /**
         * Returns the number of times add_dispatch has been called on this object.
         */
        """
        pass

    def insertDispatch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_dispatch(const ComputeNode self, int i, const LVecBase3i num_groups)
        
        /**
         * Inserts a dispatch command with the given number of work groups in the X,
         * Y, and Z dimensions at the given position in the list of dispatch commands.
         * Any of these values may be set to 1 if the respective dimension should not
         * be used.
         */
        """
        pass

    def insert_dispatch(self, const_ComputeNode_self, int_i, const_LVecBase3i_num_groups): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_dispatch(const ComputeNode self, int i, const LVecBase3i num_groups)
        
        /**
         * Inserts a dispatch command with the given number of work groups in the X,
         * Y, and Z dimensions at the given position in the list of dispatch commands.
         * Any of these values may be set to 1 if the respective dimension should not
         * be used.
         */
        """
        pass

    def removeDispatch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_dispatch(const ComputeNode self, int i)
        
        /**
         * Erases the given dispatch index from the list.
         */
        """
        pass

    def remove_dispatch(self, const_ComputeNode_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_dispatch(const ComputeNode self, int i)
        
        /**
         * Erases the given dispatch index from the list.
         */
        """
        pass

    def setDispatch(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_dispatch(const ComputeNode self, int i, const LVecBase3i num_groups)
        
        /**
         * Sets the group counts of the nth dispatch associated with this object.
         */
        """
        pass

    def set_dispatch(self, const_ComputeNode_self, int_i, const_LVecBase3i_num_groups): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_dispatch(const ComputeNode self, int i, const LVecBase3i num_groups)
        
        /**
         * Sets the group counts of the nth dispatch associated with this object.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    dispatches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A special node, the sole purpose of which is to invoke a dispatch operation\n * on the assigned compute shader.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ComputeNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE287360>'
        'addDispatch': None, # (!) real value is "<method 'addDispatch' of 'panda3d.core.ComputeNode' objects>"
        'add_dispatch': None, # (!) real value is "<method 'add_dispatch' of 'panda3d.core.ComputeNode' objects>"
        'clearDispatches': None, # (!) real value is "<method 'clearDispatches' of 'panda3d.core.ComputeNode' objects>"
        'clear_dispatches': None, # (!) real value is "<method 'clear_dispatches' of 'panda3d.core.ComputeNode' objects>"
        'dispatches': None, # (!) real value is "<attribute 'dispatches' of 'panda3d.core.ComputeNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE287360>)>'
        'getDispatch': None, # (!) real value is "<method 'getDispatch' of 'panda3d.core.ComputeNode' objects>"
        'getDispatches': None, # (!) real value is "<method 'getDispatches' of 'panda3d.core.ComputeNode' objects>"
        'getNumDispatches': None, # (!) real value is "<method 'getNumDispatches' of 'panda3d.core.ComputeNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE287360>)>'
        'get_dispatch': None, # (!) real value is "<method 'get_dispatch' of 'panda3d.core.ComputeNode' objects>"
        'get_dispatches': None, # (!) real value is "<method 'get_dispatches' of 'panda3d.core.ComputeNode' objects>"
        'get_num_dispatches': None, # (!) real value is "<method 'get_num_dispatches' of 'panda3d.core.ComputeNode' objects>"
        'insertDispatch': None, # (!) real value is "<method 'insertDispatch' of 'panda3d.core.ComputeNode' objects>"
        'insert_dispatch': None, # (!) real value is "<method 'insert_dispatch' of 'panda3d.core.ComputeNode' objects>"
        'removeDispatch': None, # (!) real value is "<method 'removeDispatch' of 'panda3d.core.ComputeNode' objects>"
        'remove_dispatch': None, # (!) real value is "<method 'remove_dispatch' of 'panda3d.core.ComputeNode' objects>"
        'setDispatch': None, # (!) real value is "<method 'setDispatch' of 'panda3d.core.ComputeNode' objects>"
        'set_dispatch': None, # (!) real value is "<method 'set_dispatch' of 'panda3d.core.ComputeNode' objects>"
    }


