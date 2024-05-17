# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedObject import TypedObject

class MeshDrawer(TypedObject):
    """
    /**
     * Mesh drawer creates a single geom object that can be shaped with different
     * draw commands.  This is an efficient way to render bunch of billboards,
     * particles, fast changing triangles.  Its implemented by recycling same geom
     * over and over again.  Max budget specifies how many triangles are allowed.
     * Some uses of this class can be : particle system, radar icons, health bars,
     * 2d icons, 2d ui, bullets, missile trails.  Any that can be drawn with
     * triangles can be drawn with this class.  At the low level this uses the
     * GeomVertexRewriter's.  The internal geom consists of vertex, normal, uv and
     * color channels.
     */
    """
    def begin(self, const_MeshDrawer_self, NodePath_camera, NodePath_render): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        begin(const MeshDrawer self, NodePath camera, NodePath render)
        
        /**
         * Pass the current camera node and the root node.  Passing the camera is
         * required to generate bill boards that face it.
         */
        """
        pass

    def billboard(self, const_MeshDrawer_self, const_LVector3f_pos, const_LVector4f_frame, float_size, const_LVector4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        billboard(const MeshDrawer self, const LVector3f pos, const LVector4f frame, float size, const LVector4f color)
        
        /**
         * Draws a billboard - particle with no rotation.  Billboards always face the
         * camera.  Frame contains u,v,u-size,v-size quadruple.
         */
        """
        pass

    def blendedParticle(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        blended_particle(const MeshDrawer self, const LVector3f pos, const LVector4f frame1, const LVector4f frame2, float blend, float size, const LVector4f color, float rotation)
        
        /**
         * Works just like particle but accepts 2 frames and a blend (from 0 to 1)
         * component between them Frame contains u,v,u-size,v-size quadruple.
         */
        """
        pass

    def blended_particle(self, const_MeshDrawer_self, const_LVector3f_pos, const_LVector4f_frame1, const_LVector4f_frame2, float_blend, float_size, const_LVector4f_color, float_rotation): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        blended_particle(const MeshDrawer self, const LVector3f pos, const LVector4f frame1, const LVector4f frame2, float blend, float size, const LVector4f color, float rotation)
        
        /**
         * Works just like particle but accepts 2 frames and a blend (from 0 to 1)
         * component between them Frame contains u,v,u-size,v-size quadruple.
         */
        """
        pass

    def crossSegment(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        cross_segment(const MeshDrawer self, const LVector3f start, const LVector3f stop, const LVector4f frame, float thickness, const LVector4f color)
        
        /**
         * Draws a segment a line with a thickness.  This segment does not use the
         * bill boarding behavior and instead draws 2 planes in a cross.  Stars at
         * start and ends at stop.  Frame contains u,v,u-size,v-size quadruple.
         */
        """
        pass

    def cross_segment(self, const_MeshDrawer_self, const_LVector3f_start, const_LVector3f_stop, const_LVector4f_frame, float_thickness, const_LVector4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        cross_segment(const MeshDrawer self, const LVector3f start, const LVector3f stop, const LVector4f frame, float thickness, const LVector4f color)
        
        /**
         * Draws a segment a line with a thickness.  This segment does not use the
         * bill boarding behavior and instead draws 2 planes in a cross.  Stars at
         * start and ends at stop.  Frame contains u,v,u-size,v-size quadruple.
         */
        """
        pass

    def end(self, const_MeshDrawer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        end(const MeshDrawer self)
        
        /**
         * Finish the drawing and clearing off the remaining vertexes.
         */
        """
        pass

    def explosion(self, const_MeshDrawer_self, const_LVector3f_pos, const_LVector4f_frame, float_size, const_LVector4f_color, int_seed, int_number, float_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        explosion(const MeshDrawer self, const LVector3f pos, const LVector4f frame, float size, const LVector4f color, int seed, int number, float distance)
        
        /**
         * Draws number of particles in a sphere like emitter.  Frame contains
         * u,v,u-size,v-size quadruple.
         */
        """
        pass

    def geometry(self, const_MeshDrawer_self, NodePath_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        geometry(const MeshDrawer self, NodePath node)
        
        /**
         * Draws the geometry that is inside this node path into the MeshDrawer
         * object.  This performs a similar functions as RigidBodyCombiner but for
         * very dynamic situations that share the same texture like physcal chunks of
         * explosions.  It can be a little slow
         */
        """
        pass

    def getBudget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_budget(const MeshDrawer self)
        
        /**
         * Gets the total triangle budget of the drawer
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_root(const MeshDrawer self)
        
        /**
         * Returns the root NodePath.  You should use this node to reparent mesh
         * drawer onto the scene might also want to disable depth draw or enable
         * transparency.
         */
        """
        pass

    def get_budget(self, const_MeshDrawer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_budget(const MeshDrawer self)
        
        /**
         * Gets the total triangle budget of the drawer
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_root(self, const_MeshDrawer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_root(const MeshDrawer self)
        
        /**
         * Returns the root NodePath.  You should use this node to reparent mesh
         * drawer onto the scene might also want to disable depth draw or enable
         * transparency.
         */
        """
        pass

    def linkSegment(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        link_segment(const MeshDrawer self, const LVector3f pos, const LVector4f frame, float thickness, const LVector4f color)
        
        /**
         * Stars or continues linked segment.  Control position, frame, thickness and
         * color with parameters.  Frame contains u,v,u-size,v-size quadruple.
         * Note that for the first two calls to this method, the "frame" parameter is
         * ignored; it first takes effect as of the third call.
         * Similarly, note that in the second call to this method, the "color" parameter
         * is ignored; it only has effect in the first call and calls from the third
         * onwards.
         */
        """
        pass

    def linkSegmentEnd(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        link_segment_end(const MeshDrawer self, const LVector4f frame, const LVector4f color)
        
        /**
         * Finish drawing linked segments, needs at least two calls to link_segment
         * before it can end the linked segment.  Frame contains u,v,u-size,v-size
         * quadruple.
         */
        """
        pass

    def link_segment(self, const_MeshDrawer_self, const_LVector3f_pos, const_LVector4f_frame, float_thickness, const_LVector4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        link_segment(const MeshDrawer self, const LVector3f pos, const LVector4f frame, float thickness, const LVector4f color)
        
        /**
         * Stars or continues linked segment.  Control position, frame, thickness and
         * color with parameters.  Frame contains u,v,u-size,v-size quadruple.
         * Note that for the first two calls to this method, the "frame" parameter is
         * ignored; it first takes effect as of the third call.
         * Similarly, note that in the second call to this method, the "color" parameter
         * is ignored; it only has effect in the first call and calls from the third
         * onwards.
         */
        """
        pass

    def link_segment_end(self, const_MeshDrawer_self, const_LVector4f_frame, const_LVector4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        link_segment_end(const MeshDrawer self, const LVector4f frame, const LVector4f color)
        
        /**
         * Finish drawing linked segments, needs at least two calls to link_segment
         * before it can end the linked segment.  Frame contains u,v,u-size,v-size
         * quadruple.
         */
        """
        pass

    def particle(self, const_MeshDrawer_self, const_LVector3f_pos, const_LVector4f_frame, float_size, const_LVector4f_color, float_rotation): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        particle(const MeshDrawer self, const LVector3f pos, const LVector4f frame, float size, const LVector4f color, float rotation)
        
        /**
         * Draws a particle that is sort of like a bill board but has an extra
         * rotation component.  Frame contains u,v,u-size,v-size quadruple.
         */
        """
        pass

    def segment(self, const_MeshDrawer_self, const_LVector3f_start, const_LVector3f_stop, const_LVector4f_frame, float_thickness, const_LVector4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        segment(const MeshDrawer self, const LVector3f start, const LVector3f stop, const LVector4f frame, float thickness, const LVector4f color)
        
        /**
         * Draws a segment a line with a thickness.  That has billboarding effect.
         * Frame contains u,v,u-size,v-size quadruple.
         */
        """
        pass

    def setBudget(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_budget(const MeshDrawer self, int budget)
        
        /**
         * Sets the total triangle budget of the drawer.  This will not be exceeded.
         * Don't set some thing too large because it will be slow
         */
        """
        pass

    def set_budget(self, const_MeshDrawer_self, int_budget): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_budget(const MeshDrawer self, int budget)
        
        /**
         * Sets the total triangle budget of the drawer.  This will not be exceeded.
         * Don't set some thing too large because it will be slow
         */
        """
        pass

    def stream(self, const_MeshDrawer_self, const_LVector3f_start, const_LVector3f_stop, const_LVector4f_frame, float_size, const_LVector4f_color, int_number, float_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stream(const MeshDrawer self, const LVector3f start, const LVector3f stop, const LVector4f frame, float size, const LVector4f color, int number, float offset)
        
        /**
         * Draws a number of particles in a big line with a shift dictated by the
         * offset.  Frame contains u,v,u-size,v-size quadruple.
         */
        """
        pass

    def tri(self, const_MeshDrawer_self, const_LVector3f_v1, const_LVector4f_c1, const_LVector2f_uv1, const_LVector3f_v2, const_LVector4f_c2, const_LVector2f_uv2, const_LVector3f_v3, const_LVector4f_c3, const_LVector2f_uv3): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        tri(const MeshDrawer self, const LVector3f v1, const LVector4f c1, const LVector2f uv1, const LVector3f v2, const LVector4f c2, const LVector2f uv2, const LVector3f v3, const LVector4f c3, const LVector2f uv3)
        
        /**
         * Draws a triangle with the given parameters.
         */
        """
        pass

    def unevenSegment(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uneven_segment(const MeshDrawer self, const LVector3f start, const LVector3f stop, const LVector4f frame, float thickness_start, const LVector4f color_start, float thickness_stop, const LVector4f color_stop)
        
        /**
         * Draws a segment a line with different thickness and color on both sides.
         * Stars at start and ends at stop.  Frame contains u,v,u-size,v-size
         * quadruple.
         */
        """
        pass

    def uneven_segment(self, const_MeshDrawer_self, const_LVector3f_start, const_LVector3f_stop, const_LVector4f_frame, float_thickness_start, const_LVector4f_color_start, float_thickness_stop, const_LVector4f_color_stop): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uneven_segment(const MeshDrawer self, const LVector3f start, const LVector3f stop, const LVector4f frame, float thickness_start, const LVector4f color_start, float thickness_stop, const LVector4f color_stop)
        
        /**
         * Draws a segment a line with different thickness and color on both sides.
         * Stars at start and ends at stop.  Frame contains u,v,u-size,v-size
         * quadruple.
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
        '__doc__': "/**\n * Mesh drawer creates a single geom object that can be shaped with different\n * draw commands.  This is an efficient way to render bunch of billboards,\n * particles, fast changing triangles.  Its implemented by recycling same geom\n * over and over again.  Max budget specifies how many triangles are allowed.\n * Some uses of this class can be : particle system, radar icons, health bars,\n * 2d icons, 2d ui, bullets, missile trails.  Any that can be drawn with\n * triangles can be drawn with this class.  At the low level this uses the\n * GeomVertexRewriter's.  The internal geom consists of vertex, normal, uv and\n * color channels.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MeshDrawer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BCAD0>'
        'begin': None, # (!) real value is "<method 'begin' of 'panda3d.core.MeshDrawer' objects>"
        'billboard': None, # (!) real value is "<method 'billboard' of 'panda3d.core.MeshDrawer' objects>"
        'blendedParticle': None, # (!) real value is "<method 'blendedParticle' of 'panda3d.core.MeshDrawer' objects>"
        'blended_particle': None, # (!) real value is "<method 'blended_particle' of 'panda3d.core.MeshDrawer' objects>"
        'crossSegment': None, # (!) real value is "<method 'crossSegment' of 'panda3d.core.MeshDrawer' objects>"
        'cross_segment': None, # (!) real value is "<method 'cross_segment' of 'panda3d.core.MeshDrawer' objects>"
        'end': None, # (!) real value is "<method 'end' of 'panda3d.core.MeshDrawer' objects>"
        'explosion': None, # (!) real value is "<method 'explosion' of 'panda3d.core.MeshDrawer' objects>"
        'geometry': None, # (!) real value is "<method 'geometry' of 'panda3d.core.MeshDrawer' objects>"
        'getBudget': None, # (!) real value is "<method 'getBudget' of 'panda3d.core.MeshDrawer' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2BCAD0>)>'
        'getRoot': None, # (!) real value is "<method 'getRoot' of 'panda3d.core.MeshDrawer' objects>"
        'get_budget': None, # (!) real value is "<method 'get_budget' of 'panda3d.core.MeshDrawer' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2BCAD0>)>'
        'get_root': None, # (!) real value is "<method 'get_root' of 'panda3d.core.MeshDrawer' objects>"
        'linkSegment': None, # (!) real value is "<method 'linkSegment' of 'panda3d.core.MeshDrawer' objects>"
        'linkSegmentEnd': None, # (!) real value is "<method 'linkSegmentEnd' of 'panda3d.core.MeshDrawer' objects>"
        'link_segment': None, # (!) real value is "<method 'link_segment' of 'panda3d.core.MeshDrawer' objects>"
        'link_segment_end': None, # (!) real value is "<method 'link_segment_end' of 'panda3d.core.MeshDrawer' objects>"
        'particle': None, # (!) real value is "<method 'particle' of 'panda3d.core.MeshDrawer' objects>"
        'segment': None, # (!) real value is "<method 'segment' of 'panda3d.core.MeshDrawer' objects>"
        'setBudget': None, # (!) real value is "<method 'setBudget' of 'panda3d.core.MeshDrawer' objects>"
        'set_budget': None, # (!) real value is "<method 'set_budget' of 'panda3d.core.MeshDrawer' objects>"
        'stream': None, # (!) real value is "<method 'stream' of 'panda3d.core.MeshDrawer' objects>"
        'tri': None, # (!) real value is "<method 'tri' of 'panda3d.core.MeshDrawer' objects>"
        'unevenSegment': None, # (!) real value is "<method 'unevenSegment' of 'panda3d.core.MeshDrawer' objects>"
        'uneven_segment': None, # (!) real value is "<method 'uneven_segment' of 'panda3d.core.MeshDrawer' objects>"
    }


