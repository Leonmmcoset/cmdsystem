# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PartSubset(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class is used to define a subset of part names to apply to the
     * PartBundle::bind_anim() operation.  Only those part names within the subset
     * will be included in the bind.
     */
    """
    def addExcludeJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_exclude_joint(const PartSubset self, const GlobPattern name)
        
        /**
         * Adds the named joint to the list of joints that will be explicitly
         * exlcluded from the subset.  Any joint at or below a named node will not be
         * included in the subset (unless a lower node is also listed in the include
         * list).
         *
         * Since the name is a GlobPattern, it may of course include filename globbing
         * characters like * and ?.
         */
        """
        pass

    def addIncludeJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_include_joint(const PartSubset self, const GlobPattern name)
        
        /**
         * Adds the named joint to the list of joints that will be explicitly included
         * in the subset.  Any joint at or below a named node will be included in the
         * subset (unless a lower node is also listed in the exclude list).
         *
         * Since the name is a GlobPattern, it may of course include filename globbing
         * characters like * and ?.
         */
        """
        pass

    def add_exclude_joint(self, const_PartSubset_self, const_GlobPattern_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_exclude_joint(const PartSubset self, const GlobPattern name)
        
        /**
         * Adds the named joint to the list of joints that will be explicitly
         * exlcluded from the subset.  Any joint at or below a named node will not be
         * included in the subset (unless a lower node is also listed in the include
         * list).
         *
         * Since the name is a GlobPattern, it may of course include filename globbing
         * characters like * and ?.
         */
        """
        pass

    def add_include_joint(self, const_PartSubset_self, const_GlobPattern_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_include_joint(const PartSubset self, const GlobPattern name)
        
        /**
         * Adds the named joint to the list of joints that will be explicitly included
         * in the subset.  Any joint at or below a named node will be included in the
         * subset (unless a lower node is also listed in the exclude list).
         *
         * Since the name is a GlobPattern, it may of course include filename globbing
         * characters like * and ?.
         */
        """
        pass

    def append(self, const_PartSubset_self, const_PartSubset_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append(const PartSubset self, const PartSubset other)
        
        /**
         * Appends the include and exclude list from the other object onto this
         * object's lists.
         */
        """
        pass

    def assign(self, const_PartSubset_self, const_PartSubset_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const PartSubset self, const PartSubset copy)
        """
        pass

    def isIncludeEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_include_empty(PartSubset self)
        
        /**
         * Returns true if the include list is completely empty, false otherwise.  If
         * it is empty, it is the same thing as including all joints.
         */
        """
        pass

    def is_include_empty(self, PartSubset_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_include_empty(PartSubset self)
        
        /**
         * Returns true if the include list is completely empty, false otherwise.  If
         * it is empty, it is the same thing as including all joints.
         */
        """
        pass

    def matchesExclude(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        matches_exclude(PartSubset self, str joint_name)
        
        /**
         * Returns true if the indicated name matches a name on the exclude list,
         * false otherwise.
         */
        """
        pass

    def matchesInclude(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        matches_include(PartSubset self, str joint_name)
        
        /**
         * Returns true if the indicated name matches a name on the include list,
         * false otherwise.
         */
        """
        pass

    def matches_exclude(self, PartSubset_self, str_joint_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        matches_exclude(PartSubset self, str joint_name)
        
        /**
         * Returns true if the indicated name matches a name on the exclude list,
         * false otherwise.
         */
        """
        pass

    def matches_include(self, PartSubset_self, str_joint_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        matches_include(PartSubset self, str joint_name)
        
        /**
         * Returns true if the indicated name matches a name on the include list,
         * false otherwise.
         */
        """
        pass

    def output(self, PartSubset_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(PartSubset self, ostream out)
        
        /**
         *
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PartSubset' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PartSubset' objects>"
        '__doc__': '/**\n * This class is used to define a subset of part names to apply to the\n * PartBundle::bind_anim() operation.  Only those part names within the subset\n * will be included in the bind.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PartSubset' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C43D0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.PartSubset' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.PartSubset' objects>"
        'addExcludeJoint': None, # (!) real value is "<method 'addExcludeJoint' of 'panda3d.core.PartSubset' objects>"
        'addIncludeJoint': None, # (!) real value is "<method 'addIncludeJoint' of 'panda3d.core.PartSubset' objects>"
        'add_exclude_joint': None, # (!) real value is "<method 'add_exclude_joint' of 'panda3d.core.PartSubset' objects>"
        'add_include_joint': None, # (!) real value is "<method 'add_include_joint' of 'panda3d.core.PartSubset' objects>"
        'append': None, # (!) real value is "<method 'append' of 'panda3d.core.PartSubset' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.PartSubset' objects>"
        'isIncludeEmpty': None, # (!) real value is "<method 'isIncludeEmpty' of 'panda3d.core.PartSubset' objects>"
        'is_include_empty': None, # (!) real value is "<method 'is_include_empty' of 'panda3d.core.PartSubset' objects>"
        'matchesExclude': None, # (!) real value is "<method 'matchesExclude' of 'panda3d.core.PartSubset' objects>"
        'matchesInclude': None, # (!) real value is "<method 'matchesInclude' of 'panda3d.core.PartSubset' objects>"
        'matches_exclude': None, # (!) real value is "<method 'matches_exclude' of 'panda3d.core.PartSubset' objects>"
        'matches_include': None, # (!) real value is "<method 'matches_include' of 'panda3d.core.PartSubset' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.PartSubset' objects>"
    }


