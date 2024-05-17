# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderEffect import RenderEffect

class ScissorEffect(RenderEffect):
    """
    /**
     * This provides a higher-level wrapper around ScissorAttrib.  It allows for
     * the scissor region to be defined via points relative to the current node,
     * and also performs culling based on the scissor region.
     */
    """
    def addPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_point(ScissorEffect self, const LPoint3f point, const NodePath node)
        
        /**
         * Returns a new ScissorEffect with the indicated point added.  It is only
         * valid to call this on a "node" type ScissorEffect.  The full set of points,
         * projected into screen space, defines the bounding volume of the rectangular
         * scissor region.
         *
         * Each point may be relative to a different node, if desired.
         */
        """
        pass

    def add_point(self, ScissorEffect_self, const_LPoint3f_point, const_NodePath_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_point(ScissorEffect self, const LPoint3f point, const NodePath node)
        
        /**
         * Returns a new ScissorEffect with the indicated point added.  It is only
         * valid to call this on a "node" type ScissorEffect.  The full set of points,
         * projected into screen space, defines the bounding volume of the rectangular
         * scissor region.
         *
         * Each point may be relative to a different node, if desired.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getClip(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_clip(ScissorEffect self)
        
        /**
         * Returns true if this ScissorEffect actually enables scissoring, or false if
         * it culls only.
         */
        """
        pass

    def getFrame(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame(ScissorEffect self)
        
        /**
         * If is_screen() returns true, this method may be called to query the screen-
         * based scissor frame.  This is a series of left, right, bottom, top,
         * representing the scissor frame relative to the current DisplayRegion.  See
         * ScissorAttrib.
         */
        """
        pass

    def getNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node(ScissorEffect self, int n)
        
        /**
         * Returns the node to which the nth point is relative, or empty NodePath to
         * indicate the current node.
         */
        """
        pass

    def getNodes(self, *args, **kwargs): # real signature unknown
        pass

    def getNumPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_points(ScissorEffect self)
        
        /**
         * Returns the number of node-based scissor points.  See get_point().
         */
        """
        pass

    def getPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point(ScissorEffect self, int n)
        
        /**
         * If is_screen() returns false, then get_num_points() and get_point() may be
         * called to query the node-based scissor frame.  These return n points (at
         * least two), which are understood to be in the space of this node, and which
         * define any opposite corners of the scissor frame.
         */
        """
        pass

    def getPoints(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_clip(self, ScissorEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_clip(ScissorEffect self)
        
        /**
         * Returns true if this ScissorEffect actually enables scissoring, or false if
         * it culls only.
         */
        """
        pass

    def get_frame(self, ScissorEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame(ScissorEffect self)
        
        /**
         * If is_screen() returns true, this method may be called to query the screen-
         * based scissor frame.  This is a series of left, right, bottom, top,
         * representing the scissor frame relative to the current DisplayRegion.  See
         * ScissorAttrib.
         */
        """
        pass

    def get_node(self, ScissorEffect_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(ScissorEffect self, int n)
        
        /**
         * Returns the node to which the nth point is relative, or empty NodePath to
         * indicate the current node.
         */
        """
        pass

    def get_nodes(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_points(self, ScissorEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_points(ScissorEffect self)
        
        /**
         * Returns the number of node-based scissor points.  See get_point().
         */
        """
        pass

    def get_point(self, ScissorEffect_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point(ScissorEffect self, int n)
        
        /**
         * If is_screen() returns false, then get_num_points() and get_point() may be
         * called to query the node-based scissor frame.  These return n points (at
         * least two), which are understood to be in the space of this node, and which
         * define any opposite corners of the scissor frame.
         */
        """
        pass

    def get_points(self, *args, **kwargs): # real signature unknown
        pass

    def isScreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_screen(ScissorEffect self)
        
        /**
         * Returns true if the ScissorEffect is a screen-based effect, meaning
         * get_frame() has a meaningful value, but get_a() and get_b() do not.
         */
        """
        pass

    def is_screen(self, ScissorEffect_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_screen(ScissorEffect self)
        
        /**
         * Returns true if the ScissorEffect is a screen-based effect, meaning
         * get_frame() has a meaningful value, but get_a() and get_b() do not.
         */
        """
        pass

    def makeNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_node()
        make_node(bool clip)
        make_node(const LPoint3f a, const LPoint3f b)
        make_node(const LPoint3f a, const LPoint3f b, const NodePath node)
        make_node(const LPoint3f a, const LPoint3f b, const LPoint3f c, const LPoint3f d, const NodePath node)
        
        /**
         * Constructs a new node-relative ScissorEffect, with no points.  This empty
         * ScissorEffect does nothing.  You must then call add_point a number of times
         * to add the points you require.
         */
        
        /**
         * Constructs a new node-relative ScissorEffect.  The two points are
         * understood to be relative to the indicated node, or the current node if the
         * NodePath is empty, and determine the diagonally opposite corners of the
         * scissor region.
         */
        
        /**
         * Constructs a new node-relative ScissorEffect.  The four points are
         * understood to be relative to the indicated node, or the current node if the
         * indicated NodePath is empty, and determine four points surrounding the
         * scissor region.
         */
        """
        pass

    def makeScreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_screen(const LVecBase4f frame, bool clip)
        
        /**
         * Constructs a new screen-relative ScissorEffect.  The frame defines a left,
         * right, bottom, top region, relative to the DisplayRegion.  See
         * ScissorAttrib.
         */
        """
        pass

    def make_node(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_node()
        make_node(bool clip)
        make_node(const LPoint3f a, const LPoint3f b)
        make_node(const LPoint3f a, const LPoint3f b, const NodePath node)
        make_node(const LPoint3f a, const LPoint3f b, const LPoint3f c, const LPoint3f d, const NodePath node)
        
        /**
         * Constructs a new node-relative ScissorEffect, with no points.  This empty
         * ScissorEffect does nothing.  You must then call add_point a number of times
         * to add the points you require.
         */
        
        /**
         * Constructs a new node-relative ScissorEffect.  The two points are
         * understood to be relative to the indicated node, or the current node if the
         * NodePath is empty, and determine the diagonally opposite corners of the
         * scissor region.
         */
        
        /**
         * Constructs a new node-relative ScissorEffect.  The four points are
         * understood to be relative to the indicated node, or the current node if the
         * indicated NodePath is empty, and determine four points surrounding the
         * scissor region.
         */
        """
        pass

    def make_screen(self, const_LVecBase4f_frame, bool_clip): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_screen(const LVecBase4f frame, bool clip)
        
        /**
         * Constructs a new screen-relative ScissorEffect.  The frame defines a left,
         * right, bottom, top region, relative to the DisplayRegion.  See
         * ScissorAttrib.
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
        '__doc__': '/**\n * This provides a higher-level wrapper around ScissorAttrib.  It allows for\n * the scissor region to be defined via points relative to the current node,\n * and also performs culling based on the scissor region.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ScissorEffect' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE29A730>'
        'addPoint': None, # (!) real value is "<method 'addPoint' of 'panda3d.core.ScissorEffect' objects>"
        'add_point': None, # (!) real value is "<method 'add_point' of 'panda3d.core.ScissorEffect' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE29A730>)>'
        'getClip': None, # (!) real value is "<method 'getClip' of 'panda3d.core.ScissorEffect' objects>"
        'getFrame': None, # (!) real value is "<method 'getFrame' of 'panda3d.core.ScissorEffect' objects>"
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.core.ScissorEffect' objects>"
        'getNodes': None, # (!) real value is "<method 'getNodes' of 'panda3d.core.ScissorEffect' objects>"
        'getNumPoints': None, # (!) real value is "<method 'getNumPoints' of 'panda3d.core.ScissorEffect' objects>"
        'getPoint': None, # (!) real value is "<method 'getPoint' of 'panda3d.core.ScissorEffect' objects>"
        'getPoints': None, # (!) real value is "<method 'getPoints' of 'panda3d.core.ScissorEffect' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE29A730>)>'
        'get_clip': None, # (!) real value is "<method 'get_clip' of 'panda3d.core.ScissorEffect' objects>"
        'get_frame': None, # (!) real value is "<method 'get_frame' of 'panda3d.core.ScissorEffect' objects>"
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.core.ScissorEffect' objects>"
        'get_nodes': None, # (!) real value is "<method 'get_nodes' of 'panda3d.core.ScissorEffect' objects>"
        'get_num_points': None, # (!) real value is "<method 'get_num_points' of 'panda3d.core.ScissorEffect' objects>"
        'get_point': None, # (!) real value is "<method 'get_point' of 'panda3d.core.ScissorEffect' objects>"
        'get_points': None, # (!) real value is "<method 'get_points' of 'panda3d.core.ScissorEffect' objects>"
        'isScreen': None, # (!) real value is "<method 'isScreen' of 'panda3d.core.ScissorEffect' objects>"
        'is_screen': None, # (!) real value is "<method 'is_screen' of 'panda3d.core.ScissorEffect' objects>"
        'makeNode': None, # (!) real value is '<staticmethod(<built-in method makeNode of type object at 0x00007FFCFE29A730>)>'
        'makeScreen': None, # (!) real value is '<staticmethod(<built-in method makeScreen of type object at 0x00007FFCFE29A730>)>'
        'make_node': None, # (!) real value is '<staticmethod(<built-in method make_node of type object at 0x00007FFCFE29A730>)>'
        'make_screen': None, # (!) real value is '<staticmethod(<built-in method make_screen of type object at 0x00007FFCFE29A730>)>'
    }


