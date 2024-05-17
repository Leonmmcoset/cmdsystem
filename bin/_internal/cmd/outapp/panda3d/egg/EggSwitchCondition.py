# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggObject import EggObject

class EggSwitchCondition(EggObject):
    """
    /**
     * This corresponds to a <SwitchCondition> entry within a group.  It indicates
     * the condition at which a level-of-detail is switched in or out.  This is
     * actually an abstract base class for potentially any number of specific
     * different kinds of switching conditions; presently, only a <Distance> type
     * is actually supported.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(EggSwitchCondition self)
        """
        pass

    def make_copy(self, EggSwitchCondition_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(EggSwitchCondition self)
        """
        pass

    def transform(self, const_EggSwitchCondition_self, const_LMatrix4d_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        transform(const EggSwitchCondition self, const LMatrix4d mat)
        """
        pass

    def write(self, EggSwitchCondition_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(EggSwitchCondition self, ostream out, int indent_level)
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggSwitchCondition' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggSwitchCondition' objects>"
        '__doc__': '/**\n * This corresponds to a <SwitchCondition> entry within a group.  It indicates\n * the condition at which a level-of-detail is switched in or out.  This is\n * actually an abstract base class for potentially any number of specific\n * different kinds of switching conditions; presently, only a <Distance> type\n * is actually supported.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggSwitchCondition' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CDF10>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.egg.EggSwitchCondition' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CDF10>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CDF10>)>'
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.egg.EggSwitchCondition' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.egg.EggSwitchCondition' objects>"
        'transform': None, # (!) real value is "<method 'transform' of 'panda3d.egg.EggSwitchCondition' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.egg.EggSwitchCondition' objects>"
    }


