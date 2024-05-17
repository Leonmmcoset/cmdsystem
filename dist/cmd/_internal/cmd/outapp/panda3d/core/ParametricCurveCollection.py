# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .ReferenceCount import ReferenceCount

class ParametricCurveCollection(ReferenceCount):
    """
    /**
     * This is a set of zero or more ParametricCurves, which may or may not be
     * related.  If they are related, the set should contain no more than one XYZ
     * curve, no more than one HPR curve, and zero or more Timewarp curves, which
     * can then be evaluated as a unit to return a single transformation matrix
     * for a given unit of time.
     */
    """
    def addCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_curve(const ParametricCurveCollection self, ParametricCurve curve)
        add_curve(const ParametricCurveCollection self, ParametricCurve curve, int index)
        
        /**
         * Adds a new ParametricCurve to the collection at the indicated index.
         * @deprecated Use insert_curve(index, curve) instead.
         */
        
        /**
         * Adds a new ParametricCurve to the collection.
         */
        """
        pass

    def addCurves(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_curves(const ParametricCurveCollection self, PandaNode node)
        
        /**
         * Adds all the curves found in the scene graph rooted at the given node.
         * Returns the number of curves found.
         */
        """
        pass

    def add_curve(self, const_ParametricCurveCollection_self, ParametricCurve_curve): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_curve(const ParametricCurveCollection self, ParametricCurve curve)
        add_curve(const ParametricCurveCollection self, ParametricCurve curve, int index)
        
        /**
         * Adds a new ParametricCurve to the collection at the indicated index.
         * @deprecated Use insert_curve(index, curve) instead.
         */
        
        /**
         * Adds a new ParametricCurve to the collection.
         */
        """
        pass

    def add_curves(self, const_ParametricCurveCollection_self, PandaNode_node): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_curves(const ParametricCurveCollection self, PandaNode node)
        
        /**
         * Adds all the curves found in the scene graph rooted at the given node.
         * Returns the number of curves found.
         */
        """
        pass

    def adjustHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        adjust_hpr(const ParametricCurveCollection self, float t, const LVecBase3f xyz)
        adjust_hpr(const ParametricCurveCollection self, float t, float h, float p, float r)
        
        /**
         * Adjust the HPR curve at the indicated time to the new value.  The curve
         * shape will change correspondingly.  Returns true if successful, false if
         * unable to make the adjustment for some reason.
         */
        
        /**
         * Adjust the HPR curve at the indicated time to the new value.  The curve
         * shape will change correspondingly.  Returns true if successful, false if
         * unable to make the adjustment for some reason.
         */
        """
        pass

    def adjustXyz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        adjust_xyz(const ParametricCurveCollection self, float t, const LVecBase3f xyz)
        adjust_xyz(const ParametricCurveCollection self, float t, float x, float y, float z)
        
        /**
         * Adjust the XYZ curve at the indicated time to the new value.  The curve
         * shape will change correspondingly.  Returns true if successful, false if
         * unable to make the adjustment for some reason.
         */
        
        /**
         * Adjust the XYZ curve at the indicated time to the new value.  The curve
         * shape will change correspondingly.  Returns true if successful, false if
         * unable to make the adjustment for some reason.
         */
        """
        pass

    def adjust_hpr(self, const_ParametricCurveCollection_self, float_t, const_LVecBase3f_xyz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        adjust_hpr(const ParametricCurveCollection self, float t, const LVecBase3f xyz)
        adjust_hpr(const ParametricCurveCollection self, float t, float h, float p, float r)
        
        /**
         * Adjust the HPR curve at the indicated time to the new value.  The curve
         * shape will change correspondingly.  Returns true if successful, false if
         * unable to make the adjustment for some reason.
         */
        
        /**
         * Adjust the HPR curve at the indicated time to the new value.  The curve
         * shape will change correspondingly.  Returns true if successful, false if
         * unable to make the adjustment for some reason.
         */
        """
        pass

    def adjust_xyz(self, const_ParametricCurveCollection_self, float_t, const_LVecBase3f_xyz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        adjust_xyz(const ParametricCurveCollection self, float t, const LVecBase3f xyz)
        adjust_xyz(const ParametricCurveCollection self, float t, float x, float y, float z)
        
        /**
         * Adjust the XYZ curve at the indicated time to the new value.  The curve
         * shape will change correspondingly.  Returns true if successful, false if
         * unable to make the adjustment for some reason.
         */
        
        /**
         * Adjust the XYZ curve at the indicated time to the new value.  The curve
         * shape will change correspondingly.  Returns true if successful, false if
         * unable to make the adjustment for some reason.
         */
        """
        pass

    def clear(self, const_ParametricCurveCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const ParametricCurveCollection self)
        
        /**
         * Removes all ParametricCurves from the collection.
         */
        """
        pass

    def clearTimewarps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_timewarps(const ParametricCurveCollection self)
        
        /**
         * Removes all the timewarp curves from the collection.
         */
        """
        pass

    def clear_timewarps(self, const_ParametricCurveCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_timewarps(const ParametricCurveCollection self)
        
        /**
         * Removes all the timewarp curves from the collection.
         */
        """
        pass

    def evaluate(self, ParametricCurveCollection_self, float_t, LMatrix4f_result): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evaluate(ParametricCurveCollection self, float t, LMatrix4f result)
        evaluate(ParametricCurveCollection self, float t, LVecBase3f xyz, LVecBase3f hpr)
        evaluate(ParametricCurveCollection self, float t, LMatrix4f result, int cs)
        
        /**
         * Computes the position and rotation represented by the first XYZ and HPR
         * curves in the collection at the given point t, after t has been modified by
         * all the timewarp curves in the collection applied in sequence, from back to
         * front.
         *
         * Returns true if the point is valid (i.e.  t is within the bounds indicated
         * by all the timewarp curves and within the bounds of the curves themselves),
         * or false otherwise.
         */
        
        /**
         * Computes the transform matrix representing translation to the position
         * indicated by the first XYZ curve in the collection and the rotation
         * indicated by the first HPR curve in the collection, after t has been
         * modified by all the timewarp curves in the collection applied in sequence,
         * from back to front.
         *
         * Returns true if the point is valid (i.e.  t is within the bounds indicated
         * by all the timewarp curves and within the bounds of the curves themselves),
         * or false otherwise.
         */
        """
        pass

    def evaluateHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        evaluate_hpr(ParametricCurveCollection self, float t, LVecBase3f hpr)
        
        /**
         * Computes only the HPR part of the curves.  See evaluate().
         */
        """
        pass

    def evaluateT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        evaluate_t(ParametricCurveCollection self, float t)
        
        /**
         * Determines the value of t that should be passed to the XYZ and HPR curves,
         * after applying the given value of t to all the timewarps.  Return -1.0f if
         * the value of t exceeds one of the timewarps' ranges.
         */
        """
        pass

    def evaluateXyz(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        evaluate_xyz(ParametricCurveCollection self, float t, LVecBase3f xyz)
        
        /**
         * Computes only the XYZ part of the curves.  See evaluate().
         */
        """
        pass

    def evaluate_hpr(self, ParametricCurveCollection_self, float_t, LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evaluate_hpr(ParametricCurveCollection self, float t, LVecBase3f hpr)
        
        /**
         * Computes only the HPR part of the curves.  See evaluate().
         */
        """
        pass

    def evaluate_t(self, ParametricCurveCollection_self, float_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evaluate_t(ParametricCurveCollection self, float t)
        
        /**
         * Determines the value of t that should be passed to the XYZ and HPR curves,
         * after applying the given value of t to all the timewarps.  Return -1.0f if
         * the value of t exceeds one of the timewarps' ranges.
         */
        """
        pass

    def evaluate_xyz(self, ParametricCurveCollection_self, float_t, LVecBase3f_xyz): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        evaluate_xyz(ParametricCurveCollection self, float t, LVecBase3f xyz)
        
        /**
         * Computes only the XYZ part of the curves.  See evaluate().
         */
        """
        pass

    def faceForward(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        face_forward(const ParametricCurveCollection self, float segments_per_unit)
        
        /**
         * Discards the existing HPR curve and generates a new one that looks in the
         * direction of travel along the XYZ curve, based on the XYZ curve's tangent
         * at each point.
         */
        """
        pass

    def face_forward(self, const_ParametricCurveCollection_self, float_segments_per_unit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        face_forward(const ParametricCurveCollection self, float segments_per_unit)
        
        /**
         * Discards the existing HPR curve and generates a new one that looks in the
         * direction of travel along the XYZ curve, based on the XYZ curve's tangent
         * at each point.
         */
        """
        pass

    def getCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_curve(ParametricCurveCollection self, int index)
        
        /**
         * Returns the nth ParametricCurve in the collection.
         */
        """
        pass

    def getCurves(self, *args, **kwargs): # real signature unknown
        pass

    def getDefaultCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_curve(ParametricCurveCollection self)
        
        /**
         * If there is an XYZ curve in the collection, returns it; otherwise, returns
         * the first curve whose type is unspecified.  Returns NULL if no curve meets
         * the criteria.
         */
        """
        pass

    def getHprCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hpr_curve(ParametricCurveCollection self)
        
        /**
         * Returns the first HPR curve in the collection, if any, or NULL if there are
         * none.
         */
        """
        pass

    def getMaxT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_max_t(ParametricCurveCollection self)
        
        /**
         * Returns the maximum T value associated with the *last* curve in the
         * collection.  Normally, this will be either the XYZ or HPR curve, or a
         * timewarp curve.
         */
        """
        pass

    def getNumCurves(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_curves(ParametricCurveCollection self)
        
        /**
         * Returns the number of ParametricCurves in the collection.
         */
        """
        pass

    def getNumTimewarps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_timewarps(ParametricCurveCollection self)
        
        /**
         * Returns the number of timewarp curves in the collection.
         */
        """
        pass

    def getTimewarpCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_timewarp_curve(ParametricCurveCollection self, int n)
        
        /**
         * Returns the nth timewarp curve in the collection.
         */
        """
        pass

    def getTimewarpCurves(self, *args, **kwargs): # real signature unknown
        pass

    def getXyzCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_xyz_curve(ParametricCurveCollection self)
        
        /**
         * Returns the first XYZ curve in the collection, if any, or NULL if there are
         * none.
         */
        """
        pass

    def get_curve(self, ParametricCurveCollection_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_curve(ParametricCurveCollection self, int index)
        
        /**
         * Returns the nth ParametricCurve in the collection.
         */
        """
        pass

    def get_curves(self, *args, **kwargs): # real signature unknown
        pass

    def get_default_curve(self, ParametricCurveCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_curve(ParametricCurveCollection self)
        
        /**
         * If there is an XYZ curve in the collection, returns it; otherwise, returns
         * the first curve whose type is unspecified.  Returns NULL if no curve meets
         * the criteria.
         */
        """
        pass

    def get_hpr_curve(self, ParametricCurveCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hpr_curve(ParametricCurveCollection self)
        
        /**
         * Returns the first HPR curve in the collection, if any, or NULL if there are
         * none.
         */
        """
        pass

    def get_max_t(self, ParametricCurveCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_max_t(ParametricCurveCollection self)
        
        /**
         * Returns the maximum T value associated with the *last* curve in the
         * collection.  Normally, this will be either the XYZ or HPR curve, or a
         * timewarp curve.
         */
        """
        pass

    def get_num_curves(self, ParametricCurveCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_curves(ParametricCurveCollection self)
        
        /**
         * Returns the number of ParametricCurves in the collection.
         */
        """
        pass

    def get_num_timewarps(self, ParametricCurveCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_timewarps(ParametricCurveCollection self)
        
        /**
         * Returns the number of timewarp curves in the collection.
         */
        """
        pass

    def get_timewarp_curve(self, ParametricCurveCollection_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_timewarp_curve(ParametricCurveCollection self, int n)
        
        /**
         * Returns the nth timewarp curve in the collection.
         */
        """
        pass

    def get_timewarp_curves(self, *args, **kwargs): # real signature unknown
        pass

    def get_xyz_curve(self, ParametricCurveCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_xyz_curve(ParametricCurveCollection self)
        
        /**
         * Returns the first XYZ curve in the collection, if any, or NULL if there are
         * none.
         */
        """
        pass

    def hasCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_curve(ParametricCurveCollection self, ParametricCurve curve)
        
        /**
         * Returns true if the indicated ParametricCurve appears in this collection,
         * false otherwise.
         */
        """
        pass

    def has_curve(self, ParametricCurveCollection_self, ParametricCurve_curve): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_curve(ParametricCurveCollection self, ParametricCurve curve)
        
        /**
         * Returns true if the indicated ParametricCurve appears in this collection,
         * false otherwise.
         */
        """
        pass

    def insertCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        insert_curve(const ParametricCurveCollection self, int index, ParametricCurve curve)
        
        /**
         * Adds a new ParametricCurve to the collection at the indicated index.
         */
        """
        pass

    def insert_curve(self, const_ParametricCurveCollection_self, int_index, ParametricCurve_curve): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        insert_curve(const ParametricCurveCollection self, int index, ParametricCurve curve)
        
        /**
         * Adds a new ParametricCurve to the collection at the indicated index.
         */
        """
        pass

    def makeEven(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_even(const ParametricCurveCollection self, float max_t, float segments_per_unit)
        
        /**
         * Discards all existing timewarp curves and recomputes a new timewarp curve
         * that maps distance along the curve to parametric time, so that the distance
         * between any two points in parametric time is proportional to the
         * approximate distance of those same two points along the XYZ curve.
         *
         * segments_per_unit represents the number of segments to take per each unit
         * of parametric time of the original XYZ curve.
         *
         * The new timewarp curve (and thus, the apparent range of the collection)
         * will range from 0 to max_t.
         */
        """
        pass

    def make_even(self, const_ParametricCurveCollection_self, float_max_t, float_segments_per_unit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_even(const ParametricCurveCollection self, float max_t, float segments_per_unit)
        
        /**
         * Discards all existing timewarp curves and recomputes a new timewarp curve
         * that maps distance along the curve to parametric time, so that the distance
         * between any two points in parametric time is proportional to the
         * approximate distance of those same two points along the XYZ curve.
         *
         * segments_per_unit represents the number of segments to take per each unit
         * of parametric time of the original XYZ curve.
         *
         * The new timewarp curve (and thus, the apparent range of the collection)
         * will range from 0 to max_t.
         */
        """
        pass

    def output(self, ParametricCurveCollection_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ParametricCurveCollection self, ostream out)
        
        /**
         * Writes a brief one-line description of the ParametricCurveCollection to the
         * indicated output stream.
         */
        """
        pass

    def recompute(self, const_ParametricCurveCollection_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        recompute(const ParametricCurveCollection self)
        
        /**
         * Ensures all the curves are freshly computed and up-to-date.  Returns true
         * if everything is valid, false if at least one curve is incorrect.
         */
        """
        pass

    def removeCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_curve(const ParametricCurveCollection self, ParametricCurve curve)
        remove_curve(const ParametricCurveCollection self, int index)
        
        /**
         * Removes the indicated ParametricCurve from the collection.  Returns true if
         * the curve was removed, false if it was not a member of the collection.
         */
        
        /**
         * Removes the indicated ParametricCurve from the collection, by its index
         * number.
         */
        """
        pass

    def remove_curve(self, const_ParametricCurveCollection_self, ParametricCurve_curve): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_curve(const ParametricCurveCollection self, ParametricCurve curve)
        remove_curve(const ParametricCurveCollection self, int index)
        
        /**
         * Removes the indicated ParametricCurve from the collection.  Returns true if
         * the curve was removed, false if it was not a member of the collection.
         */
        
        /**
         * Removes the indicated ParametricCurve from the collection, by its index
         * number.
         */
        """
        pass

    def resetMaxT(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        reset_max_t(const ParametricCurveCollection self, float max_t)
        
        /**
         * Adjusts the apparent length of the curve by applying a new timewarp that
         * maps the range [0..max_t] to the range [0..get_max_t()].  After this call,
         * the curve collection will contain one more timewarp curve, and get_max_t()
         * will return the given max_t value.
         */
        """
        pass

    def reset_max_t(self, const_ParametricCurveCollection_self, float_max_t): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        reset_max_t(const ParametricCurveCollection self, float max_t)
        
        /**
         * Adjusts the apparent length of the curve by applying a new timewarp that
         * maps the range [0..max_t] to the range [0..get_max_t()].  After this call,
         * the curve collection will contain one more timewarp curve, and get_max_t()
         * will return the given max_t value.
         */
        """
        pass

    def setCurve(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_curve(const ParametricCurveCollection self, int index, ParametricCurve curve)
        
        /**
         * Replaces the indicated ParametricCurve from the collection, by its index
         * number.
         */
        """
        pass

    def set_curve(self, const_ParametricCurveCollection_self, int_index, ParametricCurve_curve): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_curve(const ParametricCurveCollection self, int index, ParametricCurve curve)
        
        /**
         * Replaces the indicated ParametricCurve from the collection, by its index
         * number.
         */
        """
        pass

    def stitch(self, const_ParametricCurveCollection_self, const_ParametricCurveCollection_a, const_ParametricCurveCollection_b): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        stitch(const ParametricCurveCollection self, const ParametricCurveCollection a, const ParametricCurveCollection b)
        
        /**
         * Regenerates this curve as one long curve: the first curve connected end-to-
         * end with the second one.  Either a or b may be the same as 'this'.  This
         * will lose any timewarps on the input curves.
         *
         * Returns true if successful, false on failure.
         */
        """
        pass

    def write(self, ParametricCurveCollection_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ParametricCurveCollection self, ostream out, int indent_level)
        
        /**
         * Writes a complete multi-line description of the ParametricCurveCollection
         * to the indicated output stream.
         */
        """
        pass

    def writeEgg(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_egg(const ParametricCurveCollection self, Filename filename)
        write_egg(const ParametricCurveCollection self, Filename filename, int cs)
        write_egg(const ParametricCurveCollection self, ostream out, const Filename filename, int cs)
        
        /**
         * Writes an egg description of all the nurbs curves in the collection to the
         * specified output file.  Returns true if the file is successfully written.
         */
        
        /**
         * Writes an egg description of all the nurbs curves in the collection to the
         * specified output stream.  Returns true if the file is successfully written.
         */
        """
        pass

    def write_egg(self, const_ParametricCurveCollection_self, Filename_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_egg(const ParametricCurveCollection self, Filename filename)
        write_egg(const ParametricCurveCollection self, Filename filename, int cs)
        write_egg(const ParametricCurveCollection self, ostream out, const Filename filename, int cs)
        
        /**
         * Writes an egg description of all the nurbs curves in the collection to the
         * specified output file.  Returns true if the file is successfully written.
         */
        
        /**
         * Writes an egg description of all the nurbs curves in the collection to the
         * specified output stream.  Returns true if the file is successfully written.
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

    curves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hpr_curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_t = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timewarp_curves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xyz_curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ParametricCurveCollection' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ParametricCurveCollection' objects>"
        '__doc__': '/**\n * This is a set of zero or more ParametricCurves, which may or may not be\n * related.  If they are related, the set should contain no more than one XYZ\n * curve, no more than one HPR curve, and zero or more Timewarp curves, which\n * can then be evaluated as a unit to return a single transformation matrix\n * for a given unit of time.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ParametricCurveCollection' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE34E250>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ParametricCurveCollection' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ParametricCurveCollection' objects>"
        'addCurve': None, # (!) real value is "<method 'addCurve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'addCurves': None, # (!) real value is "<method 'addCurves' of 'panda3d.core.ParametricCurveCollection' objects>"
        'add_curve': None, # (!) real value is "<method 'add_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'add_curves': None, # (!) real value is "<method 'add_curves' of 'panda3d.core.ParametricCurveCollection' objects>"
        'adjustHpr': None, # (!) real value is "<method 'adjustHpr' of 'panda3d.core.ParametricCurveCollection' objects>"
        'adjustXyz': None, # (!) real value is "<method 'adjustXyz' of 'panda3d.core.ParametricCurveCollection' objects>"
        'adjust_hpr': None, # (!) real value is "<method 'adjust_hpr' of 'panda3d.core.ParametricCurveCollection' objects>"
        'adjust_xyz': None, # (!) real value is "<method 'adjust_xyz' of 'panda3d.core.ParametricCurveCollection' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.ParametricCurveCollection' objects>"
        'clearTimewarps': None, # (!) real value is "<method 'clearTimewarps' of 'panda3d.core.ParametricCurveCollection' objects>"
        'clear_timewarps': None, # (!) real value is "<method 'clear_timewarps' of 'panda3d.core.ParametricCurveCollection' objects>"
        'curves': None, # (!) real value is "<attribute 'curves' of 'panda3d.core.ParametricCurveCollection' objects>"
        'default_curve': None, # (!) real value is "<attribute 'default_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'evaluate': None, # (!) real value is "<method 'evaluate' of 'panda3d.core.ParametricCurveCollection' objects>"
        'evaluateHpr': None, # (!) real value is "<method 'evaluateHpr' of 'panda3d.core.ParametricCurveCollection' objects>"
        'evaluateT': None, # (!) real value is "<method 'evaluateT' of 'panda3d.core.ParametricCurveCollection' objects>"
        'evaluateXyz': None, # (!) real value is "<method 'evaluateXyz' of 'panda3d.core.ParametricCurveCollection' objects>"
        'evaluate_hpr': None, # (!) real value is "<method 'evaluate_hpr' of 'panda3d.core.ParametricCurveCollection' objects>"
        'evaluate_t': None, # (!) real value is "<method 'evaluate_t' of 'panda3d.core.ParametricCurveCollection' objects>"
        'evaluate_xyz': None, # (!) real value is "<method 'evaluate_xyz' of 'panda3d.core.ParametricCurveCollection' objects>"
        'faceForward': None, # (!) real value is "<method 'faceForward' of 'panda3d.core.ParametricCurveCollection' objects>"
        'face_forward': None, # (!) real value is "<method 'face_forward' of 'panda3d.core.ParametricCurveCollection' objects>"
        'getCurve': None, # (!) real value is "<method 'getCurve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'getCurves': None, # (!) real value is "<method 'getCurves' of 'panda3d.core.ParametricCurveCollection' objects>"
        'getDefaultCurve': None, # (!) real value is "<method 'getDefaultCurve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'getHprCurve': None, # (!) real value is "<method 'getHprCurve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'getMaxT': None, # (!) real value is "<method 'getMaxT' of 'panda3d.core.ParametricCurveCollection' objects>"
        'getNumCurves': None, # (!) real value is "<method 'getNumCurves' of 'panda3d.core.ParametricCurveCollection' objects>"
        'getNumTimewarps': None, # (!) real value is "<method 'getNumTimewarps' of 'panda3d.core.ParametricCurveCollection' objects>"
        'getTimewarpCurve': None, # (!) real value is "<method 'getTimewarpCurve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'getTimewarpCurves': None, # (!) real value is "<method 'getTimewarpCurves' of 'panda3d.core.ParametricCurveCollection' objects>"
        'getXyzCurve': None, # (!) real value is "<method 'getXyzCurve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'get_curve': None, # (!) real value is "<method 'get_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'get_curves': None, # (!) real value is "<method 'get_curves' of 'panda3d.core.ParametricCurveCollection' objects>"
        'get_default_curve': None, # (!) real value is "<method 'get_default_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'get_hpr_curve': None, # (!) real value is "<method 'get_hpr_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'get_max_t': None, # (!) real value is "<method 'get_max_t' of 'panda3d.core.ParametricCurveCollection' objects>"
        'get_num_curves': None, # (!) real value is "<method 'get_num_curves' of 'panda3d.core.ParametricCurveCollection' objects>"
        'get_num_timewarps': None, # (!) real value is "<method 'get_num_timewarps' of 'panda3d.core.ParametricCurveCollection' objects>"
        'get_timewarp_curve': None, # (!) real value is "<method 'get_timewarp_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'get_timewarp_curves': None, # (!) real value is "<method 'get_timewarp_curves' of 'panda3d.core.ParametricCurveCollection' objects>"
        'get_xyz_curve': None, # (!) real value is "<method 'get_xyz_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'hasCurve': None, # (!) real value is "<method 'hasCurve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'has_curve': None, # (!) real value is "<method 'has_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'hpr_curve': None, # (!) real value is "<attribute 'hpr_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'insertCurve': None, # (!) real value is "<method 'insertCurve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'insert_curve': None, # (!) real value is "<method 'insert_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'makeEven': None, # (!) real value is "<method 'makeEven' of 'panda3d.core.ParametricCurveCollection' objects>"
        'make_even': None, # (!) real value is "<method 'make_even' of 'panda3d.core.ParametricCurveCollection' objects>"
        'max_t': None, # (!) real value is "<attribute 'max_t' of 'panda3d.core.ParametricCurveCollection' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ParametricCurveCollection' objects>"
        'recompute': None, # (!) real value is "<method 'recompute' of 'panda3d.core.ParametricCurveCollection' objects>"
        'removeCurve': None, # (!) real value is "<method 'removeCurve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'remove_curve': None, # (!) real value is "<method 'remove_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'resetMaxT': None, # (!) real value is "<method 'resetMaxT' of 'panda3d.core.ParametricCurveCollection' objects>"
        'reset_max_t': None, # (!) real value is "<method 'reset_max_t' of 'panda3d.core.ParametricCurveCollection' objects>"
        'setCurve': None, # (!) real value is "<method 'setCurve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'set_curve': None, # (!) real value is "<method 'set_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
        'stitch': None, # (!) real value is "<method 'stitch' of 'panda3d.core.ParametricCurveCollection' objects>"
        'timewarp_curves': None, # (!) real value is "<attribute 'timewarp_curves' of 'panda3d.core.ParametricCurveCollection' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ParametricCurveCollection' objects>"
        'writeEgg': None, # (!) real value is "<method 'writeEgg' of 'panda3d.core.ParametricCurveCollection' objects>"
        'write_egg': None, # (!) real value is "<method 'write_egg' of 'panda3d.core.ParametricCurveCollection' objects>"
        'xyz_curve': None, # (!) real value is "<attribute 'xyz_curve' of 'panda3d.core.ParametricCurveCollection' objects>"
    }


