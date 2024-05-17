# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderEffect import RenderEffect

class PolylightEffect(RenderEffect):
    """
    /**
     * A PolylightEffect can be used on a node to define a LightGroup  for that
     * node.  A LightGroup contains PolylightNodes which are essentially nodes
     * that add color to the polygons of a model based on distance.  PolylightNode
     * is a cheap way to get lighting effects specially for night scenes
     */
    """
    def addLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_light(PolylightEffect self, const NodePath newlight)
        
        /**
         * Add a PolylightNode object to this effect and return a new effect
         */
        """
        pass

    def add_light(self, PolylightEffect_self, const_NodePath_newlight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_light(PolylightEffect self, const NodePath newlight)
        
        /**
         * Add a PolylightNode object to this effect and return a new effect
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getContrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contrib(PolylightEffect self)
        
        /**
         * Returns CT_all or CT_proximal
         */
        """
        pass

    def getEffectCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_effect_center(PolylightEffect self)
        
        /**
         * Return the value of the _effect_center
         */
        """
        pass

    def getWeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_weight(PolylightEffect self)
        
        /**
         * Get the weight value
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_contrib(self, PolylightEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contrib(PolylightEffect self)
        
        /**
         * Returns CT_all or CT_proximal
         */
        """
        pass

    def get_effect_center(self, PolylightEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_effect_center(PolylightEffect self)
        
        /**
         * Return the value of the _effect_center
         */
        """
        pass

    def get_weight(self, PolylightEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_weight(PolylightEffect self)
        
        /**
         * Get the weight value
         */
        """
        pass

    def hasLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_light(PolylightEffect self, const NodePath light)
        
        /**
         * Returns true if the indicated light is listed in the PolylightEffect, false
         * otherwise.
         */
        """
        pass

    def has_light(self, PolylightEffect_self, const_NodePath_light): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_light(PolylightEffect self, const NodePath light)
        
        /**
         * Returns true if the indicated light is listed in the PolylightEffect, false
         * otherwise.
         */
        """
        pass

    def make(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make()
        make(float weight, int contrib, const LPoint3f effect_center)
        
        /**
         * Constructs a new PolylightEffect object.
         */
        
        /**
         * Constructs a new PolylightEffect object.
         */
        
        /**
         * Constructs a new PolylightEffect object.
         */
        """
        pass

    def removeLight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_light(PolylightEffect self, const NodePath newlight)
        
        /**
         * Remove a light from this effect.  Return the new updated effect
         */
        """
        pass

    def remove_light(self, PolylightEffect_self, const_NodePath_newlight): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_light(PolylightEffect self, const NodePath newlight)
        
        /**
         * Remove a light from this effect.  Return the new updated effect
         */
        """
        pass

    def setContrib(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_contrib(PolylightEffect self, int c)
        
        /**
         * Set Contrib Type and return a new effect... the reason this couldnt be done
         * through make was because that would return a new effect without the
         * lightgroup which is static and cant be accessed Here, we just pass that to
         * the make
         */
        """
        pass

    def setEffectCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_effect_center(PolylightEffect self, const LPoint3f ec)
        
        /**
         * Set weight and return a new effect... the reason this couldnt be done
         * through make was because that would return a new effect without the
         * lightgroup which is static and cant be accessed Here, we just pass that to
         * the make
         */
        """
        pass

    def setWeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_weight(PolylightEffect self, float w)
        
        /**
         * Set weight and return a new effect... the reason this couldnt be done
         * through make was because that would return a new effect without the
         * lightgroup which is static and cant be accessed Here, we just pass that to
         * the make
         */
        """
        pass

    def set_contrib(self, PolylightEffect_self, int_c): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_contrib(PolylightEffect self, int c)
        
        /**
         * Set Contrib Type and return a new effect... the reason this couldnt be done
         * through make was because that would return a new effect without the
         * lightgroup which is static and cant be accessed Here, we just pass that to
         * the make
         */
        """
        pass

    def set_effect_center(self, PolylightEffect_self, const_LPoint3f_ec): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_effect_center(PolylightEffect self, const LPoint3f ec)
        
        /**
         * Set weight and return a new effect... the reason this couldnt be done
         * through make was because that would return a new effect without the
         * lightgroup which is static and cant be accessed Here, we just pass that to
         * the make
         */
        """
        pass

    def set_weight(self, PolylightEffect_self, float_w): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_weight(PolylightEffect self, float w)
        
        /**
         * Set weight and return a new effect... the reason this couldnt be done
         * through make was because that would return a new effect without the
         * lightgroup which is static and cant be accessed Here, we just pass that to
         * the make
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CTAll = 1
    CTProximal = 0
    CT_all = 1
    CT_proximal = 0
    DtoolClassDict = {
        'CTAll': 1,
        'CTProximal': 0,
        'CT_all': 1,
        'CT_proximal': 0,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A PolylightEffect can be used on a node to define a LightGroup  for that\n * node.  A LightGroup contains PolylightNodes which are essentially nodes\n * that add color to the polygons of a model based on distance.  PolylightNode\n * is a cheap way to get lighting effects specially for night scenes\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PolylightEffect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE299FF0>'
        'addLight': None, # (!) real value is "<method 'addLight' of 'panda3d.core.PolylightEffect' objects>"
        'add_light': None, # (!) real value is "<method 'add_light' of 'panda3d.core.PolylightEffect' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE299FF0>)>'
        'getContrib': None, # (!) real value is "<method 'getContrib' of 'panda3d.core.PolylightEffect' objects>"
        'getEffectCenter': None, # (!) real value is "<method 'getEffectCenter' of 'panda3d.core.PolylightEffect' objects>"
        'getWeight': None, # (!) real value is "<method 'getWeight' of 'panda3d.core.PolylightEffect' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE299FF0>)>'
        'get_contrib': None, # (!) real value is "<method 'get_contrib' of 'panda3d.core.PolylightEffect' objects>"
        'get_effect_center': None, # (!) real value is "<method 'get_effect_center' of 'panda3d.core.PolylightEffect' objects>"
        'get_weight': None, # (!) real value is "<method 'get_weight' of 'panda3d.core.PolylightEffect' objects>"
        'hasLight': None, # (!) real value is "<method 'hasLight' of 'panda3d.core.PolylightEffect' objects>"
        'has_light': None, # (!) real value is "<method 'has_light' of 'panda3d.core.PolylightEffect' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE299FF0>)>'
        'removeLight': None, # (!) real value is "<method 'removeLight' of 'panda3d.core.PolylightEffect' objects>"
        'remove_light': None, # (!) real value is "<method 'remove_light' of 'panda3d.core.PolylightEffect' objects>"
        'setContrib': None, # (!) real value is "<method 'setContrib' of 'panda3d.core.PolylightEffect' objects>"
        'setEffectCenter': None, # (!) real value is "<method 'setEffectCenter' of 'panda3d.core.PolylightEffect' objects>"
        'setWeight': None, # (!) real value is "<method 'setWeight' of 'panda3d.core.PolylightEffect' objects>"
        'set_contrib': None, # (!) real value is "<method 'set_contrib' of 'panda3d.core.PolylightEffect' objects>"
        'set_effect_center': None, # (!) real value is "<method 'set_effect_center' of 'panda3d.core.PolylightEffect' objects>"
        'set_weight': None, # (!) real value is "<method 'set_weight' of 'panda3d.core.PolylightEffect' objects>"
    }


