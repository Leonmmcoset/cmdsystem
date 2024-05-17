# encoding: utf-8
# module panda3d.fx
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\fx.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


# Variables with simple values

Dtool_PyNativeInterface = 1

# functions

def Dtool_BorrowThisReference(*args, **kwargs): # real signature unknown
    """
    Used to borrow 'this' pointer (to, from)
    Assumes no ownership.
    """
    pass

# classes

class CylindricalLens(__panda3d_core.Lens):
    """
    /**
     * A cylindrical lens.  This is the kind of lens generally used for extremely
     * wide panoramic shots.  It behaves like a normal perspective lens in the
     * vertical direction, but it is non-linear in the horizontal dimension: a
     * point on the film corresponds to a point in space in linear proportion to
     * its angle to the camera, not to its straight-line distance from the center.
     *
     * This allows up to 360 degree lenses in the horizontal dimension, with
     * relatively little distortion.  The distortion is not very apparent between
     * two relatively nearby points on the film, but it becomes increasingly
     * evident as you compare points widely spaced on the film.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
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
        '__doc__': '/**\n * A cylindrical lens.  This is the kind of lens generally used for extremely\n * wide panoramic shots.  It behaves like a normal perspective lens in the\n * vertical direction, but it is non-linear in the horizontal dimension: a\n * point on the film corresponds to a point in space in linear proportion to\n * its angle to the camera, not to its straight-line distance from the center.\n *\n * This allows up to 360 degree lenses in the horizontal dimension, with\n * relatively little distortion.  The distortion is not very apparent between\n * two relatively nearby points on the film, but it becomes increasingly\n * evident as you compare points widely spaced on the film.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.fx.CylindricalLens' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE565B590>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDE565B590>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDE565B590>)>'
    }


class FisheyeLens(__panda3d_core.Lens):
    """
    /**
     * A fisheye lens.  This nonlinear lens introduces a spherical distortion to
     * the image, which is minimal at small angles from the lens, and increases at
     * larger angles from the lens.  The field of view may extend to 360 degrees.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
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
        '__doc__': '/**\n * A fisheye lens.  This nonlinear lens introduces a spherical distortion to\n * the image, which is minimal at small angles from the lens, and increases at\n * larger angles from the lens.  The field of view may extend to 360 degrees.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.fx.FisheyeLens' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE565B770>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDE565B770>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDE565B770>)>'
    }


class NonlinearImager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class object combines the rendered output of a 3-d from one or more
     * linear (e.g.  perspective) cameras, as seen through a single, possibly
     * nonlinear camera.
     *
     * This can be used to generate real-time imagery of a 3-d scene using a
     * nonlinear camera, for instance a fisheye camera, even though the underlying
     * graphics engine may only support linear cameras.  It can also pre-distort
     * imagery to compensate for off-axis projectors, and/or curved screens of any
     * complexity.
     *
    
     *
     * A NonlinearImager may be visualized as a dark room into which a number of
     * projection screens have been placed, of arbitrary size and shape and at any
     * arbitrary position and orientation to each other.  Onto each of these
     * screens is projected the view as seen by a normal perspective camera that
     * exists in the world (that is, under render).
     *
     * There also exist in the room one or more (possibly nonlinear) cameras,
     * called viewers, that observe these screens.  The image of the projection
     * screens seen by each viewer is finally displayed on the viewer's associated
     * DisplayRegion.  By placing the viewer(s) appropriately relative to the
     * screens, and by choosing suitable lens properties for the viewer(s), you
     * can achieve a wide variety of distortion effects.
     *
    
     *
     * There are several different LensNode (Camera) objects involved at each
     * stage in the process.  To help keep them all straight, different words are
     * used to refer to each different kind of Camera used within this object.
     * The camera(s) under render, that capture the original view of the world to
     * be projected onto the screens, are called source cameras, and are set per
     * screen via set_source_camera().  The LensNode that is associated with each
     * screen to project the image as seen from the screen's source camera is
     * called a projector; these are set via the ProjectionScreen::set_projector()
     * interface.  Finally, the cameras that view the whole configuration of
     * screens are called viewers; each of these is associated with a
     * DisplayRegion, and they are set via set_viewer_camera().
     *
     * Of all these lenses, only the source cameras must use linear (that is,
     * perspective or orthographic) lenses.  The projectors and viewers may be any
     * arbitrary lens, linear or otherwise.
     */
    """
    def addScreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_screen(const NonlinearImager self, ProjectionScreen screen)
        add_screen(const NonlinearImager self, const NodePath screen, str name)
        
        /**
         * This version of this method is deprecated and will soon be removed.  Use
         * the version that takes two parameters instead.
         *
         * @deprecated Use the version that takes two parameters instead.
         */
        
        /**
         * Adds a new ProjectionScreen to the list of screens that will be processed
         * by the NonlinearImager.  Each ProjectionScreen represents a view into the
         * world.  It must be based on a linear camera (or whatever kind of camera is
         * respected by the graphics engine).
         *
         * Each ProjectionScreen object should already have some screen geometry
         * created.
         *
         * As each frame is rendered, an offscreen image will be rendered from the
         * source camera associated with each ProjectionScreen, and the resulting
         * image will be applied to the screen geometry.
         *
         * The return value is the index number of the new screen.
         */
        """
        pass

    def addViewer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_viewer(const NonlinearImager self, DisplayRegion dr)
        
        /**
         * Adds the indicated DisplayRegion as a viewer into the NonlinearImager room.
         * The camera associated with the DisplayRegion at the time add_viewer() is
         * called is used as the initial viewer camera; it may have a nonlinear lens,
         * like a fisheye or cylindrical lens.
         *
         * This sets up a special scene graph for this DisplayRegion alone and sets up
         * the DisplayRegion with a specialty camera.  If future changes to the camera
         * are desired, you should use the set_viewer_camera() interface.
         *
         * All viewers must share the same GraphicsEngine.
         *
         * The return value is the index of the new viewer.
         */
        """
        pass

    def add_screen(self, const_NonlinearImager_self, ProjectionScreen_screen): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_screen(const NonlinearImager self, ProjectionScreen screen)
        add_screen(const NonlinearImager self, const NodePath screen, str name)
        
        /**
         * This version of this method is deprecated and will soon be removed.  Use
         * the version that takes two parameters instead.
         *
         * @deprecated Use the version that takes two parameters instead.
         */
        
        /**
         * Adds a new ProjectionScreen to the list of screens that will be processed
         * by the NonlinearImager.  Each ProjectionScreen represents a view into the
         * world.  It must be based on a linear camera (or whatever kind of camera is
         * respected by the graphics engine).
         *
         * Each ProjectionScreen object should already have some screen geometry
         * created.
         *
         * As each frame is rendered, an offscreen image will be rendered from the
         * source camera associated with each ProjectionScreen, and the resulting
         * image will be applied to the screen geometry.
         *
         * The return value is the index number of the new screen.
         */
        """
        pass

    def add_viewer(self, const_NonlinearImager_self, DisplayRegion_dr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_viewer(const NonlinearImager self, DisplayRegion dr)
        
        /**
         * Adds the indicated DisplayRegion as a viewer into the NonlinearImager room.
         * The camera associated with the DisplayRegion at the time add_viewer() is
         * called is used as the initial viewer camera; it may have a nonlinear lens,
         * like a fisheye or cylindrical lens.
         *
         * This sets up a special scene graph for this DisplayRegion alone and sets up
         * the DisplayRegion with a specialty camera.  If future changes to the camera
         * are desired, you should use the set_viewer_camera() interface.
         *
         * All viewers must share the same GraphicsEngine.
         *
         * The return value is the index of the new viewer.
         */
        """
        pass

    def findScreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_screen(NonlinearImager self, const NodePath screen)
        
        /**
         * Returns the index number of the first appearance of the indicated screen
         * within the imager's list, or -1 if it does not appear.
         */
        """
        pass

    def findViewer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_viewer(NonlinearImager self, DisplayRegion dr)
        
        /**
         * Returns the index number of the indicated DisplayRegion within the list of
         * viewers, or -1 if it is not found.
         */
        """
        pass

    def find_screen(self, NonlinearImager_self, const_NodePath_screen): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_screen(NonlinearImager self, const NodePath screen)
        
        /**
         * Returns the index number of the first appearance of the indicated screen
         * within the imager's list, or -1 if it does not appear.
         */
        """
        pass

    def find_viewer(self, NonlinearImager_self, DisplayRegion_dr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_viewer(NonlinearImager self, DisplayRegion dr)
        
        /**
         * Returns the index number of the indicated DisplayRegion within the list of
         * viewers, or -1 if it is not found.
         */
        """
        pass

    def getBuffer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_buffer(NonlinearImager self, int index)
        
        /**
         * Returns the offscreen buffer that is automatically created for the nth
         * projection screen.  This may return NULL if the screen is inactive or if it
         * has not been rendered yet.
         */
        """
        pass

    def getBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def getDarkRoom(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_dark_room(NonlinearImager self)
        
        /**
         * Returns the NodePath to the root of the dark room scene.  This is the scene
         * in which all of the ProjectionScreens and the viewer cameras reside.  It's
         * a standalone scene with a few projection screens arranged artfully around
         * one or more viewers; it's so named because it's a little virtual theater.
         *
         * Normally this scene is not rendered directly; it only exists as an abstract
         * concept, and to define the relation between the ProjectionScreens and the
         * viewers.  But it may be rendered to help visualize the NonlinearImager's
         * behavior.
         */
        """
        pass

    def getGraphicsEngine(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_graphics_engine(NonlinearImager self)
        
        /**
         * Returns the GraphicsEngine that all of the viewers added to the
         * NonlinearImager have in common.
         */
        """
        pass

    def getNumScreens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_screens(NonlinearImager self)
        
        /**
         * Returns the number of screens that have been added to the imager.
         */
        """
        pass

    def getNumViewers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_viewers(NonlinearImager self)
        
        /**
         * Returns the number of viewers that have been added to the imager.
         */
        """
        pass

    def getScreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_screen(NonlinearImager self, int index)
        
        /**
         * Returns the nth screen that has been added to the imager.
         */
        """
        pass

    def getScreenActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_screen_active(NonlinearImager self, int index)
        
        /**
         * Returns the active flag on the indicated screen.
         */
        """
        pass

    def getScreens(self, *args, **kwargs): # real signature unknown
        pass

    def getViewer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_viewer(NonlinearImager self, int index)
        
        /**
         * Returns the nth viewer's DisplayRegion that has been added to the imager.
         */
        """
        pass

    def getViewerCamera(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_viewer_camera(NonlinearImager self, int index)
        
        /**
         * Returns the NodePath to the LensNode that is to serve as nth viewer for
         * this screen.
         */
        """
        pass

    def getViewers(self, *args, **kwargs): # real signature unknown
        pass

    def getViewerScene(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_viewer_scene(NonlinearImager self, int index)
        
        /**
         * Returns a pointer to the root node of the internal scene graph for the nth
         * viewer, which is used to render all of the screen meshes for this viewer.
         *
         * This is the scene graph in which the screen meshes within the dark room
         * have been flattened into the appropriate transformation according to the
         * viewer's lens properties (and position relative to the screens).  It is
         * this scene graph that is finally rendered to the window.
         */
        """
        pass

    def get_buffer(self, NonlinearImager_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_buffer(NonlinearImager self, int index)
        
        /**
         * Returns the offscreen buffer that is automatically created for the nth
         * projection screen.  This may return NULL if the screen is inactive or if it
         * has not been rendered yet.
         */
        """
        pass

    def get_buffers(self, *args, **kwargs): # real signature unknown
        pass

    def get_dark_room(self, NonlinearImager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_dark_room(NonlinearImager self)
        
        /**
         * Returns the NodePath to the root of the dark room scene.  This is the scene
         * in which all of the ProjectionScreens and the viewer cameras reside.  It's
         * a standalone scene with a few projection screens arranged artfully around
         * one or more viewers; it's so named because it's a little virtual theater.
         *
         * Normally this scene is not rendered directly; it only exists as an abstract
         * concept, and to define the relation between the ProjectionScreens and the
         * viewers.  But it may be rendered to help visualize the NonlinearImager's
         * behavior.
         */
        """
        pass

    def get_graphics_engine(self, NonlinearImager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_graphics_engine(NonlinearImager self)
        
        /**
         * Returns the GraphicsEngine that all of the viewers added to the
         * NonlinearImager have in common.
         */
        """
        pass

    def get_num_screens(self, NonlinearImager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_screens(NonlinearImager self)
        
        /**
         * Returns the number of screens that have been added to the imager.
         */
        """
        pass

    def get_num_viewers(self, NonlinearImager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_viewers(NonlinearImager self)
        
        /**
         * Returns the number of viewers that have been added to the imager.
         */
        """
        pass

    def get_screen(self, NonlinearImager_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_screen(NonlinearImager self, int index)
        
        /**
         * Returns the nth screen that has been added to the imager.
         */
        """
        pass

    def get_screens(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen_active(self, NonlinearImager_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_screen_active(NonlinearImager self, int index)
        
        /**
         * Returns the active flag on the indicated screen.
         */
        """
        pass

    def get_viewer(self, NonlinearImager_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_viewer(NonlinearImager self, int index)
        
        /**
         * Returns the nth viewer's DisplayRegion that has been added to the imager.
         */
        """
        pass

    def get_viewers(self, *args, **kwargs): # real signature unknown
        pass

    def get_viewer_camera(self, NonlinearImager_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_viewer_camera(NonlinearImager self, int index)
        
        /**
         * Returns the NodePath to the LensNode that is to serve as nth viewer for
         * this screen.
         */
        """
        pass

    def get_viewer_scene(self, NonlinearImager_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_viewer_scene(NonlinearImager self, int index)
        
        /**
         * Returns a pointer to the root node of the internal scene graph for the nth
         * viewer, which is used to render all of the screen meshes for this viewer.
         *
         * This is the scene graph in which the screen meshes within the dark room
         * have been flattened into the appropriate transformation according to the
         * viewer's lens properties (and position relative to the screens).  It is
         * this scene graph that is finally rendered to the window.
         */
        """
        pass

    def recompute(self, const_NonlinearImager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute(const NonlinearImager self)
        
        /**
         * Forces a regeneration of all the mesh objects, etc.
         */
        """
        pass

    def removeAllScreens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_all_screens(const NonlinearImager self)
        
        /**
         * Removes all screens from the imager.
         */
        """
        pass

    def removeAllViewers(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_all_viewers(const NonlinearImager self)
        
        /**
         * Removes all viewers from the imager.
         */
        """
        pass

    def removeScreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_screen(const NonlinearImager self, int index)
        
        /**
         * Removes the screen with the indicated index number from the imager.
         */
        """
        pass

    def removeViewer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_viewer(const NonlinearImager self, int index)
        
        /**
         * Removes the viewer with the indicated index number from the imager.
         */
        """
        pass

    def remove_all_screens(self, const_NonlinearImager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_all_screens(const NonlinearImager self)
        
        /**
         * Removes all screens from the imager.
         */
        """
        pass

    def remove_all_viewers(self, const_NonlinearImager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_all_viewers(const NonlinearImager self)
        
        /**
         * Removes all viewers from the imager.
         */
        """
        pass

    def remove_screen(self, const_NonlinearImager_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_screen(const NonlinearImager self, int index)
        
        /**
         * Removes the screen with the indicated index number from the imager.
         */
        """
        pass

    def remove_viewer(self, const_NonlinearImager_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_viewer(const NonlinearImager self, int index)
        
        /**
         * Removes the viewer with the indicated index number from the imager.
         */
        """
        pass

    def setScreenActive(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_screen_active(const NonlinearImager self, int index, bool active)
        
        /**
         * Sets the active flag on the indicated screen.  If the active flag is true,
         * the screen will be used; otherwise, it will not appear.
         */
        """
        pass

    def setSourceCamera(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_source_camera(const NonlinearImager self, int index, const NodePath source_camera)
        
        /**
         * Specifies the camera that will be used to render the image for this
         * particular screen.
         *
         * The parameter must be a NodePath whose node is a Camera.  The camera itself
         * indicates the scene that is to be rendered.
         */
        """
        pass

    def setTextureSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture_size(const NonlinearImager self, int index, int width, int height)
        
        /**
         * Sets the width and height of the texture used to render the scene for the
         * indicated screen.  This must be less than or equal to the window size, and
         * it should be a power of two.
         *
         * In general, the larger the texture, the greater the detail of the rendered
         * scene.
         */
        """
        pass

    def setViewerCamera(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_viewer_camera(const NonlinearImager self, int index, const NodePath viewer_camera)
        
        /**
         * Specifies the LensNode that is to serve as the viewer for this screen.  The
         * relative position of the LensNode to the NonlinearImager, as well as the
         * properties of the lens associated with the LensNode, determines the UV's
         * that will be assigned to the geometry within the NonlinearImager.
         *
         * It is not necessary to call this except to change the camera after a viewer
         * has been added, since the default is to use whatever camera is associated
         * with the DisplayRegion at the time the viewer is added.
         *
         * The NodePath must refer to a LensNode (or a Camera).
         */
        """
        pass

    def set_screen_active(self, const_NonlinearImager_self, int_index, bool_active): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_screen_active(const NonlinearImager self, int index, bool active)
        
        /**
         * Sets the active flag on the indicated screen.  If the active flag is true,
         * the screen will be used; otherwise, it will not appear.
         */
        """
        pass

    def set_source_camera(self, const_NonlinearImager_self, int_index, const_NodePath_source_camera): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_source_camera(const NonlinearImager self, int index, const NodePath source_camera)
        
        /**
         * Specifies the camera that will be used to render the image for this
         * particular screen.
         *
         * The parameter must be a NodePath whose node is a Camera.  The camera itself
         * indicates the scene that is to be rendered.
         */
        """
        pass

    def set_texture_size(self, const_NonlinearImager_self, int_index, int_width, int_height): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture_size(const NonlinearImager self, int index, int width, int height)
        
        /**
         * Sets the width and height of the texture used to render the scene for the
         * indicated screen.  This must be less than or equal to the window size, and
         * it should be a power of two.
         *
         * In general, the larger the texture, the greater the detail of the rendered
         * scene.
         */
        """
        pass

    def set_viewer_camera(self, const_NonlinearImager_self, int_index, const_NodePath_viewer_camera): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_viewer_camera(const NonlinearImager self, int index, const NodePath viewer_camera)
        
        /**
         * Specifies the LensNode that is to serve as the viewer for this screen.  The
         * relative position of the LensNode to the NonlinearImager, as well as the
         * properties of the lens associated with the LensNode, determines the UV's
         * that will be assigned to the geometry within the NonlinearImager.
         *
         * It is not necessary to call this except to change the camera after a viewer
         * has been added, since the default is to use whatever camera is associated
         * with the DisplayRegion at the time the viewer is added.
         *
         * The NodePath must refer to a LensNode (or a Camera).
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.fx.NonlinearImager' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.fx.NonlinearImager' objects>"
        '__doc__': "/**\n * This class object combines the rendered output of a 3-d from one or more\n * linear (e.g.  perspective) cameras, as seen through a single, possibly\n * nonlinear camera.\n *\n * This can be used to generate real-time imagery of a 3-d scene using a\n * nonlinear camera, for instance a fisheye camera, even though the underlying\n * graphics engine may only support linear cameras.  It can also pre-distort\n * imagery to compensate for off-axis projectors, and/or curved screens of any\n * complexity.\n *\n\n *\n * A NonlinearImager may be visualized as a dark room into which a number of\n * projection screens have been placed, of arbitrary size and shape and at any\n * arbitrary position and orientation to each other.  Onto each of these\n * screens is projected the view as seen by a normal perspective camera that\n * exists in the world (that is, under render).\n *\n * There also exist in the room one or more (possibly nonlinear) cameras,\n * called viewers, that observe these screens.  The image of the projection\n * screens seen by each viewer is finally displayed on the viewer's associated\n * DisplayRegion.  By placing the viewer(s) appropriately relative to the\n * screens, and by choosing suitable lens properties for the viewer(s), you\n * can achieve a wide variety of distortion effects.\n *\n\n *\n * There are several different LensNode (Camera) objects involved at each\n * stage in the process.  To help keep them all straight, different words are\n * used to refer to each different kind of Camera used within this object.\n * The camera(s) under render, that capture the original view of the world to\n * be projected onto the screens, are called source cameras, and are set per\n * screen via set_source_camera().  The LensNode that is associated with each\n * screen to project the image as seen from the screen's source camera is\n * called a projector; these are set via the ProjectionScreen::set_projector()\n * interface.  Finally, the cameras that view the whole configuration of\n * screens are called viewers; each of these is associated with a\n * DisplayRegion, and they are set via set_viewer_camera().\n *\n * Of all these lenses, only the source cameras must use linear (that is,\n * perspective or orthographic) lenses.  The projectors and viewers may be any\n * arbitrary lens, linear or otherwise.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.fx.NonlinearImager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE565BB10>'
        'addScreen': None, # (!) real value is "<method 'addScreen' of 'panda3d.fx.NonlinearImager' objects>"
        'addViewer': None, # (!) real value is "<method 'addViewer' of 'panda3d.fx.NonlinearImager' objects>"
        'add_screen': None, # (!) real value is "<method 'add_screen' of 'panda3d.fx.NonlinearImager' objects>"
        'add_viewer': None, # (!) real value is "<method 'add_viewer' of 'panda3d.fx.NonlinearImager' objects>"
        'findScreen': None, # (!) real value is "<method 'findScreen' of 'panda3d.fx.NonlinearImager' objects>"
        'findViewer': None, # (!) real value is "<method 'findViewer' of 'panda3d.fx.NonlinearImager' objects>"
        'find_screen': None, # (!) real value is "<method 'find_screen' of 'panda3d.fx.NonlinearImager' objects>"
        'find_viewer': None, # (!) real value is "<method 'find_viewer' of 'panda3d.fx.NonlinearImager' objects>"
        'getBuffer': None, # (!) real value is "<method 'getBuffer' of 'panda3d.fx.NonlinearImager' objects>"
        'getBuffers': None, # (!) real value is "<method 'getBuffers' of 'panda3d.fx.NonlinearImager' objects>"
        'getDarkRoom': None, # (!) real value is "<method 'getDarkRoom' of 'panda3d.fx.NonlinearImager' objects>"
        'getGraphicsEngine': None, # (!) real value is "<method 'getGraphicsEngine' of 'panda3d.fx.NonlinearImager' objects>"
        'getNumScreens': None, # (!) real value is "<method 'getNumScreens' of 'panda3d.fx.NonlinearImager' objects>"
        'getNumViewers': None, # (!) real value is "<method 'getNumViewers' of 'panda3d.fx.NonlinearImager' objects>"
        'getScreen': None, # (!) real value is "<method 'getScreen' of 'panda3d.fx.NonlinearImager' objects>"
        'getScreenActive': None, # (!) real value is "<method 'getScreenActive' of 'panda3d.fx.NonlinearImager' objects>"
        'getScreens': None, # (!) real value is "<method 'getScreens' of 'panda3d.fx.NonlinearImager' objects>"
        'getViewer': None, # (!) real value is "<method 'getViewer' of 'panda3d.fx.NonlinearImager' objects>"
        'getViewerCamera': None, # (!) real value is "<method 'getViewerCamera' of 'panda3d.fx.NonlinearImager' objects>"
        'getViewerScene': None, # (!) real value is "<method 'getViewerScene' of 'panda3d.fx.NonlinearImager' objects>"
        'getViewers': None, # (!) real value is "<method 'getViewers' of 'panda3d.fx.NonlinearImager' objects>"
        'get_buffer': None, # (!) real value is "<method 'get_buffer' of 'panda3d.fx.NonlinearImager' objects>"
        'get_buffers': None, # (!) real value is "<method 'get_buffers' of 'panda3d.fx.NonlinearImager' objects>"
        'get_dark_room': None, # (!) real value is "<method 'get_dark_room' of 'panda3d.fx.NonlinearImager' objects>"
        'get_graphics_engine': None, # (!) real value is "<method 'get_graphics_engine' of 'panda3d.fx.NonlinearImager' objects>"
        'get_num_screens': None, # (!) real value is "<method 'get_num_screens' of 'panda3d.fx.NonlinearImager' objects>"
        'get_num_viewers': None, # (!) real value is "<method 'get_num_viewers' of 'panda3d.fx.NonlinearImager' objects>"
        'get_screen': None, # (!) real value is "<method 'get_screen' of 'panda3d.fx.NonlinearImager' objects>"
        'get_screen_active': None, # (!) real value is "<method 'get_screen_active' of 'panda3d.fx.NonlinearImager' objects>"
        'get_screens': None, # (!) real value is "<method 'get_screens' of 'panda3d.fx.NonlinearImager' objects>"
        'get_viewer': None, # (!) real value is "<method 'get_viewer' of 'panda3d.fx.NonlinearImager' objects>"
        'get_viewer_camera': None, # (!) real value is "<method 'get_viewer_camera' of 'panda3d.fx.NonlinearImager' objects>"
        'get_viewer_scene': None, # (!) real value is "<method 'get_viewer_scene' of 'panda3d.fx.NonlinearImager' objects>"
        'get_viewers': None, # (!) real value is "<method 'get_viewers' of 'panda3d.fx.NonlinearImager' objects>"
        'recompute': None, # (!) real value is "<method 'recompute' of 'panda3d.fx.NonlinearImager' objects>"
        'removeAllScreens': None, # (!) real value is "<method 'removeAllScreens' of 'panda3d.fx.NonlinearImager' objects>"
        'removeAllViewers': None, # (!) real value is "<method 'removeAllViewers' of 'panda3d.fx.NonlinearImager' objects>"
        'removeScreen': None, # (!) real value is "<method 'removeScreen' of 'panda3d.fx.NonlinearImager' objects>"
        'removeViewer': None, # (!) real value is "<method 'removeViewer' of 'panda3d.fx.NonlinearImager' objects>"
        'remove_all_screens': None, # (!) real value is "<method 'remove_all_screens' of 'panda3d.fx.NonlinearImager' objects>"
        'remove_all_viewers': None, # (!) real value is "<method 'remove_all_viewers' of 'panda3d.fx.NonlinearImager' objects>"
        'remove_screen': None, # (!) real value is "<method 'remove_screen' of 'panda3d.fx.NonlinearImager' objects>"
        'remove_viewer': None, # (!) real value is "<method 'remove_viewer' of 'panda3d.fx.NonlinearImager' objects>"
        'setScreenActive': None, # (!) real value is "<method 'setScreenActive' of 'panda3d.fx.NonlinearImager' objects>"
        'setSourceCamera': None, # (!) real value is "<method 'setSourceCamera' of 'panda3d.fx.NonlinearImager' objects>"
        'setTextureSize': None, # (!) real value is "<method 'setTextureSize' of 'panda3d.fx.NonlinearImager' objects>"
        'setViewerCamera': None, # (!) real value is "<method 'setViewerCamera' of 'panda3d.fx.NonlinearImager' objects>"
        'set_screen_active': None, # (!) real value is "<method 'set_screen_active' of 'panda3d.fx.NonlinearImager' objects>"
        'set_source_camera': None, # (!) real value is "<method 'set_source_camera' of 'panda3d.fx.NonlinearImager' objects>"
        'set_texture_size': None, # (!) real value is "<method 'set_texture_size' of 'panda3d.fx.NonlinearImager' objects>"
        'set_viewer_camera': None, # (!) real value is "<method 'set_viewer_camera' of 'panda3d.fx.NonlinearImager' objects>"
    }


class OSphereLens(__panda3d_core.Lens):
    """
    /**
     * A OSphereLens is a special nonlinear lens that doesn't correspond to any
     * real physical lenses.  It's primarily useful for generating 360-degree
     * wraparound images while avoiding the distortion associated with fisheye
     * images.
     *
     * A OSphereLens is similar to a Cylindrical lens and PSphereLens, except that
     * it is orthographic in the vertical direction.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
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
        '__doc__': "/**\n * A OSphereLens is a special nonlinear lens that doesn't correspond to any\n * real physical lenses.  It's primarily useful for generating 360-degree\n * wraparound images while avoiding the distortion associated with fisheye\n * images.\n *\n * A OSphereLens is similar to a Cylindrical lens and PSphereLens, except that\n * it is orthographic in the vertical direction.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.fx.OSphereLens' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE565BCE0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDE565BCE0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDE565BCE0>)>'
    }


class ProjectionScreen(__panda3d_core.PandaNode):
    """
    /**
     * A ProjectionScreen implements a simple system for projective texturing.
     * The ProjectionScreen node is the parent of a hierarchy of geometry that is
     * considered a "screen"; the ProjectionScreen will automatically recompute
     * all the UV's (for a particular texture stage) on its subordinate geometry
     * according to the relative position and lens parameters of the indicated
     * LensNode.
     *
     * All this does is recompute UV's; the caller is responsible for applying the
     * appropriate texture(s) to the geometry.
     *
     * This does not take advantage of any hardware-assisted projective texturing;
     * all of the UV's are computed in the CPU.  (Use NodePath::project_texture()
     * to enable hardware-assisted projective texturing.)  However, the
     * ProjectionScreen interface does support any kind of lens, linear or
     * nonlinear, that might be defined using the Lens interface, including
     * fisheye and cylindrical lenses.
     */
    """
    def clearUndistLut(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_undist_lut(const ProjectionScreen self)
        
        /**
         * Removes the distortion lookup table from the projector, if specified.
         */
        """
        pass

    def clear_undist_lut(self, const_ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_undist_lut(const ProjectionScreen self)
        
        /**
         * Removes the distortion lookup table from the projector, if specified.
         */
        """
        pass

    def generateScreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_screen(const ProjectionScreen self, const NodePath projector, str screen_name, int num_x_verts, int num_y_verts, float distance, float fill_ratio)
        
        /**
         * Synthesizes a polygon mesh based on the projection area of the indicated
         * projector.  This generates and returns a new GeomNode but does not
         * automatically parent it to the ProjectionScreen node; see
         * regenerate_screen().
         *
         * The specified projector need not be the same as the projector given to the
         * ProjectionScreen with set_projector() (although this is often what you
         * want).
         *
         * num_x_verts and num_y_verts specify the number of vertices to make in the
         * grid across the horizontal and vertical dimension of the projector,
         * respectively; distance represents the approximate distance of the screen
         * from the lens center.
         *
         * The fill_ratio parameter specifies the fraction of the image to cover.  If
         * it is 1.0, the entire image is shown full-size; if it is 0.9, 10% of the
         * image around the edges is not part of the grid (and the grid is drawn
         * smaller by the same 10%).  This is intended to work around graphics drivers
         * that tend to show dark edges or other unsatisfactory artifacts around the
         * edges of textures: render the texture larger than necessary by a certain
         * fraction, and make the screen smaller by the inverse fraction.
         */
        """
        pass

    def generate_screen(self, const_ProjectionScreen_self, const_NodePath_projector, str_screen_name, int_num_x_verts, int_num_y_verts, float_distance, float_fill_ratio): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_screen(const ProjectionScreen self, const NodePath projector, str screen_name, int num_x_verts, int num_y_verts, float distance, float fill_ratio)
        
        /**
         * Synthesizes a polygon mesh based on the projection area of the indicated
         * projector.  This generates and returns a new GeomNode but does not
         * automatically parent it to the ProjectionScreen node; see
         * regenerate_screen().
         *
         * The specified projector need not be the same as the projector given to the
         * ProjectionScreen with set_projector() (although this is often what you
         * want).
         *
         * num_x_verts and num_y_verts specify the number of vertices to make in the
         * grid across the horizontal and vertical dimension of the projector,
         * respectively; distance represents the approximate distance of the screen
         * from the lens center.
         *
         * The fill_ratio parameter specifies the fraction of the image to cover.  If
         * it is 1.0, the entire image is shown full-size; if it is 0.9, 10% of the
         * image around the edges is not part of the grid (and the grid is drawn
         * smaller by the same 10%).  This is intended to work around graphics drivers
         * that tend to show dark edges or other unsatisfactory artifacts around the
         * edges of textures: render the texture larger than necessary by a certain
         * fraction, and make the screen smaller by the inverse fraction.
         */
        """
        pass

    def getAutoRecompute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_recompute(ProjectionScreen self)
        
        /**
         * Returns the auto_recompute flag.  When this is true, the ProjectionScreen
         * will always be recomputed if necessary before the frame is drawn; when it
         * is false, an explicit call to recompute_if_stale() may be required.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFrameColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_frame_color(ProjectionScreen self)
        
        /**
         * Returns the color the screen will be painted at the portions outside of the
         * lens' frustum.  See set_frame_color().
         */
        """
        pass

    def getInvertUvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_invert_uvs(ProjectionScreen self)
        
        /**
         * Returns whether this screen is compensating for a graphics driver inverting
         * the framebuffer image.  See set_invert_uvs().
         */
        """
        pass

    def getLastScreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_last_screen(ProjectionScreen self)
        
        /**
         * Returns an UpdateSeq corresponding to the last time a screen mesh was
         * generated for the ProjectionScreen.  Each time generate_screen() is called,
         * this number is incremented; this allows other objects (like
         * NonlinearImager) to know when they need to recompute themselves.
         */
        """
        pass

    def getProjector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_projector(ProjectionScreen self)
        
        /**
         * Returns the NodePath to the LensNode that is to serve as the projector for
         * this screen, or empty if no projector is associated.
         */
        """
        pass

    def getTexcoord3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texcoord_3d(ProjectionScreen self)
        
        /**
         * See set_texcoord_3d().
         */
        """
        pass

    def getTexcoordName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texcoord_name(ProjectionScreen self)
        
        /**
         * Returns the name of the texture coordinates that will be generated by this
         * particular ProjectionScreen, as set by set_texcoord_name().
         */
        """
        pass

    def getUndistLut(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_undist_lut(ProjectionScreen self)
        
        /**
         * Returns the distortion lookup table provided via set_undist_lut(), if any.
         */
        """
        pass

    def getVignetteColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vignette_color(ProjectionScreen self)
        
        /**
         * Returns the color the screen will be painted at the portions outside of the
         * lens' frustum.  See set_vignette_color().
         */
        """
        pass

    def getVignetteOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vignette_on(ProjectionScreen self)
        
        /**
         * Returns true if vertex-based vignetting is on, false otherwise.  See
         * set_vignette_on().
         */
        """
        pass

    def get_auto_recompute(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_recompute(ProjectionScreen self)
        
        /**
         * Returns the auto_recompute flag.  When this is true, the ProjectionScreen
         * will always be recomputed if necessary before the frame is drawn; when it
         * is false, an explicit call to recompute_if_stale() may be required.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_frame_color(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_frame_color(ProjectionScreen self)
        
        /**
         * Returns the color the screen will be painted at the portions outside of the
         * lens' frustum.  See set_frame_color().
         */
        """
        pass

    def get_invert_uvs(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_invert_uvs(ProjectionScreen self)
        
        /**
         * Returns whether this screen is compensating for a graphics driver inverting
         * the framebuffer image.  See set_invert_uvs().
         */
        """
        pass

    def get_last_screen(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_last_screen(ProjectionScreen self)
        
        /**
         * Returns an UpdateSeq corresponding to the last time a screen mesh was
         * generated for the ProjectionScreen.  Each time generate_screen() is called,
         * this number is incremented; this allows other objects (like
         * NonlinearImager) to know when they need to recompute themselves.
         */
        """
        pass

    def get_projector(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_projector(ProjectionScreen self)
        
        /**
         * Returns the NodePath to the LensNode that is to serve as the projector for
         * this screen, or empty if no projector is associated.
         */
        """
        pass

    def get_texcoord_3d(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texcoord_3d(ProjectionScreen self)
        
        /**
         * See set_texcoord_3d().
         */
        """
        pass

    def get_texcoord_name(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texcoord_name(ProjectionScreen self)
        
        /**
         * Returns the name of the texture coordinates that will be generated by this
         * particular ProjectionScreen, as set by set_texcoord_name().
         */
        """
        pass

    def get_undist_lut(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_undist_lut(ProjectionScreen self)
        
        /**
         * Returns the distortion lookup table provided via set_undist_lut(), if any.
         */
        """
        pass

    def get_vignette_color(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vignette_color(ProjectionScreen self)
        
        /**
         * Returns the color the screen will be painted at the portions outside of the
         * lens' frustum.  See set_vignette_color().
         */
        """
        pass

    def get_vignette_on(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vignette_on(ProjectionScreen self)
        
        /**
         * Returns true if vertex-based vignetting is on, false otherwise.  See
         * set_vignette_on().
         */
        """
        pass

    def hasUndistLut(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_undist_lut(ProjectionScreen self)
        
        /**
         * Returns true if a valid distortion lookup table was provided via
         * set_undist_lut(), false otherwise.
         */
        """
        pass

    def has_undist_lut(self, ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_undist_lut(ProjectionScreen self)
        
        /**
         * Returns true if a valid distortion lookup table was provided via
         * set_undist_lut(), false otherwise.
         */
        """
        pass

    def makeFlatMesh(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_flat_mesh(const ProjectionScreen self, const NodePath this_np, const NodePath camera)
        
        /**
         * Generates a deep copy of the hierarchy at the ProjectionScreen node and
         * below, with vertices flattened into two dimensions as if they were seen by
         * the indicated camera node.
         *
         * This is useful for rendering an image as seen through a non-linear lens.
         * The resulting mesh will have vertices in the range [-1, 1] in both x and y,
         * and may be then rendered with an ordinary orthographic lens, to generate
         * the effect of seeing the image through the specified non-linear lens.
         *
         * The returned node has no parent; it is up to the caller to parent it
         * somewhere or store it so that it does not get dereferenced and deleted.
         */
        """
        pass

    def make_flat_mesh(self, const_ProjectionScreen_self, const_NodePath_this_np, const_NodePath_camera): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_flat_mesh(const ProjectionScreen self, const NodePath this_np, const NodePath camera)
        
        /**
         * Generates a deep copy of the hierarchy at the ProjectionScreen node and
         * below, with vertices flattened into two dimensions as if they were seen by
         * the indicated camera node.
         *
         * This is useful for rendering an image as seen through a non-linear lens.
         * The resulting mesh will have vertices in the range [-1, 1] in both x and y,
         * and may be then rendered with an ordinary orthographic lens, to generate
         * the effect of seeing the image through the specified non-linear lens.
         *
         * The returned node has no parent; it is up to the caller to parent it
         * somewhere or store it so that it does not get dereferenced and deleted.
         */
        """
        pass

    def recompute(self, const_ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute(const ProjectionScreen self)
        
        /**
         * Recomputes all the UV's for geometry below the ProjectionScreen node, as if
         * the texture were projected from the associated projector.
         *
         * This function is normally called automatically whenever the relevant
         * properties change, so it should not normally need to be called directly by
         * the user.  However, it does no harm to call this if there is any doubt.
         */
        """
        pass

    def recomputeIfStale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        recompute_if_stale(const ProjectionScreen self)
        recompute_if_stale(const ProjectionScreen self, const NodePath this_np)
        
        /**
         * Calls recompute() only if the relative transform between the
         * ProjectionScreen and the projector has changed, or if any other relevant
         * property has changed.  Returns true if recomputed, false otherwise.
         */
        
        /**
         * Calls recompute() only if the relative transform between the
         * ProjectionScreen and the projector has changed, or if any other relevant
         * property has changed.  Returns true if recomputed, false otherwise.
         */
        """
        pass

    def recompute_if_stale(self, const_ProjectionScreen_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute_if_stale(const ProjectionScreen self)
        recompute_if_stale(const ProjectionScreen self, const NodePath this_np)
        
        /**
         * Calls recompute() only if the relative transform between the
         * ProjectionScreen and the projector has changed, or if any other relevant
         * property has changed.  Returns true if recomputed, false otherwise.
         */
        
        /**
         * Calls recompute() only if the relative transform between the
         * ProjectionScreen and the projector has changed, or if any other relevant
         * property has changed.  Returns true if recomputed, false otherwise.
         */
        """
        pass

    def regenerateScreen(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        regenerate_screen(const ProjectionScreen self, const NodePath projector, str screen_name, int num_x_verts, int num_y_verts, float distance, float fill_ratio)
        
        /**
         * Removes all the children from the ProjectionScreen node, and adds the newly
         * generated child returned by generate_screen().
         */
        """
        pass

    def regenerate_screen(self, const_ProjectionScreen_self, const_NodePath_projector, str_screen_name, int_num_x_verts, int_num_y_verts, float_distance, float_fill_ratio): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        regenerate_screen(const ProjectionScreen self, const NodePath projector, str screen_name, int num_x_verts, int num_y_verts, float distance, float fill_ratio)
        
        /**
         * Removes all the children from the ProjectionScreen node, and adds the newly
         * generated child returned by generate_screen().
         */
        """
        pass

    def setAutoRecompute(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_recompute(const ProjectionScreen self, bool auto_recompute)
        
        /**
         * Sets the auto_recompute flag.  When this is true, the ProjectionScreen will
         * always be recomputed if necessary before the frame is drawn; when it is
         * false, an explicit call to recompute_if_stale() may be required.
         */
        """
        pass

    def setFrameColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frame_color(const ProjectionScreen self, const LVecBase4f frame_color)
        
        /**
         * Specifies the color the screen will be painted at the portions outside of
         * the lens' frustum; i.e.  where the lens can't see it or illuminate it.
         * This color is only used if the vignette_on flag is true; see
         * set_vignette_on().
         */
        """
        pass

    def setInvertUvs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_invert_uvs(const ProjectionScreen self, bool invert_uvs)
        
        /**
         * Some OpenGL graphics drivers are known to invert the framebuffer image when
         * they copy it to texture.  (This is arguably a problem with the OpenGL spec,
         * which seems to be unclear about the proper ordering of pixels in this
         * operation.)
         *
         * In any case, set this true to compensate for this effect by inverting the
         * UV's of the projection screen.  The default is taken from the Configrc
         * variable project-invert-uvs.
         */
        """
        pass

    def setProjector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_projector(const ProjectionScreen self, const NodePath projector)
        
        /**
         * Specifies the LensNode that is to serve as the projector for this screen.
         * The relative position of the LensNode to the ProjectionScreen, as well as
         * the properties of the lens associated with the LensNode, determines the
         * UV's that will be assigned to the geometry within the ProjectionScreen.
         *
         * The NodePath must refer to a LensNode (or a Camera).
         */
        """
        pass

    def setTexcoord3d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texcoord_3d(const ProjectionScreen self, bool texcoord_3d)
        
        /**
         * Set this true to force 3-D texture coordinates to be created for the
         * geometry.  When this is true and the geometry has only 2-D texture
         * coordinates, those texture coordinates are dumped in favor of 3-D
         * coordinates.  When this is false, whatever texture coordinates already
         * exist are preserved as-is.
         */
        """
        pass

    def setTexcoordName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texcoord_name(const ProjectionScreen self, str texcoord_name)
        
        /**
         * Specifies the name of the texture coordinates that are generated by this
         * particular ProjectionScreen.  This can be used in the presence of
         * multitexturing to compute the UV's for just a subset of all of the active
         * stages of the multitexture pipeline.
         */
        """
        pass

    def setUndistLut(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_undist_lut(const ProjectionScreen self, const PfmFile undist_lut)
        
        /**
         * Applies a distortion lookup table to the projector.  This mapping warps the
         * lens effect by passing each ray through an indirection table: the point
         * (u,v) in the indicated lookup table stores the actual (u,v) that the lens
         * produces.
         *
         * This does not affect the operation of generate_screen().
         */
        """
        pass

    def setVignetteColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vignette_color(const ProjectionScreen self, const LVecBase4f vignette_color)
        
        /**
         * Specifies the color the screen will be painted at the portions outside of
         * the lens' frustum; i.e.  where the lens can't see it or illuminate it.
         * This color is only used if the vignette_on flag is true; see
         * set_vignette_on().
         */
        """
        pass

    def setVignetteOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vignette_on(const ProjectionScreen self, bool vignette_on)
        
        /**
         * Specifies whether vertex-based vignetting should be on.  When this is
         * enabled, vertex color will be set on the screen vertices to color the
         * screen two distinct colors, usually white and black, for the parts of the
         * screen in front of and outside the lens' frustum, respectively.  When this
         * is not enabled, the screen color will be left alone.
         *
         * This effect generally looks terrible, but it does at least make the
         * boundaries of the lens clear.
         */
        """
        pass

    def set_auto_recompute(self, const_ProjectionScreen_self, bool_auto_recompute): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_recompute(const ProjectionScreen self, bool auto_recompute)
        
        /**
         * Sets the auto_recompute flag.  When this is true, the ProjectionScreen will
         * always be recomputed if necessary before the frame is drawn; when it is
         * false, an explicit call to recompute_if_stale() may be required.
         */
        """
        pass

    def set_frame_color(self, const_ProjectionScreen_self, const_LVecBase4f_frame_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frame_color(const ProjectionScreen self, const LVecBase4f frame_color)
        
        /**
         * Specifies the color the screen will be painted at the portions outside of
         * the lens' frustum; i.e.  where the lens can't see it or illuminate it.
         * This color is only used if the vignette_on flag is true; see
         * set_vignette_on().
         */
        """
        pass

    def set_invert_uvs(self, const_ProjectionScreen_self, bool_invert_uvs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_invert_uvs(const ProjectionScreen self, bool invert_uvs)
        
        /**
         * Some OpenGL graphics drivers are known to invert the framebuffer image when
         * they copy it to texture.  (This is arguably a problem with the OpenGL spec,
         * which seems to be unclear about the proper ordering of pixels in this
         * operation.)
         *
         * In any case, set this true to compensate for this effect by inverting the
         * UV's of the projection screen.  The default is taken from the Configrc
         * variable project-invert-uvs.
         */
        """
        pass

    def set_projector(self, const_ProjectionScreen_self, const_NodePath_projector): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_projector(const ProjectionScreen self, const NodePath projector)
        
        /**
         * Specifies the LensNode that is to serve as the projector for this screen.
         * The relative position of the LensNode to the ProjectionScreen, as well as
         * the properties of the lens associated with the LensNode, determines the
         * UV's that will be assigned to the geometry within the ProjectionScreen.
         *
         * The NodePath must refer to a LensNode (or a Camera).
         */
        """
        pass

    def set_texcoord_3d(self, const_ProjectionScreen_self, bool_texcoord_3d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texcoord_3d(const ProjectionScreen self, bool texcoord_3d)
        
        /**
         * Set this true to force 3-D texture coordinates to be created for the
         * geometry.  When this is true and the geometry has only 2-D texture
         * coordinates, those texture coordinates are dumped in favor of 3-D
         * coordinates.  When this is false, whatever texture coordinates already
         * exist are preserved as-is.
         */
        """
        pass

    def set_texcoord_name(self, const_ProjectionScreen_self, str_texcoord_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texcoord_name(const ProjectionScreen self, str texcoord_name)
        
        /**
         * Specifies the name of the texture coordinates that are generated by this
         * particular ProjectionScreen.  This can be used in the presence of
         * multitexturing to compute the UV's for just a subset of all of the active
         * stages of the multitexture pipeline.
         */
        """
        pass

    def set_undist_lut(self, const_ProjectionScreen_self, const_PfmFile_undist_lut): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_undist_lut(const ProjectionScreen self, const PfmFile undist_lut)
        
        /**
         * Applies a distortion lookup table to the projector.  This mapping warps the
         * lens effect by passing each ray through an indirection table: the point
         * (u,v) in the indicated lookup table stores the actual (u,v) that the lens
         * produces.
         *
         * This does not affect the operation of generate_screen().
         */
        """
        pass

    def set_vignette_color(self, const_ProjectionScreen_self, const_LVecBase4f_vignette_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vignette_color(const ProjectionScreen self, const LVecBase4f vignette_color)
        
        /**
         * Specifies the color the screen will be painted at the portions outside of
         * the lens' frustum; i.e.  where the lens can't see it or illuminate it.
         * This color is only used if the vignette_on flag is true; see
         * set_vignette_on().
         */
        """
        pass

    def set_vignette_on(self, const_ProjectionScreen_self, bool_vignette_on): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vignette_on(const ProjectionScreen self, bool vignette_on)
        
        /**
         * Specifies whether vertex-based vignetting should be on.  When this is
         * enabled, vertex color will be set on the screen vertices to color the
         * screen two distinct colors, usually white and black, for the parts of the
         * screen in front of and outside the lens' frustum, respectively.  When this
         * is not enabled, the screen color will be left alone.
         *
         * This effect generally looks terrible, but it does at least make the
         * boundaries of the lens clear.
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
        '__doc__': '/**\n * A ProjectionScreen implements a simple system for projective texturing.\n * The ProjectionScreen node is the parent of a hierarchy of geometry that is\n * considered a "screen"; the ProjectionScreen will automatically recompute\n * all the UV\'s (for a particular texture stage) on its subordinate geometry\n * according to the relative position and lens parameters of the indicated\n * LensNode.\n *\n * All this does is recompute UV\'s; the caller is responsible for applying the\n * appropriate texture(s) to the geometry.\n *\n * This does not take advantage of any hardware-assisted projective texturing;\n * all of the UV\'s are computed in the CPU.  (Use NodePath::project_texture()\n * to enable hardware-assisted projective texturing.)  However, the\n * ProjectionScreen interface does support any kind of lens, linear or\n * nonlinear, that might be defined using the Lens interface, including\n * fisheye and cylindrical lenses.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.fx.ProjectionScreen' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE565B940>'
        'clearUndistLut': None, # (!) real value is "<method 'clearUndistLut' of 'panda3d.fx.ProjectionScreen' objects>"
        'clear_undist_lut': None, # (!) real value is "<method 'clear_undist_lut' of 'panda3d.fx.ProjectionScreen' objects>"
        'generateScreen': None, # (!) real value is "<method 'generateScreen' of 'panda3d.fx.ProjectionScreen' objects>"
        'generate_screen': None, # (!) real value is "<method 'generate_screen' of 'panda3d.fx.ProjectionScreen' objects>"
        'getAutoRecompute': None, # (!) real value is "<method 'getAutoRecompute' of 'panda3d.fx.ProjectionScreen' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDE565B940>)>'
        'getFrameColor': None, # (!) real value is "<method 'getFrameColor' of 'panda3d.fx.ProjectionScreen' objects>"
        'getInvertUvs': None, # (!) real value is "<method 'getInvertUvs' of 'panda3d.fx.ProjectionScreen' objects>"
        'getLastScreen': None, # (!) real value is "<method 'getLastScreen' of 'panda3d.fx.ProjectionScreen' objects>"
        'getProjector': None, # (!) real value is "<method 'getProjector' of 'panda3d.fx.ProjectionScreen' objects>"
        'getTexcoord3d': None, # (!) real value is "<method 'getTexcoord3d' of 'panda3d.fx.ProjectionScreen' objects>"
        'getTexcoordName': None, # (!) real value is "<method 'getTexcoordName' of 'panda3d.fx.ProjectionScreen' objects>"
        'getUndistLut': None, # (!) real value is "<method 'getUndistLut' of 'panda3d.fx.ProjectionScreen' objects>"
        'getVignetteColor': None, # (!) real value is "<method 'getVignetteColor' of 'panda3d.fx.ProjectionScreen' objects>"
        'getVignetteOn': None, # (!) real value is "<method 'getVignetteOn' of 'panda3d.fx.ProjectionScreen' objects>"
        'get_auto_recompute': None, # (!) real value is "<method 'get_auto_recompute' of 'panda3d.fx.ProjectionScreen' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDE565B940>)>'
        'get_frame_color': None, # (!) real value is "<method 'get_frame_color' of 'panda3d.fx.ProjectionScreen' objects>"
        'get_invert_uvs': None, # (!) real value is "<method 'get_invert_uvs' of 'panda3d.fx.ProjectionScreen' objects>"
        'get_last_screen': None, # (!) real value is "<method 'get_last_screen' of 'panda3d.fx.ProjectionScreen' objects>"
        'get_projector': None, # (!) real value is "<method 'get_projector' of 'panda3d.fx.ProjectionScreen' objects>"
        'get_texcoord_3d': None, # (!) real value is "<method 'get_texcoord_3d' of 'panda3d.fx.ProjectionScreen' objects>"
        'get_texcoord_name': None, # (!) real value is "<method 'get_texcoord_name' of 'panda3d.fx.ProjectionScreen' objects>"
        'get_undist_lut': None, # (!) real value is "<method 'get_undist_lut' of 'panda3d.fx.ProjectionScreen' objects>"
        'get_vignette_color': None, # (!) real value is "<method 'get_vignette_color' of 'panda3d.fx.ProjectionScreen' objects>"
        'get_vignette_on': None, # (!) real value is "<method 'get_vignette_on' of 'panda3d.fx.ProjectionScreen' objects>"
        'hasUndistLut': None, # (!) real value is "<method 'hasUndistLut' of 'panda3d.fx.ProjectionScreen' objects>"
        'has_undist_lut': None, # (!) real value is "<method 'has_undist_lut' of 'panda3d.fx.ProjectionScreen' objects>"
        'makeFlatMesh': None, # (!) real value is "<method 'makeFlatMesh' of 'panda3d.fx.ProjectionScreen' objects>"
        'make_flat_mesh': None, # (!) real value is "<method 'make_flat_mesh' of 'panda3d.fx.ProjectionScreen' objects>"
        'recompute': None, # (!) real value is "<method 'recompute' of 'panda3d.fx.ProjectionScreen' objects>"
        'recomputeIfStale': None, # (!) real value is "<method 'recomputeIfStale' of 'panda3d.fx.ProjectionScreen' objects>"
        'recompute_if_stale': None, # (!) real value is "<method 'recompute_if_stale' of 'panda3d.fx.ProjectionScreen' objects>"
        'regenerateScreen': None, # (!) real value is "<method 'regenerateScreen' of 'panda3d.fx.ProjectionScreen' objects>"
        'regenerate_screen': None, # (!) real value is "<method 'regenerate_screen' of 'panda3d.fx.ProjectionScreen' objects>"
        'setAutoRecompute': None, # (!) real value is "<method 'setAutoRecompute' of 'panda3d.fx.ProjectionScreen' objects>"
        'setFrameColor': None, # (!) real value is "<method 'setFrameColor' of 'panda3d.fx.ProjectionScreen' objects>"
        'setInvertUvs': None, # (!) real value is "<method 'setInvertUvs' of 'panda3d.fx.ProjectionScreen' objects>"
        'setProjector': None, # (!) real value is "<method 'setProjector' of 'panda3d.fx.ProjectionScreen' objects>"
        'setTexcoord3d': None, # (!) real value is "<method 'setTexcoord3d' of 'panda3d.fx.ProjectionScreen' objects>"
        'setTexcoordName': None, # (!) real value is "<method 'setTexcoordName' of 'panda3d.fx.ProjectionScreen' objects>"
        'setUndistLut': None, # (!) real value is "<method 'setUndistLut' of 'panda3d.fx.ProjectionScreen' objects>"
        'setVignetteColor': None, # (!) real value is "<method 'setVignetteColor' of 'panda3d.fx.ProjectionScreen' objects>"
        'setVignetteOn': None, # (!) real value is "<method 'setVignetteOn' of 'panda3d.fx.ProjectionScreen' objects>"
        'set_auto_recompute': None, # (!) real value is "<method 'set_auto_recompute' of 'panda3d.fx.ProjectionScreen' objects>"
        'set_frame_color': None, # (!) real value is "<method 'set_frame_color' of 'panda3d.fx.ProjectionScreen' objects>"
        'set_invert_uvs': None, # (!) real value is "<method 'set_invert_uvs' of 'panda3d.fx.ProjectionScreen' objects>"
        'set_projector': None, # (!) real value is "<method 'set_projector' of 'panda3d.fx.ProjectionScreen' objects>"
        'set_texcoord_3d': None, # (!) real value is "<method 'set_texcoord_3d' of 'panda3d.fx.ProjectionScreen' objects>"
        'set_texcoord_name': None, # (!) real value is "<method 'set_texcoord_name' of 'panda3d.fx.ProjectionScreen' objects>"
        'set_undist_lut': None, # (!) real value is "<method 'set_undist_lut' of 'panda3d.fx.ProjectionScreen' objects>"
        'set_vignette_color': None, # (!) real value is "<method 'set_vignette_color' of 'panda3d.fx.ProjectionScreen' objects>"
        'set_vignette_on': None, # (!) real value is "<method 'set_vignette_on' of 'panda3d.fx.ProjectionScreen' objects>"
    }


class PSphereLens(__panda3d_core.Lens):
    """
    /**
     * A PSphereLens is a special nonlinear lens that doesn't correspond to any
     * real physical lenses.  It's primarily useful for generating 360-degree
     * wraparound images while avoiding the distortion associated with fisheye
     * images.
     *
     * A PSphereLens is similar to a cylindrical lens, except it is also curved in
     * the vertical direction.  This allows it to extend to both poles in the
     * vertical direction.  The mapping is similar to what many modeling packages
     * call a sphere mapping: the x coordinate is proportional to azimuth, while
     * the y coordinate is proportional to altitude.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
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
        '__doc__': "/**\n * A PSphereLens is a special nonlinear lens that doesn't correspond to any\n * real physical lenses.  It's primarily useful for generating 360-degree\n * wraparound images while avoiding the distortion associated with fisheye\n * images.\n *\n * A PSphereLens is similar to a cylindrical lens, except it is also curved in\n * the vertical direction.  This allows it to extend to both poles in the\n * vertical direction.  The mapping is similar to what many modeling packages\n * call a sphere mapping: the x coordinate is proportional to azimuth, while\n * the y coordinate is proportional to altitude.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.fx.PSphereLens' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDE565BEB0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDE565BEB0>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDE565BEB0>)>'
    }


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021890179A90>'

__spec__ = None # (!) real value is "ModuleSpec(name='panda3d.fx', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021890179A90>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\LeonRandomPlus\\\\venv\\\\Lib\\\\site-packages\\\\panda3d\\\\fx.cp311-win_amd64.pyd')"

