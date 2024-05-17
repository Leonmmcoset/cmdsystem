# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedObject import TypedObject

class GeoMipTerrain(TypedObject):
    """
    /**
     * GeoMipTerrain, meaning Panda3D GeoMipMapping, can convert a heightfield
     * image into a 3D terrain, consisting of several GeomNodes.  It uses the
     * GeoMipMapping algorithm, or Geometrical MipMapping, based on the LOD (Level
     * of Detail) algorithm.  For more information about the GeoMipMapping
     * algoritm, see this paper, written by Willem H. de Boer:
     * https://flipcode.com/articles/article_geomipmaps.pdf
     */
    """
    def calcAmbientOcclusion(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_ambient_occlusion(const GeoMipTerrain self, float radius, float contrast, float brightness)
        
        /**
         * Calculates an approximate for the ambient occlusion and stores it in the
         * color map, so that it will be written to the vertex colors.  Any existing
         * color map will be discarded.  You need to call this before generating the
         * geometry.
         */
        """
        pass

    def calc_ambient_occlusion(self, const_GeoMipTerrain_self, float_radius, float_contrast, float_brightness): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_ambient_occlusion(const GeoMipTerrain self, float radius, float contrast, float brightness)
        
        /**
         * Calculates an approximate for the ambient occlusion and stores it in the
         * color map, so that it will be written to the vertex colors.  Any existing
         * color map will be discarded.  You need to call this before generating the
         * geometry.
         */
        """
        pass

    def clearColorMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_color_map(const GeoMipTerrain self)
        
        /**
         * Clears the color map.
         */
        """
        pass

    def clear_color_map(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_color_map(const GeoMipTerrain self)
        
        /**
         * Clears the color map.
         */
        """
        pass

    def colorMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        color_map(const GeoMipTerrain self)
        
        /**
         * Returns a reference to the color map (a PNMImage) contained inside
         * GeoMipTerrain.  You can use the reference to alter the color map.
         */
        """
        pass

    def color_map(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        color_map(const GeoMipTerrain self)
        
        /**
         * Returns a reference to the color map (a PNMImage) contained inside
         * GeoMipTerrain.  You can use the reference to alter the color map.
         */
        """
        pass

    def generate(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate(const GeoMipTerrain self)
        
        /**
         * (Re)generates the entire terrain, erasing the current.  This call un-
         * flattens the terrain, so make sure you have set auto-flatten if you want to
         * keep your terrain flattened.
         */
        """
        pass

    def getBlockFromPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_block_from_pos(const GeoMipTerrain self, double x, double y)
        
        /**
         * Gets the coordinates of the block at the specified position.  This position
         * must be relative to the terrain, not to render.  Returns an array
         * containing two values: the block x and the block y coords.  If the
         * positions are out of range, the closest block is taken.  Note that the
         * VecBase returned does not represent a vector, position, or rotation, but it
         * contains the block index of the block which you can use in
         * GeoMipTerrain::get_block_node_path.
         */
        """
        pass

    def getBlockNodePath(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_block_node_path(const GeoMipTerrain self, int mx, int my)
        
        /**
         * Returns the NodePath of the specified block.  If auto-flatten is enabled
         * and the node is getting removed during the flattening process, it will
         * still return a NodePath with the appropriate terrain chunk, but it will be
         * in a temporary scenegraph.  Please note that this returns a const object
         * and you can not modify the node.  Modify the heightfield instead.
         */
        """
        pass

    def getBlockSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_block_size(const GeoMipTerrain self)
        
        /**
         * Gets the block size.
         */
        """
        pass

    def getBorderStitching(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_border_stitching(const GeoMipTerrain self)
        
        /**
         * Returns the current stitching setting.  False by default, unless
         * set_stitching has been set.
         */
        """
        pass

    def getBruteforce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_bruteforce(const GeoMipTerrain self)
        
        /**
         * Returns a boolean whether the terrain is rendered bruteforce or not.  See
         * set_bruteforce for more information.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getElevation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_elevation(const GeoMipTerrain self, double x, double y)
        
        /**
         * Fetches the elevation at (x, y), where the input coordinate is specified in
         * pixels.  This ignores the current LOD level and instead provides an
         * accurate number.  Linear blending is used for non-integral coordinates.
         * Terrain scale is NOT taken into account!  To get accurate normals, please
         * multiply this with the terrain Z scale!
         *
         * trueElev = terr.get_elevation(x,y) * terr.get_sz();
         */
        """
        pass

    def getFar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_far(const GeoMipTerrain self)
        
        /**
         * Returns the far LOD distance in the terrain coordinate space
         */
        """
        pass

    def getFlattenMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flatten_mode(const GeoMipTerrain self)
        
        /**
         * Returns the automatic-flatten mode (e.g., off, flatten_light,
         * flatten_medium, or flatten_strong)
         */
        """
        pass

    def getFocalPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_focal_point(GeoMipTerrain self)
        
        /**
         * Returns the focal point, as a NodePath.  If you have set it to be just a
         * point, it will return an empty node at the focal position.
         */
        """
        pass

    def getMaxLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_level(const GeoMipTerrain self)
        
        /**
         * Returns the highest level possible for this block size.  When a block is at
         * this level, it will be the worst quality possible.
         */
        """
        pass

    def getMinLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min_level(const GeoMipTerrain self)
        
        /**
         * Gets the minimum level of detail at which blocks may be generated by
         * generate() or update(). The default value is 0, which is the highest
         * quality.
         */
        """
        pass

    def getNear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_near(const GeoMipTerrain self)
        
        /**
         * Returns the near LOD distance in the terrain coordinate space
         */
        """
        pass

    def getNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_normal(const GeoMipTerrain self, int x, int y)
        get_normal(const GeoMipTerrain self, int mx, int my, int x, int y)
        
        /**
         * Fetches the terrain normal at (x,y), where the input coordinate is
         * specified in pixels.  This ignores the current LOD level and instead
         * provides an accurate number.  Terrain scale is NOT taken into account!  To
         * get accurate normals, please divide it by the terrain scale and normalize
         * it again!
         */
        
        /**
         * Fetches the terrain normal at (x, y), where the input coordinate is
         * specified in pixels.  This ignores the current LOD level and instead
         * provides an accurate number.  Terrain scale is NOT taken into account!  To
         * get accurate normals, please divide it by the terrain scale and normalize
         * it again, like this:
         *
         * LVector3 normal (terr.get_normal(x, y)); normal.set(normal.get_x() /
         * root.get_sx(), normal.get_y() / root.get_sy(), normal.get_z() /
         * root.get_sz()); normal.normalize();
         */
        """
        pass

    def getRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_root(GeoMipTerrain self)
        
        /**
         * Returns the root of the terrain.  This is a single PandaNode to which all
         * the rest of the terrain is parented.  The generate and update operations
         * replace the nodes which are parented to this root, but they don't replace
         * this root itself.
         */
        """
        pass

    def get_block_from_pos(self, const_GeoMipTerrain_self, double_x, double_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_block_from_pos(const GeoMipTerrain self, double x, double y)
        
        /**
         * Gets the coordinates of the block at the specified position.  This position
         * must be relative to the terrain, not to render.  Returns an array
         * containing two values: the block x and the block y coords.  If the
         * positions are out of range, the closest block is taken.  Note that the
         * VecBase returned does not represent a vector, position, or rotation, but it
         * contains the block index of the block which you can use in
         * GeoMipTerrain::get_block_node_path.
         */
        """
        pass

    def get_block_node_path(self, const_GeoMipTerrain_self, int_mx, int_my): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_block_node_path(const GeoMipTerrain self, int mx, int my)
        
        /**
         * Returns the NodePath of the specified block.  If auto-flatten is enabled
         * and the node is getting removed during the flattening process, it will
         * still return a NodePath with the appropriate terrain chunk, but it will be
         * in a temporary scenegraph.  Please note that this returns a const object
         * and you can not modify the node.  Modify the heightfield instead.
         */
        """
        pass

    def get_block_size(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_block_size(const GeoMipTerrain self)
        
        /**
         * Gets the block size.
         */
        """
        pass

    def get_border_stitching(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_border_stitching(const GeoMipTerrain self)
        
        /**
         * Returns the current stitching setting.  False by default, unless
         * set_stitching has been set.
         */
        """
        pass

    def get_bruteforce(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_bruteforce(const GeoMipTerrain self)
        
        /**
         * Returns a boolean whether the terrain is rendered bruteforce or not.  See
         * set_bruteforce for more information.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_elevation(self, const_GeoMipTerrain_self, double_x, double_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_elevation(const GeoMipTerrain self, double x, double y)
        
        /**
         * Fetches the elevation at (x, y), where the input coordinate is specified in
         * pixels.  This ignores the current LOD level and instead provides an
         * accurate number.  Linear blending is used for non-integral coordinates.
         * Terrain scale is NOT taken into account!  To get accurate normals, please
         * multiply this with the terrain Z scale!
         *
         * trueElev = terr.get_elevation(x,y) * terr.get_sz();
         */
        """
        pass

    def get_far(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_far(const GeoMipTerrain self)
        
        /**
         * Returns the far LOD distance in the terrain coordinate space
         */
        """
        pass

    def get_flatten_mode(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flatten_mode(const GeoMipTerrain self)
        
        /**
         * Returns the automatic-flatten mode (e.g., off, flatten_light,
         * flatten_medium, or flatten_strong)
         */
        """
        pass

    def get_focal_point(self, GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_focal_point(GeoMipTerrain self)
        
        /**
         * Returns the focal point, as a NodePath.  If you have set it to be just a
         * point, it will return an empty node at the focal position.
         */
        """
        pass

    def get_max_level(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_level(const GeoMipTerrain self)
        
        /**
         * Returns the highest level possible for this block size.  When a block is at
         * this level, it will be the worst quality possible.
         */
        """
        pass

    def get_min_level(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min_level(const GeoMipTerrain self)
        
        /**
         * Gets the minimum level of detail at which blocks may be generated by
         * generate() or update(). The default value is 0, which is the highest
         * quality.
         */
        """
        pass

    def get_near(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_near(const GeoMipTerrain self)
        
        /**
         * Returns the near LOD distance in the terrain coordinate space
         */
        """
        pass

    def get_normal(self, const_GeoMipTerrain_self, int_x, int_y): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_normal(const GeoMipTerrain self, int x, int y)
        get_normal(const GeoMipTerrain self, int mx, int my, int x, int y)
        
        /**
         * Fetches the terrain normal at (x,y), where the input coordinate is
         * specified in pixels.  This ignores the current LOD level and instead
         * provides an accurate number.  Terrain scale is NOT taken into account!  To
         * get accurate normals, please divide it by the terrain scale and normalize
         * it again!
         */
        
        /**
         * Fetches the terrain normal at (x, y), where the input coordinate is
         * specified in pixels.  This ignores the current LOD level and instead
         * provides an accurate number.  Terrain scale is NOT taken into account!  To
         * get accurate normals, please divide it by the terrain scale and normalize
         * it again, like this:
         *
         * LVector3 normal (terr.get_normal(x, y)); normal.set(normal.get_x() /
         * root.get_sx(), normal.get_y() / root.get_sy(), normal.get_z() /
         * root.get_sz()); normal.normalize();
         */
        """
        pass

    def get_root(self, GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_root(GeoMipTerrain self)
        
        /**
         * Returns the root of the terrain.  This is a single PandaNode to which all
         * the rest of the terrain is parented.  The generate and update operations
         * replace the nodes which are parented to this root, but they don't replace
         * this root itself.
         */
        """
        pass

    def hasColorMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_color_map(GeoMipTerrain self)
        
        /**
         * Returns whether a color map has been set.
         */
        """
        pass

    def has_color_map(self, GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_color_map(GeoMipTerrain self)
        
        /**
         * Returns whether a color map has been set.
         */
        """
        pass

    def heightfield(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        heightfield(const GeoMipTerrain self)
        
        /**
         * Returns a reference to the heightfield (a PNMImage) contained inside
         * GeoMipTerrain.  You can use the reference to alter the heightfield.
         */
        """
        pass

    def isDirty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_dirty(const GeoMipTerrain self)
        
        /**
         * Returns a bool indicating whether the terrain is marked 'dirty', that means
         * the terrain has to be regenerated on the next update() call, because for
         * instance the heightfield has changed.  Once the terrain has been
         * regenerated, the dirty flag automatically gets reset internally.
         */
        """
        pass

    def is_dirty(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_dirty(const GeoMipTerrain self)
        
        /**
         * Returns a bool indicating whether the terrain is marked 'dirty', that means
         * the terrain has to be regenerated on the next update() call, because for
         * instance the heightfield has changed.  Once the terrain has been
         * regenerated, the dirty flag automatically gets reset internally.
         */
        """
        pass

    def makeSlopeImage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_slope_image(const GeoMipTerrain self)
        
        /**
         * Returns a new grayscale image containing the slope angles.  A white pixel
         * value means a vertical slope, while a black pixel will mean that the
         * terrain is entirely flat at that pixel.  You can translate it to degrees by
         * mapping the greyscale values from 0 to 90 degrees.  The resulting image
         * will have the same size as the heightfield image.  The scale will be taken
         * into respect -- meaning, if you change the terrain scale, the slope image
         * will need to be regenerated in order to be correct.
         */
        """
        pass

    def make_slope_image(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_slope_image(const GeoMipTerrain self)
        
        /**
         * Returns a new grayscale image containing the slope angles.  A white pixel
         * value means a vertical slope, while a black pixel will mean that the
         * terrain is entirely flat at that pixel.  You can translate it to degrees by
         * mapping the greyscale values from 0 to 90 degrees.  The resulting image
         * will have the same size as the heightfield image.  The scale will be taken
         * into respect -- meaning, if you change the terrain scale, the slope image
         * will need to be regenerated in order to be correct.
         */
        """
        pass

    def setAutoFlatten(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_flatten(const GeoMipTerrain self, int mode)
        
        /**
         * The terrain can be automatically flattened (using flatten_light,
         * flatten_medium, or flatten_strong) after each update.  This only affects
         * future updates, it doesn't flatten the current terrain.
         */
        """
        pass

    def setBlockSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_block_size(const GeoMipTerrain self, int newbs)
        
        /**
         * Sets the block size.  If it is not a power of two, the closest power of two
         * is used.
         */
        """
        pass

    def setBorderStitching(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_border_stitching(const GeoMipTerrain self, bool stitching)
        
        /**
         * If this value is true, the LOD level at the borders of the terrain will be
         * 0. This is useful if you have multiple terrains attached and you want to
         * stitch them together, to fix seams.  This setting also has effect when
         * bruteforce is enabled, although in that case you are probably better off
         * with setting the minlevels to the same value.
         */
        """
        pass

    def setBruteforce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_bruteforce(const GeoMipTerrain self, bool bf)
        
        /**
         * Sets a boolean specifying whether the terrain will be rendered bruteforce.
         * If the terrain is rendered bruteforce, there will be no Level of Detail,
         * and the update() call will only update the terrain if it is marked dirty.
         */
        """
        pass

    def setColorMap(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color_map(const GeoMipTerrain self, const Filename filename)
        set_color_map(const GeoMipTerrain self, const Texture image)
        set_color_map(const GeoMipTerrain self, const PNMImage image)
        set_color_map(const GeoMipTerrain self, str path)
        
        /**
         * Loads the specified image as color map.  The next time generate() is
         * called, the terrain is painted with this color map using the vertex color
         * column.  Returns a boolean indicating whether the operation has succeeded.
         */
        """
        pass

    def setFactor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_factor(const GeoMipTerrain self, float factor)
        
        /**
         * DEPRECATED method.  Use set_near/far instead.  Sets the quality factor at
         * which blocks must be generated.  The higher this level, the better quality
         * the terrain will be, but more expensive to render.  A value of 0 makes the
         * terrain the lowest quality possible, depending on blocksize.  The default
         * value is 100.
         */
        """
        pass

    def setFar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_far(const GeoMipTerrain self, double input_far)
        
        /**
         * Sets the far LOD distance, at which the terrain will be rendered at lowest
         * quality.  This distance is in the terrain's coordinate space!
         */
        """
        pass

    def setFocalPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_focal_point(const GeoMipTerrain self, const LPoint2f fp)
        set_focal_point(const GeoMipTerrain self, const LPoint3d fp)
        set_focal_point(const GeoMipTerrain self, const LPoint2d fp)
        set_focal_point(const GeoMipTerrain self, const LPoint3f fp)
        set_focal_point(const GeoMipTerrain self, NodePath fnp)
        set_focal_point(const GeoMipTerrain self, double x, double y)
        
        // The focal point is the point at which the terrain will have the highest
        // quality (lowest level of detail). Parts farther away from the focal point
        // will have a lower quality (higher level of detail). The focal point is
        // not taken in respect if bruteforce is set true.
        
        /**
         * Sets the focal point.  GeoMipTerrain generates high-resolution terrain
         * around the focal point, and progressively lower and lower resolution
         * terrain as you get farther away.  If a point is supplied and not a
         * NodePath, make sure it's relative to the terrain.  Only the x and y
         * coordinates of the focal point are taken in respect.
         */
        """
        pass

    def setHeightfield(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_heightfield(const GeoMipTerrain self, const Filename filename)
        set_heightfield(const GeoMipTerrain self, const PNMImage image)
        
        /**
         * Loads the specified heightmap image file into the heightfield.  Returns
         * true if succeeded, or false if an error has occured.  If the heightmap is
         * not a power of two plus one, it is scaled up using a gaussian filter.
         */
        
        /**
         * Loads the specified heightmap image file into the heightfield.  Returns
         * true if succeeded, or false if an error has occured.  If the heightmap is
         * not a power of two plus one, it is scaled up using a gaussian filter.
         */
        """
        pass

    def setMinLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_min_level(const GeoMipTerrain self, int minlevel)
        
        /**
         * Sets the minimum level of detail at which blocks may be generated by
         * generate() or update(). The default value is 0, which is the highest
         * quality.  This value is also taken in respect when generating the terrain
         * bruteforce.
         */
        """
        pass

    def setNear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_near(const GeoMipTerrain self, double input_near)
        
        /**
         * Sets the near LOD distance, at which the terrain will be rendered at
         * highest quality.  This distance is in the terrain's coordinate space!
         */
        """
        pass

    def setNearFar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_near_far(const GeoMipTerrain self, double input_near, double input_far)
        
        /**
         * Sets the near and far LOD distances in one call.
         */
        """
        pass

    def set_auto_flatten(self, const_GeoMipTerrain_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_flatten(const GeoMipTerrain self, int mode)
        
        /**
         * The terrain can be automatically flattened (using flatten_light,
         * flatten_medium, or flatten_strong) after each update.  This only affects
         * future updates, it doesn't flatten the current terrain.
         */
        """
        pass

    def set_block_size(self, const_GeoMipTerrain_self, int_newbs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_block_size(const GeoMipTerrain self, int newbs)
        
        /**
         * Sets the block size.  If it is not a power of two, the closest power of two
         * is used.
         */
        """
        pass

    def set_border_stitching(self, const_GeoMipTerrain_self, bool_stitching): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_border_stitching(const GeoMipTerrain self, bool stitching)
        
        /**
         * If this value is true, the LOD level at the borders of the terrain will be
         * 0. This is useful if you have multiple terrains attached and you want to
         * stitch them together, to fix seams.  This setting also has effect when
         * bruteforce is enabled, although in that case you are probably better off
         * with setting the minlevels to the same value.
         */
        """
        pass

    def set_bruteforce(self, const_GeoMipTerrain_self, bool_bf): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_bruteforce(const GeoMipTerrain self, bool bf)
        
        /**
         * Sets a boolean specifying whether the terrain will be rendered bruteforce.
         * If the terrain is rendered bruteforce, there will be no Level of Detail,
         * and the update() call will only update the terrain if it is marked dirty.
         */
        """
        pass

    def set_color_map(self, const_GeoMipTerrain_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color_map(const GeoMipTerrain self, const Filename filename)
        set_color_map(const GeoMipTerrain self, const Texture image)
        set_color_map(const GeoMipTerrain self, const PNMImage image)
        set_color_map(const GeoMipTerrain self, str path)
        
        /**
         * Loads the specified image as color map.  The next time generate() is
         * called, the terrain is painted with this color map using the vertex color
         * column.  Returns a boolean indicating whether the operation has succeeded.
         */
        """
        pass

    def set_factor(self, const_GeoMipTerrain_self, float_factor): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_factor(const GeoMipTerrain self, float factor)
        
        /**
         * DEPRECATED method.  Use set_near/far instead.  Sets the quality factor at
         * which blocks must be generated.  The higher this level, the better quality
         * the terrain will be, but more expensive to render.  A value of 0 makes the
         * terrain the lowest quality possible, depending on blocksize.  The default
         * value is 100.
         */
        """
        pass

    def set_far(self, const_GeoMipTerrain_self, double_input_far): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_far(const GeoMipTerrain self, double input_far)
        
        /**
         * Sets the far LOD distance, at which the terrain will be rendered at lowest
         * quality.  This distance is in the terrain's coordinate space!
         */
        """
        pass

    def set_focal_point(self, const_GeoMipTerrain_self, const_LPoint2f_fp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_focal_point(const GeoMipTerrain self, const LPoint2f fp)
        set_focal_point(const GeoMipTerrain self, const LPoint3d fp)
        set_focal_point(const GeoMipTerrain self, const LPoint2d fp)
        set_focal_point(const GeoMipTerrain self, const LPoint3f fp)
        set_focal_point(const GeoMipTerrain self, NodePath fnp)
        set_focal_point(const GeoMipTerrain self, double x, double y)
        
        // The focal point is the point at which the terrain will have the highest
        // quality (lowest level of detail). Parts farther away from the focal point
        // will have a lower quality (higher level of detail). The focal point is
        // not taken in respect if bruteforce is set true.
        
        /**
         * Sets the focal point.  GeoMipTerrain generates high-resolution terrain
         * around the focal point, and progressively lower and lower resolution
         * terrain as you get farther away.  If a point is supplied and not a
         * NodePath, make sure it's relative to the terrain.  Only the x and y
         * coordinates of the focal point are taken in respect.
         */
        """
        pass

    def set_heightfield(self, const_GeoMipTerrain_self, const_Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_heightfield(const GeoMipTerrain self, const Filename filename)
        set_heightfield(const GeoMipTerrain self, const PNMImage image)
        
        /**
         * Loads the specified heightmap image file into the heightfield.  Returns
         * true if succeeded, or false if an error has occured.  If the heightmap is
         * not a power of two plus one, it is scaled up using a gaussian filter.
         */
        
        /**
         * Loads the specified heightmap image file into the heightfield.  Returns
         * true if succeeded, or false if an error has occured.  If the heightmap is
         * not a power of two plus one, it is scaled up using a gaussian filter.
         */
        """
        pass

    def set_min_level(self, const_GeoMipTerrain_self, int_minlevel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_min_level(const GeoMipTerrain self, int minlevel)
        
        /**
         * Sets the minimum level of detail at which blocks may be generated by
         * generate() or update(). The default value is 0, which is the highest
         * quality.  This value is also taken in respect when generating the terrain
         * bruteforce.
         */
        """
        pass

    def set_near(self, const_GeoMipTerrain_self, double_input_near): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_near(const GeoMipTerrain self, double input_near)
        
        /**
         * Sets the near LOD distance, at which the terrain will be rendered at
         * highest quality.  This distance is in the terrain's coordinate space!
         */
        """
        pass

    def set_near_far(self, const_GeoMipTerrain_self, double_input_near, double_input_far): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_near_far(const GeoMipTerrain self, double input_near, double input_far)
        
        /**
         * Sets the near and far LOD distances in one call.
         */
        """
        pass

    def update(self, const_GeoMipTerrain_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const GeoMipTerrain self)
        
        /**
         * Loops through all of the terrain blocks, and checks whether they need to be
         * updated.  If that is indeed the case, it regenerates the mipmap.  Returns a
         * true when the terrain has changed.  Returns false when the terrain isn't
         * updated at all.  If there is no terrain yet, it generates the entire
         * terrain.  This call un-flattens the terrain, so make sure you have set
         * auto-flatten if you want to keep your terrain flattened.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AFMLight = 1
    AFMMedium = 2
    AFMOff = 0
    AFMStrong = 3
    AFM_light = 1
    AFM_medium = 2
    AFM_off = 0
    AFM_strong = 3
    DtoolClassDict = {
        'AFMLight': 1,
        'AFMMedium': 2,
        'AFMOff': 0,
        'AFMStrong': 3,
        'AFM_light': 1,
        'AFM_medium': 2,
        'AFM_off': 0,
        'AFM_strong': 3,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * GeoMipTerrain, meaning Panda3D GeoMipMapping, can convert a heightfield\n * image into a 3D terrain, consisting of several GeomNodes.  It uses the\n * GeoMipMapping algorithm, or Geometrical MipMapping, based on the LOD (Level\n * of Detail) algorithm.  For more information about the GeoMipMapping\n * algoritm, see this paper, written by Willem H. de Boer:\n * https://flipcode.com/articles/article_geomipmaps.pdf\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeoMipTerrain' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BC560>'
        'calcAmbientOcclusion': None, # (!) real value is "<method 'calcAmbientOcclusion' of 'panda3d.core.GeoMipTerrain' objects>"
        'calc_ambient_occlusion': None, # (!) real value is "<method 'calc_ambient_occlusion' of 'panda3d.core.GeoMipTerrain' objects>"
        'clearColorMap': None, # (!) real value is "<method 'clearColorMap' of 'panda3d.core.GeoMipTerrain' objects>"
        'clear_color_map': None, # (!) real value is "<method 'clear_color_map' of 'panda3d.core.GeoMipTerrain' objects>"
        'colorMap': None, # (!) real value is "<method 'colorMap' of 'panda3d.core.GeoMipTerrain' objects>"
        'color_map': None, # (!) real value is "<method 'color_map' of 'panda3d.core.GeoMipTerrain' objects>"
        'generate': None, # (!) real value is "<method 'generate' of 'panda3d.core.GeoMipTerrain' objects>"
        'getBlockFromPos': None, # (!) real value is "<method 'getBlockFromPos' of 'panda3d.core.GeoMipTerrain' objects>"
        'getBlockNodePath': None, # (!) real value is "<method 'getBlockNodePath' of 'panda3d.core.GeoMipTerrain' objects>"
        'getBlockSize': None, # (!) real value is "<method 'getBlockSize' of 'panda3d.core.GeoMipTerrain' objects>"
        'getBorderStitching': None, # (!) real value is "<method 'getBorderStitching' of 'panda3d.core.GeoMipTerrain' objects>"
        'getBruteforce': None, # (!) real value is "<method 'getBruteforce' of 'panda3d.core.GeoMipTerrain' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2BC560>)>'
        'getElevation': None, # (!) real value is "<method 'getElevation' of 'panda3d.core.GeoMipTerrain' objects>"
        'getFar': None, # (!) real value is "<method 'getFar' of 'panda3d.core.GeoMipTerrain' objects>"
        'getFlattenMode': None, # (!) real value is "<method 'getFlattenMode' of 'panda3d.core.GeoMipTerrain' objects>"
        'getFocalPoint': None, # (!) real value is "<method 'getFocalPoint' of 'panda3d.core.GeoMipTerrain' objects>"
        'getMaxLevel': None, # (!) real value is "<method 'getMaxLevel' of 'panda3d.core.GeoMipTerrain' objects>"
        'getMinLevel': None, # (!) real value is "<method 'getMinLevel' of 'panda3d.core.GeoMipTerrain' objects>"
        'getNear': None, # (!) real value is "<method 'getNear' of 'panda3d.core.GeoMipTerrain' objects>"
        'getNormal': None, # (!) real value is "<method 'getNormal' of 'panda3d.core.GeoMipTerrain' objects>"
        'getRoot': None, # (!) real value is "<method 'getRoot' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_block_from_pos': None, # (!) real value is "<method 'get_block_from_pos' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_block_node_path': None, # (!) real value is "<method 'get_block_node_path' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_block_size': None, # (!) real value is "<method 'get_block_size' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_border_stitching': None, # (!) real value is "<method 'get_border_stitching' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_bruteforce': None, # (!) real value is "<method 'get_bruteforce' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2BC560>)>'
        'get_elevation': None, # (!) real value is "<method 'get_elevation' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_far': None, # (!) real value is "<method 'get_far' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_flatten_mode': None, # (!) real value is "<method 'get_flatten_mode' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_focal_point': None, # (!) real value is "<method 'get_focal_point' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_max_level': None, # (!) real value is "<method 'get_max_level' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_min_level': None, # (!) real value is "<method 'get_min_level' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_near': None, # (!) real value is "<method 'get_near' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_normal': None, # (!) real value is "<method 'get_normal' of 'panda3d.core.GeoMipTerrain' objects>"
        'get_root': None, # (!) real value is "<method 'get_root' of 'panda3d.core.GeoMipTerrain' objects>"
        'hasColorMap': None, # (!) real value is "<method 'hasColorMap' of 'panda3d.core.GeoMipTerrain' objects>"
        'has_color_map': None, # (!) real value is "<method 'has_color_map' of 'panda3d.core.GeoMipTerrain' objects>"
        'heightfield': None, # (!) real value is "<method 'heightfield' of 'panda3d.core.GeoMipTerrain' objects>"
        'isDirty': None, # (!) real value is "<method 'isDirty' of 'panda3d.core.GeoMipTerrain' objects>"
        'is_dirty': None, # (!) real value is "<method 'is_dirty' of 'panda3d.core.GeoMipTerrain' objects>"
        'makeSlopeImage': None, # (!) real value is "<method 'makeSlopeImage' of 'panda3d.core.GeoMipTerrain' objects>"
        'make_slope_image': None, # (!) real value is "<method 'make_slope_image' of 'panda3d.core.GeoMipTerrain' objects>"
        'setAutoFlatten': None, # (!) real value is "<method 'setAutoFlatten' of 'panda3d.core.GeoMipTerrain' objects>"
        'setBlockSize': None, # (!) real value is "<method 'setBlockSize' of 'panda3d.core.GeoMipTerrain' objects>"
        'setBorderStitching': None, # (!) real value is "<method 'setBorderStitching' of 'panda3d.core.GeoMipTerrain' objects>"
        'setBruteforce': None, # (!) real value is "<method 'setBruteforce' of 'panda3d.core.GeoMipTerrain' objects>"
        'setColorMap': None, # (!) real value is "<method 'setColorMap' of 'panda3d.core.GeoMipTerrain' objects>"
        'setFactor': None, # (!) real value is "<method 'setFactor' of 'panda3d.core.GeoMipTerrain' objects>"
        'setFar': None, # (!) real value is "<method 'setFar' of 'panda3d.core.GeoMipTerrain' objects>"
        'setFocalPoint': None, # (!) real value is "<method 'setFocalPoint' of 'panda3d.core.GeoMipTerrain' objects>"
        'setHeightfield': None, # (!) real value is "<method 'setHeightfield' of 'panda3d.core.GeoMipTerrain' objects>"
        'setMinLevel': None, # (!) real value is "<method 'setMinLevel' of 'panda3d.core.GeoMipTerrain' objects>"
        'setNear': None, # (!) real value is "<method 'setNear' of 'panda3d.core.GeoMipTerrain' objects>"
        'setNearFar': None, # (!) real value is "<method 'setNearFar' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_auto_flatten': None, # (!) real value is "<method 'set_auto_flatten' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_block_size': None, # (!) real value is "<method 'set_block_size' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_border_stitching': None, # (!) real value is "<method 'set_border_stitching' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_bruteforce': None, # (!) real value is "<method 'set_bruteforce' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_color_map': None, # (!) real value is "<method 'set_color_map' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_factor': None, # (!) real value is "<method 'set_factor' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_far': None, # (!) real value is "<method 'set_far' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_focal_point': None, # (!) real value is "<method 'set_focal_point' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_heightfield': None, # (!) real value is "<method 'set_heightfield' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_min_level': None, # (!) real value is "<method 'set_min_level' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_near': None, # (!) real value is "<method 'set_near' of 'panda3d.core.GeoMipTerrain' objects>"
        'set_near_far': None, # (!) real value is "<method 'set_near_far' of 'panda3d.core.GeoMipTerrain' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d.core.GeoMipTerrain' objects>"
    }


