# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class PfmVizzer(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class aids in the visualization and manipulation of PfmFile objects.
     */
    """
    def addVisColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_vis_column(const PfmVizzer self, int source, int target, InternalName name, const TransformState transform, const Lens lens, const PfmFile undist_lut)
        
        /**
         * Adds a new vis column specification to the list of vertex data columns that
         * will be generated at the next call to generate_vis_points() or
         * generate_vis_mesh().  This advanced interface supercedes the higher-level
         * set_vis_inverse(), set_flat_texcoord_name(), and set_vis_2d().
         *
         * If you use this advanced interface, you must specify explicitly the
         * complete list of data columns to be created in the resulting
         * GeomVertexData, by calling add_vis_column() each time.  For each column,
         * you specify the source of the column in the PFMFile, the target column and
         * name in the GeomVertexData, and an optional transform matrix and/or lens to
         * transform and project the point before generating it.
         */
        
        /**
         * The private implementation of the public add_vis_column(), this adds the
         * column to the indicated specific vector.
         */
        """
        pass

    def add_vis_column(self, const_PfmVizzer_self, int_source, int_target, InternalName_name, const_TransformState_transform, const_Lens_lens, const_PfmFile_undist_lut): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_vis_column(const PfmVizzer self, int source, int target, InternalName name, const TransformState transform, const Lens lens, const PfmFile undist_lut)
        
        /**
         * Adds a new vis column specification to the list of vertex data columns that
         * will be generated at the next call to generate_vis_points() or
         * generate_vis_mesh().  This advanced interface supercedes the higher-level
         * set_vis_inverse(), set_flat_texcoord_name(), and set_vis_2d().
         *
         * If you use this advanced interface, you must specify explicitly the
         * complete list of data columns to be created in the resulting
         * GeomVertexData, by calling add_vis_column() each time.  For each column,
         * you specify the source of the column in the PFMFile, the target column and
         * name in the GeomVertexData, and an optional transform matrix and/or lens to
         * transform and project the point before generating it.
         */
        
        /**
         * The private implementation of the public add_vis_column(), this adds the
         * column to the indicated specific vector.
         */
        """
        pass

    def calcMaxUDisplacement(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_max_u_displacement(PfmVizzer self)
        
        /**
         * Computes the maximum amount of shift, in pixels either left or right, of
         * any pixel in the distortion map.  This can be passed to
         * make_displacement(); see that function for more information.
         */
        """
        pass

    def calcMaxVDisplacement(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        calc_max_v_displacement(PfmVizzer self)
        
        /**
         * Computes the maximum amount of shift, in pixels either up or down, of any
         * pixel in the distortion map.  This can be passed to make_displacement();
         * see that function for more information.
         */
        """
        pass

    def calc_max_u_displacement(self, PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_max_u_displacement(PfmVizzer self)
        
        /**
         * Computes the maximum amount of shift, in pixels either left or right, of
         * any pixel in the distortion map.  This can be passed to
         * make_displacement(); see that function for more information.
         */
        """
        pass

    def calc_max_v_displacement(self, PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        calc_max_v_displacement(PfmVizzer self)
        
        /**
         * Computes the maximum amount of shift, in pixels either up or down, of any
         * pixel in the distortion map.  This can be passed to make_displacement();
         * see that function for more information.
         */
        """
        pass

    def clearAuxPfm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_aux_pfm(const PfmVizzer self)
        
        /**
         * Removes the auxiliary PfmFile from this PfmVizzer.
         */
        """
        pass

    def clearFlatTexcoordName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_flat_texcoord_name(const PfmVizzer self)
        
        /**
         * Resets the flat_texcoord_name to empty, so that additional texture
         * coordinates are not created.
         *
         * This may be used in lieu of the lower-level add_vis_column().
         */
        """
        pass

    def clearVisBlend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_vis_blend(const PfmVizzer self)
        
        /**
         * Removes the blending map set by a prior call to set_vis_blend().
         */
        """
        pass

    def clearVisColumns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_vis_columns(const PfmVizzer self)
        
        /**
         * Removes all of the previously-added vis columns in preparation for building
         * a new list.  See add_vis_column().
         */
        """
        pass

    def clear_aux_pfm(self, const_PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_aux_pfm(const PfmVizzer self)
        
        /**
         * Removes the auxiliary PfmFile from this PfmVizzer.
         */
        """
        pass

    def clear_flat_texcoord_name(self, const_PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_flat_texcoord_name(const PfmVizzer self)
        
        /**
         * Resets the flat_texcoord_name to empty, so that additional texture
         * coordinates are not created.
         *
         * This may be used in lieu of the lower-level add_vis_column().
         */
        """
        pass

    def clear_vis_blend(self, const_PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_vis_blend(const PfmVizzer self)
        
        /**
         * Removes the blending map set by a prior call to set_vis_blend().
         */
        """
        pass

    def clear_vis_columns(self, const_PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_vis_columns(const PfmVizzer self)
        
        /**
         * Removes all of the previously-added vis columns in preparation for building
         * a new list.  See add_vis_column().
         */
        """
        pass

    def extrude(self, const_PfmVizzer_self, const_Lens_lens): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        extrude(const PfmVizzer self, const Lens lens)
        
        /**
         * Converts each (u, v, depth) point of the Pfm file to an (x, y, z) point, by
         * reversing project().  If the original file is only a 1-d file, assumes that
         * it is a depth map with implicit (u, v) coordinates.
         *
         * This method is only valid for a linear lens (e.g.  a PerspectiveLens or
         * OrthographicLens).  Non-linear lenses don't necessarily compute a sensible
         * depth coordinate.
         */
        """
        pass

    def generateVisMesh(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_vis_mesh(PfmVizzer self, int face)
        
        /**
         * Creates a triangle mesh with the points of the pfm as 3-d coordinates in
         * space, and texture coordinates ranging from 0 .. 1 based on the position
         * within the pfm grid.
         */
        """
        pass

    def generateVisPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        generate_vis_points(PfmVizzer self)
        
        /**
         * Creates a point cloud with the points of the pfm as 3-d coordinates in
         * space, and texture coordinates ranging from 0 .. 1 based on the position
         * within the pfm grid.
         */
        """
        pass

    def generate_vis_mesh(self, PfmVizzer_self, int_face): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_vis_mesh(PfmVizzer self, int face)
        
        /**
         * Creates a triangle mesh with the points of the pfm as 3-d coordinates in
         * space, and texture coordinates ranging from 0 .. 1 based on the position
         * within the pfm grid.
         */
        """
        pass

    def generate_vis_points(self, PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        generate_vis_points(PfmVizzer self)
        
        /**
         * Creates a point cloud with the points of the pfm as 3-d coordinates in
         * space, and texture coordinates ranging from 0 .. 1 based on the position
         * within the pfm grid.
         */
        """
        pass

    def getAuxPfm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aux_pfm(PfmVizzer self)
        
        /**
         * Returns the reference to the auxiliary PfmFile queried by this PfmVizzer.
         * This contains the values that will be reflected in CT_aux_vertex3 etc.  See
         * set_aux_pfm().
         */
        """
        pass

    def getFlatTexcoordName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flat_texcoord_name(PfmVizzer self)
        
        /**
         * Returns the flat_texcoord_name.  See set_flat_texcoord_name().
         */
        """
        pass

    def getKeepBeyondLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keep_beyond_lens(PfmVizzer self)
        
        /**
         * Returns the keep_beyond_lens flag.  See set_keep_beyond_lens().
         */
        """
        pass

    def getPfm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pfm(const PfmVizzer self)
        get_pfm(PfmVizzer self)
        
        /**
         * Returns the reference to the PfmFile manipulated by this PfmVizzer.
         */
        
        /**
         * Returns the reference to the PfmFile manipulated by this PfmVizzer.
         */
        """
        pass

    def getVis2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vis_2d(PfmVizzer self)
        
        /**
         * Returns the vis_2d flag.  See set_vis_2d().
         */
        """
        pass

    def getVisBlend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vis_blend(PfmVizzer self)
        
        /**
         * Returns the blending map set by the most recent call to set_vis_blend(), or
         * NULL if there is no blending map in effect.
         */
        """
        pass

    def getVisInverse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vis_inverse(PfmVizzer self)
        
        /**
         * Returns the vis_inverse flag.  See set_vis_inverse().
         */
        """
        pass

    def get_aux_pfm(self, PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aux_pfm(PfmVizzer self)
        
        /**
         * Returns the reference to the auxiliary PfmFile queried by this PfmVizzer.
         * This contains the values that will be reflected in CT_aux_vertex3 etc.  See
         * set_aux_pfm().
         */
        """
        pass

    def get_flat_texcoord_name(self, PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flat_texcoord_name(PfmVizzer self)
        
        /**
         * Returns the flat_texcoord_name.  See set_flat_texcoord_name().
         */
        """
        pass

    def get_keep_beyond_lens(self, PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keep_beyond_lens(PfmVizzer self)
        
        /**
         * Returns the keep_beyond_lens flag.  See set_keep_beyond_lens().
         */
        """
        pass

    def get_pfm(self, const_PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pfm(const PfmVizzer self)
        get_pfm(PfmVizzer self)
        
        /**
         * Returns the reference to the PfmFile manipulated by this PfmVizzer.
         */
        
        /**
         * Returns the reference to the PfmFile manipulated by this PfmVizzer.
         */
        """
        pass

    def get_vis_2d(self, PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vis_2d(PfmVizzer self)
        
        /**
         * Returns the vis_2d flag.  See set_vis_2d().
         */
        """
        pass

    def get_vis_blend(self, PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vis_blend(PfmVizzer self)
        
        /**
         * Returns the blending map set by the most recent call to set_vis_blend(), or
         * NULL if there is no blending map in effect.
         */
        """
        pass

    def get_vis_inverse(self, PfmVizzer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vis_inverse(PfmVizzer self)
        
        /**
         * Returns the vis_inverse flag.  See set_vis_inverse().
         */
        """
        pass

    def makeDisplacement(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_displacement(PfmVizzer self, PNMImage result, double max_u, double max_v, bool for_32bit)
        make_displacement(PfmVizzer self, PfmFile result, double max_u, double max_v, bool for_32bit)
        
        /**
         * Assuming the underlying PfmFile is a 2-d distortion mesh, with the U and V
         * in the first two components and the third component unused, this computes
         * an AfterEffects-style displacement map that represents the same distortion.
         * The indicated PNMImage will be filled in with a displacement map image,
         * with horizontal shift in the red channel and vertical shift in the green
         * channel, where a fully bright (or fully black) pixel indicates a shift of
         * max_u or max_v pixels.
         *
         * Use calc_max_u_displacement() and calc_max_v_displacement() to compute
         * suitable values for max_u and max_v.
         *
         * This generates an integer 16-bit displacement image.  It is a good idea,
         * though not necessarily essential, to check "Preserve RGB" in the interpret
         * footage section for each displacement image.  Set for_32bit true if this is
         * meant to be used in a 32-bit project file, and false if it is meant to be
         * used in a 16-bit project file.
         */
        
        /**
         * Assuming the underlying PfmFile is a 2-d distortion mesh, with the U and V
         * in the first two components and the third component unused, this computes
         * an AfterEffects-style displacement map that represents the same distortion.
         * The indicated PNMImage will be filled in with a displacement map image,
         * with horizontal shift in the red channel and vertical shift in the green
         * channel, where a fully bright (or fully black) pixel indicates a shift of
         * max_u or max_v pixels.
         *
         * Use calc_max_u_displacement() and calc_max_v_displacement() to compute
         * suitable values for max_u and max_v.
         *
         * This generates a 32-bit floating-point displacement image.  It is essential
         * to check "Preserve RGB" in the interpret footage section for each
         * displacement image.  Set for_32bit true if this is meant to be used in a
         * 32-bit project file, and false if it is meant to be used in a 16-bit
         * project file.
         */
        """
        pass

    def make_displacement(self, PfmVizzer_self, PNMImage_result, double_max_u, double_max_v, bool_for_32bit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_displacement(PfmVizzer self, PNMImage result, double max_u, double max_v, bool for_32bit)
        make_displacement(PfmVizzer self, PfmFile result, double max_u, double max_v, bool for_32bit)
        
        /**
         * Assuming the underlying PfmFile is a 2-d distortion mesh, with the U and V
         * in the first two components and the third component unused, this computes
         * an AfterEffects-style displacement map that represents the same distortion.
         * The indicated PNMImage will be filled in with a displacement map image,
         * with horizontal shift in the red channel and vertical shift in the green
         * channel, where a fully bright (or fully black) pixel indicates a shift of
         * max_u or max_v pixels.
         *
         * Use calc_max_u_displacement() and calc_max_v_displacement() to compute
         * suitable values for max_u and max_v.
         *
         * This generates an integer 16-bit displacement image.  It is a good idea,
         * though not necessarily essential, to check "Preserve RGB" in the interpret
         * footage section for each displacement image.  Set for_32bit true if this is
         * meant to be used in a 32-bit project file, and false if it is meant to be
         * used in a 16-bit project file.
         */
        
        /**
         * Assuming the underlying PfmFile is a 2-d distortion mesh, with the U and V
         * in the first two components and the third component unused, this computes
         * an AfterEffects-style displacement map that represents the same distortion.
         * The indicated PNMImage will be filled in with a displacement map image,
         * with horizontal shift in the red channel and vertical shift in the green
         * channel, where a fully bright (or fully black) pixel indicates a shift of
         * max_u or max_v pixels.
         *
         * Use calc_max_u_displacement() and calc_max_v_displacement() to compute
         * suitable values for max_u and max_v.
         *
         * This generates a 32-bit floating-point displacement image.  It is essential
         * to check "Preserve RGB" in the interpret footage section for each
         * displacement image.  Set for_32bit true if this is meant to be used in a
         * 32-bit project file, and false if it is meant to be used in a 16-bit
         * project file.
         */
        """
        pass

    def project(self, const_PfmVizzer_self, const_Lens_lens, const_PfmFile_undist_lut): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        project(const PfmVizzer self, const Lens lens, const PfmFile undist_lut)
        
        /**
         * Adjusts each (x, y, z) point of the Pfm file by projecting it through the
         * indicated lens, converting each point to a (u, v, w) texture coordinate.
         * The resulting file can be generated to a mesh (with set_vis_inverse(true)
         * and generate_vis_mesh()) that will apply the lens distortion to an
         * arbitrary texture image.
         */
        """
        pass

    def setAuxPfm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_aux_pfm(const PfmVizzer self, const PfmFile pfm)
        
        /**
         * Assigns an auxiliary PfmFile to this PfmVizzer.  This file will be queried
         * by column types CT_aux_vertex1/2/3, but has no other meaning to the vizzer.
         * This size of this PfmFile should exactly match the base PfmFile.  No
         * reference count is held and no copy is made; the caller is responsible for
         * ensuring that the auxiliary PfmFile will persist throughout the lifetime of
         * the PfmVizzer it is assigned to.
         */
        """
        pass

    def setFlatTexcoordName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_flat_texcoord_name(const PfmVizzer self, InternalName flat_texcoord_name)
        
        /**
         * If the flat_texcoord_name is specified, it is the name of an additional
         * vertex column that will be created for the "flat" texture coordinates, i.e.
         * the original 0..1 values that correspond to the 2-D index position of each
         * point in the original pfm file.
         *
         * These are the same values that will be assigned to the default texture
         * coordinates if the vis_inverse flag is *not* true.
         *
         * This may be used in lieu of the lower-level add_vis_column().
         */
        """
        pass

    def setKeepBeyondLens(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_keep_beyond_lens(const PfmVizzer self, bool keep_beyond_lens)
        
        /**
         * Sets the keep_beyond_lens flag.  When this flag is true, points that fall
         * outside of the normal lens range in project() or in add_vis_column() will
         * be retained anyway; when it is false, these points will be discarded.
         */
        """
        pass

    def setVis2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vis_2d(const PfmVizzer self, bool vis_2d)
        
        /**
         * Sets the vis_2d flag.  When this flag is true, only the first two (x, y)
         * value of each depth point is considered meaningful; the z component is
         * ignored.  This is only relevant for generating visualizations.
         *
         * This may be used in lieu of the lower-level add_vis_column().
         */
        """
        pass

    def setVisBlend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vis_blend(const PfmVizzer self, const PNMImage vis_blend)
        
        /**
         * Specifies a blending map--a grayscale image--that will be applied to the
         * vertex color during generate_vis_mesh() and generate_vis_points().  The
         * image size must exactly match the mesh size of the PfmVizzer.
         *
         * Ownership of the pointer is not kept by the PfmVizzer; it is your
         * responsibility to ensure it does not destruct during the lifetime of the
         * PfmVizzer (or at least not before your subsequent call to
         * generate_vis_mesh()).
         */
        """
        pass

    def setVisInverse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vis_inverse(const PfmVizzer self, bool vis_inverse)
        
        /**
         * Sets the vis_inverse flag.  When this flag is true, vis meshes and point
         * clouds are generated with the 3-d depth value in the texture coordinates,
         * and the 2-d index value in the vertex position.  When it is false, meshes
         * are generated normally, with the 3-d depth value in the vertex position and
         * the 2-d index value in the texture coordinates.
         *
         * This may be used in lieu of the lower-level add_vis_column().
         */
        """
        pass

    def set_aux_pfm(self, const_PfmVizzer_self, const_PfmFile_pfm): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_aux_pfm(const PfmVizzer self, const PfmFile pfm)
        
        /**
         * Assigns an auxiliary PfmFile to this PfmVizzer.  This file will be queried
         * by column types CT_aux_vertex1/2/3, but has no other meaning to the vizzer.
         * This size of this PfmFile should exactly match the base PfmFile.  No
         * reference count is held and no copy is made; the caller is responsible for
         * ensuring that the auxiliary PfmFile will persist throughout the lifetime of
         * the PfmVizzer it is assigned to.
         */
        """
        pass

    def set_flat_texcoord_name(self, const_PfmVizzer_self, InternalName_flat_texcoord_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_flat_texcoord_name(const PfmVizzer self, InternalName flat_texcoord_name)
        
        /**
         * If the flat_texcoord_name is specified, it is the name of an additional
         * vertex column that will be created for the "flat" texture coordinates, i.e.
         * the original 0..1 values that correspond to the 2-D index position of each
         * point in the original pfm file.
         *
         * These are the same values that will be assigned to the default texture
         * coordinates if the vis_inverse flag is *not* true.
         *
         * This may be used in lieu of the lower-level add_vis_column().
         */
        """
        pass

    def set_keep_beyond_lens(self, const_PfmVizzer_self, bool_keep_beyond_lens): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_keep_beyond_lens(const PfmVizzer self, bool keep_beyond_lens)
        
        /**
         * Sets the keep_beyond_lens flag.  When this flag is true, points that fall
         * outside of the normal lens range in project() or in add_vis_column() will
         * be retained anyway; when it is false, these points will be discarded.
         */
        """
        pass

    def set_vis_2d(self, const_PfmVizzer_self, bool_vis_2d): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vis_2d(const PfmVizzer self, bool vis_2d)
        
        /**
         * Sets the vis_2d flag.  When this flag is true, only the first two (x, y)
         * value of each depth point is considered meaningful; the z component is
         * ignored.  This is only relevant for generating visualizations.
         *
         * This may be used in lieu of the lower-level add_vis_column().
         */
        """
        pass

    def set_vis_blend(self, const_PfmVizzer_self, const_PNMImage_vis_blend): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vis_blend(const PfmVizzer self, const PNMImage vis_blend)
        
        /**
         * Specifies a blending map--a grayscale image--that will be applied to the
         * vertex color during generate_vis_mesh() and generate_vis_points().  The
         * image size must exactly match the mesh size of the PfmVizzer.
         *
         * Ownership of the pointer is not kept by the PfmVizzer; it is your
         * responsibility to ensure it does not destruct during the lifetime of the
         * PfmVizzer (or at least not before your subsequent call to
         * generate_vis_mesh()).
         */
        """
        pass

    def set_vis_inverse(self, const_PfmVizzer_self, bool_vis_inverse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vis_inverse(const PfmVizzer self, bool vis_inverse)
        
        /**
         * Sets the vis_inverse flag.  When this flag is true, vis meshes and point
         * clouds are generated with the 3-d depth value in the texture coordinates,
         * and the 2-d index value in the vertex position.  When it is false, meshes
         * are generated normally, with the 3-d depth value in the vertex position and
         * the 2-d index value in the texture coordinates.
         *
         * This may be used in lieu of the lower-level add_vis_column().
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

    CTAuxVertex1 = 7
    CTAuxVertex2 = 8
    CTAuxVertex3 = 9
    CTBlend1 = 6
    CTNormal3 = 5
    CTTexcoord2 = 0
    CTTexcoord3 = 1
    CTVertex1 = 2
    CTVertex2 = 3
    CTVertex3 = 4
    CT_aux_vertex1 = 7
    CT_aux_vertex2 = 8
    CT_aux_vertex3 = 9
    CT_blend1 = 6
    CT_normal3 = 5
    CT_texcoord2 = 0
    CT_texcoord3 = 1
    CT_vertex1 = 2
    CT_vertex2 = 3
    CT_vertex3 = 4
    DtoolClassDict = {
        'CTAuxVertex1': 7,
        'CTAuxVertex2': 8,
        'CTAuxVertex3': 9,
        'CTBlend1': 6,
        'CTNormal3': 5,
        'CTTexcoord2': 0,
        'CTTexcoord3': 1,
        'CTVertex1': 2,
        'CTVertex2': 3,
        'CTVertex3': 4,
        'CT_aux_vertex1': 7,
        'CT_aux_vertex2': 8,
        'CT_aux_vertex3': 9,
        'CT_blend1': 6,
        'CT_normal3': 5,
        'CT_texcoord2': 0,
        'CT_texcoord3': 1,
        'CT_vertex1': 2,
        'CT_vertex2': 3,
        'CT_vertex3': 4,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MFBack': 2,
        'MFBoth': 3,
        'MFFront': 1,
        'MF_back': 2,
        'MF_both': 3,
        'MF_front': 1,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PfmVizzer' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PfmVizzer' objects>"
        '__doc__': '/**\n * This class aids in the visualization and manipulation of PfmFile objects.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PfmVizzer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2BDB20>'
        'addVisColumn': None, # (!) real value is "<method 'addVisColumn' of 'panda3d.core.PfmVizzer' objects>"
        'add_vis_column': None, # (!) real value is "<method 'add_vis_column' of 'panda3d.core.PfmVizzer' objects>"
        'calcMaxUDisplacement': None, # (!) real value is "<method 'calcMaxUDisplacement' of 'panda3d.core.PfmVizzer' objects>"
        'calcMaxVDisplacement': None, # (!) real value is "<method 'calcMaxVDisplacement' of 'panda3d.core.PfmVizzer' objects>"
        'calc_max_u_displacement': None, # (!) real value is "<method 'calc_max_u_displacement' of 'panda3d.core.PfmVizzer' objects>"
        'calc_max_v_displacement': None, # (!) real value is "<method 'calc_max_v_displacement' of 'panda3d.core.PfmVizzer' objects>"
        'clearAuxPfm': None, # (!) real value is "<method 'clearAuxPfm' of 'panda3d.core.PfmVizzer' objects>"
        'clearFlatTexcoordName': None, # (!) real value is "<method 'clearFlatTexcoordName' of 'panda3d.core.PfmVizzer' objects>"
        'clearVisBlend': None, # (!) real value is "<method 'clearVisBlend' of 'panda3d.core.PfmVizzer' objects>"
        'clearVisColumns': None, # (!) real value is "<method 'clearVisColumns' of 'panda3d.core.PfmVizzer' objects>"
        'clear_aux_pfm': None, # (!) real value is "<method 'clear_aux_pfm' of 'panda3d.core.PfmVizzer' objects>"
        'clear_flat_texcoord_name': None, # (!) real value is "<method 'clear_flat_texcoord_name' of 'panda3d.core.PfmVizzer' objects>"
        'clear_vis_blend': None, # (!) real value is "<method 'clear_vis_blend' of 'panda3d.core.PfmVizzer' objects>"
        'clear_vis_columns': None, # (!) real value is "<method 'clear_vis_columns' of 'panda3d.core.PfmVizzer' objects>"
        'extrude': None, # (!) real value is "<method 'extrude' of 'panda3d.core.PfmVizzer' objects>"
        'generateVisMesh': None, # (!) real value is "<method 'generateVisMesh' of 'panda3d.core.PfmVizzer' objects>"
        'generateVisPoints': None, # (!) real value is "<method 'generateVisPoints' of 'panda3d.core.PfmVizzer' objects>"
        'generate_vis_mesh': None, # (!) real value is "<method 'generate_vis_mesh' of 'panda3d.core.PfmVizzer' objects>"
        'generate_vis_points': None, # (!) real value is "<method 'generate_vis_points' of 'panda3d.core.PfmVizzer' objects>"
        'getAuxPfm': None, # (!) real value is "<method 'getAuxPfm' of 'panda3d.core.PfmVizzer' objects>"
        'getFlatTexcoordName': None, # (!) real value is "<method 'getFlatTexcoordName' of 'panda3d.core.PfmVizzer' objects>"
        'getKeepBeyondLens': None, # (!) real value is "<method 'getKeepBeyondLens' of 'panda3d.core.PfmVizzer' objects>"
        'getPfm': None, # (!) real value is "<method 'getPfm' of 'panda3d.core.PfmVizzer' objects>"
        'getVis2d': None, # (!) real value is "<method 'getVis2d' of 'panda3d.core.PfmVizzer' objects>"
        'getVisBlend': None, # (!) real value is "<method 'getVisBlend' of 'panda3d.core.PfmVizzer' objects>"
        'getVisInverse': None, # (!) real value is "<method 'getVisInverse' of 'panda3d.core.PfmVizzer' objects>"
        'get_aux_pfm': None, # (!) real value is "<method 'get_aux_pfm' of 'panda3d.core.PfmVizzer' objects>"
        'get_flat_texcoord_name': None, # (!) real value is "<method 'get_flat_texcoord_name' of 'panda3d.core.PfmVizzer' objects>"
        'get_keep_beyond_lens': None, # (!) real value is "<method 'get_keep_beyond_lens' of 'panda3d.core.PfmVizzer' objects>"
        'get_pfm': None, # (!) real value is "<method 'get_pfm' of 'panda3d.core.PfmVizzer' objects>"
        'get_vis_2d': None, # (!) real value is "<method 'get_vis_2d' of 'panda3d.core.PfmVizzer' objects>"
        'get_vis_blend': None, # (!) real value is "<method 'get_vis_blend' of 'panda3d.core.PfmVizzer' objects>"
        'get_vis_inverse': None, # (!) real value is "<method 'get_vis_inverse' of 'panda3d.core.PfmVizzer' objects>"
        'makeDisplacement': None, # (!) real value is "<method 'makeDisplacement' of 'panda3d.core.PfmVizzer' objects>"
        'make_displacement': None, # (!) real value is "<method 'make_displacement' of 'panda3d.core.PfmVizzer' objects>"
        'project': None, # (!) real value is "<method 'project' of 'panda3d.core.PfmVizzer' objects>"
        'setAuxPfm': None, # (!) real value is "<method 'setAuxPfm' of 'panda3d.core.PfmVizzer' objects>"
        'setFlatTexcoordName': None, # (!) real value is "<method 'setFlatTexcoordName' of 'panda3d.core.PfmVizzer' objects>"
        'setKeepBeyondLens': None, # (!) real value is "<method 'setKeepBeyondLens' of 'panda3d.core.PfmVizzer' objects>"
        'setVis2d': None, # (!) real value is "<method 'setVis2d' of 'panda3d.core.PfmVizzer' objects>"
        'setVisBlend': None, # (!) real value is "<method 'setVisBlend' of 'panda3d.core.PfmVizzer' objects>"
        'setVisInverse': None, # (!) real value is "<method 'setVisInverse' of 'panda3d.core.PfmVizzer' objects>"
        'set_aux_pfm': None, # (!) real value is "<method 'set_aux_pfm' of 'panda3d.core.PfmVizzer' objects>"
        'set_flat_texcoord_name': None, # (!) real value is "<method 'set_flat_texcoord_name' of 'panda3d.core.PfmVizzer' objects>"
        'set_keep_beyond_lens': None, # (!) real value is "<method 'set_keep_beyond_lens' of 'panda3d.core.PfmVizzer' objects>"
        'set_vis_2d': None, # (!) real value is "<method 'set_vis_2d' of 'panda3d.core.PfmVizzer' objects>"
        'set_vis_blend': None, # (!) real value is "<method 'set_vis_blend' of 'panda3d.core.PfmVizzer' objects>"
        'set_vis_inverse': None, # (!) real value is "<method 'set_vis_inverse' of 'panda3d.core.PfmVizzer' objects>"
    }
    MFBack = 2
    MFBoth = 3
    MFFront = 1
    MF_back = 2
    MF_both = 3
    MF_front = 1


