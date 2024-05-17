# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .VertexTransform import VertexTransform

class JointVertexTransform(VertexTransform):
    """
    /**
     * This is a specialization on VertexTransform that returns the transform
     * necessary to move vertices as if they were assigned to the indicated joint.
     * The geometry itself should be parented to the scene graph at the level of
     * the character's root joint; that is, it should not be parented under a node
     * directly animated by any joints.
     *
     * Multiple combinations of these with different weights are used to implement
     * soft-skinned vertices for an animated character.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getJoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_joint(JointVertexTransform self)
        
        /**
         * Returns the joint for which this object returns the transform.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_joint(self, JointVertexTransform_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_joint(JointVertexTransform self)
        
        /**
         * Returns the joint for which this object returns the transform.
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
        '__doc__': "/**\n * This is a specialization on VertexTransform that returns the transform\n * necessary to move vertices as if they were assigned to the indicated joint.\n * The geometry itself should be parented to the scene graph at the level of\n * the character's root joint; that is, it should not be parented under a node\n * directly animated by any joints.\n *\n * Multiple combinations of these with different weights are used to implement\n * soft-skinned vertices for an animated character.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.JointVertexTransform' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2CB260>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2CB260>)>'
        'getJoint': None, # (!) real value is "<method 'getJoint' of 'panda3d.core.JointVertexTransform' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2CB260>)>'
        'get_joint': None, # (!) real value is "<method 'get_joint' of 'panda3d.core.JointVertexTransform' objects>"
    }


