# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class PStatCollectorForwardBase(ReferenceCount):
    """
    /**
     * This class serves as a cheap forward reference to a PStatCollector, which
     * is defined in the pstatclient module (and is not directly accessible here
     * in the express module).
     *
     * This is subclassed as PStatCollectorForward, which defines the actual
     * functionality.
     */
    """
    def addLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_level(const PStatCollectorForwardBase self, double level)
        """
        pass

    def add_level(self, const_PStatCollectorForwardBase_self, double_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_level(const PStatCollectorForwardBase self, double level)
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
        '__doc__': '/**\n * This class serves as a cheap forward reference to a PStatCollector, which\n * is defined in the pstatclient module (and is not directly accessible here\n * in the express module).\n *\n * This is subclassed as PStatCollectorForward, which defines the actual\n * functionality.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PStatCollectorForwardBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2775B0>'
        'addLevel': None, # (!) real value is "<method 'addLevel' of 'panda3d.core.PStatCollectorForwardBase' objects>"
        'add_level': None, # (!) real value is "<method 'add_level' of 'panda3d.core.PStatCollectorForwardBase' objects>"
    }


