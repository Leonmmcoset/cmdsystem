# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .PhysicalNode import PhysicalNode

class ActorNode(PhysicalNode):
    """
    /**
     * Like a physical node, but with a little more.  The actornode assumes
     * responsibility for its own transform, and changes in its own PhysicsObject
     * will be reflected as transforms.  This relation goes both ways; changes in
     * the transform will update the object's position (shoves).
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getContactVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contact_vector(ActorNode self)
        
        /**
         *
         */
        """
        pass

    def getPhysicsObject(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_physics_object(const ActorNode self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_contact_vector(self, ActorNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contact_vector(ActorNode self)
        
        /**
         *
         */
        """
        pass

    def get_physics_object(self, const_ActorNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_physics_object(const ActorNode self)
        """
        pass

    def setContactVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_contact_vector(const ActorNode self, const LVector3f contact_vector)
        
        /**
         *
         */
        """
        pass

    def setTransformLimit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_transform_limit(const ActorNode self, float limit)
        """
        pass

    def set_contact_vector(self, const_ActorNode_self, const_LVector3f_contact_vector): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_contact_vector(const ActorNode self, const LVector3f contact_vector)
        
        /**
         *
         */
        """
        pass

    def set_transform_limit(self, const_ActorNode_self, float_limit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_transform_limit(const ActorNode self, float limit)
        """
        pass

    def updateTransform(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        update_transform(const ActorNode self)
        
        // update the parent scene graph node with PhysicsObject information i.e.
        // copy from PhysicsObject to PandaNode
        
        /**
         * this sets the transform generated by the contained Physical, moving the
         * node and subsequent geometry.  i.e.  copy from PhysicsObject to PandaNode
         */
        """
        pass

    def update_transform(self, const_ActorNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update_transform(const ActorNode self)
        
        // update the parent scene graph node with PhysicsObject information i.e.
        // copy from PhysicsObject to PandaNode
        
        /**
         * this sets the transform generated by the contained Physical, moving the
         * node and subsequent geometry.  i.e.  copy from PhysicsObject to PandaNode
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.ActorNode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.ActorNode' objects>"
        '__doc__': "/**\n * Like a physical node, but with a little more.  The actornode assumes\n * responsibility for its own transform, and changes in its own PhysicsObject\n * will be reflected as transforms.  This relation goes both ways; changes in\n * the transform will update the object's position (shoves).\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.ActorNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEC090>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEC090>)>'
        'getContactVector': None, # (!) real value is "<method 'getContactVector' of 'panda3d.physics.ActorNode' objects>"
        'getPhysicsObject': None, # (!) real value is "<method 'getPhysicsObject' of 'panda3d.physics.ActorNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEC090>)>'
        'get_contact_vector': None, # (!) real value is "<method 'get_contact_vector' of 'panda3d.physics.ActorNode' objects>"
        'get_physics_object': None, # (!) real value is "<method 'get_physics_object' of 'panda3d.physics.ActorNode' objects>"
        'setContactVector': None, # (!) real value is "<method 'setContactVector' of 'panda3d.physics.ActorNode' objects>"
        'setTransformLimit': None, # (!) real value is "<method 'setTransformLimit' of 'panda3d.physics.ActorNode' objects>"
        'set_contact_vector': None, # (!) real value is "<method 'set_contact_vector' of 'panda3d.physics.ActorNode' objects>"
        'set_transform_limit': None, # (!) real value is "<method 'set_transform_limit' of 'panda3d.physics.ActorNode' objects>"
        'updateTransform': None, # (!) real value is "<method 'updateTransform' of 'panda3d.physics.ActorNode' objects>"
        'update_transform': None, # (!) real value is "<method 'update_transform' of 'panda3d.physics.ActorNode' objects>"
    }

