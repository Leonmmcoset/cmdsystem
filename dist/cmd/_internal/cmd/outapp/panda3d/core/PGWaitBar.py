# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PGItem import PGItem

class PGWaitBar(PGItem):
    """
    /**
     * This is a particular kind of PGItem that draws a little bar that fills from
     * left to right to indicate a slow process gradually completing, like a
     * traditional "wait, loading" bar.
     */
    """
    def getBarStyle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bar_style(PGWaitBar self)
        
        /**
         * Returns the kind of frame that is drawn on top of the WaitBar to represent
         * the amount completed.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPercent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_percent(PGWaitBar self)
        
        /**
         * Returns the percentage complete.
         */
        """
        pass

    def getRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_range(PGWaitBar self)
        
        /**
         * Returns the value at which the WaitBar indicates 100%.
         */
        """
        pass

    def getValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_value(PGWaitBar self)
        
        /**
         * Returns the current value of the bar.
         */
        """
        pass

    def get_bar_style(self, PGWaitBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bar_style(PGWaitBar self)
        
        /**
         * Returns the kind of frame that is drawn on top of the WaitBar to represent
         * the amount completed.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_percent(self, PGWaitBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_percent(PGWaitBar self)
        
        /**
         * Returns the percentage complete.
         */
        """
        pass

    def get_range(self, PGWaitBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_range(PGWaitBar self)
        
        /**
         * Returns the value at which the WaitBar indicates 100%.
         */
        """
        pass

    def get_value(self, PGWaitBar_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_value(PGWaitBar self)
        
        /**
         * Returns the current value of the bar.
         */
        """
        pass

    def setBarStyle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bar_style(const PGWaitBar self, const PGFrameStyle style)
        
        /**
         * Sets the kind of frame that is drawn on top of the WaitBar to represent the
         * amount completed.
         */
        """
        pass

    def setRange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_range(const PGWaitBar self, float range)
        
        /**
         * Sets the value at which the WaitBar indicates 100%.
         */
        """
        pass

    def setup(self, const_PGWaitBar_self, float_width, float_height, float_range): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        setup(const PGWaitBar self, float width, float height, float range)
        
        /**
         * Creates a PGWaitBar with the indicated dimensions, with the indicated
         * maximum range.
         */
        """
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_value(const PGWaitBar self, float value)
        
        /**
         * Sets the current value of the bar.  This should range between 0 and
         * get_range().
         */
        """
        pass

    def set_bar_style(self, const_PGWaitBar_self, const_PGFrameStyle_style): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bar_style(const PGWaitBar self, const PGFrameStyle style)
        
        /**
         * Sets the kind of frame that is drawn on top of the WaitBar to represent the
         * amount completed.
         */
        """
        pass

    def set_range(self, const_PGWaitBar_self, float_range): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_range(const PGWaitBar self, float range)
        
        /**
         * Sets the value at which the WaitBar indicates 100%.
         */
        """
        pass

    def set_value(self, const_PGWaitBar_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_value(const PGWaitBar self, float value)
        
        /**
         * Sets the current value of the bar.  This should range between 0 and
         * get_range().
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
        '__doc__': '/**\n * This is a particular kind of PGItem that draws a little bar that fills from\n * left to right to indicate a slow process gradually completing, like a\n * traditional "wait, loading" bar.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PGWaitBar' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE385020>'
        'getBarStyle': None, # (!) real value is "<method 'getBarStyle' of 'panda3d.core.PGWaitBar' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE385020>)>'
        'getPercent': None, # (!) real value is "<method 'getPercent' of 'panda3d.core.PGWaitBar' objects>"
        'getRange': None, # (!) real value is "<method 'getRange' of 'panda3d.core.PGWaitBar' objects>"
        'getValue': None, # (!) real value is "<method 'getValue' of 'panda3d.core.PGWaitBar' objects>"
        'get_bar_style': None, # (!) real value is "<method 'get_bar_style' of 'panda3d.core.PGWaitBar' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE385020>)>'
        'get_percent': None, # (!) real value is "<method 'get_percent' of 'panda3d.core.PGWaitBar' objects>"
        'get_range': None, # (!) real value is "<method 'get_range' of 'panda3d.core.PGWaitBar' objects>"
        'get_value': None, # (!) real value is "<method 'get_value' of 'panda3d.core.PGWaitBar' objects>"
        'setBarStyle': None, # (!) real value is "<method 'setBarStyle' of 'panda3d.core.PGWaitBar' objects>"
        'setRange': None, # (!) real value is "<method 'setRange' of 'panda3d.core.PGWaitBar' objects>"
        'setValue': None, # (!) real value is "<method 'setValue' of 'panda3d.core.PGWaitBar' objects>"
        'set_bar_style': None, # (!) real value is "<method 'set_bar_style' of 'panda3d.core.PGWaitBar' objects>"
        'set_range': None, # (!) real value is "<method 'set_range' of 'panda3d.core.PGWaitBar' objects>"
        'set_value': None, # (!) real value is "<method 'set_value' of 'panda3d.core.PGWaitBar' objects>"
        'setup': None, # (!) real value is "<method 'setup' of 'panda3d.core.PGWaitBar' objects>"
    }


