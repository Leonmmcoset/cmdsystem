# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PartGroup import PartGroup

class MovingPartBase(PartGroup):
    """
    /**
     * This is the base class for a single animatable piece that may be bound to
     * one channel (or more, if blending is in effect).  It corresponds to, for
     * instance, a single joint or slider of a character.
     *
     * MovingPartBase does not have a particular value type.  See the derived
     * template class, MovingPart, for this.
     */
    """
    def getBound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bound(MovingPartBase self, int n)
        
        /**
         * Returns the nth bound channel on this PartGroup.  n can be determined by
         * iterating from 0 to one less than get_max_bound(); or n might be
         * AnimControl::get_channel_index().
         *
         * This will return NULL if there is no channel bound on the indicated index.
         * It is an error to call this if n is less than zero or greater than or equal
         * to get_max_bound().
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getMaxBound(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_bound(MovingPartBase self)
        
        /**
         * Returns the number of channels that might be bound to this PartGroup.  This
         * might not be the actual number of channels, since there might be holes in
         * the list; it is one more than the index number of the highest bound
         * channel.  Thus, it is called get_max_bound() instead of get_num_bound().
         */
        """
        pass

    def get_bound(self, MovingPartBase_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bound(MovingPartBase self, int n)
        
        /**
         * Returns the nth bound channel on this PartGroup.  n can be determined by
         * iterating from 0 to one less than get_max_bound(); or n might be
         * AnimControl::get_channel_index().
         *
         * This will return NULL if there is no channel bound on the indicated index.
         * It is an error to call this if n is less than zero or greater than or equal
         * to get_max_bound().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_max_bound(self, MovingPartBase_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_bound(MovingPartBase self)
        
        /**
         * Returns the number of channels that might be bound to this PartGroup.  This
         * might not be the actual number of channels, since there might be holes in
         * the list; it is one more than the index number of the highest bound
         * channel.  Thus, it is called get_max_bound() instead of get_num_bound().
         */
        """
        pass

    def outputValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        output_value(MovingPartBase self, ostream out)
        """
        pass

    def output_value(self, MovingPartBase_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output_value(MovingPartBase self, ostream out)
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
        '__doc__': '/**\n * This is the base class for a single animatable piece that may be bound to\n * one channel (or more, if blending is in effect).  It corresponds to, for\n * instance, a single joint or slider of a character.\n *\n * MovingPartBase does not have a particular value type.  See the derived\n * template class, MovingPart, for this.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MovingPartBase' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C4CE0>'
        'getBound': None, # (!) real value is "<method 'getBound' of 'panda3d.core.MovingPartBase' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C4CE0>)>'
        'getMaxBound': None, # (!) real value is "<method 'getMaxBound' of 'panda3d.core.MovingPartBase' objects>"
        'get_bound': None, # (!) real value is "<method 'get_bound' of 'panda3d.core.MovingPartBase' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C4CE0>)>'
        'get_max_bound': None, # (!) real value is "<method 'get_max_bound' of 'panda3d.core.MovingPartBase' objects>"
        'outputValue': None, # (!) real value is "<method 'outputValue' of 'panda3d.core.MovingPartBase' objects>"
        'output_value': None, # (!) real value is "<method 'output_value' of 'panda3d.core.MovingPartBase' objects>"
    }


