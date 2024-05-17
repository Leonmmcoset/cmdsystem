# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .CLerpInterval import CLerpInterval

class CLerpNodePathInterval(CLerpInterval):
    """
    /**
     * An interval that lerps one or more properties (like pos, hpr, etc.) on a
     * NodePath over time.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_node(CLerpNodePathInterval self)
        
        /**
         * Returns the node being lerped.
         */
        """
        pass

    def getOther(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_other(CLerpNodePathInterval self)
        
        /**
         * Returns the "other" node, which the lerped node is being moved relative to.
         * If this is an empty node path, the lerped node is being moved in its own
         * coordinate system.
         */
        """
        pass

    def getOverride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_override(CLerpNodePathInterval self)
        
        /**
         * Returns the override value that will be associated with any state changes
         * applied by the lerp.  See set_override().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_node(self, CLerpNodePathInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_node(CLerpNodePathInterval self)
        
        /**
         * Returns the node being lerped.
         */
        """
        pass

    def get_other(self, CLerpNodePathInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_other(CLerpNodePathInterval self)
        
        /**
         * Returns the "other" node, which the lerped node is being moved relative to.
         * If this is an empty node path, the lerped node is being moved in its own
         * coordinate system.
         */
        """
        pass

    def get_override(self, CLerpNodePathInterval_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_override(CLerpNodePathInterval self)
        
        /**
         * Returns the override value that will be associated with any state changes
         * applied by the lerp.  See set_override().
         */
        """
        pass

    def setEndColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_end_color(const CLerpNodePathInterval self, const LVecBase4f color)
        
        /**
         * Indicates that the color of the node should be lerped, and specifies the
         * final color of the node.  This should be called before priv_initialize().
         * If this is not called, the node's color will not be affected by the lerp.
         */
        """
        pass

    def setEndColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_end_color_scale(const CLerpNodePathInterval self, const LVecBase4f color_scale)
        
        /**
         * Indicates that the color scale of the node should be lerped, and specifies
         * the final color scale of the node.  This should be called before
         * priv_initialize().  If this is not called, the node's color scale will not
         * be affected by the lerp.
         */
        """
        pass

    def setEndHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_end_hpr(const CLerpNodePathInterval self, const LQuaternionf quat)
        set_end_hpr(const CLerpNodePathInterval self, const LVecBase3f hpr)
        
        /**
         * Indicates that the rotation of the node should be lerped, and specifies the
         * final rotation of the node.  This should be called before
         * priv_initialize().
         *
         * This replaces a previous call to set_end_quat().  If neither set_end_hpr()
         * nor set_end_quat() is called, the node's rotation will not be affected by
         * the lerp.
         */
        
        /**
         * Indicates that the rotation of the node should be lerped, and specifies the
         * final rotation of the node.  This should be called before
         * priv_initialize().
         *
         * This special function is overloaded to accept a quaternion, even though the
         * function name is set_end_hpr().  The quaternion will be implicitly
         * converted to a HPR trio, and the lerp will be performed in HPR space,
         * componentwise.
         */
        """
        pass

    def setEndPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_end_pos(const CLerpNodePathInterval self, const LVecBase3f pos)
        
        /**
         * Indicates that the position of the node should be lerped, and specifies the
         * final position of the node.  This should be called before
         * priv_initialize().  If this is not called, the node's position will not be
         * affected by the lerp.
         */
        """
        pass

    def setEndQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_end_quat(const CLerpNodePathInterval self, const LQuaternionf quat)
        set_end_quat(const CLerpNodePathInterval self, const LVecBase3f hpr)
        
        /**
         * Indicates that the rotation of the node should be lerped, and specifies the
         * final rotation of the node.  This should be called before
         * priv_initialize().
         *
         * This replaces a previous call to set_end_hpr().  If neither set_end_quat()
         * nor set_end_hpr() is called, the node's rotation will not be affected by
         * the lerp.
         *
         * This special function is overloaded to accept a HPR trio, even though the
         * function name is set_end_quat().  The HPR will be implicitly converted to a
         * quaternion, and the lerp will be performed in quaternion space, as a
         * spherical lerp.
         */
        
        /**
         * Indicates that the rotation of the node should be lerped, and specifies the
         * final rotation of the node.  This should be called before
         * priv_initialize().
         *
         * This replaces a previous call to set_end_hpr().  If neither set_end_quat()
         * nor set_end_hpr() is called, the node's rotation will not be affected by
         * the lerp.
         *
         * The given quaternion needs to be normalized.
         */
        """
        pass

    def setEndScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_end_scale(const CLerpNodePathInterval self, const LVecBase3f scale)
        set_end_scale(const CLerpNodePathInterval self, float scale)
        
        /**
         * Indicates that the scale of the node should be lerped, and specifies the
         * final scale of the node.  This should be called before priv_initialize().
         * If this is not called, the node's scale will not be affected by the lerp.
         */
        
        /**
         * Indicates that the scale of the node should be lerped, and specifies the
         * final scale of the node.  This should be called before priv_initialize().
         * If this is not called, the node's scale will not be affected by the lerp.
         */
        """
        pass

    def setEndShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_end_shear(const CLerpNodePathInterval self, const LVecBase3f shear)
        
        /**
         * Indicates that the shear of the node should be lerped, and specifies the
         * final shear of the node.  This should be called before priv_initialize().
         * If this is not called, the node's shear will not be affected by the lerp.
         */
        """
        pass

    def setEndTexOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_end_tex_offset(const CLerpNodePathInterval self, const LVecBase2f tex_offset)
        
        /**
         * Indicates that the UV offset of the node should be lerped, and specifies
         * the final UV offset of the node.  This should be called before
         * priv_initialize().  If this is not called, the node's UV offset will not be
         * affected by the lerp.
         */
        """
        pass

    def setEndTexRotate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_end_tex_rotate(const CLerpNodePathInterval self, float tex_rotate)
        
        /**
         * Indicates that the UV rotate of the node should be lerped, and specifies
         * the final UV rotate of the node.  This should be called before
         * priv_initialize().  If this is not called, the node's UV rotate will not be
         * affected by the lerp.
         */
        """
        pass

    def setEndTexScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_end_tex_scale(const CLerpNodePathInterval self, const LVecBase2f tex_scale)
        
        /**
         * Indicates that the UV scale of the node should be lerped, and specifies the
         * final UV scale of the node.  This should be called before
         * priv_initialize().  If this is not called, the node's UV scale will not be
         * affected by the lerp.
         */
        """
        pass

    def setOverride(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_override(const CLerpNodePathInterval self, int override)
        
        /**
         * Changes the override value that will be associated with any state changes
         * applied by the lerp.  If this lerp is changing state (for instance, a color
         * lerp or a tex matrix lerp), then the new attributes created by this lerp
         * will be assigned the indicated override value when they are applied to the
         * node.
         */
        """
        pass

    def setStartColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_color(const CLerpNodePathInterval self, const LVecBase4f color)
        
        /**
         * Indicates the initial color of the lerped node.  This is meaningful only if
         * set_end_color() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual color at the
         * time the lerp is performed.
         */
        """
        pass

    def setStartColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_color_scale(const CLerpNodePathInterval self, const LVecBase4f color_scale)
        
        /**
         * Indicates the initial color scale of the lerped node.  This is meaningful
         * only if set_end_color_scale() is also called.  This parameter is optional;
         * if unspecified, the value will be taken from the node's actual color scale
         * at the time the lerp is performed.
         */
        """
        pass

    def setStartHpr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_hpr(const CLerpNodePathInterval self, const LVecBase3f hpr)
        
        /**
         * Indicates the initial rotation of the lerped node.  This is meaningful only
         * if either set_end_hpr() or set_end_quat() is also called.  This parameter
         * is optional; if unspecified, the value will be taken from the node's actual
         * rotation at the time the lerp is performed.
         */
        """
        pass

    def setStartPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_pos(const CLerpNodePathInterval self, const LVecBase3f pos)
        
        /**
         * Indicates the initial position of the lerped node.  This is meaningful only
         * if set_end_pos() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual position at the
         * time the lerp is performed.
         */
        """
        pass

    def setStartQuat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_quat(const CLerpNodePathInterval self, const LQuaternionf quat)
        
        /**
         * Indicates the initial rotation of the lerped node.  This is meaningful only
         * if either set_end_quat() or set_end_hpr() is also called.  This parameter
         * is optional; if unspecified, the value will be taken from the node's actual
         * rotation at the time the lerp is performed.
         *
         * The given quaternion needs to be normalized.
         */
        """
        pass

    def setStartScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_scale(const CLerpNodePathInterval self, const LVecBase3f scale)
        set_start_scale(const CLerpNodePathInterval self, float scale)
        
        /**
         * Indicates the initial scale of the lerped node.  This is meaningful only if
         * set_end_scale() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual scale at the
         * time the lerp is performed.
         */
        
        /**
         * Indicates the initial scale of the lerped node.  This is meaningful only if
         * set_end_scale() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual scale at the
         * time the lerp is performed.
         */
        """
        pass

    def setStartShear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_shear(const CLerpNodePathInterval self, const LVecBase3f shear)
        
        /**
         * Indicates the initial shear of the lerped node.  This is meaningful only if
         * set_end_shear() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual shear at the
         * time the lerp is performed.
         */
        """
        pass

    def setStartTexOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_tex_offset(const CLerpNodePathInterval self, const LVecBase2f tex_offset)
        
        /**
         * Indicates the initial UV offset of the lerped node.  This is meaningful
         * only if set_end_tex_offset() is also called.  This parameter is optional;
         * if unspecified, the value will be taken from the node's actual UV offset at
         * the time the lerp is performed.
         */
        """
        pass

    def setStartTexRotate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_tex_rotate(const CLerpNodePathInterval self, float tex_rotate)
        
        /**
         * Indicates the initial UV rotate of the lerped node.  This is meaningful
         * only if set_end_tex_rotate() is also called.  This parameter is optional;
         * if unspecified, the value will be taken from the node's actual UV rotate at
         * the time the lerp is performed.
         */
        """
        pass

    def setStartTexScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_start_tex_scale(const CLerpNodePathInterval self, const LVecBase2f tex_scale)
        
        /**
         * Indicates the initial UV scale of the lerped node.  This is meaningful only
         * if set_end_tex_scale() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual UV scale at the
         * time the lerp is performed.
         */
        """
        pass

    def setTextureStage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture_stage(const CLerpNodePathInterval self, TextureStage stage)
        
        /**
         * Indicates the texture stage that is adjusted by tex_offset, tex_rotate,
         * and/or tex_scale.  If this is not set, the default is the default texture
         * stage.
         */
        """
        pass

    def set_end_color(self, const_CLerpNodePathInterval_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_end_color(const CLerpNodePathInterval self, const LVecBase4f color)
        
        /**
         * Indicates that the color of the node should be lerped, and specifies the
         * final color of the node.  This should be called before priv_initialize().
         * If this is not called, the node's color will not be affected by the lerp.
         */
        """
        pass

    def set_end_color_scale(self, const_CLerpNodePathInterval_self, const_LVecBase4f_color_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_end_color_scale(const CLerpNodePathInterval self, const LVecBase4f color_scale)
        
        /**
         * Indicates that the color scale of the node should be lerped, and specifies
         * the final color scale of the node.  This should be called before
         * priv_initialize().  If this is not called, the node's color scale will not
         * be affected by the lerp.
         */
        """
        pass

    def set_end_hpr(self, const_CLerpNodePathInterval_self, const_LQuaternionf_quat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_end_hpr(const CLerpNodePathInterval self, const LQuaternionf quat)
        set_end_hpr(const CLerpNodePathInterval self, const LVecBase3f hpr)
        
        /**
         * Indicates that the rotation of the node should be lerped, and specifies the
         * final rotation of the node.  This should be called before
         * priv_initialize().
         *
         * This replaces a previous call to set_end_quat().  If neither set_end_hpr()
         * nor set_end_quat() is called, the node's rotation will not be affected by
         * the lerp.
         */
        
        /**
         * Indicates that the rotation of the node should be lerped, and specifies the
         * final rotation of the node.  This should be called before
         * priv_initialize().
         *
         * This special function is overloaded to accept a quaternion, even though the
         * function name is set_end_hpr().  The quaternion will be implicitly
         * converted to a HPR trio, and the lerp will be performed in HPR space,
         * componentwise.
         */
        """
        pass

    def set_end_pos(self, const_CLerpNodePathInterval_self, const_LVecBase3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_end_pos(const CLerpNodePathInterval self, const LVecBase3f pos)
        
        /**
         * Indicates that the position of the node should be lerped, and specifies the
         * final position of the node.  This should be called before
         * priv_initialize().  If this is not called, the node's position will not be
         * affected by the lerp.
         */
        """
        pass

    def set_end_quat(self, const_CLerpNodePathInterval_self, const_LQuaternionf_quat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_end_quat(const CLerpNodePathInterval self, const LQuaternionf quat)
        set_end_quat(const CLerpNodePathInterval self, const LVecBase3f hpr)
        
        /**
         * Indicates that the rotation of the node should be lerped, and specifies the
         * final rotation of the node.  This should be called before
         * priv_initialize().
         *
         * This replaces a previous call to set_end_hpr().  If neither set_end_quat()
         * nor set_end_hpr() is called, the node's rotation will not be affected by
         * the lerp.
         *
         * This special function is overloaded to accept a HPR trio, even though the
         * function name is set_end_quat().  The HPR will be implicitly converted to a
         * quaternion, and the lerp will be performed in quaternion space, as a
         * spherical lerp.
         */
        
        /**
         * Indicates that the rotation of the node should be lerped, and specifies the
         * final rotation of the node.  This should be called before
         * priv_initialize().
         *
         * This replaces a previous call to set_end_hpr().  If neither set_end_quat()
         * nor set_end_hpr() is called, the node's rotation will not be affected by
         * the lerp.
         *
         * The given quaternion needs to be normalized.
         */
        """
        pass

    def set_end_scale(self, const_CLerpNodePathInterval_self, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_end_scale(const CLerpNodePathInterval self, const LVecBase3f scale)
        set_end_scale(const CLerpNodePathInterval self, float scale)
        
        /**
         * Indicates that the scale of the node should be lerped, and specifies the
         * final scale of the node.  This should be called before priv_initialize().
         * If this is not called, the node's scale will not be affected by the lerp.
         */
        
        /**
         * Indicates that the scale of the node should be lerped, and specifies the
         * final scale of the node.  This should be called before priv_initialize().
         * If this is not called, the node's scale will not be affected by the lerp.
         */
        """
        pass

    def set_end_shear(self, const_CLerpNodePathInterval_self, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_end_shear(const CLerpNodePathInterval self, const LVecBase3f shear)
        
        /**
         * Indicates that the shear of the node should be lerped, and specifies the
         * final shear of the node.  This should be called before priv_initialize().
         * If this is not called, the node's shear will not be affected by the lerp.
         */
        """
        pass

    def set_end_tex_offset(self, const_CLerpNodePathInterval_self, const_LVecBase2f_tex_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_end_tex_offset(const CLerpNodePathInterval self, const LVecBase2f tex_offset)
        
        /**
         * Indicates that the UV offset of the node should be lerped, and specifies
         * the final UV offset of the node.  This should be called before
         * priv_initialize().  If this is not called, the node's UV offset will not be
         * affected by the lerp.
         */
        """
        pass

    def set_end_tex_rotate(self, const_CLerpNodePathInterval_self, float_tex_rotate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_end_tex_rotate(const CLerpNodePathInterval self, float tex_rotate)
        
        /**
         * Indicates that the UV rotate of the node should be lerped, and specifies
         * the final UV rotate of the node.  This should be called before
         * priv_initialize().  If this is not called, the node's UV rotate will not be
         * affected by the lerp.
         */
        """
        pass

    def set_end_tex_scale(self, const_CLerpNodePathInterval_self, const_LVecBase2f_tex_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_end_tex_scale(const CLerpNodePathInterval self, const LVecBase2f tex_scale)
        
        /**
         * Indicates that the UV scale of the node should be lerped, and specifies the
         * final UV scale of the node.  This should be called before
         * priv_initialize().  If this is not called, the node's UV scale will not be
         * affected by the lerp.
         */
        """
        pass

    def set_override(self, const_CLerpNodePathInterval_self, int_override): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_override(const CLerpNodePathInterval self, int override)
        
        /**
         * Changes the override value that will be associated with any state changes
         * applied by the lerp.  If this lerp is changing state (for instance, a color
         * lerp or a tex matrix lerp), then the new attributes created by this lerp
         * will be assigned the indicated override value when they are applied to the
         * node.
         */
        """
        pass

    def set_start_color(self, const_CLerpNodePathInterval_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_color(const CLerpNodePathInterval self, const LVecBase4f color)
        
        /**
         * Indicates the initial color of the lerped node.  This is meaningful only if
         * set_end_color() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual color at the
         * time the lerp is performed.
         */
        """
        pass

    def set_start_color_scale(self, const_CLerpNodePathInterval_self, const_LVecBase4f_color_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_color_scale(const CLerpNodePathInterval self, const LVecBase4f color_scale)
        
        /**
         * Indicates the initial color scale of the lerped node.  This is meaningful
         * only if set_end_color_scale() is also called.  This parameter is optional;
         * if unspecified, the value will be taken from the node's actual color scale
         * at the time the lerp is performed.
         */
        """
        pass

    def set_start_hpr(self, const_CLerpNodePathInterval_self, const_LVecBase3f_hpr): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_hpr(const CLerpNodePathInterval self, const LVecBase3f hpr)
        
        /**
         * Indicates the initial rotation of the lerped node.  This is meaningful only
         * if either set_end_hpr() or set_end_quat() is also called.  This parameter
         * is optional; if unspecified, the value will be taken from the node's actual
         * rotation at the time the lerp is performed.
         */
        """
        pass

    def set_start_pos(self, const_CLerpNodePathInterval_self, const_LVecBase3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_pos(const CLerpNodePathInterval self, const LVecBase3f pos)
        
        /**
         * Indicates the initial position of the lerped node.  This is meaningful only
         * if set_end_pos() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual position at the
         * time the lerp is performed.
         */
        """
        pass

    def set_start_quat(self, const_CLerpNodePathInterval_self, const_LQuaternionf_quat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_quat(const CLerpNodePathInterval self, const LQuaternionf quat)
        
        /**
         * Indicates the initial rotation of the lerped node.  This is meaningful only
         * if either set_end_quat() or set_end_hpr() is also called.  This parameter
         * is optional; if unspecified, the value will be taken from the node's actual
         * rotation at the time the lerp is performed.
         *
         * The given quaternion needs to be normalized.
         */
        """
        pass

    def set_start_scale(self, const_CLerpNodePathInterval_self, const_LVecBase3f_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_scale(const CLerpNodePathInterval self, const LVecBase3f scale)
        set_start_scale(const CLerpNodePathInterval self, float scale)
        
        /**
         * Indicates the initial scale of the lerped node.  This is meaningful only if
         * set_end_scale() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual scale at the
         * time the lerp is performed.
         */
        
        /**
         * Indicates the initial scale of the lerped node.  This is meaningful only if
         * set_end_scale() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual scale at the
         * time the lerp is performed.
         */
        """
        pass

    def set_start_shear(self, const_CLerpNodePathInterval_self, const_LVecBase3f_shear): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_shear(const CLerpNodePathInterval self, const LVecBase3f shear)
        
        /**
         * Indicates the initial shear of the lerped node.  This is meaningful only if
         * set_end_shear() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual shear at the
         * time the lerp is performed.
         */
        """
        pass

    def set_start_tex_offset(self, const_CLerpNodePathInterval_self, const_LVecBase2f_tex_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_tex_offset(const CLerpNodePathInterval self, const LVecBase2f tex_offset)
        
        /**
         * Indicates the initial UV offset of the lerped node.  This is meaningful
         * only if set_end_tex_offset() is also called.  This parameter is optional;
         * if unspecified, the value will be taken from the node's actual UV offset at
         * the time the lerp is performed.
         */
        """
        pass

    def set_start_tex_rotate(self, const_CLerpNodePathInterval_self, float_tex_rotate): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_tex_rotate(const CLerpNodePathInterval self, float tex_rotate)
        
        /**
         * Indicates the initial UV rotate of the lerped node.  This is meaningful
         * only if set_end_tex_rotate() is also called.  This parameter is optional;
         * if unspecified, the value will be taken from the node's actual UV rotate at
         * the time the lerp is performed.
         */
        """
        pass

    def set_start_tex_scale(self, const_CLerpNodePathInterval_self, const_LVecBase2f_tex_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_start_tex_scale(const CLerpNodePathInterval self, const LVecBase2f tex_scale)
        
        /**
         * Indicates the initial UV scale of the lerped node.  This is meaningful only
         * if set_end_tex_scale() is also called.  This parameter is optional; if
         * unspecified, the value will be taken from the node's actual UV scale at the
         * time the lerp is performed.
         */
        """
        pass

    def set_texture_stage(self, const_CLerpNodePathInterval_self, TextureStage_stage): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture_stage(const CLerpNodePathInterval self, TextureStage stage)
        
        /**
         * Indicates the texture stage that is adjusted by tex_offset, tex_rotate,
         * and/or tex_scale.  If this is not set, the default is the default texture
         * stage.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        '__doc__': '/**\n * An interval that lerps one or more properties (like pos, hpr, etc.) on a\n * NodePath over time.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68E63C0>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC68E63C0>)>'
        'getNode': None, # (!) real value is "<method 'getNode' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'getOther': None, # (!) real value is "<method 'getOther' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'getOverride': None, # (!) real value is "<method 'getOverride' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC68E63C0>)>'
        'get_node': None, # (!) real value is "<method 'get_node' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'get_other': None, # (!) real value is "<method 'get_other' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'get_override': None, # (!) real value is "<method 'get_override' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setEndColor': None, # (!) real value is "<method 'setEndColor' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setEndColorScale': None, # (!) real value is "<method 'setEndColorScale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setEndHpr': None, # (!) real value is "<method 'setEndHpr' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setEndPos': None, # (!) real value is "<method 'setEndPos' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setEndQuat': None, # (!) real value is "<method 'setEndQuat' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setEndScale': None, # (!) real value is "<method 'setEndScale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setEndShear': None, # (!) real value is "<method 'setEndShear' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setEndTexOffset': None, # (!) real value is "<method 'setEndTexOffset' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setEndTexRotate': None, # (!) real value is "<method 'setEndTexRotate' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setEndTexScale': None, # (!) real value is "<method 'setEndTexScale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setOverride': None, # (!) real value is "<method 'setOverride' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setStartColor': None, # (!) real value is "<method 'setStartColor' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setStartColorScale': None, # (!) real value is "<method 'setStartColorScale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setStartHpr': None, # (!) real value is "<method 'setStartHpr' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setStartPos': None, # (!) real value is "<method 'setStartPos' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setStartQuat': None, # (!) real value is "<method 'setStartQuat' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setStartScale': None, # (!) real value is "<method 'setStartScale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setStartShear': None, # (!) real value is "<method 'setStartShear' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setStartTexOffset': None, # (!) real value is "<method 'setStartTexOffset' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setStartTexRotate': None, # (!) real value is "<method 'setStartTexRotate' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setStartTexScale': None, # (!) real value is "<method 'setStartTexScale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'setTextureStage': None, # (!) real value is "<method 'setTextureStage' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_end_color': None, # (!) real value is "<method 'set_end_color' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_end_color_scale': None, # (!) real value is "<method 'set_end_color_scale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_end_hpr': None, # (!) real value is "<method 'set_end_hpr' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_end_pos': None, # (!) real value is "<method 'set_end_pos' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_end_quat': None, # (!) real value is "<method 'set_end_quat' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_end_scale': None, # (!) real value is "<method 'set_end_scale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_end_shear': None, # (!) real value is "<method 'set_end_shear' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_end_tex_offset': None, # (!) real value is "<method 'set_end_tex_offset' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_end_tex_rotate': None, # (!) real value is "<method 'set_end_tex_rotate' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_end_tex_scale': None, # (!) real value is "<method 'set_end_tex_scale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_override': None, # (!) real value is "<method 'set_override' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_start_color': None, # (!) real value is "<method 'set_start_color' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_start_color_scale': None, # (!) real value is "<method 'set_start_color_scale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_start_hpr': None, # (!) real value is "<method 'set_start_hpr' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_start_pos': None, # (!) real value is "<method 'set_start_pos' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_start_quat': None, # (!) real value is "<method 'set_start_quat' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_start_scale': None, # (!) real value is "<method 'set_start_scale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_start_shear': None, # (!) real value is "<method 'set_start_shear' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_start_tex_offset': None, # (!) real value is "<method 'set_start_tex_offset' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_start_tex_rotate': None, # (!) real value is "<method 'set_start_tex_rotate' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_start_tex_scale': None, # (!) real value is "<method 'set_start_tex_scale' of 'panda3d.direct.CLerpNodePathInterval' objects>"
        'set_texture_stage': None, # (!) real value is "<method 'set_texture_stage' of 'panda3d.direct.CLerpNodePathInterval' objects>"
    }


