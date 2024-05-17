# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .MovingPartMatrix import MovingPartMatrix

class CharacterJoint(MovingPartMatrix):
    """
    /**
     * This represents one joint of the character's animation, containing an
     * animating transform matrix.
     */
    """
    def addLocalTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_local_transform(const CharacterJoint self, PandaNode node)
        
        /**
         * Adds the indicated node to the list of nodes that will be updated each
         * frame with the joint's local transform from its parent.  Returns true if
         * the node is successfully added, false if it had already been added.
         *
         * The Character pointer should be the Character object that owns this joint;
         * this will be used to create a CharacterJointEffect for this node.  If it is
         * NULL, no such effect will be created.
         *
         * A CharacterJointEffect for this joint's Character will automatically be
         * added to the specified node.
         */
        """
        pass

    def addNetTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_net_transform(const CharacterJoint self, PandaNode node)
        
        /**
         * Adds the indicated node to the list of nodes that will be updated each
         * frame with the joint's net transform from the root.  Returns true if the
         * node is successfully added, false if it had already been added.
         *
         * A CharacterJointEffect for this joint's Character will automatically be
         * added to the specified node.
         */
        """
        pass

    def add_local_transform(self, const_CharacterJoint_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_local_transform(const CharacterJoint self, PandaNode node)
        
        /**
         * Adds the indicated node to the list of nodes that will be updated each
         * frame with the joint's local transform from its parent.  Returns true if
         * the node is successfully added, false if it had already been added.
         *
         * The Character pointer should be the Character object that owns this joint;
         * this will be used to create a CharacterJointEffect for this node.  If it is
         * NULL, no such effect will be created.
         *
         * A CharacterJointEffect for this joint's Character will automatically be
         * added to the specified node.
         */
        """
        pass

    def add_net_transform(self, const_CharacterJoint_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_net_transform(const CharacterJoint self, PandaNode node)
        
        /**
         * Adds the indicated node to the list of nodes that will be updated each
         * frame with the joint's net transform from the root.  Returns true if the
         * node is successfully added, false if it had already been added.
         *
         * A CharacterJointEffect for this joint's Character will automatically be
         * added to the specified node.
         */
        """
        pass

    def clearLocalTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_local_transforms(const CharacterJoint self)
        
        /**
         * Removes all nodes from the list of nodes that will be updated each frame
         * with the joint's local transform from its parent.
         */
        """
        pass

    def clearNetTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_net_transforms(const CharacterJoint self)
        
        /**
         * Removes all nodes from the list of nodes that will be updated each frame
         * with the joint's net transform from the root.
         */
        """
        pass

    def clear_local_transforms(self, const_CharacterJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_local_transforms(const CharacterJoint self)
        
        /**
         * Removes all nodes from the list of nodes that will be updated each frame
         * with the joint's local transform from its parent.
         */
        """
        pass

    def clear_net_transforms(self, const_CharacterJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_net_transforms(const CharacterJoint self)
        
        /**
         * Removes all nodes from the list of nodes that will be updated each frame
         * with the joint's net transform from the root.
         */
        """
        pass

    def getCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_character(CharacterJoint self)
        
        /**
         * Returns the Character that owns this joint.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getLocalTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_local_transforms(const CharacterJoint self)
        
        /**
         * Returns a list of the local transforms set for this node.  Note that this
         * returns a list of NodePaths, even though the local transforms are actually
         * a list of PandaNodes.
         */
        """
        pass

    def getNetTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_transform(CharacterJoint self, LMatrix4f transform)
        
        /**
         * Copies the joint's current net transform (composed from the root of the
         * character joint hierarchy) into the indicated matrix.
         */
        """
        pass

    def getNetTransforms(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_transforms(const CharacterJoint self)
        
        /**
         * Returns a list of the net transforms set for this node.  Note that this
         * returns a list of NodePaths, even though the net transforms are actually a
         * list of PandaNodes.
         */
        """
        pass

    def getTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform(CharacterJoint self)
        get_transform(CharacterJoint self, LMatrix4f transform)
        
        /**
         * Returns the transform matrix of the joint
         */
        
        /**
         * Copies the joint's current transform into the indicated matrix.
         */
        """
        pass

    def getTransformState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform_state(CharacterJoint self)
        """
        pass

    def get_character(self, CharacterJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_character(CharacterJoint self)
        
        /**
         * Returns the Character that owns this joint.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_local_transforms(self, const_CharacterJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_local_transforms(const CharacterJoint self)
        
        /**
         * Returns a list of the local transforms set for this node.  Note that this
         * returns a list of NodePaths, even though the local transforms are actually
         * a list of PandaNodes.
         */
        """
        pass

    def get_net_transform(self, CharacterJoint_self, LMatrix4f_transform): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_transform(CharacterJoint self, LMatrix4f transform)
        
        /**
         * Copies the joint's current net transform (composed from the root of the
         * character joint hierarchy) into the indicated matrix.
         */
        """
        pass

    def get_net_transforms(self, const_CharacterJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_transforms(const CharacterJoint self)
        
        /**
         * Returns a list of the net transforms set for this node.  Note that this
         * returns a list of NodePaths, even though the net transforms are actually a
         * list of PandaNodes.
         */
        """
        pass

    def get_transform(self, CharacterJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform(CharacterJoint self)
        get_transform(CharacterJoint self, LMatrix4f transform)
        
        /**
         * Returns the transform matrix of the joint
         */
        
        /**
         * Copies the joint's current transform into the indicated matrix.
         */
        """
        pass

    def get_transform_state(self, CharacterJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform_state(CharacterJoint self)
        """
        pass

    def hasLocalTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_local_transform(CharacterJoint self, PandaNode node)
        
        /**
         * Returns true if the node is on the list of nodes that will be updated each
         * frame with the joint's local transform from its parent, false otherwise.
         */
        """
        pass

    def hasNetTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_net_transform(CharacterJoint self, PandaNode node)
        
        /**
         * Returns true if the node is on the list of nodes that will be updated each
         * frame with the joint's net transform from the root, false otherwise.
         */
        """
        pass

    def has_local_transform(self, CharacterJoint_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_local_transform(CharacterJoint self, PandaNode node)
        
        /**
         * Returns true if the node is on the list of nodes that will be updated each
         * frame with the joint's local transform from its parent, false otherwise.
         */
        """
        pass

    def has_net_transform(self, CharacterJoint_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_net_transform(CharacterJoint self, PandaNode node)
        
        /**
         * Returns true if the node is on the list of nodes that will be updated each
         * frame with the joint's net transform from the root, false otherwise.
         */
        """
        pass

    def removeLocalTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_local_transform(const CharacterJoint self, PandaNode node)
        
        /**
         * Removes the indicated node from the list of nodes that will be updated each
         * frame with the joint's local transform from its parent.  Returns true if
         * the node is successfully removed, false if it was not on the list.
         *
         * If the node has a CharacterJointEffect that matches this joint's Character,
         * it will be cleared.
         */
        """
        pass

    def removeNetTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_net_transform(const CharacterJoint self, PandaNode node)
        
        /**
         * Removes the indicated node from the list of nodes that will be updated each
         * frame with the joint's net transform from the root.  Returns true if the
         * node is successfully removed, false if it was not on the list.
         *
         * If the node has a CharacterJointEffect that matches this joint's Character,
         * it will be cleared.
         */
        """
        pass

    def remove_local_transform(self, const_CharacterJoint_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_local_transform(const CharacterJoint self, PandaNode node)
        
        /**
         * Removes the indicated node from the list of nodes that will be updated each
         * frame with the joint's local transform from its parent.  Returns true if
         * the node is successfully removed, false if it was not on the list.
         *
         * If the node has a CharacterJointEffect that matches this joint's Character,
         * it will be cleared.
         */
        """
        pass

    def remove_net_transform(self, const_CharacterJoint_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_net_transform(const CharacterJoint self, PandaNode node)
        
        /**
         * Removes the indicated node from the list of nodes that will be updated each
         * frame with the joint's net transform from the root.  Returns true if the
         * node is successfully removed, false if it was not on the list.
         *
         * If the node has a CharacterJointEffect that matches this joint's Character,
         * it will be cleared.
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
        '__doc__': "/**\n * This represents one joint of the character's animation, containing an\n * animating transform matrix.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CharacterJoint' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CACF0>'
        'addLocalTransform': None, # (!) real value is "<method 'addLocalTransform' of 'panda3d.core.CharacterJoint' objects>"
        'addNetTransform': None, # (!) real value is "<method 'addNetTransform' of 'panda3d.core.CharacterJoint' objects>"
        'add_local_transform': None, # (!) real value is "<method 'add_local_transform' of 'panda3d.core.CharacterJoint' objects>"
        'add_net_transform': None, # (!) real value is "<method 'add_net_transform' of 'panda3d.core.CharacterJoint' objects>"
        'clearLocalTransforms': None, # (!) real value is "<method 'clearLocalTransforms' of 'panda3d.core.CharacterJoint' objects>"
        'clearNetTransforms': None, # (!) real value is "<method 'clearNetTransforms' of 'panda3d.core.CharacterJoint' objects>"
        'clear_local_transforms': None, # (!) real value is "<method 'clear_local_transforms' of 'panda3d.core.CharacterJoint' objects>"
        'clear_net_transforms': None, # (!) real value is "<method 'clear_net_transforms' of 'panda3d.core.CharacterJoint' objects>"
        'getCharacter': None, # (!) real value is "<method 'getCharacter' of 'panda3d.core.CharacterJoint' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CACF0>)>'
        'getLocalTransforms': None, # (!) real value is "<method 'getLocalTransforms' of 'panda3d.core.CharacterJoint' objects>"
        'getNetTransform': None, # (!) real value is "<method 'getNetTransform' of 'panda3d.core.CharacterJoint' objects>"
        'getNetTransforms': None, # (!) real value is "<method 'getNetTransforms' of 'panda3d.core.CharacterJoint' objects>"
        'getTransform': None, # (!) real value is "<method 'getTransform' of 'panda3d.core.CharacterJoint' objects>"
        'getTransformState': None, # (!) real value is "<method 'getTransformState' of 'panda3d.core.CharacterJoint' objects>"
        'get_character': None, # (!) real value is "<method 'get_character' of 'panda3d.core.CharacterJoint' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CACF0>)>'
        'get_local_transforms': None, # (!) real value is "<method 'get_local_transforms' of 'panda3d.core.CharacterJoint' objects>"
        'get_net_transform': None, # (!) real value is "<method 'get_net_transform' of 'panda3d.core.CharacterJoint' objects>"
        'get_net_transforms': None, # (!) real value is "<method 'get_net_transforms' of 'panda3d.core.CharacterJoint' objects>"
        'get_transform': None, # (!) real value is "<method 'get_transform' of 'panda3d.core.CharacterJoint' objects>"
        'get_transform_state': None, # (!) real value is "<method 'get_transform_state' of 'panda3d.core.CharacterJoint' objects>"
        'hasLocalTransform': None, # (!) real value is "<method 'hasLocalTransform' of 'panda3d.core.CharacterJoint' objects>"
        'hasNetTransform': None, # (!) real value is "<method 'hasNetTransform' of 'panda3d.core.CharacterJoint' objects>"
        'has_local_transform': None, # (!) real value is "<method 'has_local_transform' of 'panda3d.core.CharacterJoint' objects>"
        'has_net_transform': None, # (!) real value is "<method 'has_net_transform' of 'panda3d.core.CharacterJoint' objects>"
        'removeLocalTransform': None, # (!) real value is "<method 'removeLocalTransform' of 'panda3d.core.CharacterJoint' objects>"
        'removeNetTransform': None, # (!) real value is "<method 'removeNetTransform' of 'panda3d.core.CharacterJoint' objects>"
        'remove_local_transform': None, # (!) real value is "<method 'remove_local_transform' of 'panda3d.core.CharacterJoint' objects>"
        'remove_net_transform': None, # (!) real value is "<method 'remove_net_transform' of 'panda3d.core.CharacterJoint' objects>"
    }


