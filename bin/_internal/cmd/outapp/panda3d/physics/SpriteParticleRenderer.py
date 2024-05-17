# encoding: utf-8
# module panda3d.physics
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\physics.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


from .BaseParticleRenderer import BaseParticleRenderer

class SpriteParticleRenderer(BaseParticleRenderer):
    """
    /**
     * Renders a particle system with high-speed nasty trick sprites.
     */
    """
    def addFromNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_from_node(const SpriteParticleRenderer self, const NodePath node_path)
        add_from_node(const SpriteParticleRenderer self, const NodePath node_path, bool size_from_texels)
        add_from_node(const SpriteParticleRenderer self, const NodePath node_path, str model, str node, bool size_from_texels, bool resize)
        add_from_node(const SpriteParticleRenderer self, const NodePath node_path, bool size_from_texels, bool resize)
        
        /**
         * This will allow the renderer to randomly choose from more than one texture
         * or sequence at particle birth.
         *
         * If the source type is important, use this one.
         *
         * model and node should lead to node_path like this: node_path =
         * loader.loadModel(model).find(node)
         *
         * If resize is true, or if there are no textures currently on the renderer,
         * it will force the renderer to use the size information from this node from
         * now on.  (Default is false)
         */
        
        /**
         * This will allow the renderer to randomly choose from more than one texture
         * or sequence at particle birth.
         *
         * If resize is true, or if there are no textures currently on the renderer,
         * it will force the renderer to use the size information from this node from
         * now on.  (Default is false)
         */
        """
        pass

    def addTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_texture(const SpriteParticleRenderer self, Texture tex, float texels_per_unit, bool resize)
        
        /**
         * Adds texture to image pool, effectively creating a single frame animation
         * that can be selected at particle birth.  This should only be called after a
         * previous call to set_texture().
         */
        """
        pass

    def add_from_node(self, const_SpriteParticleRenderer_self, const_NodePath_node_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_from_node(const SpriteParticleRenderer self, const NodePath node_path)
        add_from_node(const SpriteParticleRenderer self, const NodePath node_path, bool size_from_texels)
        add_from_node(const SpriteParticleRenderer self, const NodePath node_path, str model, str node, bool size_from_texels, bool resize)
        add_from_node(const SpriteParticleRenderer self, const NodePath node_path, bool size_from_texels, bool resize)
        
        /**
         * This will allow the renderer to randomly choose from more than one texture
         * or sequence at particle birth.
         *
         * If the source type is important, use this one.
         *
         * model and node should lead to node_path like this: node_path =
         * loader.loadModel(model).find(node)
         *
         * If resize is true, or if there are no textures currently on the renderer,
         * it will force the renderer to use the size information from this node from
         * now on.  (Default is false)
         */
        
        /**
         * This will allow the renderer to randomly choose from more than one texture
         * or sequence at particle birth.
         *
         * If resize is true, or if there are no textures currently on the renderer,
         * it will force the renderer to use the size information from this node from
         * now on.  (Default is false)
         */
        """
        pass

    def add_texture(self, const_SpriteParticleRenderer_self, Texture_tex, float_texels_per_unit, bool_resize): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_texture(const SpriteParticleRenderer self, Texture tex, float texels_per_unit, bool resize)
        
        /**
         * Adds texture to image pool, effectively creating a single frame animation
         * that can be selected at particle birth.  This should only be called after a
         * previous call to set_texture().
         */
        """
        pass

    def getAlphaBlendMethod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_blend_method(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getAlphaDisable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_disable(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anim(SpriteParticleRenderer self, int n)
        """
        pass

    def getAnimAngleFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_anim_angle_flag(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getAnimateFramesEnable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_animate_frames_enable(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getAnimateFramesIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_animate_frames_index(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getAnimateFramesRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_animate_frames_rate(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getAnims(self, *args, **kwargs): # real signature unknown
        pass

    def getColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getColorInterpolationManager(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color_interpolation_manager(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getFinalXScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_final_x_scale(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getFinalYScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_final_y_scale(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getHeight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_height(SpriteParticleRenderer self)
        
        /**
         * Returns the height of each particle in world units.
         */
        """
        pass

    def getInitialXScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_initial_x_scale(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getInitialYScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_initial_y_scale(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getLastAnim(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_last_anim(SpriteParticleRenderer self)
        """
        pass

    def getLlUv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ll_uv(SpriteParticleRenderer self)
        get_ll_uv(SpriteParticleRenderer self, int anim, int frame)
        
        /**
         * Returns the UV coordinate of the lower-left corner; see set_ll_uv().
         */
        
        /**
         * Returns the UV coordinate of the lower-left corner; see set_ll_uv().
         */
        """
        pass

    def getNonanimatedTheta(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_nonanimated_theta(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getNumAnims(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_anims(SpriteParticleRenderer self)
        """
        pass

    def getTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texture(SpriteParticleRenderer self)
        get_texture(SpriteParticleRenderer self, int anim, int frame)
        
        /**
        
         */
        
        /**
        
         */
        """
        pass

    def getUrUv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ur_uv(SpriteParticleRenderer self)
        get_ur_uv(SpriteParticleRenderer self, int anim, int frame)
        
        /**
         * Returns the UV coordinate of the lower-left corner; see set_ur_uv().
         */
        
        /**
         * Returns the UV coordinate of the upper-right corner; see set_ur_uv().
         */
        """
        pass

    def getWidth(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_width(SpriteParticleRenderer self)
        
        /**
         * Returns the width of each particle in world units.
         */
        """
        pass

    def getXScaleFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_x_scale_flag(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def getYScaleFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_y_scale_flag(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_alpha_blend_method(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_blend_method(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_alpha_disable(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_disable(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_anim(self, SpriteParticleRenderer_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anim(SpriteParticleRenderer self, int n)
        """
        pass

    def get_animate_frames_enable(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_animate_frames_enable(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_animate_frames_index(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_animate_frames_index(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_animate_frames_rate(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_animate_frames_rate(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_anims(self, *args, **kwargs): # real signature unknown
        pass

    def get_anim_angle_flag(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_anim_angle_flag(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_color(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_color_interpolation_manager(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color_interpolation_manager(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_final_x_scale(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_final_x_scale(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_final_y_scale(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_final_y_scale(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_height(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_height(SpriteParticleRenderer self)
        
        /**
         * Returns the height of each particle in world units.
         */
        """
        pass

    def get_initial_x_scale(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_initial_x_scale(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_initial_y_scale(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_initial_y_scale(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_last_anim(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_last_anim(SpriteParticleRenderer self)
        """
        pass

    def get_ll_uv(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ll_uv(SpriteParticleRenderer self)
        get_ll_uv(SpriteParticleRenderer self, int anim, int frame)
        
        /**
         * Returns the UV coordinate of the lower-left corner; see set_ll_uv().
         */
        
        /**
         * Returns the UV coordinate of the lower-left corner; see set_ll_uv().
         */
        """
        pass

    def get_nonanimated_theta(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_nonanimated_theta(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_num_anims(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_anims(SpriteParticleRenderer self)
        """
        pass

    def get_texture(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texture(SpriteParticleRenderer self)
        get_texture(SpriteParticleRenderer self, int anim, int frame)
        
        /**
        
         */
        
        /**
        
         */
        """
        pass

    def get_ur_uv(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ur_uv(SpriteParticleRenderer self)
        get_ur_uv(SpriteParticleRenderer self, int anim, int frame)
        
        /**
         * Returns the UV coordinate of the lower-left corner; see set_ur_uv().
         */
        
        /**
         * Returns the UV coordinate of the upper-right corner; see set_ur_uv().
         */
        """
        pass

    def get_width(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_width(SpriteParticleRenderer self)
        
        /**
         * Returns the width of each particle in world units.
         */
        """
        pass

    def get_x_scale_flag(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_x_scale_flag(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def get_y_scale_flag(self, SpriteParticleRenderer_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_y_scale_flag(SpriteParticleRenderer self)
        
        /**
        
         */
        """
        pass

    def removeAnimation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_animation(const SpriteParticleRenderer self, int n)
        
        /**
         * Removes an animation texture set from the renderer.
         */
        """
        pass

    def remove_animation(self, const_SpriteParticleRenderer_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_animation(const SpriteParticleRenderer self, int n)
        
        /**
         * Removes an animation texture set from the renderer.
         */
        """
        pass

    def setAlphaBlendMethod(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_blend_method(const SpriteParticleRenderer self, int bm)
        
        /**
        
         */
        """
        pass

    def setAlphaDisable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_disable(const SpriteParticleRenderer self, bool ad)
        
        /**
        
         */
        """
        pass

    def setAnimAngleFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_anim_angle_flag(const SpriteParticleRenderer self, bool animate_theta)
        
        /**
        
         */
        """
        pass

    def setAnimateFramesEnable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_animate_frames_enable(const SpriteParticleRenderer self, bool an)
        
        /**
        
         */
        """
        pass

    def setAnimateFramesIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_animate_frames_index(const SpriteParticleRenderer self, int i)
        
        /**
        
         */
        """
        pass

    def setAnimateFramesRate(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_animate_frames_rate(const SpriteParticleRenderer self, float r)
        
        /**
        
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const SpriteParticleRenderer self, const LVecBase4f color)
        
        /**
        
         */
        """
        pass

    def setFinalXScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_final_x_scale(const SpriteParticleRenderer self, float final_x_scale)
        
        /**
        
         */
        """
        pass

    def setFinalYScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_final_y_scale(const SpriteParticleRenderer self, float final_y_scale)
        
        /**
        
         */
        """
        pass

    def setFromNode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_from_node(const SpriteParticleRenderer self, const NodePath node_path)
        set_from_node(const SpriteParticleRenderer self, const NodePath node_path, bool size_from_texels)
        set_from_node(const SpriteParticleRenderer self, const NodePath node_path, str model, str node, bool size_from_texels)
        
        /**
         * If the source type is important, use this one.
         *
         * model and node should lead to node_path like this: node_path =
         * loader.loadModel(model).find(node)
         *
         * This will remove all previously add textures and resize the renderer to
         * match the new geometry.
         */
        
        /**
         * Sets the properties on this renderer from the geometry referenced by the
         * indicated NodePath.  This should be a reference to a GeomNode or a
         * SequenceNode; it extracts out the texture and UV range from the node.
         *
         * This will remove all previously added textures and animations.  It will
         * also resize the renderer to match this new geometry.
         *
         * If node_path refers to a GeomNode(or has one beneath it) the texture, its
         * size, and UV data will be extracted from that.
         *
         * If node_path references a SequenceNode(or has one beneath it) with multiple
         * GeomNodes beneath it, the size data will correspond only to the first
         * GeomNode found with a valid texture, while the texture and UV information
         * will be stored for each individual node.
         *
         * If size_from_texels is true, the particle size is based on the number of
         * texels in the source image; otherwise, it is based on the size of the first
         * polygon found in the node.
         *
         * model and node are the two items used to construct node_path.  If the
         * source type is important, use set_from_node(NodePath,string,string,bool)
         * instead.
         */
        """
        pass

    def setInitialXScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_initial_x_scale(const SpriteParticleRenderer self, float initial_x_scale)
        
        /**
        
         */
        """
        pass

    def setInitialYScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_initial_y_scale(const SpriteParticleRenderer self, float initial_y_scale)
        
        /**
        
         */
        """
        pass

    def setLlUv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ll_uv(const SpriteParticleRenderer self, const LPoint2f ll_uv)
        set_ll_uv(const SpriteParticleRenderer self, const LPoint2f ll_uv, int anim, int frame)
        
        /**
         * Sets the UV coordinate of the lower-left corner of all the sprites
         * generated by this renderer.  Normally this is (0, 0), but it might be set
         * to something else to use only a portion of the texture.
         */
        
        /**
         * Sets the UV coordinate of the lower-left corner of all the sprites
         * generated by this renderer.  Normally this is (0, 0), but it might be set
         * to something else to use only a portion of the texture.
         */
        """
        pass

    def setNonanimatedTheta(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_nonanimated_theta(const SpriteParticleRenderer self, float theta)
        
        /**
        
         */
        """
        pass

    def setSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_size(const SpriteParticleRenderer self, float width, float height)
        
        /**
         * Sets the size of each particle in world units.
         */
        """
        pass

    def setTexture(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texture(const SpriteParticleRenderer self, Texture tex, float texels_per_unit)
        
        /**
         * Sets the renderer up to render the entire texture image.  The scale of each
         * particle is based on the size of the texture in each dimension, modified by
         * texels_per_unit.
         *
         * Used to set the size of the particles.  Will clear all previously loaded
         * textures and animations.
         */
        """
        pass

    def setUrUv(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ur_uv(const SpriteParticleRenderer self, const LPoint2f ur_uv)
        set_ur_uv(const SpriteParticleRenderer self, const LPoint2f ur_uv, int anim, int frame)
        
        /**
         * Sets the UV coordinate of the upper-right corner of all the sprites
         * generated by this renderer.  Normally this is (1, 1), but it might be set
         * to something else to use only a portion of the texture.
         */
        
        /**
         * Sets the UV coordinate of the upper-right corner of all the sprites
         * generated by this renderer.  Normally this is (1, 1), but it might be set
         * to something else to use only a portion of the texture.
         */
        """
        pass

    def setXScaleFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_x_scale_flag(const SpriteParticleRenderer self, bool animate_x_ratio)
        
        /**
        
         */
        """
        pass

    def setYScaleFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_y_scale_flag(const SpriteParticleRenderer self, bool animate_y_ratio)
        
        /**
        
         */
        """
        pass

    def set_alpha_blend_method(self, const_SpriteParticleRenderer_self, int_bm): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_blend_method(const SpriteParticleRenderer self, int bm)
        
        /**
        
         */
        """
        pass

    def set_alpha_disable(self, const_SpriteParticleRenderer_self, bool_ad): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_disable(const SpriteParticleRenderer self, bool ad)
        
        /**
        
         */
        """
        pass

    def set_animate_frames_enable(self, const_SpriteParticleRenderer_self, bool_an): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_animate_frames_enable(const SpriteParticleRenderer self, bool an)
        
        /**
        
         */
        """
        pass

    def set_animate_frames_index(self, const_SpriteParticleRenderer_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_animate_frames_index(const SpriteParticleRenderer self, int i)
        
        /**
        
         */
        """
        pass

    def set_animate_frames_rate(self, const_SpriteParticleRenderer_self, float_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_animate_frames_rate(const SpriteParticleRenderer self, float r)
        
        /**
        
         */
        """
        pass

    def set_anim_angle_flag(self, const_SpriteParticleRenderer_self, bool_animate_theta): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_anim_angle_flag(const SpriteParticleRenderer self, bool animate_theta)
        
        /**
        
         */
        """
        pass

    def set_color(self, const_SpriteParticleRenderer_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const SpriteParticleRenderer self, const LVecBase4f color)
        
        /**
        
         */
        """
        pass

    def set_final_x_scale(self, const_SpriteParticleRenderer_self, float_final_x_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_final_x_scale(const SpriteParticleRenderer self, float final_x_scale)
        
        /**
        
         */
        """
        pass

    def set_final_y_scale(self, const_SpriteParticleRenderer_self, float_final_y_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_final_y_scale(const SpriteParticleRenderer self, float final_y_scale)
        
        /**
        
         */
        """
        pass

    def set_from_node(self, const_SpriteParticleRenderer_self, const_NodePath_node_path): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_from_node(const SpriteParticleRenderer self, const NodePath node_path)
        set_from_node(const SpriteParticleRenderer self, const NodePath node_path, bool size_from_texels)
        set_from_node(const SpriteParticleRenderer self, const NodePath node_path, str model, str node, bool size_from_texels)
        
        /**
         * If the source type is important, use this one.
         *
         * model and node should lead to node_path like this: node_path =
         * loader.loadModel(model).find(node)
         *
         * This will remove all previously add textures and resize the renderer to
         * match the new geometry.
         */
        
        /**
         * Sets the properties on this renderer from the geometry referenced by the
         * indicated NodePath.  This should be a reference to a GeomNode or a
         * SequenceNode; it extracts out the texture and UV range from the node.
         *
         * This will remove all previously added textures and animations.  It will
         * also resize the renderer to match this new geometry.
         *
         * If node_path refers to a GeomNode(or has one beneath it) the texture, its
         * size, and UV data will be extracted from that.
         *
         * If node_path references a SequenceNode(or has one beneath it) with multiple
         * GeomNodes beneath it, the size data will correspond only to the first
         * GeomNode found with a valid texture, while the texture and UV information
         * will be stored for each individual node.
         *
         * If size_from_texels is true, the particle size is based on the number of
         * texels in the source image; otherwise, it is based on the size of the first
         * polygon found in the node.
         *
         * model and node are the two items used to construct node_path.  If the
         * source type is important, use set_from_node(NodePath,string,string,bool)
         * instead.
         */
        """
        pass

    def set_initial_x_scale(self, const_SpriteParticleRenderer_self, float_initial_x_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_initial_x_scale(const SpriteParticleRenderer self, float initial_x_scale)
        
        /**
        
         */
        """
        pass

    def set_initial_y_scale(self, const_SpriteParticleRenderer_self, float_initial_y_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_initial_y_scale(const SpriteParticleRenderer self, float initial_y_scale)
        
        /**
        
         */
        """
        pass

    def set_ll_uv(self, const_SpriteParticleRenderer_self, const_LPoint2f_ll_uv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ll_uv(const SpriteParticleRenderer self, const LPoint2f ll_uv)
        set_ll_uv(const SpriteParticleRenderer self, const LPoint2f ll_uv, int anim, int frame)
        
        /**
         * Sets the UV coordinate of the lower-left corner of all the sprites
         * generated by this renderer.  Normally this is (0, 0), but it might be set
         * to something else to use only a portion of the texture.
         */
        
        /**
         * Sets the UV coordinate of the lower-left corner of all the sprites
         * generated by this renderer.  Normally this is (0, 0), but it might be set
         * to something else to use only a portion of the texture.
         */
        """
        pass

    def set_nonanimated_theta(self, const_SpriteParticleRenderer_self, float_theta): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_nonanimated_theta(const SpriteParticleRenderer self, float theta)
        
        /**
        
         */
        """
        pass

    def set_size(self, const_SpriteParticleRenderer_self, float_width, float_height): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_size(const SpriteParticleRenderer self, float width, float height)
        
        /**
         * Sets the size of each particle in world units.
         */
        """
        pass

    def set_texture(self, const_SpriteParticleRenderer_self, Texture_tex, float_texels_per_unit): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texture(const SpriteParticleRenderer self, Texture tex, float texels_per_unit)
        
        /**
         * Sets the renderer up to render the entire texture image.  The scale of each
         * particle is based on the size of the texture in each dimension, modified by
         * texels_per_unit.
         *
         * Used to set the size of the particles.  Will clear all previously loaded
         * textures and animations.
         */
        """
        pass

    def set_ur_uv(self, const_SpriteParticleRenderer_self, const_LPoint2f_ur_uv): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ur_uv(const SpriteParticleRenderer self, const LPoint2f ur_uv)
        set_ur_uv(const SpriteParticleRenderer self, const LPoint2f ur_uv, int anim, int frame)
        
        /**
         * Sets the UV coordinate of the upper-right corner of all the sprites
         * generated by this renderer.  Normally this is (1, 1), but it might be set
         * to something else to use only a portion of the texture.
         */
        
        /**
         * Sets the UV coordinate of the upper-right corner of all the sprites
         * generated by this renderer.  Normally this is (1, 1), but it might be set
         * to something else to use only a portion of the texture.
         */
        """
        pass

    def set_x_scale_flag(self, const_SpriteParticleRenderer_self, bool_animate_x_ratio): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_x_scale_flag(const SpriteParticleRenderer self, bool animate_x_ratio)
        
        /**
        
         */
        """
        pass

    def set_y_scale_flag(self, const_SpriteParticleRenderer_self, bool_animate_y_ratio): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_y_scale_flag(const SpriteParticleRenderer self, bool animate_y_ratio)
        
        /**
        
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        '__doc__': '/**\n * Renders a particle system with high-speed nasty trick sprites.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DF5C30>'
        'addFromNode': None, # (!) real value is "<method 'addFromNode' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'addTexture': None, # (!) real value is "<method 'addTexture' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'add_from_node': None, # (!) real value is "<method 'add_from_node' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'add_texture': None, # (!) real value is "<method 'add_texture' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getAlphaBlendMethod': None, # (!) real value is "<method 'getAlphaBlendMethod' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getAlphaDisable': None, # (!) real value is "<method 'getAlphaDisable' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getAnim': None, # (!) real value is "<method 'getAnim' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getAnimAngleFlag': None, # (!) real value is "<method 'getAnimAngleFlag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getAnimateFramesEnable': None, # (!) real value is "<method 'getAnimateFramesEnable' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getAnimateFramesIndex': None, # (!) real value is "<method 'getAnimateFramesIndex' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getAnimateFramesRate': None, # (!) real value is "<method 'getAnimateFramesRate' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getAnims': None, # (!) real value is "<method 'getAnims' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getColorInterpolationManager': None, # (!) real value is "<method 'getColorInterpolationManager' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getFinalXScale': None, # (!) real value is "<method 'getFinalXScale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getFinalYScale': None, # (!) real value is "<method 'getFinalYScale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getHeight': None, # (!) real value is "<method 'getHeight' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getInitialXScale': None, # (!) real value is "<method 'getInitialXScale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getInitialYScale': None, # (!) real value is "<method 'getInitialYScale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getLastAnim': None, # (!) real value is "<method 'getLastAnim' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getLlUv': None, # (!) real value is "<method 'getLlUv' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getNonanimatedTheta': None, # (!) real value is "<method 'getNonanimatedTheta' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getNumAnims': None, # (!) real value is "<method 'getNumAnims' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getTexture': None, # (!) real value is "<method 'getTexture' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getUrUv': None, # (!) real value is "<method 'getUrUv' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getWidth': None, # (!) real value is "<method 'getWidth' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getXScaleFlag': None, # (!) real value is "<method 'getXScaleFlag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'getYScaleFlag': None, # (!) real value is "<method 'getYScaleFlag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_alpha_blend_method': None, # (!) real value is "<method 'get_alpha_blend_method' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_alpha_disable': None, # (!) real value is "<method 'get_alpha_disable' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_anim': None, # (!) real value is "<method 'get_anim' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_anim_angle_flag': None, # (!) real value is "<method 'get_anim_angle_flag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_animate_frames_enable': None, # (!) real value is "<method 'get_animate_frames_enable' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_animate_frames_index': None, # (!) real value is "<method 'get_animate_frames_index' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_animate_frames_rate': None, # (!) real value is "<method 'get_animate_frames_rate' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_anims': None, # (!) real value is "<method 'get_anims' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_color_interpolation_manager': None, # (!) real value is "<method 'get_color_interpolation_manager' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_final_x_scale': None, # (!) real value is "<method 'get_final_x_scale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_final_y_scale': None, # (!) real value is "<method 'get_final_y_scale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_height': None, # (!) real value is "<method 'get_height' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_initial_x_scale': None, # (!) real value is "<method 'get_initial_x_scale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_initial_y_scale': None, # (!) real value is "<method 'get_initial_y_scale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_last_anim': None, # (!) real value is "<method 'get_last_anim' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_ll_uv': None, # (!) real value is "<method 'get_ll_uv' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_nonanimated_theta': None, # (!) real value is "<method 'get_nonanimated_theta' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_num_anims': None, # (!) real value is "<method 'get_num_anims' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_texture': None, # (!) real value is "<method 'get_texture' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_ur_uv': None, # (!) real value is "<method 'get_ur_uv' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_width': None, # (!) real value is "<method 'get_width' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_x_scale_flag': None, # (!) real value is "<method 'get_x_scale_flag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'get_y_scale_flag': None, # (!) real value is "<method 'get_y_scale_flag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'removeAnimation': None, # (!) real value is "<method 'removeAnimation' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'remove_animation': None, # (!) real value is "<method 'remove_animation' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setAlphaBlendMethod': None, # (!) real value is "<method 'setAlphaBlendMethod' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setAlphaDisable': None, # (!) real value is "<method 'setAlphaDisable' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setAnimAngleFlag': None, # (!) real value is "<method 'setAnimAngleFlag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setAnimateFramesEnable': None, # (!) real value is "<method 'setAnimateFramesEnable' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setAnimateFramesIndex': None, # (!) real value is "<method 'setAnimateFramesIndex' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setAnimateFramesRate': None, # (!) real value is "<method 'setAnimateFramesRate' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setFinalXScale': None, # (!) real value is "<method 'setFinalXScale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setFinalYScale': None, # (!) real value is "<method 'setFinalYScale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setFromNode': None, # (!) real value is "<method 'setFromNode' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setInitialXScale': None, # (!) real value is "<method 'setInitialXScale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setInitialYScale': None, # (!) real value is "<method 'setInitialYScale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setLlUv': None, # (!) real value is "<method 'setLlUv' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setNonanimatedTheta': None, # (!) real value is "<method 'setNonanimatedTheta' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setSize': None, # (!) real value is "<method 'setSize' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setTexture': None, # (!) real value is "<method 'setTexture' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setUrUv': None, # (!) real value is "<method 'setUrUv' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setXScaleFlag': None, # (!) real value is "<method 'setXScaleFlag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'setYScaleFlag': None, # (!) real value is "<method 'setYScaleFlag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_alpha_blend_method': None, # (!) real value is "<method 'set_alpha_blend_method' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_alpha_disable': None, # (!) real value is "<method 'set_alpha_disable' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_anim_angle_flag': None, # (!) real value is "<method 'set_anim_angle_flag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_animate_frames_enable': None, # (!) real value is "<method 'set_animate_frames_enable' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_animate_frames_index': None, # (!) real value is "<method 'set_animate_frames_index' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_animate_frames_rate': None, # (!) real value is "<method 'set_animate_frames_rate' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_final_x_scale': None, # (!) real value is "<method 'set_final_x_scale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_final_y_scale': None, # (!) real value is "<method 'set_final_y_scale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_from_node': None, # (!) real value is "<method 'set_from_node' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_initial_x_scale': None, # (!) real value is "<method 'set_initial_x_scale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_initial_y_scale': None, # (!) real value is "<method 'set_initial_y_scale' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_ll_uv': None, # (!) real value is "<method 'set_ll_uv' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_nonanimated_theta': None, # (!) real value is "<method 'set_nonanimated_theta' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_size': None, # (!) real value is "<method 'set_size' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_texture': None, # (!) real value is "<method 'set_texture' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_ur_uv': None, # (!) real value is "<method 'set_ur_uv' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_x_scale_flag': None, # (!) real value is "<method 'set_x_scale_flag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
        'set_y_scale_flag': None, # (!) real value is "<method 'set_y_scale_flag' of 'panda3d.physics.SpriteParticleRenderer' objects>"
    }


