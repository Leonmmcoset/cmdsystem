# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .SelectiveChildNode import SelectiveChildNode

class SwitchNode(SelectiveChildNode):
    """
    /**
     * A node that renders only one of its children, according to the user's
     * indication.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getVisibleChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_visible_child(SwitchNode self)
        
        /**
         * Returns the index of the child that should be visible.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_visible_child(self, SwitchNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_visible_child(SwitchNode self)
        
        /**
         * Returns the index of the child that should be visible.
         */
        """
        pass

    def setVisibleChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_visible_child(const SwitchNode self, int index)
        
        /**
         * Specifies the particular child of this node, by index, that will be
         * visible.
         */
        """
        pass

    def set_visible_child(self, const_SwitchNode_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_visible_child(const SwitchNode self, int index)
        
        /**
         * Specifies the particular child of this node, by index, that will be
         * visible.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    visible_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * A node that renders only one of its children, according to the user's\n * indication.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.SwitchNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE288AF0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE288AF0>)>'
        'getVisibleChild': None, # (!) real value is "<method 'getVisibleChild' of 'panda3d.core.SwitchNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE288AF0>)>'
        'get_visible_child': None, # (!) real value is "<method 'get_visible_child' of 'panda3d.core.SwitchNode' objects>"
        'setVisibleChild': None, # (!) real value is "<method 'setVisibleChild' of 'panda3d.core.SwitchNode' objects>"
        'set_visible_child': None, # (!) real value is "<method 'set_visible_child' of 'panda3d.core.SwitchNode' objects>"
        'visible_child': None, # (!) real value is "<attribute 'visible_child' of 'panda3d.core.SwitchNode' objects>"
    }


