# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class Lens(TypedWritableReferenceCount):
    """
    /**
     * A base class for any number of different kinds of lenses, linear and
     * otherwise.  Presently, this includes perspective and orthographic lenses.
     *
     * A Lens object is the main part of a Camera node, which defines the
     * fundamental interface to point-of-view for rendering.  Lenses are also used
     * in other contexts, however; for instance, a Spotlight is also defined using
     * a lens.
     */
    """
    def clear(self, const_Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const Lens self)
        
        /**
         * Resets all lens parameters to their initial default settings.
         */
        """
        pass

    def clearCustomFilmMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_custom_film_mat(const Lens self)
        
        /**
         * Disables the lens custom_film_mat correction.
         */
        """
        pass

    def clearKeystone(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_keystone(const Lens self)
        
        /**
         * Disables the lens keystone correction.
         */
        """
        pass

    def clearViewMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_view_mat(const Lens self)
        
        /**
         * Resets the lens transform to identity.
         */
        """
        pass

    def clear_custom_film_mat(self, const_Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_custom_film_mat(const Lens self)
        
        /**
         * Disables the lens custom_film_mat correction.
         */
        """
        pass

    def clear_keystone(self, const_Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_keystone(const Lens self)
        
        /**
         * Disables the lens keystone correction.
         */
        """
        pass

    def clear_view_mat(self, const_Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_view_mat(const Lens self)
        
        /**
         * Resets the lens transform to identity.
         */
        """
        pass

    def extrude(self, Lens_self, const_LPoint2f_point2d, LPoint3f_near_point, LPoint3f_far_point): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extrude(Lens self, const LPoint2f point2d, LPoint3f near_point, LPoint3f far_point)
        extrude(Lens self, const LPoint3f point2d, LPoint3f near_point, LPoint3f far_point)
        
        /**
         * Given a 2-d point in the range (-1,1) in both dimensions, where (0,0) is
         * the center of the lens and (-1,-1) is the lower-left corner, compute the
         * corresponding vector in space that maps to this point, if such a vector can
         * be determined.  The vector is returned by indicating the points on the near
         * plane and far plane that both map to the indicated 2-d point.
         *
         * Returns true if the vector is defined, or false otherwise.
         */
        
        /**
         * Given a 2-d point in the range (-1,1) in both dimensions, where (0,0) is
         * the center of the lens and (-1,-1) is the lower-left corner, compute the
         * corresponding vector in space that maps to this point, if such a vector can
         * be determined.  The vector is returned by indicating the points on the near
         * plane and far plane that both map to the indicated 2-d point.
         *
         * The z coordinate of the 2-d point is ignored.
         *
         * Returns true if the vector is defined, or false otherwise.
         */
        """
        pass

    def extrudeDepth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extrude_depth(Lens self, const LPoint3f point2d, LPoint3f point3d)
        
        /**
         * Uses the depth component of the 3-d result from project() to compute the
         * original point in 3-d space corresponding to a particular point on the
         * lens.  This exactly reverses project(), assuming the point does fall
         * legitimately within the lens.
         */
        """
        pass

    def extrudeVec(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        extrude_vec(Lens self, const LPoint3f point2d, LVector3f vec3d)
        extrude_vec(Lens self, const LPoint2f point2d, LVector3f vec3d)
        
        /**
         * Given a 2-d point in the range (-1,1) in both dimensions, where (0,0) is
         * the center of the lens and (-1,-1) is the lower-left corner, compute the
         * vector that corresponds to the view direction.  This will be parallel to
         * the normal on the surface (the far plane) corresponding to the lens shape
         * at this point.
         *
         * See the comment block on Lens::extrude_vec_impl() for a more in-depth
         * comment on the meaning of this vector.
         *
         * Returns true if the vector is defined, or false otherwise.
         */
        
        /**
         * Given a 2-d point in the range (-1,1) in both dimensions, where (0,0) is
         * the center of the lens and (-1,-1) is the lower-left corner, compute the
         * vector that corresponds to the view direction.  This will be parallel to
         * the normal on the surface (the far plane) corresponding to the lens shape
         * at this point.
         *
         * See the comment block on Lens::extrude_vec_impl() for a more in-depth
         * comment on the meaning of this vector.
         *
         * The z coordinate of the 2-d point is ignored.
         *
         * Returns true if the vector is defined, or false otherwise.
         */
        """
        pass

    def extrude_depth(self, Lens_self, const_LPoint3f_point2d, LPoint3f_point3d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extrude_depth(Lens self, const LPoint3f point2d, LPoint3f point3d)
        
        /**
         * Uses the depth component of the 3-d result from project() to compute the
         * original point in 3-d space corresponding to a particular point on the
         * lens.  This exactly reverses project(), assuming the point does fall
         * legitimately within the lens.
         */
        """
        pass

    def extrude_vec(self, Lens_self, const_LPoint3f_point2d, LVector3f_vec3d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extrude_vec(Lens self, const LPoint3f point2d, LVector3f vec3d)
        extrude_vec(Lens self, const LPoint2f point2d, LVector3f vec3d)
        
        /**
         * Given a 2-d point in the range (-1,1) in both dimensions, where (0,0) is
         * the center of the lens and (-1,-1) is the lower-left corner, compute the
         * vector that corresponds to the view direction.  This will be parallel to
         * the normal on the surface (the far plane) corresponding to the lens shape
         * at this point.
         *
         * See the comment block on Lens::extrude_vec_impl() for a more in-depth
         * comment on the meaning of this vector.
         *
         * Returns true if the vector is defined, or false otherwise.
         */
        
        /**
         * Given a 2-d point in the range (-1,1) in both dimensions, where (0,0) is
         * the center of the lens and (-1,-1) is the lower-left corner, compute the
         * vector that corresponds to the view direction.  This will be parallel to
         * the normal on the surface (the far plane) corresponding to the lens shape
         * at this point.
         *
         * See the comment block on Lens::extrude_vec_impl() for a more in-depth
         * comment on the meaning of this vector.
         *
         * The z coordinate of the 2-d point is ignored.
         *
         * Returns true if the vector is defined, or false otherwise.
         */
        """
        pass

    def getAspectRatio(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aspect_ratio(Lens self)
        
        /**
         * Returns the aspect ratio of the Lens.  This is determined based on the
         * indicated film size; see set_film_size().
         */
        """
        pass

    def getChangeEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_change_event(Lens self)
        
        /**
         * Returns the name of the event that will be generated whenever any
         * properties of this particular Lens have changed.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getConvergenceDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_convergence_distance(Lens self)
        
        /**
         * See set_convergence_distance().
         */
        """
        pass

    def getCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_coordinate_system(Lens self)
        
        /**
         * Returns the coordinate system that all 3-d computations are performed
         * within for this Lens.  Normally, this is CS_default.
         */
        """
        pass

    def getCustomFilmMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_custom_film_mat(Lens self)
        
        /**
         * Returns the custom_film_mat specified for the lens.
         */
        """
        pass

    def getDefaultFar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_far()
        
        /**
         * Returns the default far plane distance that will be assigned to each newly-
         * created lens.  This is read from the Config.prc file.
         */
        """
        pass

    def getDefaultNear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_near()
        
        /**
         * Returns the default near plane distance that will be assigned to each
         * newly-created lens.  This is read from the Config.prc file.
         */
        """
        pass

    def getFar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_far(Lens self)
        
        /**
         * Returns the position of the far plane (or cylinder, sphere, whatever).
         */
        """
        pass

    def getFilmMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_film_mat(Lens self)
        
        /**
         * Returns the matrix that transforms from a point behind the lens to a point
         * on the film.
         */
        """
        pass

    def getFilmMatInv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_film_mat_inv(Lens self)
        
        /**
         * Returns the matrix that transforms from a point on the film to a point
         * behind the lens.
         */
        """
        pass

    def getFilmOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_film_offset(Lens self)
        
        /**
         * Returns the horizontal and vertical offset amounts of this Lens.  See
         * set_film_offset().
         */
        """
        pass

    def getFilmSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_film_size(Lens self)
        
        /**
         * Returns the horizontal and vertical film size of the virtual film.  See
         * set_film_size().
         */
        """
        pass

    def getFocalLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_focal_length(Lens self)
        
        /**
         * Returns the focal length of the lens.  This may have been set explicitly by
         * a previous call to set_focal_length(), or it may be computed based on the
         * lens' fov and film_size.  For certain kinds of lenses, the focal length has
         * no meaning.
         */
        """
        pass

    def getFov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_fov(Lens self)
        
        /**
         * Returns the horizontal and vertical film size of the virtual film.  See
         * set_fov().
         */
        """
        pass

    def getHfov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hfov(Lens self)
        
        /**
         * Returns the horizontal component of fov only.  See get_fov().
         */
        """
        pass

    def getInterocularDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_interocular_distance(Lens self)
        
        /**
         * See set_interocular_distance().
         */
        """
        pass

    def getKeystone(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keystone(Lens self)
        
        /**
         * Returns the keystone correction specified for the lens.
         */
        """
        pass

    def getLastChange(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_last_change(Lens self)
        
        /**
         * Returns the UpdateSeq that is incremented whenever the lens properties are
         * changed.  As long as this number remains the same, you may assume the lens
         * properties are unchanged.
         */
        """
        pass

    def getLensMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lens_mat(Lens self)
        
        /**
         * Returns the matrix that transforms from a point in front of the lens to a
         * point in space.
         */
        """
        pass

    def getLensMatInv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_lens_mat_inv(Lens self)
        
        /**
         * Returns the matrix that transforms from a point in space to a point in
         * front of the lens.
         */
        """
        pass

    def getMinFov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_min_fov(Lens self)
        
        /**
         * Returns the field of view of the narrowest dimension of the window.  See
         * set_min_fov().
         */
        """
        pass

    def getNear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_near(Lens self)
        
        /**
         * Returns the position of the near plane (or cylinder, sphere, whatever).
         */
        """
        pass

    def getNodalPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_nodal_point(Lens self)
        
        /**
         * Returns the center point of the lens: the point from which the lens is
         * viewing.
         */
        """
        pass

    def getProjectionMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_projection_mat(Lens self, int channel)
        
        /**
         * Returns the complete transformation matrix from a 3-d point in space to a
         * point on the film, if such a matrix exists, or the identity matrix if the
         * lens is nonlinear.
         */
        """
        pass

    def getProjectionMatInv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_projection_mat_inv(Lens self, int channel)
        
        /**
         * Returns the matrix that transforms from a 2-d point on the film to a 3-d
         * vector in space, if such a matrix exists.
         */
        """
        pass

    def getUpVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_up_vector(Lens self)
        
        /**
         * Returns the axis perpendicular to the camera's view vector that indicates
         * the "up" direction.
         */
        """
        pass

    def getVfov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vfov(Lens self)
        
        /**
         * Returns the vertical component of fov only.  See get_fov().
         */
        """
        pass

    def getViewHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_view_hpr(Lens self)
        
        /**
         * Returns the direction in which the lens is facing.
         */
        """
        pass

    def getViewMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_view_mat(Lens self)
        
        /**
         * Returns the direction in which the lens is facing.
         */
        """
        pass

    def getViewVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_view_vector(Lens self)
        
        /**
         * Returns the axis along which the lens is facing.
         */
        """
        pass

    def get_aspect_ratio(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aspect_ratio(Lens self)
        
        /**
         * Returns the aspect ratio of the Lens.  This is determined based on the
         * indicated film size; see set_film_size().
         */
        """
        pass

    def get_change_event(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_change_event(Lens self)
        
        /**
         * Returns the name of the event that will be generated whenever any
         * properties of this particular Lens have changed.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_convergence_distance(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_convergence_distance(Lens self)
        
        /**
         * See set_convergence_distance().
         */
        """
        pass

    def get_coordinate_system(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_coordinate_system(Lens self)
        
        /**
         * Returns the coordinate system that all 3-d computations are performed
         * within for this Lens.  Normally, this is CS_default.
         */
        """
        pass

    def get_custom_film_mat(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_custom_film_mat(Lens self)
        
        /**
         * Returns the custom_film_mat specified for the lens.
         */
        """
        pass

    def get_default_far(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_far()
        
        /**
         * Returns the default far plane distance that will be assigned to each newly-
         * created lens.  This is read from the Config.prc file.
         */
        """
        pass

    def get_default_near(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_near()
        
        /**
         * Returns the default near plane distance that will be assigned to each
         * newly-created lens.  This is read from the Config.prc file.
         */
        """
        pass

    def get_far(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_far(Lens self)
        
        /**
         * Returns the position of the far plane (or cylinder, sphere, whatever).
         */
        """
        pass

    def get_film_mat(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_film_mat(Lens self)
        
        /**
         * Returns the matrix that transforms from a point behind the lens to a point
         * on the film.
         */
        """
        pass

    def get_film_mat_inv(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_film_mat_inv(Lens self)
        
        /**
         * Returns the matrix that transforms from a point on the film to a point
         * behind the lens.
         */
        """
        pass

    def get_film_offset(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_film_offset(Lens self)
        
        /**
         * Returns the horizontal and vertical offset amounts of this Lens.  See
         * set_film_offset().
         */
        """
        pass

    def get_film_size(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_film_size(Lens self)
        
        /**
         * Returns the horizontal and vertical film size of the virtual film.  See
         * set_film_size().
         */
        """
        pass

    def get_focal_length(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_focal_length(Lens self)
        
        /**
         * Returns the focal length of the lens.  This may have been set explicitly by
         * a previous call to set_focal_length(), or it may be computed based on the
         * lens' fov and film_size.  For certain kinds of lenses, the focal length has
         * no meaning.
         */
        """
        pass

    def get_fov(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_fov(Lens self)
        
        /**
         * Returns the horizontal and vertical film size of the virtual film.  See
         * set_fov().
         */
        """
        pass

    def get_hfov(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hfov(Lens self)
        
        /**
         * Returns the horizontal component of fov only.  See get_fov().
         */
        """
        pass

    def get_interocular_distance(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_interocular_distance(Lens self)
        
        /**
         * See set_interocular_distance().
         */
        """
        pass

    def get_keystone(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keystone(Lens self)
        
        /**
         * Returns the keystone correction specified for the lens.
         */
        """
        pass

    def get_last_change(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_last_change(Lens self)
        
        /**
         * Returns the UpdateSeq that is incremented whenever the lens properties are
         * changed.  As long as this number remains the same, you may assume the lens
         * properties are unchanged.
         */
        """
        pass

    def get_lens_mat(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lens_mat(Lens self)
        
        /**
         * Returns the matrix that transforms from a point in front of the lens to a
         * point in space.
         */
        """
        pass

    def get_lens_mat_inv(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_lens_mat_inv(Lens self)
        
        /**
         * Returns the matrix that transforms from a point in space to a point in
         * front of the lens.
         */
        """
        pass

    def get_min_fov(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_min_fov(Lens self)
        
        /**
         * Returns the field of view of the narrowest dimension of the window.  See
         * set_min_fov().
         */
        """
        pass

    def get_near(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_near(Lens self)
        
        /**
         * Returns the position of the near plane (or cylinder, sphere, whatever).
         */
        """
        pass

    def get_nodal_point(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_nodal_point(Lens self)
        
        /**
         * Returns the center point of the lens: the point from which the lens is
         * viewing.
         */
        """
        pass

    def get_projection_mat(self, Lens_self, int_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_projection_mat(Lens self, int channel)
        
        /**
         * Returns the complete transformation matrix from a 3-d point in space to a
         * point on the film, if such a matrix exists, or the identity matrix if the
         * lens is nonlinear.
         */
        """
        pass

    def get_projection_mat_inv(self, Lens_self, int_channel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_projection_mat_inv(Lens self, int channel)
        
        /**
         * Returns the matrix that transforms from a 2-d point on the film to a 3-d
         * vector in space, if such a matrix exists.
         */
        """
        pass

    def get_up_vector(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_up_vector(Lens self)
        
        /**
         * Returns the axis perpendicular to the camera's view vector that indicates
         * the "up" direction.
         */
        """
        pass

    def get_vfov(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vfov(Lens self)
        
        /**
         * Returns the vertical component of fov only.  See get_fov().
         */
        """
        pass

    def get_view_hpr(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_view_hpr(Lens self)
        
        /**
         * Returns the direction in which the lens is facing.
         */
        """
        pass

    def get_view_mat(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_view_mat(Lens self)
        
        /**
         * Returns the direction in which the lens is facing.
         */
        """
        pass

    def get_view_vector(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_view_vector(Lens self)
        
        /**
         * Returns the axis along which the lens is facing.
         */
        """
        pass

    def isLinear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_linear(Lens self)
        
        /**
         * Returns true if the lens represents a linear projection (e.g.
         * PerspectiveLens, OrthographicLens), and therefore there is a valid matrix
         * returned by get_projection_mat(), or false otherwise.
         */
        """
        pass

    def isOrthographic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_orthographic(Lens self)
        
        /**
         * Returns true if the lens represents a orthographic projection (i.e.  it is
         * a OrthographicLens), false otherwise.
         */
        """
        pass

    def isPerspective(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_perspective(Lens self)
        
        /**
         * Returns true if the lens represents a perspective projection (i.e.  it is a
         * PerspectiveLens), false otherwise.
         */
        """
        pass

    def is_linear(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_linear(Lens self)
        
        /**
         * Returns true if the lens represents a linear projection (e.g.
         * PerspectiveLens, OrthographicLens), and therefore there is a valid matrix
         * returned by get_projection_mat(), or false otherwise.
         */
        """
        pass

    def is_orthographic(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_orthographic(Lens self)
        
        /**
         * Returns true if the lens represents a orthographic projection (i.e.  it is
         * a OrthographicLens), false otherwise.
         */
        """
        pass

    def is_perspective(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_perspective(Lens self)
        
        /**
         * Returns true if the lens represents a perspective projection (i.e.  it is a
         * PerspectiveLens), false otherwise.
         */
        """
        pass

    def makeBounds(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_bounds(Lens self)
        
        /**
         * Allocates and returns a new BoundingVolume that encloses the frustum used
         * for this kind of lens, if possible.  If a suitable bounding volume cannot
         * be created, returns NULL.
         */
        """
        pass

    def makeCopy(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_copy(Lens self)
        """
        pass

    def makeGeometry(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_geometry(const Lens self)
        
        /**
         * Allocates and returns a new Geom that can be rendered to show a visible
         * representation of the frustum used for this kind of lens, if it makes sense
         * to do so.  If a visible representation cannot be created, returns NULL.
         */
        """
        pass

    def make_bounds(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_bounds(Lens self)
        
        /**
         * Allocates and returns a new BoundingVolume that encloses the frustum used
         * for this kind of lens, if possible.  If a suitable bounding volume cannot
         * be created, returns NULL.
         */
        """
        pass

    def make_copy(self, Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_copy(Lens self)
        """
        pass

    def make_geometry(self, const_Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_geometry(const Lens self)
        
        /**
         * Allocates and returns a new Geom that can be rendered to show a visible
         * representation of the frustum used for this kind of lens, if it makes sense
         * to do so.  If a visible representation cannot be created, returns NULL.
         */
        """
        pass

    def output(self, Lens_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Lens self, ostream out)
        
        /**
         *
         */
        """
        pass

    def project(self, Lens_self, const_LPoint3f_point3d, LPoint3f_point2d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        project(Lens self, const LPoint3f point3d, LPoint3f point2d)
        project(Lens self, const LPoint3f point3d, LPoint2f point2d)
        
        /**
         * Given a 3-d point in space, determine the 2-d point this maps to, in the
         * range (-1,1) in both dimensions, where (0,0) is the center of the lens and
         * (-1,-1) is the lower-left corner.
         *
         * Returns true if the 3-d point is in front of the lens and within the
         * viewing frustum (in which case point2d is filled in), or false otherwise
         * (in which case point2d will be filled in with something, which may or may
         * not be meaningful).
         */
        
        /**
         * Given a 3-d point in space, determine the 2-d point this maps to, in the
         * range (-1,1) in both dimensions, where (0,0) is the center of the lens and
         * (-1,-1) is the lower-left corner.
         *
         * The z coordinate will also be set to a value in the range (-1, 1), where 1
         * represents a point on the near plane, and -1 represents a point on the far
         * plane.
         *
         * Returns true if the 3-d point is in front of the lens and within the
         * viewing frustum (in which case point2d is filled in), or false otherwise
         * (in which case point2d will be filled in with something, which may or may
         * not be meaningful).
         */
        """
        pass

    def recomputeAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        recompute_all(const Lens self)
        
        /**
         * Forces all internal parameters of the Lens to be recomputed.  Normally,
         * this should never need to be called; it is provided only to assist in
         * debugging.
         */
        """
        pass

    def recompute_all(self, const_Lens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute_all(const Lens self)
        
        /**
         * Forces all internal parameters of the Lens to be recomputed.  Normally,
         * this should never need to be called; it is provided only to assist in
         * debugging.
         */
        """
        pass

    def setAspectRatio(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_aspect_ratio(const Lens self, float aspect_ratio)
        
        /**
         * Sets the aspect ratio of the lens.  This is the ratio of the height to the
         * width of the generated image.  Setting this overrides the two-parameter fov
         * or film size setting.
         */
        """
        pass

    def setChangeEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_change_event(const Lens self, str event)
        
        /**
         * Sets the name of the event that will be generated whenever any properties
         * of the Lens have changed.  If this is not set for a particular lens, no
         * event will be generated.
         *
         * The event is thrown with one parameter, the lens itself.  This can be used
         * to automatically track changes to camera fov, etc.  in the application.
         */
        """
        pass

    def setConvergenceDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_convergence_distance(const Lens self, float convergence_distance)
        
        /**
         * Sets the distance between between the camera plane and the point in the
         * distance that the left and right eyes are both looking at.  This distance
         * is used to apply a stereo effect when the lens is rendered on a stereo
         * display region.  It only has an effect on a PerspectiveLens.
         *
         * This parameter must be greater than 0, but may be as large as you like.  It
         * controls the distance at which the two stereo images will appear to
         * converge, which is a normal property of stereo vision.  Normally this
         * should be set to the distance from the camera to the area of interest in
         * your scene.  Anything beyond this distance will appear to go into the
         * screen, and anything closer will appear to come out of the screen.  If you
         * want to simulate parallel stereo, set this to infinity.
         *
         * Note that this creates an off-axis frustum, which means that the lenses are
         * still pointing in the same direction, which is usually more desirable than
         * the more naive toe-in approach, where the two lenses are simply tilted
         * toward each other.
         *
         * Prior to Panda3D 1.9.0, the convergence was being calculated incorrectly.
         * It has since been corrected.  To restore the legacy behavior you can set
         * the stereo-lens-old-convergence variable to true.
         *
         * Also see set_interocular_distance(), which relates.
         */
        """
        pass

    def setCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_coordinate_system(const Lens self, int cs)
        
        /**
         * Specifies the coordinate system that all 3-d computations are performed
         * within for this Lens.  Normally, this is CS_default.
         */
        """
        pass

    def setCustomFilmMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_custom_film_mat(const Lens self, const LMatrix4f custom_film_mat)
        
        /**
         * Specifies a custom matrix to transform the points on the film after they
         * have been converted into nominal film space (-1 .. 1 in U and V).  This can
         * be used to introduce arbitrary scales, rotations, or other linear
         * transforms to the media plane.  This is normally a 2-d matrix, but a full
         * 4x4 matrix may be specified.  This is applied on top of any film size, lens
         * shift, and/or keystone correction.
         */
        """
        pass

    def setFar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_far(const Lens self, float far_distance)
        
        /**
         * Defines the position of the far plane (or cylinder, sphere, whatever).
         * Points farther from the lens than this may not be rendered.
         */
        """
        pass

    def setFilmOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_film_offset(const Lens self, const LVecBase2f film_offset)
        set_film_offset(const Lens self, float x, float y)
        
        /**
         * Sets the horizontal and vertical offset amounts of this Lens.  These are
         * both in the same units specified in set_film_size().
         *
         * This can be used to establish an off-axis lens.
         */
        
        /**
         * Sets the horizontal and vertical offset amounts of this Lens.  These are
         * both in the same units specified in set_film_size().
         *
         * This can be used to establish an off-axis lens.
         */
        """
        pass

    def setFilmSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_film_size(const Lens self, const LVecBase2f film_size)
        set_film_size(const Lens self, float width)
        set_film_size(const Lens self, float width, float height)
        
        /**
         * Sets the horizontal size of the film without changing its shape.  The
         * aspect ratio remains unchanged; this computes the vertical size of the film
         * to automatically maintain the aspect ratio.
         */
        
        /**
         * Sets the size and shape of the "film" within the lens.  This both
         * establishes the units used by calls like set_focal_length(), and
         * establishes the aspect ratio of the frame.
         *
         * In a physical camera, the field of view of a lens is determined by the
         * lens' focal length and by the size of the film area exposed by the lens.
         * For instance, a 35mm camera exposes a rectangle on the film about 24mm x
         * 36mm, which means a 50mm lens gives about a 40-degree horizontal field of
         * view.
         *
         * In the virtual camera, you may set the film size to any units here, and
         * specify a focal length in the same units to simulate the same effect.  Or,
         * you may ignore this parameter, and specify the field of view and aspect
         * ratio of the lens directly.
         */
        
        /**
         * Sets the size and shape of the "film" within the lens.  This both
         * establishes the units used by calls like set_focal_length(), and
         * establishes the aspect ratio of the frame.
         *
         * In a physical camera, the field of view of a lens is determined by the
         * lens' focal length and by the size of the film area exposed by the lens.
         * For instance, a 35mm camera exposes a rectangle on the film about 24mm x
         * 36mm, which means a 50mm lens gives about a 40-degree horizontal field of
         * view.
         *
         * In the virtual camera, you may set the film size to any units here, and
         * specify a focal length in the same units to simulate the same effect.  Or,
         * you may ignore this parameter, and specify the field of view and aspect
         * ratio of the lens directly.
         */
        """
        pass

    def setFocalLength(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_focal_length(const Lens self, float focal_length)
        
        /**
         * Sets the focal length of the lens.  This may adjust the field-of-view
         * correspondingly, and is an alternate way to specify field of view.
         *
         * For certain kinds of lenses (e.g.  OrthographicLens), the focal length has
         * no meaning.
         */
        """
        pass

    def setFov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_fov(const Lens self, const LVecBase2f fov)
        set_fov(const Lens self, float fov)
        set_fov(const Lens self, float hfov, float vfov)
        
        /**
         * Sets the horizontal field of view of the lens without changing the aspect
         * ratio.  The vertical field of view is adjusted to maintain the same aspect
         * ratio.
         */
        
        /**
         * Sets the field of view of the lens in both dimensions.  This establishes
         * both the field of view and the aspect ratio of the lens.  This is one way
         * to specify the field of view of a lens; set_focal_length() is another way.
         *
         * For certain kinds of lenses (like OrthoLens), the field of view has no
         * meaning.
         */
        
        /**
         * Sets the field of view of the lens in both dimensions.  This establishes
         * both the field of view and the aspect ratio of the lens.  This is one way
         * to specify the field of view of a lens; set_focal_length() is another way.
         *
         * For certain kinds of lenses (like OrthographicLens), the field of view has
         * no meaning.
         */
        """
        pass

    def setFrustumFromCorners(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_frustum_from_corners(const Lens self, const LVecBase3f ul, const LVecBase3f ur, const LVecBase3f ll, const LVecBase3f lr, int flags)
        
        /**
         * Sets up the lens to use the frustum defined by the four indicated points.
         * This is most useful for a PerspectiveLens, but it may be called for other
         * kinds of lenses as well.
         *
         * The frustum will be rooted at the origin (or by whatever translation might
         * have been specified in a previous call to set_view_mat).
         *
         * It is legal for the four points not to be arranged in a rectangle; if this
         * is the case, the frustum will be fitted as tightly as possible to cover all
         * four points.
         *
         * The flags parameter contains the union of one or more of the following bits
         * to control the behavior of this function:
         *
         * FC_roll - If this is included, the camera may be rotated so that its up
         * vector is perpendicular to the top line.  Otherwise, the standard up vector
         * is used.
         *
         * FC_camera_plane - This allows the camera plane to be adjusted to be as
         * nearly perpendicular to the center of the frustum as possible.  Without
         * this bit, the orientation camera plane is defined by position of the four
         * points (which should all be coplanar).  With this bit, the camera plane is
         * arbitrary, and may be chosen so that the four points do not themselves lie
         * in the camera plane (but the points will still be within the frustum).
         *
         * FC_off_axis - This allows the resulting frustum to be off-axis to get the
         * tightest possible fit.  Without this bit, the viewing axis will be centered
         * within the frustum, but there may be more wasted space along the edges.
         *
         * FC_aspect_ratio - This allows the frustum to be scaled non-proportionately
         * in the vertical and horizontal dimensions, if necessary, to get a tighter
         * fit.  Without this bit, the current aspect ratio will be preserved.
         *
         * FC_shear - This allows the frustum to be sheared, if necessary, to get the
         * tightest possible fit.  This may result in a parallelogram-based frustum,
         * which will give a slanted appearance to the rendered image.  Without this
         * bit, the frustum will be rectangle-based.
         *
         * In general, if 0 is passed in as the value for flags, the generated frustum
         * will be a loose fit but sane; if -1 is passed in, it will be a tighter fit
         * and possibly screwy.
         */
        """
        pass

    def setInterocularDistance(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_interocular_distance(const Lens self, float interocular_distance)
        
        /**
         * Sets the distance between the left and right eyes of a stereo camera.  This
         * distance is used to apply a stereo effect when the lens is rendered on a
         * stereo display region.  It only has an effect on a PerspectiveLens.
         *
         * The left eye and the right eye are each offset along the X axis by half of
         * this distance, so that this parameter specifies the total distance between
         * them.
         *
         * Also see set_convergence_distance(), which relates.
         */
        """
        pass

    def setKeystone(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_keystone(const Lens self, const LVecBase2f keystone)
        
        /**
         * Indicates the ratio of keystone correction to perform on the lens, in each
         * of three axes.  This will build a special non-affine scale factor into the
         * projection matrix that will compensate for keystoning of a projected image;
         * this can be used to compensate for a projector that for physical reasons
         * cannot be aimed directly at its screen.
         *
         * The default value is taken from the default-keystone Config variable.  0, 0
         * indicates no keystone correction; specify a small value (usually in the
         * range -1 .. 1) in either the x or y position to generate a keystone
         * correction in that axis.
         */
        """
        pass

    def setMinFov(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_min_fov(const Lens self, float min_fov)
        
        /**
         * Sets the field of view of the smallest dimension of the window.  If the
         * window is wider than it is tall, this specifies the vertical field of view;
         * if it is taller than it is wide, this specifies the horizontal field of
         * view.
         *
         * In many cases, this is preferable to setting either the horizontal or
         * vertical field of view explicitly.  Setting this parameter means that
         * pulling the window wider will widen the field of view, which is usually
         * what you expect to happen.
         */
        """
        pass

    def setNear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_near(const Lens self, float near_distance)
        
        /**
         * Defines the position of the near plane (or cylinder, sphere, whatever).
         * Points closer to the lens than this may not be rendered.
         */
        """
        pass

    def setNearFar(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_near_far(const Lens self, float near_distance, float far_distance)
        
        /**
         * Simultaneously changes the near and far planes.
         */
        """
        pass

    def setViewHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_view_hpr(const Lens self, const LVecBase3f view_hpr)
        set_view_hpr(const Lens self, float h, float p, float r)
        
        /**
         * Sets the direction in which the lens is facing.  Normally, this is down the
         * forward axis (usually the Y axis), but it may be rotated.  This is only one
         * way of specifying the rotation; you may also specify an explicit vector in
         * which to look, or you may give a complete transformation matrix.
         */
        
        /**
         * Sets the direction in which the lens is facing.  Normally, this is down the
         * forward axis (usually the Y axis), but it may be rotated.  This is only one
         * way of specifying the rotation; you may also specify an explicit vector in
         * which to look, or you may give a complete transformation matrix.
         */
        """
        pass

    def setViewMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_view_mat(const Lens self, const LMatrix4f view_mat)
        
        /**
         * Sets an arbitrary transformation on the lens.  This replaces the individual
         * transformation components like set_view_hpr().
         *
         * Setting a transformation here will have a slightly different effect than
         * putting one on the LensNode that contains this lens.  In particular,
         * lighting and other effects computations will still be performed on the lens
         * in its untransformed (facing forward) position, but the actual projection
         * matrix will be transformed by this matrix.
         */
        """
        pass

    def setViewVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_view_vector(const Lens self, const LVector3f view_vector, const LVector3f up_vector)
        set_view_vector(const Lens self, float x, float y, float z, float i, float j, float k)
        
        /**
         * Specifies the direction in which the lens is facing by giving an axis to
         * look along, and a perpendicular (or at least non-parallel) up axis.
         *
         * See also set_view_hpr().
         */
        
        /**
         * Specifies the direction in which the lens is facing by giving an axis to
         * look along, and a perpendicular (or at least non-parallel) up axis.
         *
         * See also set_view_hpr().
         */
        """
        pass

    def set_aspect_ratio(self, const_Lens_self, float_aspect_ratio): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_aspect_ratio(const Lens self, float aspect_ratio)
        
        /**
         * Sets the aspect ratio of the lens.  This is the ratio of the height to the
         * width of the generated image.  Setting this overrides the two-parameter fov
         * or film size setting.
         */
        """
        pass

    def set_change_event(self, const_Lens_self, str_event): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_change_event(const Lens self, str event)
        
        /**
         * Sets the name of the event that will be generated whenever any properties
         * of the Lens have changed.  If this is not set for a particular lens, no
         * event will be generated.
         *
         * The event is thrown with one parameter, the lens itself.  This can be used
         * to automatically track changes to camera fov, etc.  in the application.
         */
        """
        pass

    def set_convergence_distance(self, const_Lens_self, float_convergence_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_convergence_distance(const Lens self, float convergence_distance)
        
        /**
         * Sets the distance between between the camera plane and the point in the
         * distance that the left and right eyes are both looking at.  This distance
         * is used to apply a stereo effect when the lens is rendered on a stereo
         * display region.  It only has an effect on a PerspectiveLens.
         *
         * This parameter must be greater than 0, but may be as large as you like.  It
         * controls the distance at which the two stereo images will appear to
         * converge, which is a normal property of stereo vision.  Normally this
         * should be set to the distance from the camera to the area of interest in
         * your scene.  Anything beyond this distance will appear to go into the
         * screen, and anything closer will appear to come out of the screen.  If you
         * want to simulate parallel stereo, set this to infinity.
         *
         * Note that this creates an off-axis frustum, which means that the lenses are
         * still pointing in the same direction, which is usually more desirable than
         * the more naive toe-in approach, where the two lenses are simply tilted
         * toward each other.
         *
         * Prior to Panda3D 1.9.0, the convergence was being calculated incorrectly.
         * It has since been corrected.  To restore the legacy behavior you can set
         * the stereo-lens-old-convergence variable to true.
         *
         * Also see set_interocular_distance(), which relates.
         */
        """
        pass

    def set_coordinate_system(self, const_Lens_self, int_cs): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_coordinate_system(const Lens self, int cs)
        
        /**
         * Specifies the coordinate system that all 3-d computations are performed
         * within for this Lens.  Normally, this is CS_default.
         */
        """
        pass

    def set_custom_film_mat(self, const_Lens_self, const_LMatrix4f_custom_film_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_custom_film_mat(const Lens self, const LMatrix4f custom_film_mat)
        
        /**
         * Specifies a custom matrix to transform the points on the film after they
         * have been converted into nominal film space (-1 .. 1 in U and V).  This can
         * be used to introduce arbitrary scales, rotations, or other linear
         * transforms to the media plane.  This is normally a 2-d matrix, but a full
         * 4x4 matrix may be specified.  This is applied on top of any film size, lens
         * shift, and/or keystone correction.
         */
        """
        pass

    def set_far(self, const_Lens_self, float_far_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_far(const Lens self, float far_distance)
        
        /**
         * Defines the position of the far plane (or cylinder, sphere, whatever).
         * Points farther from the lens than this may not be rendered.
         */
        """
        pass

    def set_film_offset(self, const_Lens_self, const_LVecBase2f_film_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_film_offset(const Lens self, const LVecBase2f film_offset)
        set_film_offset(const Lens self, float x, float y)
        
        /**
         * Sets the horizontal and vertical offset amounts of this Lens.  These are
         * both in the same units specified in set_film_size().
         *
         * This can be used to establish an off-axis lens.
         */
        
        /**
         * Sets the horizontal and vertical offset amounts of this Lens.  These are
         * both in the same units specified in set_film_size().
         *
         * This can be used to establish an off-axis lens.
         */
        """
        pass

    def set_film_size(self, const_Lens_self, const_LVecBase2f_film_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_film_size(const Lens self, const LVecBase2f film_size)
        set_film_size(const Lens self, float width)
        set_film_size(const Lens self, float width, float height)
        
        /**
         * Sets the horizontal size of the film without changing its shape.  The
         * aspect ratio remains unchanged; this computes the vertical size of the film
         * to automatically maintain the aspect ratio.
         */
        
        /**
         * Sets the size and shape of the "film" within the lens.  This both
         * establishes the units used by calls like set_focal_length(), and
         * establishes the aspect ratio of the frame.
         *
         * In a physical camera, the field of view of a lens is determined by the
         * lens' focal length and by the size of the film area exposed by the lens.
         * For instance, a 35mm camera exposes a rectangle on the film about 24mm x
         * 36mm, which means a 50mm lens gives about a 40-degree horizontal field of
         * view.
         *
         * In the virtual camera, you may set the film size to any units here, and
         * specify a focal length in the same units to simulate the same effect.  Or,
         * you may ignore this parameter, and specify the field of view and aspect
         * ratio of the lens directly.
         */
        
        /**
         * Sets the size and shape of the "film" within the lens.  This both
         * establishes the units used by calls like set_focal_length(), and
         * establishes the aspect ratio of the frame.
         *
         * In a physical camera, the field of view of a lens is determined by the
         * lens' focal length and by the size of the film area exposed by the lens.
         * For instance, a 35mm camera exposes a rectangle on the film about 24mm x
         * 36mm, which means a 50mm lens gives about a 40-degree horizontal field of
         * view.
         *
         * In the virtual camera, you may set the film size to any units here, and
         * specify a focal length in the same units to simulate the same effect.  Or,
         * you may ignore this parameter, and specify the field of view and aspect
         * ratio of the lens directly.
         */
        """
        pass

    def set_focal_length(self, const_Lens_self, float_focal_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_focal_length(const Lens self, float focal_length)
        
        /**
         * Sets the focal length of the lens.  This may adjust the field-of-view
         * correspondingly, and is an alternate way to specify field of view.
         *
         * For certain kinds of lenses (e.g.  OrthographicLens), the focal length has
         * no meaning.
         */
        """
        pass

    def set_fov(self, const_Lens_self, const_LVecBase2f_fov): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_fov(const Lens self, const LVecBase2f fov)
        set_fov(const Lens self, float fov)
        set_fov(const Lens self, float hfov, float vfov)
        
        /**
         * Sets the horizontal field of view of the lens without changing the aspect
         * ratio.  The vertical field of view is adjusted to maintain the same aspect
         * ratio.
         */
        
        /**
         * Sets the field of view of the lens in both dimensions.  This establishes
         * both the field of view and the aspect ratio of the lens.  This is one way
         * to specify the field of view of a lens; set_focal_length() is another way.
         *
         * For certain kinds of lenses (like OrthoLens), the field of view has no
         * meaning.
         */
        
        /**
         * Sets the field of view of the lens in both dimensions.  This establishes
         * both the field of view and the aspect ratio of the lens.  This is one way
         * to specify the field of view of a lens; set_focal_length() is another way.
         *
         * For certain kinds of lenses (like OrthographicLens), the field of view has
         * no meaning.
         */
        """
        pass

    def set_frustum_from_corners(self, const_Lens_self, const_LVecBase3f_ul, const_LVecBase3f_ur, const_LVecBase3f_ll, const_LVecBase3f_lr, int_flags): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_frustum_from_corners(const Lens self, const LVecBase3f ul, const LVecBase3f ur, const LVecBase3f ll, const LVecBase3f lr, int flags)
        
        /**
         * Sets up the lens to use the frustum defined by the four indicated points.
         * This is most useful for a PerspectiveLens, but it may be called for other
         * kinds of lenses as well.
         *
         * The frustum will be rooted at the origin (or by whatever translation might
         * have been specified in a previous call to set_view_mat).
         *
         * It is legal for the four points not to be arranged in a rectangle; if this
         * is the case, the frustum will be fitted as tightly as possible to cover all
         * four points.
         *
         * The flags parameter contains the union of one or more of the following bits
         * to control the behavior of this function:
         *
         * FC_roll - If this is included, the camera may be rotated so that its up
         * vector is perpendicular to the top line.  Otherwise, the standard up vector
         * is used.
         *
         * FC_camera_plane - This allows the camera plane to be adjusted to be as
         * nearly perpendicular to the center of the frustum as possible.  Without
         * this bit, the orientation camera plane is defined by position of the four
         * points (which should all be coplanar).  With this bit, the camera plane is
         * arbitrary, and may be chosen so that the four points do not themselves lie
         * in the camera plane (but the points will still be within the frustum).
         *
         * FC_off_axis - This allows the resulting frustum to be off-axis to get the
         * tightest possible fit.  Without this bit, the viewing axis will be centered
         * within the frustum, but there may be more wasted space along the edges.
         *
         * FC_aspect_ratio - This allows the frustum to be scaled non-proportionately
         * in the vertical and horizontal dimensions, if necessary, to get a tighter
         * fit.  Without this bit, the current aspect ratio will be preserved.
         *
         * FC_shear - This allows the frustum to be sheared, if necessary, to get the
         * tightest possible fit.  This may result in a parallelogram-based frustum,
         * which will give a slanted appearance to the rendered image.  Without this
         * bit, the frustum will be rectangle-based.
         *
         * In general, if 0 is passed in as the value for flags, the generated frustum
         * will be a loose fit but sane; if -1 is passed in, it will be a tighter fit
         * and possibly screwy.
         */
        """
        pass

    def set_interocular_distance(self, const_Lens_self, float_interocular_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_interocular_distance(const Lens self, float interocular_distance)
        
        /**
         * Sets the distance between the left and right eyes of a stereo camera.  This
         * distance is used to apply a stereo effect when the lens is rendered on a
         * stereo display region.  It only has an effect on a PerspectiveLens.
         *
         * The left eye and the right eye are each offset along the X axis by half of
         * this distance, so that this parameter specifies the total distance between
         * them.
         *
         * Also see set_convergence_distance(), which relates.
         */
        """
        pass

    def set_keystone(self, const_Lens_self, const_LVecBase2f_keystone): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_keystone(const Lens self, const LVecBase2f keystone)
        
        /**
         * Indicates the ratio of keystone correction to perform on the lens, in each
         * of three axes.  This will build a special non-affine scale factor into the
         * projection matrix that will compensate for keystoning of a projected image;
         * this can be used to compensate for a projector that for physical reasons
         * cannot be aimed directly at its screen.
         *
         * The default value is taken from the default-keystone Config variable.  0, 0
         * indicates no keystone correction; specify a small value (usually in the
         * range -1 .. 1) in either the x or y position to generate a keystone
         * correction in that axis.
         */
        """
        pass

    def set_min_fov(self, const_Lens_self, float_min_fov): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_min_fov(const Lens self, float min_fov)
        
        /**
         * Sets the field of view of the smallest dimension of the window.  If the
         * window is wider than it is tall, this specifies the vertical field of view;
         * if it is taller than it is wide, this specifies the horizontal field of
         * view.
         *
         * In many cases, this is preferable to setting either the horizontal or
         * vertical field of view explicitly.  Setting this parameter means that
         * pulling the window wider will widen the field of view, which is usually
         * what you expect to happen.
         */
        """
        pass

    def set_near(self, const_Lens_self, float_near_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_near(const Lens self, float near_distance)
        
        /**
         * Defines the position of the near plane (or cylinder, sphere, whatever).
         * Points closer to the lens than this may not be rendered.
         */
        """
        pass

    def set_near_far(self, const_Lens_self, float_near_distance, float_far_distance): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_near_far(const Lens self, float near_distance, float far_distance)
        
        /**
         * Simultaneously changes the near and far planes.
         */
        """
        pass

    def set_view_hpr(self, const_Lens_self, const_LVecBase3f_view_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_view_hpr(const Lens self, const LVecBase3f view_hpr)
        set_view_hpr(const Lens self, float h, float p, float r)
        
        /**
         * Sets the direction in which the lens is facing.  Normally, this is down the
         * forward axis (usually the Y axis), but it may be rotated.  This is only one
         * way of specifying the rotation; you may also specify an explicit vector in
         * which to look, or you may give a complete transformation matrix.
         */
        
        /**
         * Sets the direction in which the lens is facing.  Normally, this is down the
         * forward axis (usually the Y axis), but it may be rotated.  This is only one
         * way of specifying the rotation; you may also specify an explicit vector in
         * which to look, or you may give a complete transformation matrix.
         */
        """
        pass

    def set_view_mat(self, const_Lens_self, const_LMatrix4f_view_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_view_mat(const Lens self, const LMatrix4f view_mat)
        
        /**
         * Sets an arbitrary transformation on the lens.  This replaces the individual
         * transformation components like set_view_hpr().
         *
         * Setting a transformation here will have a slightly different effect than
         * putting one on the LensNode that contains this lens.  In particular,
         * lighting and other effects computations will still be performed on the lens
         * in its untransformed (facing forward) position, but the actual projection
         * matrix will be transformed by this matrix.
         */
        """
        pass

    def set_view_vector(self, const_Lens_self, const_LVector3f_view_vector, const_LVector3f_up_vector): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_view_vector(const Lens self, const LVector3f view_vector, const LVector3f up_vector)
        set_view_vector(const Lens self, float x, float y, float z, float i, float j, float k)
        
        /**
         * Specifies the direction in which the lens is facing by giving an axis to
         * look along, and a perpendicular (or at least non-parallel) up axis.
         *
         * See also set_view_hpr().
         */
        
        /**
         * Specifies the direction in which the lens is facing by giving an axis to
         * look along, and a perpendicular (or at least non-parallel) up axis.
         *
         * See also set_view_hpr().
         */
        """
        pass

    def write(self, Lens_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(Lens self, ostream out, int indent_level)
        
        /**
         *
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    aspect_ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    change_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    convergence_distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    coordinate_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    far = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    film_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    film_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focal_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interocular_distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keystone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_fov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    near = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nodal_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    view_hpr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    view_mat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'FCAspectRatio': 8,
        'FCCameraPlane': 2,
        'FCKeystone': 32,
        'FCOffAxis': 4,
        'FCRoll': 1,
        'FCShear': 16,
        'FC_aspect_ratio': 8,
        'FC_camera_plane': 2,
        'FC_keystone': 32,
        'FC_off_axis': 4,
        'FC_roll': 1,
        'FC_shear': 16,
        'SCLeft': 1,
        'SCMono': 0,
        'SCRight': 2,
        'SCStereo': 3,
        'SC_left': 1,
        'SC_mono': 0,
        'SC_right': 2,
        'SC_stereo': 3,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Lens' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Lens' objects>"
        '__doc__': '/**\n * A base class for any number of different kinds of lenses, linear and\n * otherwise.  Presently, this includes perspective and orthographic lenses.\n *\n * A Lens object is the main part of a Camera node, which defines the\n * fundamental interface to point-of-view for rendering.  Lenses are also used\n * in other contexts, however; for instance, a Spotlight is also defined using\n * a lens.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Lens' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FF650>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.Lens' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Lens' objects>"
        'aspect_ratio': None, # (!) real value is "<attribute 'aspect_ratio' of 'panda3d.core.Lens' objects>"
        'change_event': None, # (!) real value is "<attribute 'change_event' of 'panda3d.core.Lens' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.Lens' objects>"
        'clearCustomFilmMat': None, # (!) real value is "<method 'clearCustomFilmMat' of 'panda3d.core.Lens' objects>"
        'clearKeystone': None, # (!) real value is "<method 'clearKeystone' of 'panda3d.core.Lens' objects>"
        'clearViewMat': None, # (!) real value is "<method 'clearViewMat' of 'panda3d.core.Lens' objects>"
        'clear_custom_film_mat': None, # (!) real value is "<method 'clear_custom_film_mat' of 'panda3d.core.Lens' objects>"
        'clear_keystone': None, # (!) real value is "<method 'clear_keystone' of 'panda3d.core.Lens' objects>"
        'clear_view_mat': None, # (!) real value is "<method 'clear_view_mat' of 'panda3d.core.Lens' objects>"
        'convergence_distance': None, # (!) real value is "<attribute 'convergence_distance' of 'panda3d.core.Lens' objects>"
        'coordinate_system': None, # (!) real value is "<attribute 'coordinate_system' of 'panda3d.core.Lens' objects>"
        'extrude': None, # (!) real value is "<method 'extrude' of 'panda3d.core.Lens' objects>"
        'extrudeDepth': None, # (!) real value is "<method 'extrudeDepth' of 'panda3d.core.Lens' objects>"
        'extrudeVec': None, # (!) real value is "<method 'extrudeVec' of 'panda3d.core.Lens' objects>"
        'extrude_depth': None, # (!) real value is "<method 'extrude_depth' of 'panda3d.core.Lens' objects>"
        'extrude_vec': None, # (!) real value is "<method 'extrude_vec' of 'panda3d.core.Lens' objects>"
        'far': None, # (!) real value is "<attribute 'far' of 'panda3d.core.Lens' objects>"
        'film_offset': None, # (!) real value is "<attribute 'film_offset' of 'panda3d.core.Lens' objects>"
        'film_size': None, # (!) real value is "<attribute 'film_size' of 'panda3d.core.Lens' objects>"
        'focal_length': None, # (!) real value is "<attribute 'focal_length' of 'panda3d.core.Lens' objects>"
        'fov': None, # (!) real value is "<attribute 'fov' of 'panda3d.core.Lens' objects>"
        'getAspectRatio': None, # (!) real value is "<method 'getAspectRatio' of 'panda3d.core.Lens' objects>"
        'getChangeEvent': None, # (!) real value is "<method 'getChangeEvent' of 'panda3d.core.Lens' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FF650>)>'
        'getConvergenceDistance': None, # (!) real value is "<method 'getConvergenceDistance' of 'panda3d.core.Lens' objects>"
        'getCoordinateSystem': None, # (!) real value is "<method 'getCoordinateSystem' of 'panda3d.core.Lens' objects>"
        'getCustomFilmMat': None, # (!) real value is "<method 'getCustomFilmMat' of 'panda3d.core.Lens' objects>"
        'getDefaultFar': None, # (!) real value is '<staticmethod(<built-in method getDefaultFar of type object at 0x00007FFCFE2FF650>)>'
        'getDefaultNear': None, # (!) real value is '<staticmethod(<built-in method getDefaultNear of type object at 0x00007FFCFE2FF650>)>'
        'getFar': None, # (!) real value is "<method 'getFar' of 'panda3d.core.Lens' objects>"
        'getFilmMat': None, # (!) real value is "<method 'getFilmMat' of 'panda3d.core.Lens' objects>"
        'getFilmMatInv': None, # (!) real value is "<method 'getFilmMatInv' of 'panda3d.core.Lens' objects>"
        'getFilmOffset': None, # (!) real value is "<method 'getFilmOffset' of 'panda3d.core.Lens' objects>"
        'getFilmSize': None, # (!) real value is "<method 'getFilmSize' of 'panda3d.core.Lens' objects>"
        'getFocalLength': None, # (!) real value is "<method 'getFocalLength' of 'panda3d.core.Lens' objects>"
        'getFov': None, # (!) real value is "<method 'getFov' of 'panda3d.core.Lens' objects>"
        'getHfov': None, # (!) real value is "<method 'getHfov' of 'panda3d.core.Lens' objects>"
        'getInterocularDistance': None, # (!) real value is "<method 'getInterocularDistance' of 'panda3d.core.Lens' objects>"
        'getKeystone': None, # (!) real value is "<method 'getKeystone' of 'panda3d.core.Lens' objects>"
        'getLastChange': None, # (!) real value is "<method 'getLastChange' of 'panda3d.core.Lens' objects>"
        'getLensMat': None, # (!) real value is "<method 'getLensMat' of 'panda3d.core.Lens' objects>"
        'getLensMatInv': None, # (!) real value is "<method 'getLensMatInv' of 'panda3d.core.Lens' objects>"
        'getMinFov': None, # (!) real value is "<method 'getMinFov' of 'panda3d.core.Lens' objects>"
        'getNear': None, # (!) real value is "<method 'getNear' of 'panda3d.core.Lens' objects>"
        'getNodalPoint': None, # (!) real value is "<method 'getNodalPoint' of 'panda3d.core.Lens' objects>"
        'getProjectionMat': None, # (!) real value is "<method 'getProjectionMat' of 'panda3d.core.Lens' objects>"
        'getProjectionMatInv': None, # (!) real value is "<method 'getProjectionMatInv' of 'panda3d.core.Lens' objects>"
        'getUpVector': None, # (!) real value is "<method 'getUpVector' of 'panda3d.core.Lens' objects>"
        'getVfov': None, # (!) real value is "<method 'getVfov' of 'panda3d.core.Lens' objects>"
        'getViewHpr': None, # (!) real value is "<method 'getViewHpr' of 'panda3d.core.Lens' objects>"
        'getViewMat': None, # (!) real value is "<method 'getViewMat' of 'panda3d.core.Lens' objects>"
        'getViewVector': None, # (!) real value is "<method 'getViewVector' of 'panda3d.core.Lens' objects>"
        'get_aspect_ratio': None, # (!) real value is "<method 'get_aspect_ratio' of 'panda3d.core.Lens' objects>"
        'get_change_event': None, # (!) real value is "<method 'get_change_event' of 'panda3d.core.Lens' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FF650>)>'
        'get_convergence_distance': None, # (!) real value is "<method 'get_convergence_distance' of 'panda3d.core.Lens' objects>"
        'get_coordinate_system': None, # (!) real value is "<method 'get_coordinate_system' of 'panda3d.core.Lens' objects>"
        'get_custom_film_mat': None, # (!) real value is "<method 'get_custom_film_mat' of 'panda3d.core.Lens' objects>"
        'get_default_far': None, # (!) real value is '<staticmethod(<built-in method get_default_far of type object at 0x00007FFCFE2FF650>)>'
        'get_default_near': None, # (!) real value is '<staticmethod(<built-in method get_default_near of type object at 0x00007FFCFE2FF650>)>'
        'get_far': None, # (!) real value is "<method 'get_far' of 'panda3d.core.Lens' objects>"
        'get_film_mat': None, # (!) real value is "<method 'get_film_mat' of 'panda3d.core.Lens' objects>"
        'get_film_mat_inv': None, # (!) real value is "<method 'get_film_mat_inv' of 'panda3d.core.Lens' objects>"
        'get_film_offset': None, # (!) real value is "<method 'get_film_offset' of 'panda3d.core.Lens' objects>"
        'get_film_size': None, # (!) real value is "<method 'get_film_size' of 'panda3d.core.Lens' objects>"
        'get_focal_length': None, # (!) real value is "<method 'get_focal_length' of 'panda3d.core.Lens' objects>"
        'get_fov': None, # (!) real value is "<method 'get_fov' of 'panda3d.core.Lens' objects>"
        'get_hfov': None, # (!) real value is "<method 'get_hfov' of 'panda3d.core.Lens' objects>"
        'get_interocular_distance': None, # (!) real value is "<method 'get_interocular_distance' of 'panda3d.core.Lens' objects>"
        'get_keystone': None, # (!) real value is "<method 'get_keystone' of 'panda3d.core.Lens' objects>"
        'get_last_change': None, # (!) real value is "<method 'get_last_change' of 'panda3d.core.Lens' objects>"
        'get_lens_mat': None, # (!) real value is "<method 'get_lens_mat' of 'panda3d.core.Lens' objects>"
        'get_lens_mat_inv': None, # (!) real value is "<method 'get_lens_mat_inv' of 'panda3d.core.Lens' objects>"
        'get_min_fov': None, # (!) real value is "<method 'get_min_fov' of 'panda3d.core.Lens' objects>"
        'get_near': None, # (!) real value is "<method 'get_near' of 'panda3d.core.Lens' objects>"
        'get_nodal_point': None, # (!) real value is "<method 'get_nodal_point' of 'panda3d.core.Lens' objects>"
        'get_projection_mat': None, # (!) real value is "<method 'get_projection_mat' of 'panda3d.core.Lens' objects>"
        'get_projection_mat_inv': None, # (!) real value is "<method 'get_projection_mat_inv' of 'panda3d.core.Lens' objects>"
        'get_up_vector': None, # (!) real value is "<method 'get_up_vector' of 'panda3d.core.Lens' objects>"
        'get_vfov': None, # (!) real value is "<method 'get_vfov' of 'panda3d.core.Lens' objects>"
        'get_view_hpr': None, # (!) real value is "<method 'get_view_hpr' of 'panda3d.core.Lens' objects>"
        'get_view_mat': None, # (!) real value is "<method 'get_view_mat' of 'panda3d.core.Lens' objects>"
        'get_view_vector': None, # (!) real value is "<method 'get_view_vector' of 'panda3d.core.Lens' objects>"
        'interocular_distance': None, # (!) real value is "<attribute 'interocular_distance' of 'panda3d.core.Lens' objects>"
        'isLinear': None, # (!) real value is "<method 'isLinear' of 'panda3d.core.Lens' objects>"
        'isOrthographic': None, # (!) real value is "<method 'isOrthographic' of 'panda3d.core.Lens' objects>"
        'isPerspective': None, # (!) real value is "<method 'isPerspective' of 'panda3d.core.Lens' objects>"
        'is_linear': None, # (!) real value is "<method 'is_linear' of 'panda3d.core.Lens' objects>"
        'is_orthographic': None, # (!) real value is "<method 'is_orthographic' of 'panda3d.core.Lens' objects>"
        'is_perspective': None, # (!) real value is "<method 'is_perspective' of 'panda3d.core.Lens' objects>"
        'keystone': None, # (!) real value is "<attribute 'keystone' of 'panda3d.core.Lens' objects>"
        'makeBounds': None, # (!) real value is "<method 'makeBounds' of 'panda3d.core.Lens' objects>"
        'makeCopy': None, # (!) real value is "<method 'makeCopy' of 'panda3d.core.Lens' objects>"
        'makeGeometry': None, # (!) real value is "<method 'makeGeometry' of 'panda3d.core.Lens' objects>"
        'make_bounds': None, # (!) real value is "<method 'make_bounds' of 'panda3d.core.Lens' objects>"
        'make_copy': None, # (!) real value is "<method 'make_copy' of 'panda3d.core.Lens' objects>"
        'make_geometry': None, # (!) real value is "<method 'make_geometry' of 'panda3d.core.Lens' objects>"
        'min_fov': None, # (!) real value is "<attribute 'min_fov' of 'panda3d.core.Lens' objects>"
        'near': None, # (!) real value is "<attribute 'near' of 'panda3d.core.Lens' objects>"
        'nodal_point': None, # (!) real value is "<attribute 'nodal_point' of 'panda3d.core.Lens' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.Lens' objects>"
        'project': None, # (!) real value is "<method 'project' of 'panda3d.core.Lens' objects>"
        'recomputeAll': None, # (!) real value is "<method 'recomputeAll' of 'panda3d.core.Lens' objects>"
        'recompute_all': None, # (!) real value is "<method 'recompute_all' of 'panda3d.core.Lens' objects>"
        'setAspectRatio': None, # (!) real value is "<method 'setAspectRatio' of 'panda3d.core.Lens' objects>"
        'setChangeEvent': None, # (!) real value is "<method 'setChangeEvent' of 'panda3d.core.Lens' objects>"
        'setConvergenceDistance': None, # (!) real value is "<method 'setConvergenceDistance' of 'panda3d.core.Lens' objects>"
        'setCoordinateSystem': None, # (!) real value is "<method 'setCoordinateSystem' of 'panda3d.core.Lens' objects>"
        'setCustomFilmMat': None, # (!) real value is "<method 'setCustomFilmMat' of 'panda3d.core.Lens' objects>"
        'setFar': None, # (!) real value is "<method 'setFar' of 'panda3d.core.Lens' objects>"
        'setFilmOffset': None, # (!) real value is "<method 'setFilmOffset' of 'panda3d.core.Lens' objects>"
        'setFilmSize': None, # (!) real value is "<method 'setFilmSize' of 'panda3d.core.Lens' objects>"
        'setFocalLength': None, # (!) real value is "<method 'setFocalLength' of 'panda3d.core.Lens' objects>"
        'setFov': None, # (!) real value is "<method 'setFov' of 'panda3d.core.Lens' objects>"
        'setFrustumFromCorners': None, # (!) real value is "<method 'setFrustumFromCorners' of 'panda3d.core.Lens' objects>"
        'setInterocularDistance': None, # (!) real value is "<method 'setInterocularDistance' of 'panda3d.core.Lens' objects>"
        'setKeystone': None, # (!) real value is "<method 'setKeystone' of 'panda3d.core.Lens' objects>"
        'setMinFov': None, # (!) real value is "<method 'setMinFov' of 'panda3d.core.Lens' objects>"
        'setNear': None, # (!) real value is "<method 'setNear' of 'panda3d.core.Lens' objects>"
        'setNearFar': None, # (!) real value is "<method 'setNearFar' of 'panda3d.core.Lens' objects>"
        'setViewHpr': None, # (!) real value is "<method 'setViewHpr' of 'panda3d.core.Lens' objects>"
        'setViewMat': None, # (!) real value is "<method 'setViewMat' of 'panda3d.core.Lens' objects>"
        'setViewVector': None, # (!) real value is "<method 'setViewVector' of 'panda3d.core.Lens' objects>"
        'set_aspect_ratio': None, # (!) real value is "<method 'set_aspect_ratio' of 'panda3d.core.Lens' objects>"
        'set_change_event': None, # (!) real value is "<method 'set_change_event' of 'panda3d.core.Lens' objects>"
        'set_convergence_distance': None, # (!) real value is "<method 'set_convergence_distance' of 'panda3d.core.Lens' objects>"
        'set_coordinate_system': None, # (!) real value is "<method 'set_coordinate_system' of 'panda3d.core.Lens' objects>"
        'set_custom_film_mat': None, # (!) real value is "<method 'set_custom_film_mat' of 'panda3d.core.Lens' objects>"
        'set_far': None, # (!) real value is "<method 'set_far' of 'panda3d.core.Lens' objects>"
        'set_film_offset': None, # (!) real value is "<method 'set_film_offset' of 'panda3d.core.Lens' objects>"
        'set_film_size': None, # (!) real value is "<method 'set_film_size' of 'panda3d.core.Lens' objects>"
        'set_focal_length': None, # (!) real value is "<method 'set_focal_length' of 'panda3d.core.Lens' objects>"
        'set_fov': None, # (!) real value is "<method 'set_fov' of 'panda3d.core.Lens' objects>"
        'set_frustum_from_corners': None, # (!) real value is "<method 'set_frustum_from_corners' of 'panda3d.core.Lens' objects>"
        'set_interocular_distance': None, # (!) real value is "<method 'set_interocular_distance' of 'panda3d.core.Lens' objects>"
        'set_keystone': None, # (!) real value is "<method 'set_keystone' of 'panda3d.core.Lens' objects>"
        'set_min_fov': None, # (!) real value is "<method 'set_min_fov' of 'panda3d.core.Lens' objects>"
        'set_near': None, # (!) real value is "<method 'set_near' of 'panda3d.core.Lens' objects>"
        'set_near_far': None, # (!) real value is "<method 'set_near_far' of 'panda3d.core.Lens' objects>"
        'set_view_hpr': None, # (!) real value is "<method 'set_view_hpr' of 'panda3d.core.Lens' objects>"
        'set_view_mat': None, # (!) real value is "<method 'set_view_mat' of 'panda3d.core.Lens' objects>"
        'set_view_vector': None, # (!) real value is "<method 'set_view_vector' of 'panda3d.core.Lens' objects>"
        'view_hpr': None, # (!) real value is "<attribute 'view_hpr' of 'panda3d.core.Lens' objects>"
        'view_mat': None, # (!) real value is "<attribute 'view_mat' of 'panda3d.core.Lens' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.Lens' objects>"
    }
    FCAspectRatio = 8
    FCCameraPlane = 2
    FCKeystone = 32
    FCOffAxis = 4
    FCRoll = 1
    FCShear = 16
    FC_aspect_ratio = 8
    FC_camera_plane = 2
    FC_keystone = 32
    FC_off_axis = 4
    FC_roll = 1
    FC_shear = 16
    SCLeft = 1
    SCMono = 0
    SCRight = 2
    SCStereo = 3
    SC_left = 1
    SC_mono = 0
    SC_right = 2
    SC_stereo = 3


