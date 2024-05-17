# encoding: utf-8
# module panda3d.egg
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\egg.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .EggGroupNode import EggGroupNode

class EggData(EggGroupNode):
    """
    /**
     * This is the primary interface into all the egg data, and the root of the
     * egg file structure.  An EggData structure corresponds exactly with an egg
     * file on the disk.
     *
     * The EggData class inherits from EggGroupNode its collection of children,
     * which are accessed by using the EggData itself as an STL container with
     * begin() and end() calls.  The children of the EggData class are the
     * toplevel nodes in the egg file.
     */
    """
    def assign(self, const_EggData_self, const_EggData_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const EggData self, const EggData copy)
        
        /**
         *
         */
        """
        pass

    def collapseEquivalentMaterials(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        collapse_equivalent_materials(const EggData self)
        
        /**
         * Removes duplicate references to the same material with the same properties.
         * Considers two material references with identical properties, but different
         * mref names, to be equivalent, and collapses them, choosing one mref name to
         * keep arbitrarily.  Returns the number of materials removed.
         */
        """
        pass

    def collapseEquivalentTextures(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        collapse_equivalent_textures(const EggData self)
        
        /**
         * Removes duplicate references to the same texture image with the same
         * properties.  Considers two texture references with identical properties,
         * but different tref names, to be equivalent, and collapses them, choosing
         * one tref name to keep arbitrarily.  Returns the number of textures removed.
         */
        """
        pass

    def collapse_equivalent_materials(self, const_EggData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collapse_equivalent_materials(const EggData self)
        
        /**
         * Removes duplicate references to the same material with the same properties.
         * Considers two material references with identical properties, but different
         * mref names, to be equivalent, and collapses them, choosing one mref name to
         * keep arbitrarily.  Returns the number of materials removed.
         */
        """
        pass

    def collapse_equivalent_textures(self, const_EggData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        collapse_equivalent_textures(const EggData self)
        
        /**
         * Removes duplicate references to the same texture image with the same
         * properties.  Considers two texture references with identical properties,
         * but different tref names, to be equivalent, and collapses them, choosing
         * one tref name to keep arbitrarily.  Returns the number of textures removed.
         */
        """
        pass

    def getAutoResolveExternals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_resolve_externals(EggData self)
        
        /**
         * Indicates whether the EggData object will automatically resolve any
         * external references when read() is called.  The default is false.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_coordinate_system(EggData self)
        
        /**
         * Returns the coordinate system in which the egg file is defined.
         */
        """
        pass

    def getEggFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_egg_filename(EggData self)
        
        /**
         * Returns the directory in which the egg file is considered to reside.
         */
        """
        pass

    def getEggTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_egg_timestamp(EggData self)
        
        /**
         * Returns the timestamp of the egg file on disk, at the time it was opened
         * for reading, or 0 if this information is not available.
         */
        """
        pass

    def get_auto_resolve_externals(self, EggData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_resolve_externals(EggData self)
        
        /**
         * Indicates whether the EggData object will automatically resolve any
         * external references when read() is called.  The default is false.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_coordinate_system(self, EggData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_coordinate_system(EggData self)
        
        /**
         * Returns the coordinate system in which the egg file is defined.
         */
        """
        pass

    def get_egg_filename(self, EggData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_egg_filename(EggData self)
        
        /**
         * Returns the directory in which the egg file is considered to reside.
         */
        """
        pass

    def get_egg_timestamp(self, EggData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_egg_timestamp(EggData self)
        
        /**
         * Returns the timestamp of the egg file on disk, at the time it was opened
         * for reading, or 0 if this information is not available.
         */
        """
        pass

    def loadExternals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        load_externals(const EggData self)
        load_externals(const EggData self, const DSearchPath searchpath)
        load_externals(const EggData self, const DSearchPath searchpath, BamCacheRecord record)
        
        /**
         * Loads up all the egg files referenced by <File> entries within the egg
         * structure, and inserts their contents in place of the <File> entries.
         * Searches for files in the searchpath, if not found directly, and writes
         * error messages to the indicated output stream.  Returns true if all
         * externals were loaded successfully, false otherwise.
         */
        
        /**
         * Loads up all the egg files referenced by <File> entries within the egg
         * structure, and inserts their contents in place of the <File> entries.
         * Searches for files in the searchpath, if not found directly, and writes
         * error messages to the indicated output stream.  Returns true if all
         * externals were loaded successfully, false otherwise.
         */
        """
        pass

    def load_externals(self, const_EggData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        load_externals(const EggData self)
        load_externals(const EggData self, const DSearchPath searchpath)
        load_externals(const EggData self, const DSearchPath searchpath, BamCacheRecord record)
        
        /**
         * Loads up all the egg files referenced by <File> entries within the egg
         * structure, and inserts their contents in place of the <File> entries.
         * Searches for files in the searchpath, if not found directly, and writes
         * error messages to the indicated output stream.  Returns true if all
         * externals were loaded successfully, false otherwise.
         */
        
        /**
         * Loads up all the egg files referenced by <File> entries within the egg
         * structure, and inserts their contents in place of the <File> entries.
         * Searches for files in the searchpath, if not found directly, and writes
         * error messages to the indicated output stream.  Returns true if all
         * externals were loaded successfully, false otherwise.
         */
        """
        pass

    def merge(self, const_EggData_self, EggData_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        merge(const EggData self, EggData other)
        
        /**
         * Appends the other egg structure to the end of this one.  The other egg
         * structure is invalidated.
         */
        """
        pass

    def originalHadAbsolutePathnames(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        original_had_absolute_pathnames(EggData self)
        
        /**
         * Returns true if the data processed in the last call to read() contained
         * absolute pathnames, or false if those pathnames were all relative.
         *
         * This method is necessary because if auto_resolve_externals() is in effect,
         * it may modify the pathnames to be absolute whether or not they were as
         * loaded from disk.  This method can be used to query the state of the
         * original egg file from disk.
         */
        """
        pass

    def original_had_absolute_pathnames(self, EggData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        original_had_absolute_pathnames(EggData self)
        
        /**
         * Returns true if the data processed in the last call to read() contained
         * absolute pathnames, or false if those pathnames were all relative.
         *
         * This method is necessary because if auto_resolve_externals() is in effect,
         * it may modify the pathnames to be absolute whether or not they were as
         * loaded from disk.  This method can be used to query the state of the
         * original egg file from disk.
         */
        """
        pass

    def read(self, const_EggData_self, Filename_filename, str_display_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read(const EggData self, Filename filename, str display_name)
        read(const EggData self, istream in)
        
        /**
         * Opens the indicated filename and reads the egg data contents from it.
         * Returns true if the file was successfully opened and read, false if there
         * were some errors, in which case the data may be partially read.
         *
         * error is the output stream to which to write error messages.
         */
        
        /**
         * Parses the egg syntax contained in the indicated input stream.  Returns
         * true if the stream was a completely valid egg file, false if there were
         * some errors, in which case the data may be partially read.
         *
         * Before you call this routine, you should probably call set_egg_filename()
         * to set the name of the egg file we're processing, if at all possible.  If
         * there is no such filename, you may set it to the empty string.
         */
        """
        pass

    def recomputePolygonNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        recompute_polygon_normals(const EggData self)
        
        /**
         * Recomputes all the polygon normals for polygon geometry at this group node
         * and below so that they accurately reflect the vertex positions.  Normals
         * are removed from the vertices and defined only on polygons, giving the
         * geometry a faceted appearance.
         *
         * This function also removes degenerate polygons that do not have enough
         * vertices to define a normal.  It does not affect normals for other kinds of
         * primitives like Nurbs or Points.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the normals removed.  Thus, it is a good idea
         * to call remove_unused_vertices() after calling this.
         */
        """
        pass

    def recomputeVertexNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        recompute_vertex_normals(const EggData self, double threshold)
        
        /**
         * Recomputes all the vertex normals for polygon geometry at this group node
         * and below so that they accurately reflect the vertex positions.  A shared
         * edge between two polygons (even in different groups) is considered smooth
         * if the angle between the two edges is less than threshold degrees.
         *
         * This function also removes degenerate polygons that do not have enough
         * vertices to define a normal.  It does not affect normals for other kinds of
         * primitives like Nurbs or Points.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the correct normals.  Thus, it is a good idea
         * to call remove_unused_vertices() after calling this.
         */
        """
        pass

    def recompute_polygon_normals(self, const_EggData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute_polygon_normals(const EggData self)
        
        /**
         * Recomputes all the polygon normals for polygon geometry at this group node
         * and below so that they accurately reflect the vertex positions.  Normals
         * are removed from the vertices and defined only on polygons, giving the
         * geometry a faceted appearance.
         *
         * This function also removes degenerate polygons that do not have enough
         * vertices to define a normal.  It does not affect normals for other kinds of
         * primitives like Nurbs or Points.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the normals removed.  Thus, it is a good idea
         * to call remove_unused_vertices() after calling this.
         */
        """
        pass

    def recompute_vertex_normals(self, const_EggData_self, double_threshold): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute_vertex_normals(const EggData self, double threshold)
        
        /**
         * Recomputes all the vertex normals for polygon geometry at this group node
         * and below so that they accurately reflect the vertex positions.  A shared
         * edge between two polygons (even in different groups) is considered smooth
         * if the angle between the two edges is less than threshold degrees.
         *
         * This function also removes degenerate polygons that do not have enough
         * vertices to define a normal.  It does not affect normals for other kinds of
         * primitives like Nurbs or Points.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the correct normals.  Thus, it is a good idea
         * to call remove_unused_vertices() after calling this.
         */
        """
        pass

    def resolveEggFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        resolve_egg_filename(Filename egg_filename, const DSearchPath searchpath)
        
        /**
         * Looks for the indicated filename, first along the indicated searchpath, and
         * then along the model_path.  If found, updates the filename to the full path
         * and returns true; otherwise, returns false.
         */
        """
        pass

    def resolve_egg_filename(self, Filename_egg_filename, const_DSearchPath_searchpath): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        resolve_egg_filename(Filename egg_filename, const DSearchPath searchpath)
        
        /**
         * Looks for the indicated filename, first along the indicated searchpath, and
         * then along the model_path.  If found, updates the filename to the full path
         * and returns true; otherwise, returns false.
         */
        """
        pass

    def setAutoResolveExternals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_resolve_externals(const EggData self, bool resolve)
        
        /**
         * Indicates whether the EggData object will automatically resolve any
         * external references when read() is called.  The default is false.
         */
        """
        pass

    def setCoordinateSystem(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_coordinate_system(const EggData self, int coordsys)
        
        /**
         * Changes the coordinate system of the EggData.  If the coordinate system was
         * previously different, this may result in a conversion of the data.
         */
        """
        pass

    def setEggFilename(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_egg_filename(const EggData self, const Filename egg_filename)
        
        /**
         * Sets the filename--especially the directory part--in which the egg file is
         * considered to reside.  This is also implicitly set by read().
         */
        """
        pass

    def setEggTimestamp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_egg_timestamp(const EggData self, int egg_timestamp)
        
        /**
         * Sets the timestamp of the egg file on disk, at the time it was opened for
         * reading.  This is also implicitly set by read().
         */
        """
        pass

    def set_auto_resolve_externals(self, const_EggData_self, bool_resolve): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_resolve_externals(const EggData self, bool resolve)
        
        /**
         * Indicates whether the EggData object will automatically resolve any
         * external references when read() is called.  The default is false.
         */
        """
        pass

    def set_coordinate_system(self, const_EggData_self, int_coordsys): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_coordinate_system(const EggData self, int coordsys)
        
        /**
         * Changes the coordinate system of the EggData.  If the coordinate system was
         * previously different, this may result in a conversion of the data.
         */
        """
        pass

    def set_egg_filename(self, const_EggData_self, const_Filename_egg_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_egg_filename(const EggData self, const Filename egg_filename)
        
        /**
         * Sets the filename--especially the directory part--in which the egg file is
         * considered to reside.  This is also implicitly set by read().
         */
        """
        pass

    def set_egg_timestamp(self, const_EggData_self, int_egg_timestamp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_egg_timestamp(const EggData self, int egg_timestamp)
        
        /**
         * Sets the timestamp of the egg file on disk, at the time it was opened for
         * reading.  This is also implicitly set by read().
         */
        """
        pass

    def stripNormals(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        strip_normals(const EggData self)
        
        /**
         * Removes all normals from primitives, and the vertices they reference, at
         * this node and below.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the normal removed.  Thus, it is a good idea to
         * call remove_unused_vertices() after calling this.
         */
        """
        pass

    def strip_normals(self, const_EggData_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        strip_normals(const EggData self)
        
        /**
         * Removes all normals from primitives, and the vertices they reference, at
         * this node and below.
         *
         * This function does not remove or adjust vertices in the vertex pool; it
         * only adds new vertices with the normal removed.  Thus, it is a good idea to
         * call remove_unused_vertices() after calling this.
         */
        """
        pass

    def writeEgg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_egg(const EggData self, ostream out)
        
        /**
         * The main interface for writing complete egg files.
         */
        
        /**
         * The main interface for writing complete egg files.
         */
        """
        pass

    def write_egg(self, const_EggData_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_egg(const EggData self, ostream out)
        
        /**
         * The main interface for writing complete egg files.
         */
        
        /**
         * The main interface for writing complete egg files.
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

    auto_resolve_externals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    coordinate_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    egg_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    egg_timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.egg.EggData' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.egg.EggData' objects>"
        '__doc__': '/**\n * This is the primary interface into all the egg data, and the root of the\n * egg file structure.  An EggData structure corresponds exactly with an egg\n * file on the disk.\n *\n * The EggData class inherits from EggGroupNode its collection of children,\n * which are accessed by using the EggData itself as an STL container with\n * begin() and end() calls.  The children of the EggData class are the\n * toplevel nodes in the egg file.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.egg.EggData' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68CF300>'
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.egg.EggData' objects>"
        'auto_resolve_externals': None, # (!) real value is "<attribute 'auto_resolve_externals' of 'panda3d.egg.EggData' objects>"
        'collapseEquivalentMaterials': None, # (!) real value is "<method 'collapseEquivalentMaterials' of 'panda3d.egg.EggData' objects>"
        'collapseEquivalentTextures': None, # (!) real value is "<method 'collapseEquivalentTextures' of 'panda3d.egg.EggData' objects>"
        'collapse_equivalent_materials': None, # (!) real value is "<method 'collapse_equivalent_materials' of 'panda3d.egg.EggData' objects>"
        'collapse_equivalent_textures': None, # (!) real value is "<method 'collapse_equivalent_textures' of 'panda3d.egg.EggData' objects>"
        'coordinate_system': None, # (!) real value is "<attribute 'coordinate_system' of 'panda3d.egg.EggData' objects>"
        'egg_filename': None, # (!) real value is "<attribute 'egg_filename' of 'panda3d.egg.EggData' objects>"
        'egg_timestamp': None, # (!) real value is "<attribute 'egg_timestamp' of 'panda3d.egg.EggData' objects>"
        'getAutoResolveExternals': None, # (!) real value is "<method 'getAutoResolveExternals' of 'panda3d.egg.EggData' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68CF300>)>'
        'getCoordinateSystem': None, # (!) real value is "<method 'getCoordinateSystem' of 'panda3d.egg.EggData' objects>"
        'getEggFilename': None, # (!) real value is "<method 'getEggFilename' of 'panda3d.egg.EggData' objects>"
        'getEggTimestamp': None, # (!) real value is "<method 'getEggTimestamp' of 'panda3d.egg.EggData' objects>"
        'get_auto_resolve_externals': None, # (!) real value is "<method 'get_auto_resolve_externals' of 'panda3d.egg.EggData' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68CF300>)>'
        'get_coordinate_system': None, # (!) real value is "<method 'get_coordinate_system' of 'panda3d.egg.EggData' objects>"
        'get_egg_filename': None, # (!) real value is "<method 'get_egg_filename' of 'panda3d.egg.EggData' objects>"
        'get_egg_timestamp': None, # (!) real value is "<method 'get_egg_timestamp' of 'panda3d.egg.EggData' objects>"
        'loadExternals': None, # (!) real value is "<method 'loadExternals' of 'panda3d.egg.EggData' objects>"
        'load_externals': None, # (!) real value is "<method 'load_externals' of 'panda3d.egg.EggData' objects>"
        'merge': None, # (!) real value is "<method 'merge' of 'panda3d.egg.EggData' objects>"
        'originalHadAbsolutePathnames': None, # (!) real value is "<method 'originalHadAbsolutePathnames' of 'panda3d.egg.EggData' objects>"
        'original_had_absolute_pathnames': None, # (!) real value is "<method 'original_had_absolute_pathnames' of 'panda3d.egg.EggData' objects>"
        'read': None, # (!) real value is "<method 'read' of 'panda3d.egg.EggData' objects>"
        'recomputePolygonNormals': None, # (!) real value is "<method 'recomputePolygonNormals' of 'panda3d.egg.EggData' objects>"
        'recomputeVertexNormals': None, # (!) real value is "<method 'recomputeVertexNormals' of 'panda3d.egg.EggData' objects>"
        'recompute_polygon_normals': None, # (!) real value is "<method 'recompute_polygon_normals' of 'panda3d.egg.EggData' objects>"
        'recompute_vertex_normals': None, # (!) real value is "<method 'recompute_vertex_normals' of 'panda3d.egg.EggData' objects>"
        'resolveEggFilename': None, # (!) real value is '<staticmethod(<built-in method resolveEggFilename of type object at 0x00007FFDC68CF300>)>'
        'resolve_egg_filename': None, # (!) real value is '<staticmethod(<built-in method resolve_egg_filename of type object at 0x00007FFDC68CF300>)>'
        'setAutoResolveExternals': None, # (!) real value is "<method 'setAutoResolveExternals' of 'panda3d.egg.EggData' objects>"
        'setCoordinateSystem': None, # (!) real value is "<method 'setCoordinateSystem' of 'panda3d.egg.EggData' objects>"
        'setEggFilename': None, # (!) real value is "<method 'setEggFilename' of 'panda3d.egg.EggData' objects>"
        'setEggTimestamp': None, # (!) real value is "<method 'setEggTimestamp' of 'panda3d.egg.EggData' objects>"
        'set_auto_resolve_externals': None, # (!) real value is "<method 'set_auto_resolve_externals' of 'panda3d.egg.EggData' objects>"
        'set_coordinate_system': None, # (!) real value is "<method 'set_coordinate_system' of 'panda3d.egg.EggData' objects>"
        'set_egg_filename': None, # (!) real value is "<method 'set_egg_filename' of 'panda3d.egg.EggData' objects>"
        'set_egg_timestamp': None, # (!) real value is "<method 'set_egg_timestamp' of 'panda3d.egg.EggData' objects>"
        'stripNormals': None, # (!) real value is "<method 'stripNormals' of 'panda3d.egg.EggData' objects>"
        'strip_normals': None, # (!) real value is "<method 'strip_normals' of 'panda3d.egg.EggData' objects>"
        'writeEgg': None, # (!) real value is "<method 'writeEgg' of 'panda3d.egg.EggData' objects>"
        'write_egg': None, # (!) real value is "<method 'write_egg' of 'panda3d.egg.EggData' objects>"
    }


