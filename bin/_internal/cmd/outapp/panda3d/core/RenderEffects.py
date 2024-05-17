# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class RenderEffects(TypedWritableReferenceCount):
    """
    /**
     * This represents a unique collection of RenderEffect objects that correspond
     * to a particular renderable state.
     *
     * You should not attempt to create or modify a RenderEffects object directly.
     * Instead, call one of the make() functions to create one for you.  And
     * instead of modifying a RenderEffects object, create a new one.
     */
    """
    def addEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_effect(RenderEffects self, const RenderEffect effect)
        
        /**
         * Returns a new RenderEffects object that represents the same as the source
         * state, with the new RenderEffect added.  If there is already a RenderEffect
         * with the same type, it is replaced.
         */
        """
        pass

    def add_effect(self, RenderEffects_self, const_RenderEffect_effect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_effect(RenderEffects self, const RenderEffect effect)
        
        /**
         * Returns a new RenderEffects object that represents the same as the source
         * state, with the new RenderEffect added.  If there is already a RenderEffect
         * with the same type, it is replaced.
         */
        """
        pass

    def findEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_effect(RenderEffects self, TypeHandle type)
        
        /**
         * Searches for an effect with the indicated type in the state, and returns
         * its index if it is found, or -1 if it is not.
         */
        """
        pass

    def find_effect(self, RenderEffects_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_effect(RenderEffects self, TypeHandle type)
        
        /**
         * Searches for an effect with the indicated type in the state, and returns
         * its index if it is found, or -1 if it is not.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effect(RenderEffects self, TypeHandle type)
        get_effect(RenderEffects self, int n)
        
        /**
         * Returns the nth effect in the state.
         */
        
        /**
         * Looks for a RenderEffect of the indicated type in the state, and returns it
         * if it is found, or NULL if it is not.
         */
        """
        pass

    def getNumEffects(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_effects(RenderEffects self)
        
        /**
         * Returns the number of separate effects indicated in the state.
         * @deprecated in Python, use len(effects) instead, or effects.size() in C++.
         */
        """
        pass

    def getNumStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_states()
        
        /**
         * Returns the total number of unique RenderEffects objects allocated in the
         * world.  This will go up and down during normal operations.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_effect(self, RenderEffects_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effect(RenderEffects self, TypeHandle type)
        get_effect(RenderEffects self, int n)
        
        /**
         * Returns the nth effect in the state.
         */
        
        /**
         * Looks for a RenderEffect of the indicated type in the state, and returns it
         * if it is found, or NULL if it is not.
         */
        """
        pass

    def get_num_effects(self, RenderEffects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_effects(RenderEffects self)
        
        /**
         * Returns the number of separate effects indicated in the state.
         * @deprecated in Python, use len(effects) instead, or effects.size() in C++.
         */
        """
        pass

    def get_num_states(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_states()
        
        /**
         * Returns the total number of unique RenderEffects objects allocated in the
         * world.  This will go up and down during normal operations.
         */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(RenderEffects self)
        
        /**
         * Returns true if the state is empty, false otherwise.
         */
        """
        pass

    def is_empty(self, RenderEffects_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(RenderEffects self)
        
        /**
         * Returns true if the state is empty, false otherwise.
         */
        """
        pass

    def listStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        list_states(ostream out)
        
        /**
         * Lists all of the RenderEffects in the cache to the output stream, one per
         * line.  This can be quite a lot of output if the cache is large, so be
         * prepared.
         */
        """
        pass

    def list_states(self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        list_states(ostream out)
        
        /**
         * Lists all of the RenderEffects in the cache to the output stream, one per
         * line.  This can be quite a lot of output if the cache is large, so be
         * prepared.
         */
        """
        pass

    def make(self, const_RenderEffect_effect): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(const RenderEffect effect)
        make(const RenderEffect effect1, const RenderEffect effect2)
        make(const RenderEffect effect1, const RenderEffect effect2, const RenderEffect effect3)
        make(const RenderEffect effect1, const RenderEffect effect2, const RenderEffect effect3, const RenderEffect effect4)
        
        /**
         * Returns a RenderEffects with one effect set.
         */
        
        /**
         * Returns a RenderEffects with two effects set.
         */
        
        /**
         * Returns a RenderEffects with three effects set.
         */
        
        /**
         * Returns a RenderEffects with four effects set.
         */
        """
        pass

    def makeEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_empty()
        
        /**
         * Returns a RenderEffects with no effects set.
         */
        """
        pass

    def make_empty(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_empty()
        
        /**
         * Returns a RenderEffects with no effects set.
         */
        """
        pass

    def output(self, RenderEffects_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(RenderEffects self, ostream out)
        
        /**
         *
         */
        """
        pass

    def removeEffect(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_effect(RenderEffects self, TypeHandle type)
        
        /**
         * Returns a new RenderEffects object that represents the same as the source
         * state, with the indicated RenderEffect removed.
         */
        """
        pass

    def remove_effect(self, RenderEffects_self, TypeHandle_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_effect(RenderEffects self, TypeHandle type)
        
        /**
         * Returns a new RenderEffects object that represents the same as the source
         * state, with the indicated RenderEffect removed.
         */
        """
        pass

    def validateStates(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        validate_states()
        
        /**
         * Ensures that the cache is still stored in sorted order.  Returns true if
         * so, false if there is a problem (which implies someone has modified one of
         * the supposedly-const RenderEffects objects).
         */
        """
        pass

    def validate_states(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        validate_states()
        
        /**
         * Ensures that the cache is still stored in sorted order.  Returns true if
         * so, false if there is a problem (which implies someone has modified one of
         * the supposedly-const RenderEffects objects).
         */
        """
        pass

    def write(self, RenderEffects_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(RenderEffects self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * This represents a unique collection of RenderEffect objects that correspond\n * to a particular renderable state.\n *\n * You should not attempt to create or modify a RenderEffects object directly.\n * Instead, call one of the make() functions to create one for you.  And\n * instead of modifying a RenderEffects object, create a new one.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.RenderEffects' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.RenderEffects' objects>"
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.RenderEffects' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.RenderEffects' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.RenderEffects' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.RenderEffects' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.RenderEffects' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.RenderEffects' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.RenderEffects' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.RenderEffects' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE292680>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.RenderEffects' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.RenderEffects' objects>"
        'addEffect': None, # (!) real value is "<method 'addEffect' of 'panda3d.core.RenderEffects' objects>"
        'add_effect': None, # (!) real value is "<method 'add_effect' of 'panda3d.core.RenderEffects' objects>"
        'findEffect': None, # (!) real value is "<method 'findEffect' of 'panda3d.core.RenderEffects' objects>"
        'find_effect': None, # (!) real value is "<method 'find_effect' of 'panda3d.core.RenderEffects' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE292680>)>'
        'getEffect': None, # (!) real value is "<method 'getEffect' of 'panda3d.core.RenderEffects' objects>"
        'getNumEffects': None, # (!) real value is "<method 'getNumEffects' of 'panda3d.core.RenderEffects' objects>"
        'getNumStates': None, # (!) real value is '<staticmethod(<built-in method getNumStates of type object at 0x00007FFCFE292680>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE292680>)>'
        'get_effect': None, # (!) real value is "<method 'get_effect' of 'panda3d.core.RenderEffects' objects>"
        'get_num_effects': None, # (!) real value is "<method 'get_num_effects' of 'panda3d.core.RenderEffects' objects>"
        'get_num_states': None, # (!) real value is '<staticmethod(<built-in method get_num_states of type object at 0x00007FFCFE292680>)>'
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.core.RenderEffects' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.core.RenderEffects' objects>"
        'listStates': None, # (!) real value is '<staticmethod(<built-in method listStates of type object at 0x00007FFCFE292680>)>'
        'list_states': None, # (!) real value is '<staticmethod(<built-in method list_states of type object at 0x00007FFCFE292680>)>'
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE292680>)>'
        'makeEmpty': None, # (!) real value is '<staticmethod(<built-in method makeEmpty of type object at 0x00007FFCFE292680>)>'
        'make_empty': None, # (!) real value is '<staticmethod(<built-in method make_empty of type object at 0x00007FFCFE292680>)>'
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.RenderEffects' objects>"
        'removeEffect': None, # (!) real value is "<method 'removeEffect' of 'panda3d.core.RenderEffects' objects>"
        'remove_effect': None, # (!) real value is "<method 'remove_effect' of 'panda3d.core.RenderEffects' objects>"
        'validateStates': None, # (!) real value is '<staticmethod(<built-in method validateStates of type object at 0x00007FFCFE292680>)>'
        'validate_states': None, # (!) real value is '<staticmethod(<built-in method validate_states of type object at 0x00007FFCFE292680>)>'
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.RenderEffects' objects>"
    }


