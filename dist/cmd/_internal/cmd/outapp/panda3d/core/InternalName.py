# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class InternalName(TypedWritableReferenceCount):
    """
    /**
     * Encodes a string name in a hash table, mapping it to a pointer.  This is
     * used to tokenify names so they may be used efficiently in low-level Panda
     * structures, for instance to differentiate the multiple sets of texture
     * coordinates that might be stored on a Geom.
     *
     * InternalNames are hierarchical, with the '.' used by convention as a
     * separator character.  You can construct a single InternalName as a
     * composition of one or more other names, or by giving it a source string
     * directly.
     */
    """
    def append(self, const_InternalName_self, str_basename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        append(const InternalName self, str basename)
        
        /**
         * Constructs a new InternalName based on this name, with the indicated string
         * following it.  This is a cheaper way to construct a hierarchical name than
         * InternalName::make(parent->get_name() + ".basename").
         */
        """
        pass

    def findAncestor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_ancestor(InternalName self, str basename)
        
        /**
         * Returns the index of the ancestor with the indicated basename, or -1 if no
         * ancestor has that basename.  Returns 0 if this name has the basename.
         *
         * This index value may be passed to get_ancestor() or get_net_basename() to
         * retrieve more information about the indicated name.
         */
        """
        pass

    def find_ancestor(self, InternalName_self, str_basename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_ancestor(InternalName self, str basename)
        
        /**
         * Returns the index of the ancestor with the indicated basename, or -1 if no
         * ancestor has that basename.  Returns 0 if this name has the basename.
         *
         * This index value may be passed to get_ancestor() or get_net_basename() to
         * retrieve more information about the indicated name.
         */
        """
        pass

    def getAncestor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ancestor(InternalName self, int n)
        
        /**
         * Returns the ancestor with the indicated index number.  0 is this name
         * itself, 1 is the name's parent, 2 is the parent's parent, and so on.  If
         * there are not enough ancestors, returns the root InternalName.
         */
        """
        pass

    def getAspectRatio(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_aspect_ratio()
        
        /**
         * Returns the standard InternalName "aspect_ratio". This is the column header
         * for the floating-point aspect ratio value, which is used to define non-
         * square points.  This number is the ratio x / y, where y is the point size
         * (above).
         */
        """
        pass

    def getBasename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_basename(InternalName self)
        
        /**
         * Return the name represented by just this particular InternalName object,
         * ignoring its parents names.  This is everything after the rightmost dot.
         */
        """
        pass

    def getBinormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_binormal()
        
        /**
         * Returns the standard InternalName "binormal".  This is the column header
         * for the tangent vector associated with each vertex, which is a unit vector
         * usually perpendicular to both the normal and the tangent, and in the
         * direction of the V texture coordinate change.  It is used for deriving bump
         * maps.
         */
        """
        pass

    def getBinormalName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_binormal_name(str name)
        
        /**
         * Returns the InternalName "binormal.name", where name is the supplied
         * string.  This is the column header for the binormal associated with the
         * named texture coordinate set.
         */
        """
        pass

    def getCamera(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_camera()
        
        /**
         * Returns the standard InternalName "camera".  This is used as a keyword in
         * the shader subsystem.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color()
        
        /**
         * Returns the standard InternalName "color".  This is the column header for
         * the 4-component color value for each vertex.
         */
        """
        pass

    def getError(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_error()
        
        /**
         * Returns the standard InternalName "error".
         */
        """
        pass

    def getIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_index()
        
        /**
         * Returns the standard InternalName "index".  This is the column header for
         * the integer vertex index.  It is not used in the vertex data itself, but is
         * used in the GeomPrimitive structure to index into the vertex data.
         */
        """
        pass

    def getModel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_model()
        
        /**
         * Returns the standard InternalName "model".  This is used as a keyword in
         * the shader subsystem.
         */
        """
        pass

    def getMorph(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_morph(InternalName column, str slider)
        
        /**
         * Returns an InternalName derived from the given base column name and the
         * given slider name, which is the column header for the offset vector that
         * should be applied to the base column name when the named morph slider is
         * engaged.
         *
         * Each morph slider requires a set of n morph columns, one for each base
         * column it applies to.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(InternalName self)
        
        /**
         * Returns the complete name represented by the InternalName and all of its
         * parents.
         */
        """
        pass

    def getNetBasename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_net_basename(InternalName self, int n)
        
        /**
         * Returns the basename of this name prefixed by the indicated number of
         * ancestors.  0 is this name's basename, 1 is parent.basename, 2 is
         * grandparent.parent.basename, and so on.
         */
        """
        pass

    def getNormal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_normal()
        
        /**
         * Returns the standard InternalName "normal".  This is the column header for
         * the 3-d lighting normal for each vertex.
         */
        """
        pass

    def getParent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_parent(InternalName self)
        
        /**
         * Return the parent of this InternalName.  All names have a parent, except
         * the root name.
         */
        """
        pass

    def getRoot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_root()
        
        // Some predefined built-in names.
        
        /**
         * Returns the standard root InternalName.  This is the root of all other
         * InternalNames.  It has no name itself, and it is the only InternalName with
         * no parent.
         */
        """
        pass

    def getRotate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rotate()
        
        /**
         * Returns the standard InternalName "rotate".  This is the column header for
         * the floating-point rotate value, which represents a number of degrees
         * counter-clockwise to rotate each point or point sprite.
         */
        """
        pass

    def getSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_size()
        
        /**
         * Returns the standard InternalName "size".  This is the column header for
         * the floating-point size value, which overrides the thickness parameter of
         * the RenderModeAttrib on a per-vertex (e.g.  per-point) basis.
         */
        """
        pass

    def getTangent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tangent()
        
        /**
         * Returns the standard InternalName "tangent".  This is the column header for
         * the tangent vector associated with each vertex, which is a unit vector
         * usually perpendicular to the normal and in the direction of the U texture
         * coordinate change.  It is used for deriving bump maps.
         */
        """
        pass

    def getTangentName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tangent_name(str name)
        
        /**
         * Returns the InternalName "tangent.name", where name is the supplied string.
         * This is the column header for the tangent associated with the named texture
         * coordinate set.
         */
        """
        pass

    def getTexcoord(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texcoord()
        
        /**
         * Returns the standard InternalName "texcoord".  This is the column header
         * for the default texture coordinate set for each vertex.  It is also used
         * for identifying the default texture coordinate set in a TextureStage.
         */
        """
        pass

    def getTexcoordName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texcoord_name(str name)
        
        /**
         * Returns the InternalName "texcoord.name", where name is the supplied
         * string.  This is the column header for the named texture coordinate set for
         * each vertex.  It is also used for identifying the named texture coordinate
         * set in a TextureStage.
         */
        """
        pass

    def getTop(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_top(InternalName self)
        
        /**
         * Returns the oldest ancestor in the InternalName's chain, not counting the
         * root.  This will be the first name in the string, e.g.  "texcoord.foo.bar"
         * will return the InternalName "texcoord".
         */
        """
        pass

    def getTransformBlend(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform_blend()
        
        /**
         * Returns the standard InternalName "transform_blend". This is the column
         * header for the integer transform_blend index, which is used to define
         * vertex animation on the CPU by indexing to a particular vertex weighting
         * from the TransformBlendTable.
         */
        """
        pass

    def getTransformIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform_index()
        
        /**
         * Returns the standard InternalName "transform_index". This is the column
         * header for the n-component transform_index value, which is used in
         * conjuntion with "transform_weight" to define vertex animation on the
         * graphics card.  The transform_index value specifies the nth transform, by
         * lookup in the TransformTable.  The transform_index column may be omitted,
         * in which case the nth transform is the nth entry in the table.
         */
        """
        pass

    def getTransformWeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_transform_weight()
        
        /**
         * Returns the standard InternalName "transform_weight". This is the column
         * header for the n-component transform_weight value, which is used in
         * conjuntion with "transform_index" to define vertex animation on the
         * graphics card.  The transform_weight value specifies the weight of the nth
         * transform.  By convention, there are 1 fewer weight values than transforms,
         * since the weights are assumed to sum to 1 (and the last value is therefore
         * implicit).
         */
        """
        pass

    def getVertex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_vertex()
        
        /**
         * Returns the standard InternalName "vertex".  This is the column header for
         * the 3-d or 4-d vertex position information for each vertex.
         */
        """
        pass

    def getView(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_view()
        
        /**
         * Returns the standard InternalName "view".  This is used as a keyword in the
         * shader subsystem.
         */
        """
        pass

    def getWorld(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_world()
        
        /**
         * Returns the standard InternalName "world".  This is used as a keyword in
         * the shader subsystem.
         */
        """
        pass

    def get_ancestor(self, InternalName_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ancestor(InternalName self, int n)
        
        /**
         * Returns the ancestor with the indicated index number.  0 is this name
         * itself, 1 is the name's parent, 2 is the parent's parent, and so on.  If
         * there are not enough ancestors, returns the root InternalName.
         */
        """
        pass

    def get_aspect_ratio(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_aspect_ratio()
        
        /**
         * Returns the standard InternalName "aspect_ratio". This is the column header
         * for the floating-point aspect ratio value, which is used to define non-
         * square points.  This number is the ratio x / y, where y is the point size
         * (above).
         */
        """
        pass

    def get_basename(self, InternalName_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_basename(InternalName self)
        
        /**
         * Return the name represented by just this particular InternalName object,
         * ignoring its parents names.  This is everything after the rightmost dot.
         */
        """
        pass

    def get_binormal(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_binormal()
        
        /**
         * Returns the standard InternalName "binormal".  This is the column header
         * for the tangent vector associated with each vertex, which is a unit vector
         * usually perpendicular to both the normal and the tangent, and in the
         * direction of the V texture coordinate change.  It is used for deriving bump
         * maps.
         */
        """
        pass

    def get_binormal_name(self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_binormal_name(str name)
        
        /**
         * Returns the InternalName "binormal.name", where name is the supplied
         * string.  This is the column header for the binormal associated with the
         * named texture coordinate set.
         */
        """
        pass

    def get_camera(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_camera()
        
        /**
         * Returns the standard InternalName "camera".  This is used as a keyword in
         * the shader subsystem.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_color(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color()
        
        /**
         * Returns the standard InternalName "color".  This is the column header for
         * the 4-component color value for each vertex.
         */
        """
        pass

    def get_error(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_error()
        
        /**
         * Returns the standard InternalName "error".
         */
        """
        pass

    def get_index(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_index()
        
        /**
         * Returns the standard InternalName "index".  This is the column header for
         * the integer vertex index.  It is not used in the vertex data itself, but is
         * used in the GeomPrimitive structure to index into the vertex data.
         */
        """
        pass

    def get_model(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_model()
        
        /**
         * Returns the standard InternalName "model".  This is used as a keyword in
         * the shader subsystem.
         */
        """
        pass

    def get_morph(self, InternalName_column, str_slider): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_morph(InternalName column, str slider)
        
        /**
         * Returns an InternalName derived from the given base column name and the
         * given slider name, which is the column header for the offset vector that
         * should be applied to the base column name when the named morph slider is
         * engaged.
         *
         * Each morph slider requires a set of n morph columns, one for each base
         * column it applies to.
         */
        """
        pass

    def get_name(self, InternalName_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(InternalName self)
        
        /**
         * Returns the complete name represented by the InternalName and all of its
         * parents.
         */
        """
        pass

    def get_net_basename(self, InternalName_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_net_basename(InternalName self, int n)
        
        /**
         * Returns the basename of this name prefixed by the indicated number of
         * ancestors.  0 is this name's basename, 1 is parent.basename, 2 is
         * grandparent.parent.basename, and so on.
         */
        """
        pass

    def get_normal(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_normal()
        
        /**
         * Returns the standard InternalName "normal".  This is the column header for
         * the 3-d lighting normal for each vertex.
         */
        """
        pass

    def get_parent(self, InternalName_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_parent(InternalName self)
        
        /**
         * Return the parent of this InternalName.  All names have a parent, except
         * the root name.
         */
        """
        pass

    def get_root(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_root()
        
        // Some predefined built-in names.
        
        /**
         * Returns the standard root InternalName.  This is the root of all other
         * InternalNames.  It has no name itself, and it is the only InternalName with
         * no parent.
         */
        """
        pass

    def get_rotate(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rotate()
        
        /**
         * Returns the standard InternalName "rotate".  This is the column header for
         * the floating-point rotate value, which represents a number of degrees
         * counter-clockwise to rotate each point or point sprite.
         */
        """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_size()
        
        /**
         * Returns the standard InternalName "size".  This is the column header for
         * the floating-point size value, which overrides the thickness parameter of
         * the RenderModeAttrib on a per-vertex (e.g.  per-point) basis.
         */
        """
        pass

    def get_tangent(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tangent()
        
        /**
         * Returns the standard InternalName "tangent".  This is the column header for
         * the tangent vector associated with each vertex, which is a unit vector
         * usually perpendicular to the normal and in the direction of the U texture
         * coordinate change.  It is used for deriving bump maps.
         */
        """
        pass

    def get_tangent_name(self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tangent_name(str name)
        
        /**
         * Returns the InternalName "tangent.name", where name is the supplied string.
         * This is the column header for the tangent associated with the named texture
         * coordinate set.
         */
        """
        pass

    def get_texcoord(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texcoord()
        
        /**
         * Returns the standard InternalName "texcoord".  This is the column header
         * for the default texture coordinate set for each vertex.  It is also used
         * for identifying the default texture coordinate set in a TextureStage.
         */
        """
        pass

    def get_texcoord_name(self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texcoord_name(str name)
        
        /**
         * Returns the InternalName "texcoord.name", where name is the supplied
         * string.  This is the column header for the named texture coordinate set for
         * each vertex.  It is also used for identifying the named texture coordinate
         * set in a TextureStage.
         */
        """
        pass

    def get_top(self, InternalName_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_top(InternalName self)
        
        /**
         * Returns the oldest ancestor in the InternalName's chain, not counting the
         * root.  This will be the first name in the string, e.g.  "texcoord.foo.bar"
         * will return the InternalName "texcoord".
         */
        """
        pass

    def get_transform_blend(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform_blend()
        
        /**
         * Returns the standard InternalName "transform_blend". This is the column
         * header for the integer transform_blend index, which is used to define
         * vertex animation on the CPU by indexing to a particular vertex weighting
         * from the TransformBlendTable.
         */
        """
        pass

    def get_transform_index(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform_index()
        
        /**
         * Returns the standard InternalName "transform_index". This is the column
         * header for the n-component transform_index value, which is used in
         * conjuntion with "transform_weight" to define vertex animation on the
         * graphics card.  The transform_index value specifies the nth transform, by
         * lookup in the TransformTable.  The transform_index column may be omitted,
         * in which case the nth transform is the nth entry in the table.
         */
        """
        pass

    def get_transform_weight(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_transform_weight()
        
        /**
         * Returns the standard InternalName "transform_weight". This is the column
         * header for the n-component transform_weight value, which is used in
         * conjuntion with "transform_index" to define vertex animation on the
         * graphics card.  The transform_weight value specifies the weight of the nth
         * transform.  By convention, there are 1 fewer weight values than transforms,
         * since the weights are assumed to sum to 1 (and the last value is therefore
         * implicit).
         */
        """
        pass

    def get_vertex(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_vertex()
        
        /**
         * Returns the standard InternalName "vertex".  This is the column header for
         * the 3-d or 4-d vertex position information for each vertex.
         */
        """
        pass

    def get_view(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_view()
        
        /**
         * Returns the standard InternalName "view".  This is used as a keyword in the
         * shader subsystem.
         */
        """
        pass

    def get_world(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_world()
        
        /**
         * Returns the standard InternalName "world".  This is used as a keyword in
         * the shader subsystem.
         */
        """
        pass

    def join(self, InternalName_self, str_sep): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        join(InternalName self, str sep)
        
        /**
         * Like get_name, but uses a custom separator instead of ".".
         */
        """
        pass

    def make(self, object_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(object str)
        make(str name, int index)
        
        // These versions are exposed to Python, which have additional logic to map
        // from Python interned strings.
        
        /**
         * The public interface for constructing an InternalName pointer.  This will
         * return a new InternalName representing the indicated name, if this is the
         * first time the particular name has been requested; if the name is already
         * in use, it will return the existing pointer.
         *
         * If the string contains the '.' character, the string will be divided at the
         * dots and the so-defined hierarchy of names will be registered.  This is
         * handled transparently.
         */
        
        /**
         * Make using a string and an integer.  Concatenates the two.
         */
        """
        pass

    def output(self, InternalName_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(InternalName self, ostream out)
        
        /**
         *
         */
        """
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

    basename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * Encodes a string name in a hash table, mapping it to a pointer.  This is\n * used to tokenify names so they may be used efficiently in low-level Panda\n * structures, for instance to differentiate the multiple sets of texture\n * coordinates that might be stored on a Geom.\n *\n * InternalNames are hierarchical, with the '.' used by convention as a\n * separator character.  You can construct a single InternalName as a\n * composition of one or more other names, or by giving it a source string\n * directly.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.InternalName' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2F9D80>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.InternalName' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.InternalName' objects>"
        'append': None, # (!) real value is "<method 'append' of 'panda3d.core.InternalName' objects>"
        'basename': None, # (!) real value is "<attribute 'basename' of 'panda3d.core.InternalName' objects>"
        'findAncestor': None, # (!) real value is "<method 'findAncestor' of 'panda3d.core.InternalName' objects>"
        'find_ancestor': None, # (!) real value is "<method 'find_ancestor' of 'panda3d.core.InternalName' objects>"
        'getAncestor': None, # (!) real value is "<method 'getAncestor' of 'panda3d.core.InternalName' objects>"
        'getAspectRatio': None, # (!) real value is '<staticmethod(<built-in method getAspectRatio of type object at 0x00007FFCFE2F9D80>)>'
        'getBasename': None, # (!) real value is "<method 'getBasename' of 'panda3d.core.InternalName' objects>"
        'getBinormal': None, # (!) real value is '<staticmethod(<built-in method getBinormal of type object at 0x00007FFCFE2F9D80>)>'
        'getBinormalName': None, # (!) real value is '<staticmethod(<built-in method getBinormalName of type object at 0x00007FFCFE2F9D80>)>'
        'getCamera': None, # (!) real value is '<staticmethod(<built-in method getCamera of type object at 0x00007FFCFE2F9D80>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2F9D80>)>'
        'getColor': None, # (!) real value is '<staticmethod(<built-in method getColor of type object at 0x00007FFCFE2F9D80>)>'
        'getError': None, # (!) real value is '<staticmethod(<built-in method getError of type object at 0x00007FFCFE2F9D80>)>'
        'getIndex': None, # (!) real value is '<staticmethod(<built-in method getIndex of type object at 0x00007FFCFE2F9D80>)>'
        'getModel': None, # (!) real value is '<staticmethod(<built-in method getModel of type object at 0x00007FFCFE2F9D80>)>'
        'getMorph': None, # (!) real value is '<staticmethod(<built-in method getMorph of type object at 0x00007FFCFE2F9D80>)>'
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.InternalName' objects>"
        'getNetBasename': None, # (!) real value is "<method 'getNetBasename' of 'panda3d.core.InternalName' objects>"
        'getNormal': None, # (!) real value is '<staticmethod(<built-in method getNormal of type object at 0x00007FFCFE2F9D80>)>'
        'getParent': None, # (!) real value is "<method 'getParent' of 'panda3d.core.InternalName' objects>"
        'getRoot': None, # (!) real value is '<staticmethod(<built-in method getRoot of type object at 0x00007FFCFE2F9D80>)>'
        'getRotate': None, # (!) real value is '<staticmethod(<built-in method getRotate of type object at 0x00007FFCFE2F9D80>)>'
        'getSize': None, # (!) real value is '<staticmethod(<built-in method getSize of type object at 0x00007FFCFE2F9D80>)>'
        'getTangent': None, # (!) real value is '<staticmethod(<built-in method getTangent of type object at 0x00007FFCFE2F9D80>)>'
        'getTangentName': None, # (!) real value is '<staticmethod(<built-in method getTangentName of type object at 0x00007FFCFE2F9D80>)>'
        'getTexcoord': None, # (!) real value is '<staticmethod(<built-in method getTexcoord of type object at 0x00007FFCFE2F9D80>)>'
        'getTexcoordName': None, # (!) real value is '<staticmethod(<built-in method getTexcoordName of type object at 0x00007FFCFE2F9D80>)>'
        'getTop': None, # (!) real value is "<method 'getTop' of 'panda3d.core.InternalName' objects>"
        'getTransformBlend': None, # (!) real value is '<staticmethod(<built-in method getTransformBlend of type object at 0x00007FFCFE2F9D80>)>'
        'getTransformIndex': None, # (!) real value is '<staticmethod(<built-in method getTransformIndex of type object at 0x00007FFCFE2F9D80>)>'
        'getTransformWeight': None, # (!) real value is '<staticmethod(<built-in method getTransformWeight of type object at 0x00007FFCFE2F9D80>)>'
        'getVertex': None, # (!) real value is '<staticmethod(<built-in method getVertex of type object at 0x00007FFCFE2F9D80>)>'
        'getView': None, # (!) real value is '<staticmethod(<built-in method getView of type object at 0x00007FFCFE2F9D80>)>'
        'getWorld': None, # (!) real value is '<staticmethod(<built-in method getWorld of type object at 0x00007FFCFE2F9D80>)>'
        'get_ancestor': None, # (!) real value is "<method 'get_ancestor' of 'panda3d.core.InternalName' objects>"
        'get_aspect_ratio': None, # (!) real value is '<staticmethod(<built-in method get_aspect_ratio of type object at 0x00007FFCFE2F9D80>)>'
        'get_basename': None, # (!) real value is "<method 'get_basename' of 'panda3d.core.InternalName' objects>"
        'get_binormal': None, # (!) real value is '<staticmethod(<built-in method get_binormal of type object at 0x00007FFCFE2F9D80>)>'
        'get_binormal_name': None, # (!) real value is '<staticmethod(<built-in method get_binormal_name of type object at 0x00007FFCFE2F9D80>)>'
        'get_camera': None, # (!) real value is '<staticmethod(<built-in method get_camera of type object at 0x00007FFCFE2F9D80>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2F9D80>)>'
        'get_color': None, # (!) real value is '<staticmethod(<built-in method get_color of type object at 0x00007FFCFE2F9D80>)>'
        'get_error': None, # (!) real value is '<staticmethod(<built-in method get_error of type object at 0x00007FFCFE2F9D80>)>'
        'get_index': None, # (!) real value is '<staticmethod(<built-in method get_index of type object at 0x00007FFCFE2F9D80>)>'
        'get_model': None, # (!) real value is '<staticmethod(<built-in method get_model of type object at 0x00007FFCFE2F9D80>)>'
        'get_morph': None, # (!) real value is '<staticmethod(<built-in method get_morph of type object at 0x00007FFCFE2F9D80>)>'
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.InternalName' objects>"
        'get_net_basename': None, # (!) real value is "<method 'get_net_basename' of 'panda3d.core.InternalName' objects>"
        'get_normal': None, # (!) real value is '<staticmethod(<built-in method get_normal of type object at 0x00007FFCFE2F9D80>)>'
        'get_parent': None, # (!) real value is "<method 'get_parent' of 'panda3d.core.InternalName' objects>"
        'get_root': None, # (!) real value is '<staticmethod(<built-in method get_root of type object at 0x00007FFCFE2F9D80>)>'
        'get_rotate': None, # (!) real value is '<staticmethod(<built-in method get_rotate of type object at 0x00007FFCFE2F9D80>)>'
        'get_size': None, # (!) real value is '<staticmethod(<built-in method get_size of type object at 0x00007FFCFE2F9D80>)>'
        'get_tangent': None, # (!) real value is '<staticmethod(<built-in method get_tangent of type object at 0x00007FFCFE2F9D80>)>'
        'get_tangent_name': None, # (!) real value is '<staticmethod(<built-in method get_tangent_name of type object at 0x00007FFCFE2F9D80>)>'
        'get_texcoord': None, # (!) real value is '<staticmethod(<built-in method get_texcoord of type object at 0x00007FFCFE2F9D80>)>'
        'get_texcoord_name': None, # (!) real value is '<staticmethod(<built-in method get_texcoord_name of type object at 0x00007FFCFE2F9D80>)>'
        'get_top': None, # (!) real value is "<method 'get_top' of 'panda3d.core.InternalName' objects>"
        'get_transform_blend': None, # (!) real value is '<staticmethod(<built-in method get_transform_blend of type object at 0x00007FFCFE2F9D80>)>'
        'get_transform_index': None, # (!) real value is '<staticmethod(<built-in method get_transform_index of type object at 0x00007FFCFE2F9D80>)>'
        'get_transform_weight': None, # (!) real value is '<staticmethod(<built-in method get_transform_weight of type object at 0x00007FFCFE2F9D80>)>'
        'get_vertex': None, # (!) real value is '<staticmethod(<built-in method get_vertex of type object at 0x00007FFCFE2F9D80>)>'
        'get_view': None, # (!) real value is '<staticmethod(<built-in method get_view of type object at 0x00007FFCFE2F9D80>)>'
        'get_world': None, # (!) real value is '<staticmethod(<built-in method get_world of type object at 0x00007FFCFE2F9D80>)>'
        'join': None, # (!) real value is "<method 'join' of 'panda3d.core.InternalName' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE2F9D80>)>'
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.InternalName' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.InternalName' objects>"
        'parent': None, # (!) real value is "<attribute 'parent' of 'panda3d.core.InternalName' objects>"
    }


