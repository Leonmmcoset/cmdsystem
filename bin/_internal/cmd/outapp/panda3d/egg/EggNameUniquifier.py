# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggObject import EggObject

class EggNameUniquifier(EggObject):
    """
    /**
     * This is a handy class for guaranteeing unique node names in an egg
     * hierarchy.  It is an abstract class; to use it you must subclass off of it.
     * See the comment above.
     */
    """
    def addName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_name(const EggNameUniquifier self, str category, str name, EggNode node)
        
        /**
         * Adds the name to the indicated category.  This name will not be used for
         * any other egg node within this category.  Returns true if the name was
         * added, or false if it was already in use for the category.
         */
        """
        pass

    def add_name(self, const_EggNameUniquifier_self, str_category, str_name, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_name(const EggNameUniquifier self, str category, str name, EggNode node)
        
        /**
         * Adds the name to the indicated category.  This name will not be used for
         * any other egg node within this category.  Returns true if the name was
         * added, or false if it was already in use for the category.
         */
        """
        pass

    def clear(self, const_EggNameUniquifier_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const EggNameUniquifier self)
        
        /**
         * Empties the table of used named and prepares the Uniquifier for a new tree.
         */
        """
        pass

    def filterName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        filter_name(const EggNameUniquifier self, EggNode node)
        
        /**
         * Returns the name of the given node, or at least the name it should be.
         * This provides a hook to adjust the name before attempting to uniquify it,
         * if desired, for instance to remove invalid characters.
         */
        """
        pass

    def filter_name(self, const_EggNameUniquifier_self, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        filter_name(const EggNameUniquifier self, EggNode node)
        
        /**
         * Returns the name of the given node, or at least the name it should be.
         * This provides a hook to adjust the name before attempting to uniquify it,
         * if desired, for instance to remove invalid characters.
         */
        """
        pass

    def generateName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_name(const EggNameUniquifier self, EggNode node, str category, int index)
        
        /**
         * Generates a new name for the given node when its existing name clashes with
         * some other node.  This function will be called repeatedly, if necessary,
         * until it returns a name that actually is unique.
         *
         * The category is the string returned by get_category(), and index is a
         * uniquely-generated number that may be useful for synthesizing the name.
         */
        """
        pass

    def generate_name(self, const_EggNameUniquifier_self, EggNode_node, str_category, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_name(const EggNameUniquifier self, EggNode node, str category, int index)
        
        /**
         * Generates a new name for the given node when its existing name clashes with
         * some other node.  This function will be called repeatedly, if necessary,
         * until it returns a name that actually is unique.
         *
         * The category is the string returned by get_category(), and index is a
         * uniquely-generated number that may be useful for synthesizing the name.
         */
        """
        pass

    def getCategory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_category(const EggNameUniquifier self, EggNode node)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node(EggNameUniquifier self, str category, str name)
        
        /**
         * Returns the node associated with the given category and name, or NULL if
         * the name has not been used.
         */
        """
        pass

    def get_category(self, const_EggNameUniquifier_self, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_category(const EggNameUniquifier self, EggNode node)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_node(self, EggNameUniquifier_self, str_category, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(EggNameUniquifier self, str category, str name)
        
        /**
         * Returns the node associated with the given category and name, or NULL if
         * the name has not been used.
         */
        """
        pass

    def hasName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_name(EggNameUniquifier self, str category, str name)
        
        /**
         * Returns true if the name has been used for the indicated category already,
         * false otherwise.
         */
        """
        pass

    def has_name(self, EggNameUniquifier_self, str_category, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_name(EggNameUniquifier self, str category, str name)
        
        /**
         * Returns true if the name has been used for the indicated category already,
         * false otherwise.
         */
        """
        pass

    def uniquify(self, const_EggNameUniquifier_self, EggNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uniquify(const EggNameUniquifier self, EggNode node)
        
        /**
         * Begins the traversal from the indicated node.
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
        '__doc__': '/**\n * This is a handy class for guaranteeing unique node names in an egg\n * hierarchy.  It is an abstract class; to use it you must subclass off of it.\n * See the comment above.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggNameUniquifier' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CFA40>'
        'addName': None, # (!) real value is "<method 'addName' of 'panda3d.egg.EggNameUniquifier' objects>"
        'add_name': None, # (!) real value is "<method 'add_name' of 'panda3d.egg.EggNameUniquifier' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.egg.EggNameUniquifier' objects>"
        'filterName': None, # (!) real value is "<method 'filterName' of 'panda3d.egg.EggNameUniquifier' objects>"
        'filter_name': None, # (!) real value is "<method 'filter_name' of 'panda3d.egg.EggNameUniquifier' objects>"
        'generateName': None, # (!) real value is "<method 'generateName' of 'panda3d.egg.EggNameUniquifier' objects>"
        'generate_name': None, # (!) real value is "<method 'generate_name' of 'panda3d.egg.EggNameUniquifier' objects>"
        'getCategory': None, # (!) real value is "<method 'getCategory' of 'panda3d.egg.EggNameUniquifier' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CFA40>)>'
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.egg.EggNameUniquifier' objects>"
        'get_category': None, # (!) real value is "<method 'get_category' of 'panda3d.egg.EggNameUniquifier' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CFA40>)>'
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.egg.EggNameUniquifier' objects>"
        'hasName': None, # (!) real value is "<method 'hasName' of 'panda3d.egg.EggNameUniquifier' objects>"
        'has_name': None, # (!) real value is "<method 'has_name' of 'panda3d.egg.EggNameUniquifier' objects>"
        'uniquify': None, # (!) real value is "<method 'uniquify' of 'panda3d.egg.EggNameUniquifier' objects>"
    }


