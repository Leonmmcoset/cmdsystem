# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderEffect import RenderEffect

class CharacterJointEffect(RenderEffect):
    """
    /**
     * This effect will be added automatically to a node by
     * CharacterJoint::add_net_transform() and
     * CharacterJoint::add_local_transform().
     *
     * The effect binds the node back to the character, so that querying the
     * relative transform of the affected node will automatically force the
     * indicated character to be updated first.
     */
    """
    def getCharacter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_character(CharacterJointEffect self)
        
        /**
         * Returns the Character that will get update() called on it when this node's
         * relative transform is queried, or NULL if there is no such character.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_character(self, CharacterJointEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_character(CharacterJointEffect self)
        
        /**
         * Returns the Character that will get update() called on it when this node's
         * relative transform is queried, or NULL if there is no such character.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def make(self, Character_character): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(Character character)
        
        /**
         * Constructs a new CharacterJointEffect object that references the indicated
         * character.  When a relative get_transform() is called on the node that
         * contains the CharacterJointEffect, it will implicitly call
         * character->update() first.
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
        '__doc__': '/**\n * This effect will be added automatically to a node by\n * CharacterJoint::add_net_transform() and\n * CharacterJoint::add_local_transform().\n *\n * The effect binds the node back to the character, so that querying the\n * relative transform of the affected node will automatically force the\n * indicated character to be updated first.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CharacterJointEffect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CB7D0>'
        'getCharacter': None, # (!) real value is "<method 'getCharacter' of 'panda3d.core.CharacterJointEffect' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CB7D0>)>'
        'get_character': None, # (!) real value is "<method 'get_character' of 'panda3d.core.CharacterJointEffect' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CB7D0>)>'
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2CB7D0>)>'
    }


