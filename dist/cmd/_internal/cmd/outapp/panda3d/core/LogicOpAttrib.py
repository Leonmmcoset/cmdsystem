# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class LogicOpAttrib(RenderAttrib):
    """
    /**
     * If enabled, specifies that a custom logical operation be performed instead
     * of any color blending.  Setting it to a value other than M_none will cause
     * color blending to be disabled and the given logic operation to be performed.
     *
     * @since 1.10.0
     */
    """
    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getOperation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_operation(LogicOpAttrib self)
        
        /**
         * Returns the logic operation specified by this attribute.
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_operation(self, LogicOpAttrib_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_operation(LogicOpAttrib self)
        
        /**
         * Returns the logic operation specified by this attribute.
         */
        """
        pass

    def make(self, int_op): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(int op)
        
        /**
         * Constructs a new LogicOpAttrib object with the given logic operation.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def makeOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new LogicOpAttrib object that disables special-effect
         * blending, allowing normal transparency to be used instead.
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a new LogicOpAttrib object that disables special-effect
         * blending, allowing normal transparency to be used instead.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    class_slot = 18
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'OAnd': 2,
        'OAndInverted': 5,
        'OAndReverse': 3,
        'OClear': 1,
        'OCopy': 4,
        'OCopyInverted': 13,
        'OEquivalent': 10,
        'OInvert': 11,
        'ONand': 15,
        'ONone': 0,
        'ONoop': 6,
        'ONor': 9,
        'OOr': 8,
        'OOrInverted': 14,
        'OOrReverse': 12,
        'OSet': 16,
        'OXor': 7,
        'O_and': 2,
        'O_and_inverted': 5,
        'O_and_reverse': 3,
        'O_clear': 1,
        'O_copy': 4,
        'O_copy_inverted': 13,
        'O_equivalent': 10,
        'O_invert': 11,
        'O_nand': 15,
        'O_none': 0,
        'O_noop': 6,
        'O_nor': 9,
        'O_or': 8,
        'O_or_inverted': 14,
        'O_or_reverse': 12,
        'O_set': 16,
        'O_xor': 7,
        '__doc__': '/**\n * If enabled, specifies that a custom logical operation be performed instead\n * of any color blending.  Setting it to a value other than M_none will cause\n * color blending to be disabled and the given logic operation to be performed.\n *\n * @since 1.10.0\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.LogicOpAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE293160>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.LogicOpAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE293160>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE293160>)>'
        'getOperation': None, # (!) real value is "<method 'getOperation' of 'panda3d.core.LogicOpAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE293160>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE293160>)>'
        'get_operation': None, # (!) real value is "<method 'get_operation' of 'panda3d.core.LogicOpAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE293160>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE293160>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE293160>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE293160>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE293160>)>'
        'operation': None, # (!) real value is "<attribute 'operation' of 'panda3d.core.LogicOpAttrib' objects>"
    }
    OAnd = 2
    OAndInverted = 5
    OAndReverse = 3
    OClear = 1
    OCopy = 4
    OCopyInverted = 13
    OEquivalent = 10
    OInvert = 11
    ONand = 15
    ONone = 0
    ONoop = 6
    ONor = 9
    OOr = 8
    OOrInverted = 14
    OOrReverse = 12
    OSet = 16
    OXor = 7
    O_and = 2
    O_and_inverted = 5
    O_and_reverse = 3
    O_clear = 1
    O_copy = 4
    O_copy_inverted = 13
    O_equivalent = 10
    O_invert = 11
    O_nand = 15
    O_none = 0
    O_noop = 6
    O_nor = 9
    O_or = 8
    O_or_inverted = 14
    O_or_reverse = 12
    O_set = 16
    O_xor = 7


