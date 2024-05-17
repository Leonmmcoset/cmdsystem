# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderEffect import RenderEffect

class CompassEffect(RenderEffect):
    """
    /**
     * A CompassEffect causes a node to inherit its rotation (or pos or scale, if
     * specified) from some other reference node in the graph, or more often from
     * the root.
     *
     * In its purest form, a CompassEffect is used to keep the node's rotation
     * fixed relative to the top of the scene graph, despite other transforms that
     * may exist above the node.  Hence the name: the node behaves like a magnetic
     * compass, always pointing in the same direction.
     *
     * As an couple of generalizing extensions, the CompassEffect may also be set
     * up to always orient its node according to some other reference node than
     * the root of the scene graph.  Furthermore, it may optionally adjust any of
     * pos, rotation, or scale, instead of necessarily rotation; and it may adjust
     * individual pos and scale components.  (Rotation may not be adjusted on an
     * individual component basis; that's just asking for trouble.)
     *
     * Be careful when using the pos and scale modes.  In these modes, it's
     * possible for the CompassEffect to move its node far from its normal
     * bounding volume, causing culling to fail.  If this is an issue, you may
     * need to explicitly set a large (or infinite) bounding volume on the effect
     * node.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getProperties(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_properties(CompassEffect self)
        
        /**
         * Returns the bitmask of properties that this CompassEffect object inherits
         * from its reference node (or from the root).
         */
        """
        pass

    def getReference(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_reference(CompassEffect self)
        
        /**
         * Returns the reference node from which the CompassEffect inherits its
         * transform.  If this is empty, it means the root of the scene graph.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_properties(self, CompassEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_properties(CompassEffect self)
        
        /**
         * Returns the bitmask of properties that this CompassEffect object inherits
         * from its reference node (or from the root).
         */
        """
        pass

    def get_reference(self, CompassEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_reference(CompassEffect self)
        
        /**
         * Returns the reference node from which the CompassEffect inherits its
         * transform.  If this is empty, it means the root of the scene graph.
         */
        """
        pass

    def make(self, const_NodePath_reference, int_properties): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(const NodePath reference, int properties)
        
        /**
         * Constructs a new CompassEffect object.  If the reference is an empty
         * NodePath, it means the CompassEffect is relative to the root of the scene
         * graph; otherwise, it's relative to the indicated node.  The properties
         * bitmask specifies the set of properties that the compass node inherits from
         * the reference instead of from its parent.
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
        'PAll': 127,
        'PPos': 7,
        'PRot': 8,
        'PScale': 112,
        'PSx': 16,
        'PSy': 32,
        'PSz': 64,
        'PX': 1,
        'PY': 2,
        'PZ': 4,
        'P_all': 127,
        'P_pos': 7,
        'P_rot': 8,
        'P_scale': 112,
        'P_sx': 16,
        'P_sy': 32,
        'P_sz': 64,
        'P_x': 1,
        'P_y': 2,
        'P_z': 4,
        '__doc__': "/**\n * A CompassEffect causes a node to inherit its rotation (or pos or scale, if\n * specified) from some other reference node in the graph, or more often from\n * the root.\n *\n * In its purest form, a CompassEffect is used to keep the node's rotation\n * fixed relative to the top of the scene graph, despite other transforms that\n * may exist above the node.  Hence the name: the node behaves like a magnetic\n * compass, always pointing in the same direction.\n *\n * As an couple of generalizing extensions, the CompassEffect may also be set\n * up to always orient its node according to some other reference node than\n * the root of the scene graph.  Furthermore, it may optionally adjust any of\n * pos, rotation, or scale, instead of necessarily rotation; and it may adjust\n * individual pos and scale components.  (Rotation may not be adjusted on an\n * individual component basis; that's just asking for trouble.)\n *\n * Be careful when using the pos and scale modes.  In these modes, it's\n * possible for the CompassEffect to move its node far from its normal\n * bounding volume, causing culling to fail.  If this is an issue, you may\n * need to explicitly set a large (or infinite) bounding volume on the effect\n * node.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CompassEffect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE295940>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE295940>)>'
        'getProperties': None, # (!) real value is "<method 'getProperties' of 'panda3d.core.CompassEffect' objects>"
        'getReference': None, # (!) real value is "<method 'getReference' of 'panda3d.core.CompassEffect' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE295940>)>'
        'get_properties': None, # (!) real value is "<method 'get_properties' of 'panda3d.core.CompassEffect' objects>"
        'get_reference': None, # (!) real value is "<method 'get_reference' of 'panda3d.core.CompassEffect' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE295940>)>'
    }
    PAll = 127
    PPos = 7
    PRot = 8
    PScale = 112
    PSx = 16
    PSy = 32
    PSz = 64
    PX = 1
    PY = 2
    PZ = 4
    P_all = 127
    P_pos = 7
    P_rot = 8
    P_scale = 112
    P_sx = 16
    P_sy = 32
    P_sz = 64
    P_x = 1
    P_y = 2
    P_z = 4


