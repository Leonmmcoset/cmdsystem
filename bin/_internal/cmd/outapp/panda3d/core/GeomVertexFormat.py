# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

from .GeomEnums import GeomEnums

class GeomVertexFormat(TypedWritableReferenceCount, GeomEnums):
    """
    /**
     * This class defines the physical layout of the vertex data stored within a
     * Geom.  The layout consists of a list of named columns, each of which has a
     * numeric type and a size.
     *
     * The columns are typically interleaved within a single array, but they may
     * also be distributed among multiple different arrays; at the extreme, each
     * column may be alone within its own array (which amounts to a parallel-array
     * definition).
     *
     * Thus, a GeomVertexFormat is really a list of GeomVertexArrayFormats, each
     * of which contains a list of columns.  However, a particular column name
     * should not appear more than once in the format, even between different
     * arrays.
     *
     * There are a handful of standard pre-defined GeomVertexFormat objects, or
     * you may define your own as needed.  You may record any combination of
     * standard and/or user-defined columns in your custom GeomVertexFormat
     * constructions.
     */
    """
    def addArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_array(const GeomVertexFormat self, const GeomVertexArrayFormat array_format)
        
        /**
         * Adds the indicated array definition to the list of arrays included within
         * this vertex format definition.  The return value is the index number of the
         * new array.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def add_array(self, const_GeomVertexFormat_self, const_GeomVertexArrayFormat_array_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_array(const GeomVertexFormat self, const GeomVertexArrayFormat array_format)
        
        /**
         * Adds the indicated array definition to the list of arrays included within
         * this vertex format definition.  The return value is the index number of the
         * new array.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def alignColumnsForAnimation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        align_columns_for_animation(const GeomVertexFormat self)
        
        /**
         * Reprocesses the columns in the format to align the C_point and C_vector
         * columns to 16-byte boundaries to allow for the more efficient SSE2
         * operations (assuming SSE2 is enabled in the build).
         *
         * Also see maybe_align_columns_for_animation().
         */
        """
        pass

    def align_columns_for_animation(self, const_GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        align_columns_for_animation(const GeomVertexFormat self)
        
        /**
         * Reprocesses the columns in the format to align the C_point and C_vector
         * columns to 16-byte boundaries to allow for the more efficient SSE2
         * operations (assuming SSE2 is enabled in the build).
         *
         * Also see maybe_align_columns_for_animation().
         */
        """
        pass

    def assign(self, const_GeomVertexFormat_self, const_GeomVertexFormat_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const GeomVertexFormat self, const GeomVertexFormat copy)
        """
        pass

    def clearArrays(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_arrays(const GeomVertexFormat self)
        
        /**
         * Removes all of the array definitions from the format and starts over.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def clear_arrays(self, const_GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_arrays(const GeomVertexFormat self)
        
        /**
         * Removes all of the array definitions from the format and starts over.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def getAnimation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_animation(GeomVertexFormat self)
        
        /**
         * Returns the GeomVertexAnimationSpec that indicates how this format's
         * vertices are set up for animation.
         */
        """
        pass

    def getArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array(GeomVertexFormat self, int array)
        
        /**
         * Returns the description of the nth array used by the format.
         */
        """
        pass

    def getArrays(self, *args, **kwargs): # real signature unknown
        pass

    def getArrayWith(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_array_with(GeomVertexFormat self, const InternalName name)
        get_array_with(GeomVertexFormat self, int i)
        
        /**
         * Returns the index number of the array with the ith column.
         *
         * The return value can be passed to get_array_format() to get the format of
         * the array.  It may also be passed to GeomVertexData::get_array_data() or
         * get_data() or set_data() to manipulate the actual array data.
         */
        
        /**
         * Returns the index number of the array with the indicated column, or -1 if
         * no arrays contained that name.
         *
         * The return value can be passed to get_array_format() to get the format of
         * the array.  It may also be passed to GeomVertexData::get_array_data() or
         * get_data() or set_data() to manipulate the actual array data.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_column(GeomVertexFormat self, const InternalName name)
        get_column(GeomVertexFormat self, int i)
        
        /**
         * Returns the ith column of the specification, across all arrays.
         */
        
        /**
         * Returns the specification with the indicated name, or NULL if the name is
         * not used.  Use get_array_with() to determine which array this column is
         * associated with.
         */
        """
        pass

    def getColumnName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_column_name(GeomVertexFormat self, int i)
        
        /**
         * Returns the name of the ith column, across all arrays.
         */
        """
        pass

    def getColumns(self, *args, **kwargs): # real signature unknown
        pass

    def getEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_empty()
        
        /**
         * Returns a standard vertex format containing no arrays at all, useful for
         * pull-style vertex rendering.
         */
        """
        pass

    def getMorphBase(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_morph_base(GeomVertexFormat self, int n)
        
        /**
         * Returns the name of the base column that the nth morph modifies.  This
         * column will also be defined within the format, and can be retrieved via
         * get_array_with() and/or get_column().
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getMorphBases(self, *args, **kwargs): # real signature unknown
        pass

    def getMorphDelta(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_morph_delta(GeomVertexFormat self, int n)
        
        /**
         * Returns the name of the column that defines the nth morph.  This contains
         * the delta offsets that are to be applied to the column defined by
         * get_morph_base().  This column will be defined within the format, and can
         * be retrieved via get_array_with() and/or get_column().
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getMorphDeltas(self, *args, **kwargs): # real signature unknown
        pass

    def getMorphSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_morph_slider(GeomVertexFormat self, int n)
        
        /**
         * Returns the slider name associated with the nth morph column.  This is the
         * name of the slider that will control the morph, and should be defined
         * within the SliderTable associated with the GeomVertexData.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getMorphSliders(self, *args, **kwargs): # real signature unknown
        pass

    def getNumArrays(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_arrays(GeomVertexFormat self)
        
        /**
         * Returns the number of individual arrays required by the format.  If the
         * array data is completely interleaved, this will be 1; if it is completely
         * parallel, this will be the same as the number of data types.
         */
        """
        pass

    def getNumColumns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_columns(GeomVertexFormat self)
        
        /**
         * Returns the total number of different columns in the specification, across
         * all arrays.
         */
        """
        pass

    def getNumMorphs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_morphs(GeomVertexFormat self)
        
        /**
         * Returns the number of columns within the format that represent morph
         * deltas.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getNumPoints(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_points(GeomVertexFormat self)
        
        /**
         * Returns the number of columns within the format that represent points in
         * space.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getNumTexcoords(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_texcoords(GeomVertexFormat self)
        
        /**
         * Returns the number of columns within the format that represent texture
         * coordinates.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getNumVectors(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_vectors(GeomVertexFormat self)
        
        /**
         * Returns the number of columns within the format that represent directional
         * vectors.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getPoint(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_point(GeomVertexFormat self, int n)
        
        /**
         * Returns the name of the nth point column.  This represents a point in
         * space, which should be transformed by any spatial transform matrix.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getPoints(self, *args, **kwargs): # real signature unknown
        pass

    def getPostAnimatedFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_post_animated_format(GeomVertexFormat self)
        
        /**
         * Returns a suitable vertex format for sending the animated vertices to the
         * graphics backend.  This is the same format as the source format, with the
         * CPU-animation data elements removed.
         *
         * This may only be called after the format has been registered.  The return
         * value will have been already registered.
         */
        """
        pass

    def getTexcoord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texcoord(GeomVertexFormat self, int n)
        
        /**
         * Returns the name of the nth texcoord column.  This represents a texture
         * coordinate.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getTexcoords(self, *args, **kwargs): # real signature unknown
        pass

    def getUnionFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_union_format(GeomVertexFormat self, const GeomVertexFormat other)
        
        /**
         * Returns a new GeomVertexFormat that includes all of the columns defined in
         * either this GeomVertexFormat or the other one.  If any column is defined in
         * both formats with different sizes (for instance, texcoord2 vs.  texcoord3),
         * the new format will include the larger of the two definitions.
         *
         * This may only be called after both source formats have been registered.
         * The return value will also have been already registered.
         */
        """
        pass

    def getV3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3()
        
        // Some standard vertex formats.  No particular requirement to use one of
        // these, but the DirectX renderers can use these formats directly, whereas
        // any other format will have to be converted first.
        
        /**
         * Returns a standard vertex format with just a 3-component vertex position.
         */
        """
        pass

    def getV3c4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3c4()
        
        // These formats, with an OpenGL-style four-byte color, are not supported
        // directly by DirectX.  If you use them, the DXGraphicsStateGuardian will
        // automatically convert to DirectX form (with a larger runtime overhead,
        // since DirectX8, and old DirectX9 drivers, require everything to be
        // interleaved together).
        
        /**
         * Returns a standard vertex format with a 4-component color and a 3-component
         * vertex position.
         */
        """
        pass

    def getV3c4t2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3c4t2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate
         * pair, a 4-component color, and a 3-component vertex position.
         */
        """
        pass

    def getV3cp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3cp()
        
        // These formats, with the DirectX-style packed color, may not be supported
        // directly by OpenGL.  If you use them and the driver does not support
        // them, the GLGraphicsStateGuardian will automatically convert to native
        // OpenGL form (with a small runtime overhead).
        
        /**
         * Returns a standard vertex format with a packed color and a 3-component
         * vertex position.
         */
        """
        pass

    def getV3cpt2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3cpt2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate
         * pair, a packed color, and a 3-component vertex position.
         */
        """
        pass

    def getV3n3(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3n3()
        
        /**
         * Returns a standard vertex format with a 3-component normal and a
         * 3-component vertex position.
         */
        """
        pass

    def getV3n3c4(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3n3c4()
        
        /**
         * Returns a standard vertex format with a 4-component color, a 3-component
         * normal, and a 3-component vertex position.
         */
        """
        pass

    def getV3n3c4t2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3n3c4t2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate
         * pair, a 4-component color, a 3-component normal, and a 3-component vertex
         * position.
         */
        """
        pass

    def getV3n3cp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3n3cp()
        
        /**
         * Returns a standard vertex format with a packed color, a 3-component normal,
         * and a 3-component vertex position.
         */
        """
        pass

    def getV3n3cpt2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3n3cpt2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate
         * pair, a packed color, a 3-component normal, and a 3-component vertex
         * position.
         */
        """
        pass

    def getV3n3t2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3n3t2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate
         * pair, a 3-component normal, and a 3-component vertex position.
         */
        """
        pass

    def getV3t2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_v3t2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate pair
         * and a 3-component vertex position.
         */
        """
        pass

    def getVector(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vector(GeomVertexFormat self, int n)
        
        /**
         * Returns the name of the nth vector column.  This represents a directional
         * vector, which should be transformed by any spatial transform matrix as a
         * vector.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def getVectors(self, *args, **kwargs): # real signature unknown
        pass

    def get_animation(self, GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_animation(GeomVertexFormat self)
        
        /**
         * Returns the GeomVertexAnimationSpec that indicates how this format's
         * vertices are set up for animation.
         */
        """
        pass

    def get_array(self, GeomVertexFormat_self, int_array): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array(GeomVertexFormat self, int array)
        
        /**
         * Returns the description of the nth array used by the format.
         */
        """
        pass

    def get_arrays(self, *args, **kwargs): # real signature unknown
        pass

    def get_array_with(self, GeomVertexFormat_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_array_with(GeomVertexFormat self, const InternalName name)
        get_array_with(GeomVertexFormat self, int i)
        
        /**
         * Returns the index number of the array with the ith column.
         *
         * The return value can be passed to get_array_format() to get the format of
         * the array.  It may also be passed to GeomVertexData::get_array_data() or
         * get_data() or set_data() to manipulate the actual array data.
         */
        
        /**
         * Returns the index number of the array with the indicated column, or -1 if
         * no arrays contained that name.
         *
         * The return value can be passed to get_array_format() to get the format of
         * the array.  It may also be passed to GeomVertexData::get_array_data() or
         * get_data() or set_data() to manipulate the actual array data.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_column(self, GeomVertexFormat_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_column(GeomVertexFormat self, const InternalName name)
        get_column(GeomVertexFormat self, int i)
        
        /**
         * Returns the ith column of the specification, across all arrays.
         */
        
        /**
         * Returns the specification with the indicated name, or NULL if the name is
         * not used.  Use get_array_with() to determine which array this column is
         * associated with.
         */
        """
        pass

    def get_columns(self, *args, **kwargs): # real signature unknown
        pass

    def get_column_name(self, GeomVertexFormat_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_column_name(GeomVertexFormat self, int i)
        
        /**
         * Returns the name of the ith column, across all arrays.
         */
        """
        pass

    def get_empty(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_empty()
        
        /**
         * Returns a standard vertex format containing no arrays at all, useful for
         * pull-style vertex rendering.
         */
        """
        pass

    def get_morph_base(self, GeomVertexFormat_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_morph_base(GeomVertexFormat self, int n)
        
        /**
         * Returns the name of the base column that the nth morph modifies.  This
         * column will also be defined within the format, and can be retrieved via
         * get_array_with() and/or get_column().
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_morph_bases(self, *args, **kwargs): # real signature unknown
        pass

    def get_morph_delta(self, GeomVertexFormat_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_morph_delta(GeomVertexFormat self, int n)
        
        /**
         * Returns the name of the column that defines the nth morph.  This contains
         * the delta offsets that are to be applied to the column defined by
         * get_morph_base().  This column will be defined within the format, and can
         * be retrieved via get_array_with() and/or get_column().
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_morph_deltas(self, *args, **kwargs): # real signature unknown
        pass

    def get_morph_slider(self, GeomVertexFormat_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_morph_slider(GeomVertexFormat self, int n)
        
        /**
         * Returns the slider name associated with the nth morph column.  This is the
         * name of the slider that will control the morph, and should be defined
         * within the SliderTable associated with the GeomVertexData.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_morph_sliders(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_arrays(self, GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_arrays(GeomVertexFormat self)
        
        /**
         * Returns the number of individual arrays required by the format.  If the
         * array data is completely interleaved, this will be 1; if it is completely
         * parallel, this will be the same as the number of data types.
         */
        """
        pass

    def get_num_columns(self, GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_columns(GeomVertexFormat self)
        
        /**
         * Returns the total number of different columns in the specification, across
         * all arrays.
         */
        """
        pass

    def get_num_morphs(self, GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_morphs(GeomVertexFormat self)
        
        /**
         * Returns the number of columns within the format that represent morph
         * deltas.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_num_points(self, GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_points(GeomVertexFormat self)
        
        /**
         * Returns the number of columns within the format that represent points in
         * space.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_num_texcoords(self, GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_texcoords(GeomVertexFormat self)
        
        /**
         * Returns the number of columns within the format that represent texture
         * coordinates.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_num_vectors(self, GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_vectors(GeomVertexFormat self)
        
        /**
         * Returns the number of columns within the format that represent directional
         * vectors.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_point(self, GeomVertexFormat_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_point(GeomVertexFormat self, int n)
        
        /**
         * Returns the name of the nth point column.  This represents a point in
         * space, which should be transformed by any spatial transform matrix.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_points(self, *args, **kwargs): # real signature unknown
        pass

    def get_post_animated_format(self, GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_post_animated_format(GeomVertexFormat self)
        
        /**
         * Returns a suitable vertex format for sending the animated vertices to the
         * graphics backend.  This is the same format as the source format, with the
         * CPU-animation data elements removed.
         *
         * This may only be called after the format has been registered.  The return
         * value will have been already registered.
         */
        """
        pass

    def get_texcoord(self, GeomVertexFormat_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texcoord(GeomVertexFormat self, int n)
        
        /**
         * Returns the name of the nth texcoord column.  This represents a texture
         * coordinate.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_texcoords(self, *args, **kwargs): # real signature unknown
        pass

    def get_union_format(self, GeomVertexFormat_self, const_GeomVertexFormat_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_union_format(GeomVertexFormat self, const GeomVertexFormat other)
        
        /**
         * Returns a new GeomVertexFormat that includes all of the columns defined in
         * either this GeomVertexFormat or the other one.  If any column is defined in
         * both formats with different sizes (for instance, texcoord2 vs.  texcoord3),
         * the new format will include the larger of the two definitions.
         *
         * This may only be called after both source formats have been registered.
         * The return value will also have been already registered.
         */
        """
        pass

    def get_v3(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3()
        
        // Some standard vertex formats.  No particular requirement to use one of
        // these, but the DirectX renderers can use these formats directly, whereas
        // any other format will have to be converted first.
        
        /**
         * Returns a standard vertex format with just a 3-component vertex position.
         */
        """
        pass

    def get_v3c4(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3c4()
        
        // These formats, with an OpenGL-style four-byte color, are not supported
        // directly by DirectX.  If you use them, the DXGraphicsStateGuardian will
        // automatically convert to DirectX form (with a larger runtime overhead,
        // since DirectX8, and old DirectX9 drivers, require everything to be
        // interleaved together).
        
        /**
         * Returns a standard vertex format with a 4-component color and a 3-component
         * vertex position.
         */
        """
        pass

    def get_v3c4t2(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3c4t2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate
         * pair, a 4-component color, and a 3-component vertex position.
         */
        """
        pass

    def get_v3cp(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3cp()
        
        // These formats, with the DirectX-style packed color, may not be supported
        // directly by OpenGL.  If you use them and the driver does not support
        // them, the GLGraphicsStateGuardian will automatically convert to native
        // OpenGL form (with a small runtime overhead).
        
        /**
         * Returns a standard vertex format with a packed color and a 3-component
         * vertex position.
         */
        """
        pass

    def get_v3cpt2(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3cpt2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate
         * pair, a packed color, and a 3-component vertex position.
         */
        """
        pass

    def get_v3n3(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3n3()
        
        /**
         * Returns a standard vertex format with a 3-component normal and a
         * 3-component vertex position.
         */
        """
        pass

    def get_v3n3c4(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3n3c4()
        
        /**
         * Returns a standard vertex format with a 4-component color, a 3-component
         * normal, and a 3-component vertex position.
         */
        """
        pass

    def get_v3n3c4t2(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3n3c4t2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate
         * pair, a 4-component color, a 3-component normal, and a 3-component vertex
         * position.
         */
        """
        pass

    def get_v3n3cp(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3n3cp()
        
        /**
         * Returns a standard vertex format with a packed color, a 3-component normal,
         * and a 3-component vertex position.
         */
        """
        pass

    def get_v3n3cpt2(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3n3cpt2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate
         * pair, a packed color, a 3-component normal, and a 3-component vertex
         * position.
         */
        """
        pass

    def get_v3n3t2(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3n3t2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate
         * pair, a 3-component normal, and a 3-component vertex position.
         */
        """
        pass

    def get_v3t2(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_v3t2()
        
        /**
         * Returns a standard vertex format with a 2-component texture coordinate pair
         * and a 3-component vertex position.
         */
        """
        pass

    def get_vector(self, GeomVertexFormat_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vector(GeomVertexFormat self, int n)
        
        /**
         * Returns the name of the nth vector column.  This represents a directional
         * vector, which should be transformed by any spatial transform matrix as a
         * vector.
         *
         * This may only be called after the format has been registered.
         */
        """
        pass

    def get_vectors(self, *args, **kwargs): # real signature unknown
        pass

    def hasColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_column(GeomVertexFormat self, const InternalName name)
        
        /**
         * Returns true if the format has the named column, false otherwise.
         */
        """
        pass

    def has_column(self, GeomVertexFormat_self, const_InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_column(GeomVertexFormat self, const InternalName name)
        
        /**
         * Returns true if the format has the named column, false otherwise.
         */
        """
        pass

    def insertArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_array(const GeomVertexFormat self, int array, const GeomVertexArrayFormat array_format)
        
        /**
         * Adds the indicated array definition to the list of arrays at the indicated
         * position.  This works just like add_array(), except that you can specify
         * which array index the new array should have.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def insert_array(self, const_GeomVertexFormat_self, int_array, const_GeomVertexArrayFormat_array_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_array(const GeomVertexFormat self, int array, const GeomVertexArrayFormat array_format)
        
        /**
         * Adds the indicated array definition to the list of arrays at the indicated
         * position.  This works just like add_array(), except that you can specify
         * which array index the new array should have.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def isRegistered(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_registered(GeomVertexFormat self)
        
        /**
         * Returns true if this format has been registered, false if it has not.  It
         * may not be used for a Geom until it has been registered, but once
         * registered, it may no longer be modified.
         */
        """
        pass

    def is_registered(self, GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_registered(GeomVertexFormat self)
        
        /**
         * Returns true if this format has been registered, false if it has not.  It
         * may not be used for a Geom until it has been registered, but once
         * registered, it may no longer be modified.
         */
        """
        pass

    def maybeAlignColumnsForAnimation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        maybe_align_columns_for_animation(const GeomVertexFormat self)
        
        /**
         * Calls align_columns_for_animation() if this format's AnimationSpec
         * indicates that it contains animated vertices, and if vertex-animation-
         * align-16 is true.
         */
        """
        pass

    def maybe_align_columns_for_animation(self, const_GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        maybe_align_columns_for_animation(const GeomVertexFormat self)
        
        /**
         * Calls align_columns_for_animation() if this format's AnimationSpec
         * indicates that it contains animated vertices, and if vertex-animation-
         * align-16 is true.
         */
        """
        pass

    def modifyArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_array(const GeomVertexFormat self, int array)
        
        /**
         * Returns a modifiable pointer to the indicated array.  This means
         * duplicating it if it is shared or registered.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def modify_array(self, const_GeomVertexFormat_self, int_array): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_array(const GeomVertexFormat self, int array)
        
        /**
         * Returns a modifiable pointer to the indicated array.  This means
         * duplicating it if it is shared or registered.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def output(self, GeomVertexFormat_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(GeomVertexFormat self, ostream out)
        
        /**
         *
         */
        """
        pass

    def packColumns(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        pack_columns(const GeomVertexFormat self)
        
        /**
         * Removes wasted space between columns.
         */
        """
        pass

    def pack_columns(self, const_GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        pack_columns(const GeomVertexFormat self)
        
        /**
         * Removes wasted space between columns.
         */
        """
        pass

    def registerFormat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        register_format(const GeomVertexFormat format)
        register_format(const GeomVertexArrayFormat format)
        
        /**
         * Adds the indicated format to the registry, if there is not an equivalent
         * format already there; in either case, returns the pointer to the equivalent
         * format now in the registry.
         *
         * This must be called before a format may be used in a Geom.  After this
         * call, you should discard the original pointer you passed in (which may or
         * may not now be invalid) and let its reference count decrement normally; you
         * should use only the returned value from this point on.
         */
        
        /**
         * This flavor of register_format() implicitly creates a one-array vertex
         * format from the array definition.
         */
        """
        pass

    def register_format(self, const_GeomVertexFormat_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        register_format(const GeomVertexFormat format)
        register_format(const GeomVertexArrayFormat format)
        
        /**
         * Adds the indicated format to the registry, if there is not an equivalent
         * format already there; in either case, returns the pointer to the equivalent
         * format now in the registry.
         *
         * This must be called before a format may be used in a Geom.  After this
         * call, you should discard the original pointer you passed in (which may or
         * may not now be invalid) and let its reference count decrement normally; you
         * should use only the returned value from this point on.
         */
        
        /**
         * This flavor of register_format() implicitly creates a one-array vertex
         * format from the array definition.
         */
        """
        pass

    def removeArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_array(const GeomVertexFormat self, int array)
        
        /**
         * Removes the nth array from the format.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def removeColumn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_column(const GeomVertexFormat self, const InternalName name, bool keep_empty_array)
        
        /**
         * Removes the named column from the format, from whichever array it exists
         * in.  If there are other columns remaining in the array, the array is left
         * with a gap where the column used to be; if this was the only column in the
         * array, the array is removed (unless keep_empty_array is true).
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def removeEmptyArrays(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_empty_arrays(const GeomVertexFormat self)
        
        /**
         * Removes the arrays that define no columns.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def remove_array(self, const_GeomVertexFormat_self, int_array): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_array(const GeomVertexFormat self, int array)
        
        /**
         * Removes the nth array from the format.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def remove_column(self, const_GeomVertexFormat_self, const_InternalName_name, bool_keep_empty_array): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_column(const GeomVertexFormat self, const InternalName name, bool keep_empty_array)
        
        /**
         * Removes the named column from the format, from whichever array it exists
         * in.  If there are other columns remaining in the array, the array is left
         * with a gap where the column used to be; if this was the only column in the
         * array, the array is removed (unless keep_empty_array is true).
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def remove_empty_arrays(self, const_GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_empty_arrays(const GeomVertexFormat self)
        
        /**
         * Removes the arrays that define no columns.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def setAnimation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_animation(const GeomVertexFormat self, const GeomVertexAnimationSpec animation)
        
        /**
         * Resets the GeomVertexAnimationSpec that indicates how this format's
         * vertices are set up for animation.  You should also, of course, change the
         * columns in the tables accordingly.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def setArray(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_array(const GeomVertexFormat self, int array, const GeomVertexArrayFormat format)
        
        /**
         * Replaces the definition of the indicated array.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def set_animation(self, const_GeomVertexFormat_self, const_GeomVertexAnimationSpec_animation): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_animation(const GeomVertexFormat self, const GeomVertexAnimationSpec animation)
        
        /**
         * Resets the GeomVertexAnimationSpec that indicates how this format's
         * vertices are set up for animation.  You should also, of course, change the
         * columns in the tables accordingly.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def set_array(self, const_GeomVertexFormat_self, int_array, const_GeomVertexArrayFormat_format): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_array(const GeomVertexFormat self, int array, const GeomVertexArrayFormat format)
        
        /**
         * Replaces the definition of the indicated array.
         *
         * This may not be called once the format has been registered.
         */
        """
        pass

    def unref(self, GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        unref(GeomVertexFormat self)
        
        /**
         * This method overrides ReferenceCount::unref() to unregister the object when
         * its reference count goes to zero.
         */
        """
        pass

    def upcastToGeomEnums(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomVertexFormat self)
        
        upcast from GeomVertexFormat to GeomEnums
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const GeomVertexFormat self)
        
        upcast from GeomVertexFormat to TypedWritableReferenceCount
        """
        pass

    def upcast_to_GeomEnums(self, const_GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_GeomEnums(const GeomVertexFormat self)
        
        upcast from GeomVertexFormat to GeomEnums
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_GeomVertexFormat_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const GeomVertexFormat self)
        
        upcast from GeomVertexFormat to TypedWritableReferenceCount
        """
        pass

    def write(self, GeomVertexFormat_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(GeomVertexFormat self, ostream out, int indent_level)
        
        /**
         *
         */
        """
        pass

    def writeWithData(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_with_data(GeomVertexFormat self, ostream out, int indent_level, const GeomVertexData data)
        
        /**
         *
         */
        """
        pass

    def write_with_data(self, GeomVertexFormat_self, ostream_out, int_indent_level, const_GeomVertexData_data): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_with_data(GeomVertexFormat self, ostream out, int indent_level, const GeomVertexData data)
        
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

    animation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    arrays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// We also define this as a mapping interface, for lookups by name."""

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    registered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.GeomVertexFormat' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.GeomVertexFormat' objects>"
        '__doc__': '/**\n * This class defines the physical layout of the vertex data stored within a\n * Geom.  The layout consists of a list of named columns, each of which has a\n * numeric type and a size.\n *\n * The columns are typically interleaved within a single array, but they may\n * also be distributed among multiple different arrays; at the extreme, each\n * column may be alone within its own array (which amounts to a parallel-array\n * definition).\n *\n * Thus, a GeomVertexFormat is really a list of GeomVertexArrayFormats, each\n * of which contains a list of columns.  However, a particular column name\n * should not appear more than once in the format, even between different\n * arrays.\n *\n * There are a handful of standard pre-defined GeomVertexFormat objects, or\n * you may define your own as needed.  You may record any combination of\n * standard and/or user-defined columns in your custom GeomVertexFormat\n * constructions.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.GeomVertexFormat' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FA2F0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.GeomVertexFormat' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.GeomVertexFormat' objects>"
        'addArray': None, # (!) real value is "<method 'addArray' of 'panda3d.core.GeomVertexFormat' objects>"
        'add_array': None, # (!) real value is "<method 'add_array' of 'panda3d.core.GeomVertexFormat' objects>"
        'alignColumnsForAnimation': None, # (!) real value is "<method 'alignColumnsForAnimation' of 'panda3d.core.GeomVertexFormat' objects>"
        'align_columns_for_animation': None, # (!) real value is "<method 'align_columns_for_animation' of 'panda3d.core.GeomVertexFormat' objects>"
        'animation': None, # (!) real value is "<attribute 'animation' of 'panda3d.core.GeomVertexFormat' objects>"
        'arrays': None, # (!) real value is "<attribute 'arrays' of 'panda3d.core.GeomVertexFormat' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.GeomVertexFormat' objects>"
        'clearArrays': None, # (!) real value is "<method 'clearArrays' of 'panda3d.core.GeomVertexFormat' objects>"
        'clear_arrays': None, # (!) real value is "<method 'clear_arrays' of 'panda3d.core.GeomVertexFormat' objects>"
        'columns': None, # (!) real value is "<attribute 'columns' of 'panda3d.core.GeomVertexFormat' objects>"
        'getAnimation': None, # (!) real value is "<method 'getAnimation' of 'panda3d.core.GeomVertexFormat' objects>"
        'getArray': None, # (!) real value is "<method 'getArray' of 'panda3d.core.GeomVertexFormat' objects>"
        'getArrayWith': None, # (!) real value is "<method 'getArrayWith' of 'panda3d.core.GeomVertexFormat' objects>"
        'getArrays': None, # (!) real value is "<method 'getArrays' of 'panda3d.core.GeomVertexFormat' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FA2F0>)>'
        'getColumn': None, # (!) real value is "<method 'getColumn' of 'panda3d.core.GeomVertexFormat' objects>"
        'getColumnName': None, # (!) real value is "<method 'getColumnName' of 'panda3d.core.GeomVertexFormat' objects>"
        'getColumns': None, # (!) real value is "<method 'getColumns' of 'panda3d.core.GeomVertexFormat' objects>"
        'getEmpty': None, # (!) real value is '<staticmethod(<built-in method getEmpty of type object at 0x00007FFCFE2FA2F0>)>'
        'getMorphBase': None, # (!) real value is "<method 'getMorphBase' of 'panda3d.core.GeomVertexFormat' objects>"
        'getMorphBases': None, # (!) real value is "<method 'getMorphBases' of 'panda3d.core.GeomVertexFormat' objects>"
        'getMorphDelta': None, # (!) real value is "<method 'getMorphDelta' of 'panda3d.core.GeomVertexFormat' objects>"
        'getMorphDeltas': None, # (!) real value is "<method 'getMorphDeltas' of 'panda3d.core.GeomVertexFormat' objects>"
        'getMorphSlider': None, # (!) real value is "<method 'getMorphSlider' of 'panda3d.core.GeomVertexFormat' objects>"
        'getMorphSliders': None, # (!) real value is "<method 'getMorphSliders' of 'panda3d.core.GeomVertexFormat' objects>"
        'getNumArrays': None, # (!) real value is "<method 'getNumArrays' of 'panda3d.core.GeomVertexFormat' objects>"
        'getNumColumns': None, # (!) real value is "<method 'getNumColumns' of 'panda3d.core.GeomVertexFormat' objects>"
        'getNumMorphs': None, # (!) real value is "<method 'getNumMorphs' of 'panda3d.core.GeomVertexFormat' objects>"
        'getNumPoints': None, # (!) real value is "<method 'getNumPoints' of 'panda3d.core.GeomVertexFormat' objects>"
        'getNumTexcoords': None, # (!) real value is "<method 'getNumTexcoords' of 'panda3d.core.GeomVertexFormat' objects>"
        'getNumVectors': None, # (!) real value is "<method 'getNumVectors' of 'panda3d.core.GeomVertexFormat' objects>"
        'getPoint': None, # (!) real value is "<method 'getPoint' of 'panda3d.core.GeomVertexFormat' objects>"
        'getPoints': None, # (!) real value is "<method 'getPoints' of 'panda3d.core.GeomVertexFormat' objects>"
        'getPostAnimatedFormat': None, # (!) real value is "<method 'getPostAnimatedFormat' of 'panda3d.core.GeomVertexFormat' objects>"
        'getTexcoord': None, # (!) real value is "<method 'getTexcoord' of 'panda3d.core.GeomVertexFormat' objects>"
        'getTexcoords': None, # (!) real value is "<method 'getTexcoords' of 'panda3d.core.GeomVertexFormat' objects>"
        'getUnionFormat': None, # (!) real value is "<method 'getUnionFormat' of 'panda3d.core.GeomVertexFormat' objects>"
        'getV3': None, # (!) real value is '<staticmethod(<built-in method getV3 of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3c4': None, # (!) real value is '<staticmethod(<built-in method getV3c4 of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3c4t2': None, # (!) real value is '<staticmethod(<built-in method getV3c4t2 of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3cp': None, # (!) real value is '<staticmethod(<built-in method getV3cp of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3cpt2': None, # (!) real value is '<staticmethod(<built-in method getV3cpt2 of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3n3': None, # (!) real value is '<staticmethod(<built-in method getV3n3 of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3n3c4': None, # (!) real value is '<staticmethod(<built-in method getV3n3c4 of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3n3c4t2': None, # (!) real value is '<staticmethod(<built-in method getV3n3c4t2 of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3n3cp': None, # (!) real value is '<staticmethod(<built-in method getV3n3cp of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3n3cpt2': None, # (!) real value is '<staticmethod(<built-in method getV3n3cpt2 of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3n3t2': None, # (!) real value is '<staticmethod(<built-in method getV3n3t2 of type object at 0x00007FFCFE2FA2F0>)>'
        'getV3t2': None, # (!) real value is '<staticmethod(<built-in method getV3t2 of type object at 0x00007FFCFE2FA2F0>)>'
        'getVector': None, # (!) real value is "<method 'getVector' of 'panda3d.core.GeomVertexFormat' objects>"
        'getVectors': None, # (!) real value is "<method 'getVectors' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_animation': None, # (!) real value is "<method 'get_animation' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_array': None, # (!) real value is "<method 'get_array' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_array_with': None, # (!) real value is "<method 'get_array_with' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_arrays': None, # (!) real value is "<method 'get_arrays' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FA2F0>)>'
        'get_column': None, # (!) real value is "<method 'get_column' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_column_name': None, # (!) real value is "<method 'get_column_name' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_columns': None, # (!) real value is "<method 'get_columns' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_empty': None, # (!) real value is '<staticmethod(<built-in method get_empty of type object at 0x00007FFCFE2FA2F0>)>'
        'get_morph_base': None, # (!) real value is "<method 'get_morph_base' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_morph_bases': None, # (!) real value is "<method 'get_morph_bases' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_morph_delta': None, # (!) real value is "<method 'get_morph_delta' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_morph_deltas': None, # (!) real value is "<method 'get_morph_deltas' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_morph_slider': None, # (!) real value is "<method 'get_morph_slider' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_morph_sliders': None, # (!) real value is "<method 'get_morph_sliders' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_num_arrays': None, # (!) real value is "<method 'get_num_arrays' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_num_columns': None, # (!) real value is "<method 'get_num_columns' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_num_morphs': None, # (!) real value is "<method 'get_num_morphs' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_num_points': None, # (!) real value is "<method 'get_num_points' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_num_texcoords': None, # (!) real value is "<method 'get_num_texcoords' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_num_vectors': None, # (!) real value is "<method 'get_num_vectors' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_point': None, # (!) real value is "<method 'get_point' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_points': None, # (!) real value is "<method 'get_points' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_post_animated_format': None, # (!) real value is "<method 'get_post_animated_format' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_texcoord': None, # (!) real value is "<method 'get_texcoord' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_texcoords': None, # (!) real value is "<method 'get_texcoords' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_union_format': None, # (!) real value is "<method 'get_union_format' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_v3': None, # (!) real value is '<staticmethod(<built-in method get_v3 of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3c4': None, # (!) real value is '<staticmethod(<built-in method get_v3c4 of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3c4t2': None, # (!) real value is '<staticmethod(<built-in method get_v3c4t2 of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3cp': None, # (!) real value is '<staticmethod(<built-in method get_v3cp of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3cpt2': None, # (!) real value is '<staticmethod(<built-in method get_v3cpt2 of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3n3': None, # (!) real value is '<staticmethod(<built-in method get_v3n3 of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3n3c4': None, # (!) real value is '<staticmethod(<built-in method get_v3n3c4 of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3n3c4t2': None, # (!) real value is '<staticmethod(<built-in method get_v3n3c4t2 of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3n3cp': None, # (!) real value is '<staticmethod(<built-in method get_v3n3cp of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3n3cpt2': None, # (!) real value is '<staticmethod(<built-in method get_v3n3cpt2 of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3n3t2': None, # (!) real value is '<staticmethod(<built-in method get_v3n3t2 of type object at 0x00007FFCFE2FA2F0>)>'
        'get_v3t2': None, # (!) real value is '<staticmethod(<built-in method get_v3t2 of type object at 0x00007FFCFE2FA2F0>)>'
        'get_vector': None, # (!) real value is "<method 'get_vector' of 'panda3d.core.GeomVertexFormat' objects>"
        'get_vectors': None, # (!) real value is "<method 'get_vectors' of 'panda3d.core.GeomVertexFormat' objects>"
        'hasColumn': None, # (!) real value is "<method 'hasColumn' of 'panda3d.core.GeomVertexFormat' objects>"
        'has_column': None, # (!) real value is "<method 'has_column' of 'panda3d.core.GeomVertexFormat' objects>"
        'insertArray': None, # (!) real value is "<method 'insertArray' of 'panda3d.core.GeomVertexFormat' objects>"
        'insert_array': None, # (!) real value is "<method 'insert_array' of 'panda3d.core.GeomVertexFormat' objects>"
        'isRegistered': None, # (!) real value is "<method 'isRegistered' of 'panda3d.core.GeomVertexFormat' objects>"
        'is_registered': None, # (!) real value is "<method 'is_registered' of 'panda3d.core.GeomVertexFormat' objects>"
        'maybeAlignColumnsForAnimation': None, # (!) real value is "<method 'maybeAlignColumnsForAnimation' of 'panda3d.core.GeomVertexFormat' objects>"
        'maybe_align_columns_for_animation': None, # (!) real value is "<method 'maybe_align_columns_for_animation' of 'panda3d.core.GeomVertexFormat' objects>"
        'modifyArray': None, # (!) real value is "<method 'modifyArray' of 'panda3d.core.GeomVertexFormat' objects>"
        'modify_array': None, # (!) real value is "<method 'modify_array' of 'panda3d.core.GeomVertexFormat' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.GeomVertexFormat' objects>"
        'packColumns': None, # (!) real value is "<method 'packColumns' of 'panda3d.core.GeomVertexFormat' objects>"
        'pack_columns': None, # (!) real value is "<method 'pack_columns' of 'panda3d.core.GeomVertexFormat' objects>"
        'points': None, # (!) real value is "<attribute 'points' of 'panda3d.core.GeomVertexFormat' objects>"
        'registerFormat': None, # (!) real value is '<staticmethod(<built-in method registerFormat of type object at 0x00007FFCFE2FA2F0>)>'
        'register_format': None, # (!) real value is '<staticmethod(<built-in method register_format of type object at 0x00007FFCFE2FA2F0>)>'
        'registered': None, # (!) real value is "<attribute 'registered' of 'panda3d.core.GeomVertexFormat' objects>"
        'removeArray': None, # (!) real value is "<method 'removeArray' of 'panda3d.core.GeomVertexFormat' objects>"
        'removeColumn': None, # (!) real value is "<method 'removeColumn' of 'panda3d.core.GeomVertexFormat' objects>"
        'removeEmptyArrays': None, # (!) real value is "<method 'removeEmptyArrays' of 'panda3d.core.GeomVertexFormat' objects>"
        'remove_array': None, # (!) real value is "<method 'remove_array' of 'panda3d.core.GeomVertexFormat' objects>"
        'remove_column': None, # (!) real value is "<method 'remove_column' of 'panda3d.core.GeomVertexFormat' objects>"
        'remove_empty_arrays': None, # (!) real value is "<method 'remove_empty_arrays' of 'panda3d.core.GeomVertexFormat' objects>"
        'setAnimation': None, # (!) real value is "<method 'setAnimation' of 'panda3d.core.GeomVertexFormat' objects>"
        'setArray': None, # (!) real value is "<method 'setArray' of 'panda3d.core.GeomVertexFormat' objects>"
        'set_animation': None, # (!) real value is "<method 'set_animation' of 'panda3d.core.GeomVertexFormat' objects>"
        'set_array': None, # (!) real value is "<method 'set_array' of 'panda3d.core.GeomVertexFormat' objects>"
        'unref': None, # (!) real value is "<method 'unref' of 'panda3d.core.GeomVertexFormat' objects>"
        'upcastToGeomEnums': None, # (!) real value is "<method 'upcastToGeomEnums' of 'panda3d.core.GeomVertexFormat' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.GeomVertexFormat' objects>"
        'upcast_to_GeomEnums': None, # (!) real value is "<method 'upcast_to_GeomEnums' of 'panda3d.core.GeomVertexFormat' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.GeomVertexFormat' objects>"
        'vectors': None, # (!) real value is "<attribute 'vectors' of 'panda3d.core.GeomVertexFormat' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.GeomVertexFormat' objects>"
        'writeWithData': None, # (!) real value is "<method 'writeWithData' of 'panda3d.core.GeomVertexFormat' objects>"
        'write_with_data': None, # (!) real value is "<method 'write_with_data' of 'panda3d.core.GeomVertexFormat' objects>"
    }


