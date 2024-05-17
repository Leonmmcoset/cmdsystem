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

class PartGroup(TypedWritableReferenceCount, Namable):
    """
    /**
     * This is the base class for PartRoot and MovingPart.  It defines a hierarchy
     * of MovingParts.
     */
    """
    def applyControl(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_control(const PartGroup self, PandaNode node)
        
        /**
         * Specifies a node to influence this particular joint so that it will always
         * hold the node's transform.  Returns true if this is a joint that can be so
         * controlled, false otherwise.
         *
         * This is normally only called internally by PartBundle::control_joint(), but
         * you may also call it directly.
         */
        """
        pass

    def applyFreeze(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_freeze(const PartGroup self, const TransformState transform)
        
        /**
         * Freezes this particular joint so that it will always hold the specified
         * transform.  Returns true if this is a joint that can be so frozen, false
         * otherwise.
         *
         * This is normally only called internally by PartBundle::freeze_joint(), but
         * you may also call it directly.
         */
        """
        pass

    def applyFreezeMatrix(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_freeze_matrix(const PartGroup self, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale)
        
        /**
         * Freezes this particular joint so that it will always hold the specified
         * transform.  Returns true if this is a joint that can be so frozen, false
         * otherwise.
         *
         * This is normally only called internally by PartBundle::freeze_joint(), but
         * you may also call it directly.
         */
        """
        pass

    def applyFreezeScalar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_freeze_scalar(const PartGroup self, float value)
        
        /**
         * Freezes this particular joint so that it will always hold the specified
         * transform.  Returns true if this is a joint that can be so frozen, false
         * otherwise.
         *
         * This is normally only called internally by PartBundle::freeze_joint(), but
         * you may also call it directly.
         */
        """
        pass

    def apply_control(self, const_PartGroup_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_control(const PartGroup self, PandaNode node)
        
        /**
         * Specifies a node to influence this particular joint so that it will always
         * hold the node's transform.  Returns true if this is a joint that can be so
         * controlled, false otherwise.
         *
         * This is normally only called internally by PartBundle::control_joint(), but
         * you may also call it directly.
         */
        """
        pass

    def apply_freeze(self, const_PartGroup_self, const_TransformState_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_freeze(const PartGroup self, const TransformState transform)
        
        /**
         * Freezes this particular joint so that it will always hold the specified
         * transform.  Returns true if this is a joint that can be so frozen, false
         * otherwise.
         *
         * This is normally only called internally by PartBundle::freeze_joint(), but
         * you may also call it directly.
         */
        """
        pass

    def apply_freeze_matrix(self, const_PartGroup_self, const_LVecBase3f_pos, const_LVecBase3f_hpr, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_freeze_matrix(const PartGroup self, const LVecBase3f pos, const LVecBase3f hpr, const LVecBase3f scale)
        
        /**
         * Freezes this particular joint so that it will always hold the specified
         * transform.  Returns true if this is a joint that can be so frozen, false
         * otherwise.
         *
         * This is normally only called internally by PartBundle::freeze_joint(), but
         * you may also call it directly.
         */
        """
        pass

    def apply_freeze_scalar(self, const_PartGroup_self, float_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_freeze_scalar(const PartGroup self, float value)
        
        /**
         * Freezes this particular joint so that it will always hold the specified
         * transform.  Returns true if this is a joint that can be so frozen, false
         * otherwise.
         *
         * This is normally only called internally by PartBundle::freeze_joint(), but
         * you may also call it directly.
         */
        """
        pass

    def clearForcedChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_forced_channel(const PartGroup self)
        
        /**
         * Undoes the effect of a previous call to apply_freeze() or apply_control().
         * Returns true if the joint was modified, false otherwise.
         *
         * This is normally only called internally by PartBundle::release_joint(), but
         * you may also call it directly.
         */
        """
        pass

    def clear_forced_channel(self, const_PartGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_forced_channel(const PartGroup self)
        
        /**
         * Undoes the effect of a previous call to apply_freeze() or apply_control().
         * Returns true if the joint was modified, false otherwise.
         *
         * This is normally only called internally by PartBundle::release_joint(), but
         * you may also call it directly.
         */
        """
        pass

    def copySubgraph(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        copy_subgraph(PartGroup self)
        
        /**
         * Allocates and returns a new copy of this node and of all of its children.
         */
        """
        pass

    def copy_subgraph(self, PartGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        copy_subgraph(PartGroup self)
        
        /**
         * Allocates and returns a new copy of this node and of all of its children.
         */
        """
        pass

    def findChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_child(PartGroup self, str name)
        
        /**
         * Returns the first descendant found with the indicated name, or NULL if no
         * such descendant exists.  This method searches the entire graph beginning at
         * this PartGroup; see also get_child_named().
         */
        """
        pass

    def find_child(self, PartGroup_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_child(PartGroup self, str name)
        
        /**
         * Returns the first descendant found with the indicated name, or NULL if no
         * such descendant exists.  This method searches the entire graph beginning at
         * this PartGroup; see also get_child_named().
         */
        """
        pass

    def getChild(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child(PartGroup self, int n)
        
        /**
         * Returns the nth child of the group.
         */
        """
        pass

    def getChildNamed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_child_named(PartGroup self, str name)
        
        /**
         * Returns the first child found with the indicated name, or NULL if no such
         * child exists.  This method searches only the children of this particular
         * PartGroup; it does not recursively search the entire graph.  See also
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

    def getForcedChannel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_forced_channel(PartGroup self)
        
        /**
         * Returns the AnimChannelBase that has been forced to this joint by a
         * previous call to apply_freeze() or apply_control(), or NULL if no such
         * channel has been applied.
         */
        """
        pass

    def getNumChildren(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_children(PartGroup self)
        
        /**
         * Returns the number of child nodes of the group.
         */
        """
        pass

    def get_child(self, PartGroup_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child(PartGroup self, int n)
        
        /**
         * Returns the nth child of the group.
         */
        """
        pass

    def get_children(self, *args, **kwargs): # real signature unknown
        pass

    def get_child_named(self, PartGroup_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_child_named(PartGroup self, str name)
        
        /**
         * Returns the first child found with the indicated name, or NULL if no such
         * child exists.  This method searches only the children of this particular
         * PartGroup; it does not recursively search the entire graph.  See also
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

    def get_forced_channel(self, PartGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_forced_channel(PartGroup self)
        
        /**
         * Returns the AnimChannelBase that has been forced to this joint by a
         * previous call to apply_freeze() or apply_control(), or NULL if no such
         * channel has been applied.
         */
        """
        pass

    def get_num_children(self, PartGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_children(PartGroup self)
        
        /**
         * Returns the number of child nodes of the group.
         */
        """
        pass

    def isCharacterJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_character_joint(PartGroup self)
        
        /**
         * Returns true if this part is a CharacterJoint, false otherwise.  This is a
         * tiny optimization over is_of_type(CharacterType::get_class_type()).
         */
        """
        pass

    def is_character_joint(self, PartGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_character_joint(PartGroup self)
        
        /**
         * Returns true if this part is a CharacterJoint, false otherwise.  This is a
         * tiny optimization over is_of_type(CharacterType::get_class_type()).
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(PartGroup self)
        
        /**
         * Allocates and returns a new copy of the node.  Children are not copied, but
         * see copy_subgraph().
         */
        """
        pass

    def make_copy(self, PartGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(PartGroup self)
        
        /**
         * Allocates and returns a new copy of the node.  Children are not copied, but
         * see copy_subgraph().
         */
        """
        pass

    def sortDescendants(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        sort_descendants(const PartGroup self)
        
        /**
         * Sorts the children nodes at each level of the hierarchy into alphabetical
         * order.  This should be done after creating the hierarchy, to guarantee that
         * the correct names will match up together when the AnimBundle is later bound
         * to a PlayerRoot.
         */
        """
        pass

    def sort_descendants(self, const_PartGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        sort_descendants(const PartGroup self)
        
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
        upcast_to_Namable(const PartGroup self)
        
        upcast from PartGroup to Namable
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const PartGroup self)
        
        upcast from PartGroup to TypedWritableReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_PartGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const PartGroup self)
        
        upcast from PartGroup to Namable
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_PartGroup_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const PartGroup self)
        
        upcast from PartGroup to TypedWritableReferenceCount
        """
        pass

    def write(self, PartGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(PartGroup self, ostream out, int indent_level)
        
        /**
         * Writes a brief description of the group and all of its descendants.
         */
        """
        pass

    def writeWithValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_with_value(PartGroup self, ostream out, int indent_level)
        
        /**
         * Writes a brief description of the group, showing its current value, and
         * that of all of its descendants.
         */
        """
        pass

    def write_with_value(self, PartGroup_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_with_value(PartGroup self, ostream out, int indent_level)
        
        /**
         * Writes a brief description of the group, showing its current value, and
         * that of all of its descendants.
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'HMFOkAnimExtra': 2,
        'HMFOkPartExtra': 1,
        'HMFOkWrongRootName': 4,
        'HMF_ok_anim_extra': 2,
        'HMF_ok_part_extra': 1,
        'HMF_ok_wrong_root_name': 4,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PartGroup' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PartGroup' objects>"
        '__doc__': '/**\n * This is the base class for PartRoot and MovingPart.  It defines a hierarchy\n * of MovingParts.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PartGroup' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2C2FE0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.PartGroup' objects>"
        'applyControl': None, # (!) real value is "<method 'applyControl' of 'panda3d.core.PartGroup' objects>"
        'applyFreeze': None, # (!) real value is "<method 'applyFreeze' of 'panda3d.core.PartGroup' objects>"
        'applyFreezeMatrix': None, # (!) real value is "<method 'applyFreezeMatrix' of 'panda3d.core.PartGroup' objects>"
        'applyFreezeScalar': None, # (!) real value is "<method 'applyFreezeScalar' of 'panda3d.core.PartGroup' objects>"
        'apply_control': None, # (!) real value is "<method 'apply_control' of 'panda3d.core.PartGroup' objects>"
        'apply_freeze': None, # (!) real value is "<method 'apply_freeze' of 'panda3d.core.PartGroup' objects>"
        'apply_freeze_matrix': None, # (!) real value is "<method 'apply_freeze_matrix' of 'panda3d.core.PartGroup' objects>"
        'apply_freeze_scalar': None, # (!) real value is "<method 'apply_freeze_scalar' of 'panda3d.core.PartGroup' objects>"
        'children': None, # (!) real value is "<attribute 'children' of 'panda3d.core.PartGroup' objects>"
        'clearForcedChannel': None, # (!) real value is "<method 'clearForcedChannel' of 'panda3d.core.PartGroup' objects>"
        'clear_forced_channel': None, # (!) real value is "<method 'clear_forced_channel' of 'panda3d.core.PartGroup' objects>"
        'copySubgraph': None, # (!) real value is "<method 'copySubgraph' of 'panda3d.core.PartGroup' objects>"
        'copy_subgraph': None, # (!) real value is "<method 'copy_subgraph' of 'panda3d.core.PartGroup' objects>"
        'findChild': None, # (!) real value is "<method 'findChild' of 'panda3d.core.PartGroup' objects>"
        'find_child': None, # (!) real value is "<method 'find_child' of 'panda3d.core.PartGroup' objects>"
        'getChild': None, # (!) real value is "<method 'getChild' of 'panda3d.core.PartGroup' objects>"
        'getChildNamed': None, # (!) real value is "<method 'getChildNamed' of 'panda3d.core.PartGroup' objects>"
        'getChildren': None, # (!) real value is "<method 'getChildren' of 'panda3d.core.PartGroup' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2C2FE0>)>'
        'getForcedChannel': None, # (!) real value is "<method 'getForcedChannel' of 'panda3d.core.PartGroup' objects>"
        'getNumChildren': None, # (!) real value is "<method 'getNumChildren' of 'panda3d.core.PartGroup' objects>"
        'get_child': None, # (!) real value is "<method 'get_child' of 'panda3d.core.PartGroup' objects>"
        'get_child_named': None, # (!) real value is "<method 'get_child_named' of 'panda3d.core.PartGroup' objects>"
        'get_children': None, # (!) real value is "<method 'get_children' of 'panda3d.core.PartGroup' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2C2FE0>)>'
        'get_forced_channel': None, # (!) real value is "<method 'get_forced_channel' of 'panda3d.core.PartGroup' objects>"
        'get_num_children': None, # (!) real value is "<method 'get_num_children' of 'panda3d.core.PartGroup' objects>"
        'isCharacterJoint': None, # (!) real value is "<method 'isCharacterJoint' of 'panda3d.core.PartGroup' objects>"
        'is_character_joint': None, # (!) real value is "<method 'is_character_joint' of 'panda3d.core.PartGroup' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.core.PartGroup' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.core.PartGroup' objects>"
        'sortDescendants': None, # (!) real value is "<method 'sortDescendants' of 'panda3d.core.PartGroup' objects>"
        'sort_descendants': None, # (!) real value is "<method 'sort_descendants' of 'panda3d.core.PartGroup' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.PartGroup' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.PartGroup' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.PartGroup' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.PartGroup' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.PartGroup' objects>"
        'writeWithValue': None, # (!) real value is "<method 'writeWithValue' of 'panda3d.core.PartGroup' objects>"
        'write_with_value': None, # (!) real value is "<method 'write_with_value' of 'panda3d.core.PartGroup' objects>"
    }
    HMFOkAnimExtra = 2
    HMFOkPartExtra = 1
    HMFOkWrongRootName = 4
    HMF_ok_anim_extra = 2
    HMF_ok_part_extra = 1
    HMF_ok_wrong_root_name = 4


