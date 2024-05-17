# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .CallbackData import CallbackData

class NodeCullCallbackData(CallbackData):
    """
    /**
     * This kind of CallbackData is passed to the CallbackObject added to
     * CallbackNode:set_cull_callback().
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_data(NodeCullCallbackData self)
        
        /**
         * Returns the CullTraverserData in use at the time of the callback.  This
         * object contains data that changes at each node of the traversal, such as
         * the current node and the current net transform to that node.
         */
        """
        pass

    def getTrav(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_trav(NodeCullCallbackData self)
        
        /**
         * Returns the CullTraverser in use at the time of the callback.  This object
         * contains data that does not change during the traversal, such as the
         * DisplayRegion and Camera in use.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_data(self, NodeCullCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_data(NodeCullCallbackData self)
        
        /**
         * Returns the CullTraverserData in use at the time of the callback.  This
         * object contains data that changes at each node of the traversal, such as
         * the current node and the current net transform to that node.
         */
        """
        pass

    def get_trav(self, NodeCullCallbackData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_trav(NodeCullCallbackData self)
        
        /**
         * Returns the CullTraverser in use at the time of the callback.  This object
         * contains data that does not change during the traversal, such as the
         * DisplayRegion and Camera in use.
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
        '__doc__': '/**\n * This kind of CallbackData is passed to the CallbackObject added to\n * CallbackNode:set_cull_callback().\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.NodeCullCallbackData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE287C70>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE287C70>)>'
        'getData': None, # (!) real value is "<method 'getData' of 'panda3d.core.NodeCullCallbackData' objects>"
        'getTrav': None, # (!) real value is "<method 'getTrav' of 'panda3d.core.NodeCullCallbackData' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE287C70>)>'
        'get_data': None, # (!) real value is "<method 'get_data' of 'panda3d.core.NodeCullCallbackData' objects>"
        'get_trav': None, # (!) real value is "<method 'get_trav' of 'panda3d.core.NodeCullCallbackData' objects>"
    }


