# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class InternalNameCollection(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     *
     */
    """
    def addName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_name(const InternalNameCollection self, const InternalName name)
        
        /**
         * Adds a new InternalName to the collection.
         */
        """
        pass

    def addNamesFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_names_from(const InternalNameCollection self, const InternalNameCollection other)
        
        /**
         * Adds all the InternalNames indicated in the other collection to this name.
         * The other names are simply appended to the end of the names in this list;
         * duplicates are not automatically removed.
         */
        """
        pass

    def add_name(self, const_InternalNameCollection_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_name(const InternalNameCollection self, const InternalName name)
        
        /**
         * Adds a new InternalName to the collection.
         */
        """
        pass

    def add_names_from(self, const_InternalNameCollection_self, const_InternalNameCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_names_from(const InternalNameCollection self, const InternalNameCollection other)
        
        /**
         * Adds all the InternalNames indicated in the other collection to this name.
         * The other names are simply appended to the end of the names in this list;
         * duplicates are not automatically removed.
         */
        """
        pass

    def assign(self, const_InternalNameCollection_self, const_InternalNameCollection_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const InternalNameCollection self, const InternalNameCollection copy)
        """
        pass

    def clear(self, const_InternalNameCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const InternalNameCollection self)
        
        /**
         * Removes all InternalNames from the collection.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(InternalNameCollection self, int index)
        
        /**
         * Returns the nth InternalName in the collection.
         */
        """
        pass

    def getNames(self, *args, **kwargs): # real signature unknown
        pass

    def getNumNames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_names(InternalNameCollection self)
        
        /**
         * Returns the number of InternalNames in the collection.
         */
        """
        pass

    def get_name(self, InternalNameCollection_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(InternalNameCollection self, int index)
        
        /**
         * Returns the nth InternalName in the collection.
         */
        """
        pass

    def get_names(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_names(self, InternalNameCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_names(InternalNameCollection self)
        
        /**
         * Returns the number of InternalNames in the collection.
         */
        """
        pass

    def hasName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_name(InternalNameCollection self, const InternalName name)
        
        /**
         * Returns true if the indicated InternalName appears in this collection,
         * false otherwise.
         */
        """
        pass

    def has_name(self, InternalNameCollection_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_name(InternalNameCollection self, const InternalName name)
        
        /**
         * Returns true if the indicated InternalName appears in this collection,
         * false otherwise.
         */
        """
        pass

    def output(self, InternalNameCollection_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(InternalNameCollection self, ostream out)
        
        /**
         * Writes a brief one-line description of the InternalNameCollection to the
         * indicated output stream.
         */
        """
        pass

    def removeDuplicateNames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_duplicate_names(const InternalNameCollection self)
        
        /**
         * Removes any duplicate entries of the same InternalNames on this collection.
         * If a InternalName appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def removeName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_name(const InternalNameCollection self, const InternalName name)
        
        /**
         * Removes the indicated InternalName from the collection.  Returns true if
         * the name was removed, false if it was not a member of the collection.
         */
        """
        pass

    def removeNamesFrom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_names_from(const InternalNameCollection self, const InternalNameCollection other)
        
        /**
         * Removes from this collection all of the InternalNames listed in the other
         * collection.
         */
        """
        pass

    def remove_duplicate_names(self, const_InternalNameCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_duplicate_names(const InternalNameCollection self)
        
        /**
         * Removes any duplicate entries of the same InternalNames on this collection.
         * If a InternalName appears multiple times, the first appearance is retained;
         * subsequent appearances are removed.
         */
        """
        pass

    def remove_name(self, const_InternalNameCollection_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_name(const InternalNameCollection self, const InternalName name)
        
        /**
         * Removes the indicated InternalName from the collection.  Returns true if
         * the name was removed, false if it was not a member of the collection.
         */
        """
        pass

    def remove_names_from(self, const_InternalNameCollection_self, const_InternalNameCollection_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_names_from(const InternalNameCollection self, const InternalNameCollection other)
        
        /**
         * Removes from this collection all of the InternalNames listed in the other
         * collection.
         */
        """
        pass

    def write(self, InternalNameCollection_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(InternalNameCollection self, ostream out, int indent_level)
        
        /**
         * Writes a complete multi-line description of the InternalNameCollection to
         * the indicated output stream.
         */
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__add__': None, # (!) real value is "<slot wrapper '__add__' of 'panda3d.core.InternalNameCollection' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.InternalNameCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.InternalNameCollection' objects>"
        '__doc__': '/**\n *\n */',
        '__getitem__': None, # (!) real value is "<slot wrapper '__getitem__' of 'panda3d.core.InternalNameCollection' objects>"
        '__iadd__': None, # (!) real value is "<slot wrapper '__iadd__' of 'panda3d.core.InternalNameCollection' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.InternalNameCollection' objects>"
        '__len__': None, # (!) real value is "<slot wrapper '__len__' of 'panda3d.core.InternalNameCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE293500>'
        '__radd__': None, # (!) real value is "<slot wrapper '__radd__' of 'panda3d.core.InternalNameCollection' objects>"
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.InternalNameCollection' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.InternalNameCollection' objects>"
        'addName': None, # (!) real value is "<method 'addName' of 'panda3d.core.InternalNameCollection' objects>"
        'addNamesFrom': None, # (!) real value is "<method 'addNamesFrom' of 'panda3d.core.InternalNameCollection' objects>"
        'add_name': None, # (!) real value is "<method 'add_name' of 'panda3d.core.InternalNameCollection' objects>"
        'add_names_from': None, # (!) real value is "<method 'add_names_from' of 'panda3d.core.InternalNameCollection' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.InternalNameCollection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.InternalNameCollection' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.InternalNameCollection' objects>"
        'getNames': None, # (!) real value is "<method 'getNames' of 'panda3d.core.InternalNameCollection' objects>"
        'getNumNames': None, # (!) real value is "<method 'getNumNames' of 'panda3d.core.InternalNameCollection' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.InternalNameCollection' objects>"
        'get_names': None, # (!) real value is "<method 'get_names' of 'panda3d.core.InternalNameCollection' objects>"
        'get_num_names': None, # (!) real value is "<method 'get_num_names' of 'panda3d.core.InternalNameCollection' objects>"
        'hasName': None, # (!) real value is "<method 'hasName' of 'panda3d.core.InternalNameCollection' objects>"
        'has_name': None, # (!) real value is "<method 'has_name' of 'panda3d.core.InternalNameCollection' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.InternalNameCollection' objects>"
        'removeDuplicateNames': None, # (!) real value is "<method 'removeDuplicateNames' of 'panda3d.core.InternalNameCollection' objects>"
        'removeName': None, # (!) real value is "<method 'removeName' of 'panda3d.core.InternalNameCollection' objects>"
        'removeNamesFrom': None, # (!) real value is "<method 'removeNamesFrom' of 'panda3d.core.InternalNameCollection' objects>"
        'remove_duplicate_names': None, # (!) real value is "<method 'remove_duplicate_names' of 'panda3d.core.InternalNameCollection' objects>"
        'remove_name': None, # (!) real value is "<method 'remove_name' of 'panda3d.core.InternalNameCollection' objects>"
        'remove_names_from': None, # (!) real value is "<method 'remove_names_from' of 'panda3d.core.InternalNameCollection' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.InternalNameCollection' objects>"
    }


