# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class UpdateSeq(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This is a sequence number that increments monotonically.  It can be used to
     * track cache updates, or serve as a kind of timestamp for any changing
     * properties.
     *
     * A special class is used instead of simply an int, so we can elegantly
     * handle such things as wraparound and special cases.  There are two special
     * cases.  Firstly, a sequence number is 'initial' when it is first created.
     * This sequence is older than any other sequence number.  Secondly, a
     * sequence number may be explicitly set to 'old'.  This is older than any
     * other sequence number except 'initial'.  Finally, we have the explicit
     * number 'fresh', which is newer than any other sequence number.  All other
     * sequences are numeric and are monotonically increasing.
     */
    """
    def assign(self, const_UpdateSeq_self, const_UpdateSeq_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const UpdateSeq self, const UpdateSeq copy)
        
        /**
         *
         */
        """
        pass

    def clear(self, const_UpdateSeq_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const UpdateSeq self)
        
        /**
         * Resets the UpdateSeq to the 'initial' state.
         */
        """
        pass

    def fresh(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        fresh()
        """
        pass

    def getSeq(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_seq(UpdateSeq self)
        
        /**
         * Returns the internal integer value associated with the UpdateSeq.  Useful
         * for debugging only.
         */
        """
        pass

    def get_seq(self, UpdateSeq_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_seq(UpdateSeq self)
        
        /**
         * Returns the internal integer value associated with the UpdateSeq.  Useful
         * for debugging only.
         */
        """
        pass

    def increment(self, const_UpdateSeq_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        increment(const UpdateSeq self)
        """
        pass

    def initial(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        initial()
        """
        pass

    def isFresh(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_fresh(UpdateSeq self)
        
        /**
         * Returns true if the UpdateSeq is in the 'fresh' state.
         */
        """
        pass

    def isInitial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_initial(UpdateSeq self)
        
        /**
         * Returns true if the UpdateSeq is in the 'initial' state.
         */
        """
        pass

    def isOld(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_old(UpdateSeq self)
        
        /**
         * Returns true if the UpdateSeq is in the 'old' state.
         */
        """
        pass

    def isSpecial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_special(UpdateSeq self)
        
        /**
         * Returns true if the UpdateSeq is in any special states, i.e.  'initial',
         * 'old', or 'fresh'.
         */
        """
        pass

    def is_fresh(self, UpdateSeq_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_fresh(UpdateSeq self)
        
        /**
         * Returns true if the UpdateSeq is in the 'fresh' state.
         */
        """
        pass

    def is_initial(self, UpdateSeq_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_initial(UpdateSeq self)
        
        /**
         * Returns true if the UpdateSeq is in the 'initial' state.
         */
        """
        pass

    def is_old(self, UpdateSeq_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_old(UpdateSeq self)
        
        /**
         * Returns true if the UpdateSeq is in the 'old' state.
         */
        """
        pass

    def is_special(self, UpdateSeq_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_special(UpdateSeq self)
        
        /**
         * Returns true if the UpdateSeq is in any special states, i.e.  'initial',
         * 'old', or 'fresh'.
         */
        """
        pass

    def old(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        old()
        """
        pass

    def output(self, UpdateSeq_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(UpdateSeq self, ostream out)
        
        /**
         *
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    seq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.UpdateSeq' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.UpdateSeq' objects>"
        '__doc__': "/**\n * This is a sequence number that increments monotonically.  It can be used to\n * track cache updates, or serve as a kind of timestamp for any changing\n * properties.\n *\n * A special class is used instead of simply an int, so we can elegantly\n * handle such things as wraparound and special cases.  There are two special\n * cases.  Firstly, a sequence number is 'initial' when it is first created.\n * This sequence is older than any other sequence number.  Secondly, a\n * sequence number may be explicitly set to 'old'.  This is older than any\n * other sequence number except 'initial'.  Finally, we have the explicit\n * number 'fresh', which is newer than any other sequence number.  All other\n * sequences are numeric and are monotonically increasing.\n */",
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.UpdateSeq' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.UpdateSeq' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.UpdateSeq' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.UpdateSeq' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.UpdateSeq' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.UpdateSeq' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.UpdateSeq' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.UpdateSeq' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE36F360>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.UpdateSeq' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.UpdateSeq' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.UpdateSeq' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.UpdateSeq' objects>"
        'fresh': None, # (!) real value is '<staticmethod(<built-in method fresh of type object at 0x00007FFCFE36F360>)>'
        'getSeq': None, # (!) real value is "<method 'getSeq' of 'panda3d.core.UpdateSeq' objects>"
        'get_seq': None, # (!) real value is "<method 'get_seq' of 'panda3d.core.UpdateSeq' objects>"
        'increment': None, # (!) real value is "<method 'increment' of 'panda3d.core.UpdateSeq' objects>"
        'initial': None, # (!) real value is '<staticmethod(<built-in method initial of type object at 0x00007FFCFE36F360>)>'
        'isFresh': None, # (!) real value is "<method 'isFresh' of 'panda3d.core.UpdateSeq' objects>"
        'isInitial': None, # (!) real value is "<method 'isInitial' of 'panda3d.core.UpdateSeq' objects>"
        'isOld': None, # (!) real value is "<method 'isOld' of 'panda3d.core.UpdateSeq' objects>"
        'isSpecial': None, # (!) real value is "<method 'isSpecial' of 'panda3d.core.UpdateSeq' objects>"
        'is_fresh': None, # (!) real value is "<method 'is_fresh' of 'panda3d.core.UpdateSeq' objects>"
        'is_initial': None, # (!) real value is "<method 'is_initial' of 'panda3d.core.UpdateSeq' objects>"
        'is_old': None, # (!) real value is "<method 'is_old' of 'panda3d.core.UpdateSeq' objects>"
        'is_special': None, # (!) real value is "<method 'is_special' of 'panda3d.core.UpdateSeq' objects>"
        'old': None, # (!) real value is '<staticmethod(<built-in method old of type object at 0x00007FFCFE36F360>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.UpdateSeq' objects>"
        'seq': None, # (!) real value is "<attribute 'seq' of 'panda3d.core.UpdateSeq' objects>"
    }


