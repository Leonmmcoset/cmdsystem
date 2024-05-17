# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

from .Namable import Namable

class AnimGroup(TypedWritableReferenceCount, Namable):
    """
    /**
     * This is the base class for AnimChannel and AnimBundle.  It implements a
     * hierarchy of AnimChannels.  The root of the hierarchy must be an
     * AnimBundle.
     */
    """
    def findChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_child(AnimGroup self, str name)
        
        /**
         * Returns the first descendant found with the indicated name, or NULL if no
         * such descendant exists.  This method searches the entire graph beginning at
         * this AnimGroup; see also get_child_named().
         */
        """
        pass

    def find_child(self, AnimGroup_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_child(AnimGroup self, str name)
        
        /**
         * Returns the first descendant found with the indicated name, or NULL if no
         * such descendant exists.  This method searches the entire graph beginning at
         * this AnimGroup; see also get_child_named().
         */
        """
        pass

    def getChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child(AnimGroup self, int n)
        
        /**
         * Returns the nth child of the group.
         */
        """
        pass

    def getChildNamed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child_named(AnimGroup self, str name)
        
        /**
         * Returns the first child found with the indicated name, or NULL if no such
         * child exists.  This method searches only the children of this particular
         * AnimGroup; it does not recursively search the entire graph.  See also
         * find_child().
         */
        """
        pass

    def getChildren(self, *args, **kwargs): # real signature unknown
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNumChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_children(AnimGroup self)
        
        /**
         * Returns the number of child nodes of the group.
         */
        """
        pass

    def get_child(self, AnimGroup_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child(AnimGroup self, int n)
        
        /**
         * Returns the nth child of the group.
         */
        """
        pass

    def get_children(self, *args, **kwargs): # real signature unknown
        pass

    def get_child_named(self, AnimGroup_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child_named(AnimGroup self, str name)
        
        /**
         * Returns the first child found with the indicated name, or NULL if no such
         * child exists.  This method searches only the children of this particular
         * AnimGroup; it does not recursively search the entire graph.  See also
         * find_child().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_num_children(self, AnimGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_children(AnimGroup self)
        
        /**
         * Returns the number of child nodes of the group.
         */
        """
        pass

    def output(self, AnimGroup_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(AnimGroup self, ostream out)
        
        /**
         * Writes a one-line description of the group.
         */
        """
        pass

    def sortDescendants(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sort_descendants(const AnimGroup self)
        
        /**
         * Sorts the children nodes at each level of the hierarchy into alphabetical
         * order.  This should be done after creating the hierarchy, to guarantee that
         * the correct names will match up together when the AnimBundle is later bound
         * to a PlayerRoot.
         */
        """
        pass

    def sort_descendants(self, const_AnimGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sort_descendants(const AnimGroup self)
        
        /**
         * Sorts the children nodes at each level of the hierarchy into alphabetical
         * order.  This should be done after creating the hierarchy, to guarantee that
         * the correct names will match up together when the AnimBundle is later bound
         * to a PlayerRoot.
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const AnimGroup self)
        
        upcast from AnimGroup to Namable
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const AnimGroup self)
        
        upcast from AnimGroup to TypedWritableReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_AnimGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const AnimGroup self)
        
        upcast from AnimGroup to Namable
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_AnimGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const AnimGroup self)
        
        upcast from AnimGroup to TypedWritableReferenceCount
        """
        pass

    def write(self, AnimGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(AnimGroup self, ostream out, int indent_level)
        
        /**
         * Writes a brief description of the group and all of its descendants.
         */
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.AnimGroup' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.AnimGroup' objects>"
        '__doc__': '/**\n * This is the base class for AnimChannel and AnimBundle.  It implements a\n * hierarchy of AnimChannels.  The root of the hierarchy must be an\n * AnimBundle.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.AnimGroup' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C2A60>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.AnimGroup' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.AnimGroup' objects>"
        'children': None, # (!) real value is "<attribute 'children' of 'panda3d.core.AnimGroup' objects>"
        'findChild': None, # (!) real value is "<method 'findChild' of 'panda3d.core.AnimGroup' objects>"
        'find_child': None, # (!) real value is "<method 'find_child' of 'panda3d.core.AnimGroup' objects>"
        'getChild': None, # (!) real value is "<method 'getChild' of 'panda3d.core.AnimGroup' objects>"
        'getChildNamed': None, # (!) real value is "<method 'getChildNamed' of 'panda3d.core.AnimGroup' objects>"
        'getChildren': None, # (!) real value is "<method 'getChildren' of 'panda3d.core.AnimGroup' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C2A60>)>'
        'getNumChildren': None, # (!) real value is "<method 'getNumChildren' of 'panda3d.core.AnimGroup' objects>"
        'get_child': None, # (!) real value is "<method 'get_child' of 'panda3d.core.AnimGroup' objects>"
        'get_child_named': None, # (!) real value is "<method 'get_child_named' of 'panda3d.core.AnimGroup' objects>"
        'get_children': None, # (!) real value is "<method 'get_children' of 'panda3d.core.AnimGroup' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C2A60>)>'
        'get_num_children': None, # (!) real value is "<method 'get_num_children' of 'panda3d.core.AnimGroup' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.AnimGroup' objects>"
        'sortDescendants': None, # (!) real value is "<method 'sortDescendants' of 'panda3d.core.AnimGroup' objects>"
        'sort_descendants': None, # (!) real value is "<method 'sort_descendants' of 'panda3d.core.AnimGroup' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.AnimGroup' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.AnimGroup' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.AnimGroup' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.AnimGroup' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.AnimGroup' objects>"
    }


