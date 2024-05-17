# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

class TextureStage(TypedWritableReferenceCount):
    """
    /**
     * Defines the properties of a named stage of the multitexture pipeline.  The
     * TextureAttrib will associated a number of these stages with Texture
     * objects, and the GSG will render geometry by sorting all of the currently
     * active TextureStages in order and then issuing the appropriate rendering
     * calls to activate them.
     */
    """
    def assign(self, const_TextureStage_self, const_TextureStage_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const TextureStage self, const TextureStage copy)
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(TextureStage self, const TextureStage other)
        
        /**
         * Returns a number less than zero if this TextureStage sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         * The sorting order is arbitrary and largely meaningless, except to
         * differentiate different stages.
         */
        """
        pass

    def compare_to(self, TextureStage_self, const_TextureStage_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(TextureStage self, const TextureStage other)
        
        /**
         * Returns a number less than zero if this TextureStage sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         * The sorting order is arbitrary and largely meaningless, except to
         * differentiate different stages.
         */
        """
        pass

    def getAlphaScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_alpha_scale(TextureStage self)
        
        /**
         * See set_alpha_scale().
         */
        """
        pass

    def getBinormalName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_binormal_name(TextureStage self)
        
        /**
         * Returns the set of binormals this texture stage will use.  This is the same
         * as get_binormal_name(), except that the first part is "binormal".
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
        get_color(TextureStage self)
        
        /**
         * return the color for this stage
         */
        """
        pass

    def getCombineAlphaMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_alpha_mode(TextureStage self)
        
        /**
         * Get combine_alpha_mode
         */
        """
        pass

    def getCombineAlphaOperand0(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_alpha_operand0(TextureStage self)
        
        /**
         * Get operand0 of combine_alpha_mode
         */
        """
        pass

    def getCombineAlphaOperand1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_alpha_operand1(TextureStage self)
        
        /**
         * Get operand1 of combine_alpha_mode
         */
        """
        pass

    def getCombineAlphaOperand2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_alpha_operand2(TextureStage self)
        
        /**
         * Get operand2 of combine_alpha_mode
         */
        """
        pass

    def getCombineAlphaSource0(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_alpha_source0(TextureStage self)
        
        /**
         * Get source0 of combine_alpha_mode
         */
        """
        pass

    def getCombineAlphaSource1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_alpha_source1(TextureStage self)
        
        /**
         * Get source1 of combine_alpha_mode
         */
        """
        pass

    def getCombineAlphaSource2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_alpha_source2(TextureStage self)
        
        /**
         * Get source2 of combine_alpha_mode
         */
        """
        pass

    def getCombineRgbMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_rgb_mode(TextureStage self)
        
        /**
         * Get the combine_rgb_mode
         */
        """
        pass

    def getCombineRgbOperand0(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_rgb_operand0(TextureStage self)
        
        /**
         * Get operand0 of combine_rgb_mode
         */
        """
        pass

    def getCombineRgbOperand1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_rgb_operand1(TextureStage self)
        
        /**
         * Get operand1 of combine_rgb_mode
         */
        """
        pass

    def getCombineRgbOperand2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_rgb_operand2(TextureStage self)
        
        /**
         * Get operand2 of combine_rgb_mode
         */
        """
        pass

    def getCombineRgbSource0(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_rgb_source0(TextureStage self)
        
        /**
         * Get source0 of combine_rgb_mode
         */
        """
        pass

    def getCombineRgbSource1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_rgb_source1(TextureStage self)
        
        /**
         * Get source1 of combine_rgb_mode
         */
        """
        pass

    def getCombineRgbSource2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_combine_rgb_source2(TextureStage self)
        
        /**
         * Get source2 of combine_rgb_mode
         */
        """
        pass

    def getDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default()
        
        /**
         * Returns the default TextureStage that will be used for all texturing that
         * does not name a particular stage.  This generally handles the normal
         * single-texture case.
         */
        """
        pass

    def getMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mode(TextureStage self)
        
        /**
         * Return the mode of this stage
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(TextureStage self)
        
        /**
         * Returns the name of this texture stage
         */
        """
        pass

    def getNumCombineAlphaOperands(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_combine_alpha_operands(TextureStage self)
        
        /**
         * Returns the number of meaningful operands that may be retrieved via
         * get_combine_alpha_sourceN() and get_combine_alpha_operandN().
         */
        """
        pass

    def getNumCombineRgbOperands(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_combine_rgb_operands(TextureStage self)
        
        /**
         * Returns the number of meaningful operands that may be retrieved via
         * get_combine_rgb_sourceN() and get_combine_rgb_operandN().
         */
        """
        pass

    def getPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_priority(TextureStage self)
        
        /**
         * Returns the priority associated with this stage.
         *
         * This is specially helpful for cards that do not support more than n stages
         * of multi-texturing.
         */
        """
        pass

    def getRgbScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_rgb_scale(TextureStage self)
        
        /**
         * See set_rgb_scale().
         */
        """
        pass

    def getSavedResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_saved_result(TextureStage self)
        
        /**
         * Returns the current setting of the saved_result flag.  See
         * set_saved_result().
         */
        """
        pass

    def getSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sort(TextureStage self)
        
        /**
         * Returns the sort order of this texture stage.
         */
        """
        pass

    def getTangentName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tangent_name(TextureStage self)
        
        /**
         * Returns the set of tangents this texture stage will use.  This is the same
         * as get_texcoord_name(), except that the first part is "tangent".
         */
        """
        pass

    def getTexcoordName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_texcoord_name(TextureStage self)
        
        /**
         * See set_texcoord_name.  The default is InternalName::get_texcoord().
         */
        """
        pass

    def getTexViewOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_tex_view_offset(TextureStage self)
        
        /**
         * Returns the current setting of the tex_view_offset.  See
         * set_tex_view_offset().
         */
        """
        pass

    def get_alpha_scale(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_alpha_scale(TextureStage self)
        
        /**
         * See set_alpha_scale().
         */
        """
        pass

    def get_binormal_name(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_binormal_name(TextureStage self)
        
        /**
         * Returns the set of binormals this texture stage will use.  This is the same
         * as get_binormal_name(), except that the first part is "binormal".
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_color(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(TextureStage self)
        
        /**
         * return the color for this stage
         */
        """
        pass

    def get_combine_alpha_mode(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_alpha_mode(TextureStage self)
        
        /**
         * Get combine_alpha_mode
         */
        """
        pass

    def get_combine_alpha_operand0(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_alpha_operand0(TextureStage self)
        
        /**
         * Get operand0 of combine_alpha_mode
         */
        """
        pass

    def get_combine_alpha_operand1(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_alpha_operand1(TextureStage self)
        
        /**
         * Get operand1 of combine_alpha_mode
         */
        """
        pass

    def get_combine_alpha_operand2(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_alpha_operand2(TextureStage self)
        
        /**
         * Get operand2 of combine_alpha_mode
         */
        """
        pass

    def get_combine_alpha_source0(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_alpha_source0(TextureStage self)
        
        /**
         * Get source0 of combine_alpha_mode
         */
        """
        pass

    def get_combine_alpha_source1(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_alpha_source1(TextureStage self)
        
        /**
         * Get source1 of combine_alpha_mode
         */
        """
        pass

    def get_combine_alpha_source2(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_alpha_source2(TextureStage self)
        
        /**
         * Get source2 of combine_alpha_mode
         */
        """
        pass

    def get_combine_rgb_mode(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_rgb_mode(TextureStage self)
        
        /**
         * Get the combine_rgb_mode
         */
        """
        pass

    def get_combine_rgb_operand0(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_rgb_operand0(TextureStage self)
        
        /**
         * Get operand0 of combine_rgb_mode
         */
        """
        pass

    def get_combine_rgb_operand1(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_rgb_operand1(TextureStage self)
        
        /**
         * Get operand1 of combine_rgb_mode
         */
        """
        pass

    def get_combine_rgb_operand2(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_rgb_operand2(TextureStage self)
        
        /**
         * Get operand2 of combine_rgb_mode
         */
        """
        pass

    def get_combine_rgb_source0(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_rgb_source0(TextureStage self)
        
        /**
         * Get source0 of combine_rgb_mode
         */
        """
        pass

    def get_combine_rgb_source1(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_rgb_source1(TextureStage self)
        
        /**
         * Get source1 of combine_rgb_mode
         */
        """
        pass

    def get_combine_rgb_source2(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_combine_rgb_source2(TextureStage self)
        
        /**
         * Get source2 of combine_rgb_mode
         */
        """
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default()
        
        /**
         * Returns the default TextureStage that will be used for all texturing that
         * does not name a particular stage.  This generally handles the normal
         * single-texture case.
         */
        """
        pass

    def get_mode(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mode(TextureStage self)
        
        /**
         * Return the mode of this stage
         */
        """
        pass

    def get_name(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(TextureStage self)
        
        /**
         * Returns the name of this texture stage
         */
        """
        pass

    def get_num_combine_alpha_operands(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_combine_alpha_operands(TextureStage self)
        
        /**
         * Returns the number of meaningful operands that may be retrieved via
         * get_combine_alpha_sourceN() and get_combine_alpha_operandN().
         */
        """
        pass

    def get_num_combine_rgb_operands(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_combine_rgb_operands(TextureStage self)
        
        /**
         * Returns the number of meaningful operands that may be retrieved via
         * get_combine_rgb_sourceN() and get_combine_rgb_operandN().
         */
        """
        pass

    def get_priority(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_priority(TextureStage self)
        
        /**
         * Returns the priority associated with this stage.
         *
         * This is specially helpful for cards that do not support more than n stages
         * of multi-texturing.
         */
        """
        pass

    def get_rgb_scale(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_rgb_scale(TextureStage self)
        
        /**
         * See set_rgb_scale().
         */
        """
        pass

    def get_saved_result(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_saved_result(TextureStage self)
        
        /**
         * Returns the current setting of the saved_result flag.  See
         * set_saved_result().
         */
        """
        pass

    def get_sort(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sort(TextureStage self)
        
        /**
         * Returns the sort order of this texture stage.
         */
        """
        pass

    def get_tangent_name(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tangent_name(TextureStage self)
        
        /**
         * Returns the set of tangents this texture stage will use.  This is the same
         * as get_texcoord_name(), except that the first part is "tangent".
         */
        """
        pass

    def get_texcoord_name(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_texcoord_name(TextureStage self)
        
        /**
         * See set_texcoord_name.  The default is InternalName::get_texcoord().
         */
        """
        pass

    def get_tex_view_offset(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_tex_view_offset(TextureStage self)
        
        /**
         * Returns the current setting of the tex_view_offset.  See
         * set_tex_view_offset().
         */
        """
        pass

    def involvesColorScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        involves_color_scale(TextureStage self)
        
        /**
         * Returns true if the TextureStage is affected by the setting of the current
         * ColorScaleAttrib, false otherwise.
         */
        """
        pass

    def involves_color_scale(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        involves_color_scale(TextureStage self)
        
        /**
         * Returns true if the TextureStage is affected by the setting of the current
         * ColorScaleAttrib, false otherwise.
         */
        """
        pass

    def isFixedFunction(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_fixed_function(TextureStage self)
        
        /**
         * Returns true if the TextureStage is relevant to the classic fixed function
         * pipeline.  This excludes texture stages such as normal mapping and the
         * like.
         */
        """
        pass

    def is_fixed_function(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_fixed_function(TextureStage self)
        
        /**
         * Returns true if the TextureStage is relevant to the classic fixed function
         * pipeline.  This excludes texture stages such as normal mapping and the
         * like.
         */
        """
        pass

    def output(self, TextureStage_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(TextureStage self, ostream out)
        
        /**
         * Just a single line output
         */
        """
        pass

    def setAlphaScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_alpha_scale(const TextureStage self, int alpha_scale)
        
        /**
         * Sets an additional factor that will scale the alpha component after the
         * texture has been applied.  This is used only when the mode is CM_combine.
         *
         * The only legal values are 1, 2, or 4.
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const TextureStage self, const LVecBase4f color)
        
        /**
         * Set the color for this stage
         */
        """
        pass

    def setCombineAlpha(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_combine_alpha(const TextureStage self, int mode, int source0, int operand0)
        set_combine_alpha(const TextureStage self, int mode, int source0, int operand0, int source1, int operand1)
        set_combine_alpha(const TextureStage self, int mode, int source0, int operand0, int source1, int operand1, int source2, int operand2)
        
        /**
         * Specifies any of the CombineMode values that represent a one-parameter
         * operation.  Specifically, this is CM_replace only.
         */
        
        /**
         * Specifies any of the CombineMode values that represent a two-parameter
         * operation.  Specifically, this is everything except for CM_replace and
         * CM_interpolate.
         */
        
        /**
         * Specifies any of the CombineMode values that represent a one-parameter
         * operation.  Specifically, this is CM_interpolate only.
         */
        """
        pass

    def setCombineRgb(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_combine_rgb(const TextureStage self, int mode, int source0, int operand0)
        set_combine_rgb(const TextureStage self, int mode, int source0, int operand0, int source1, int operand1)
        set_combine_rgb(const TextureStage self, int mode, int source0, int operand0, int source1, int operand1, int source2, int operand2)
        
        /**
         * Specifies any of the CombineMode values that represent a one-parameter
         * operation.  Specifically, this is CM_replace only.
         */
        
        /**
         * Specifies any of the CombineMode values that represent a two-parameter
         * operation.  Specifically, this is everything except for CM_replace and
         * CM_interpolate.
         */
        
        /**
         * Specifies any of the CombineMode values that represent a one-parameter
         * operation.  Specifically, this is CM_interpolate only.
         */
        """
        pass

    def setMode(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_mode(const TextureStage self, int mode)
        
        /**
         * Set the mode of this texture stage
         */
        """
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_name(const TextureStage self, str name)
        
        /**
         * Changes the name of this texture stage
         */
        """
        pass

    def setPriority(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_priority(const TextureStage self, int priority)
        
        /**
         * Changes the relative importance of the texture associated with this stage
         * relative to the other texture stages that are applied simultaneously.
         *
         * This is unrelated to set_sort(), which controls the order in which multiple
         * textures are applied.  The priority number is used to decide which of the
         * requested textures are to be selected for rendering when more textures are
         * requested than the hardware will support.  The highest-priority n textures
         * are selected for rendering, and then rendered in order by their sort
         * factor.
         */
        """
        pass

    def setRgbScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_rgb_scale(const TextureStage self, int rgb_scale)
        
        /**
         * Sets an additional factor that will scale all three r, g, b components
         * after the texture has been applied.  This is used only when the mode is
         * CM_combine.
         *
         * The only legal values are 1, 2, or 4.
         */
        """
        pass

    def setSavedResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_saved_result(const TextureStage self, bool saved_result)
        
        /**
         * Sets the saved_result flag.  When this is true, the output of this stage
         * will be supplied as the "last_saved_result" source for any future stages,
         * until the next TextureStage with a saved_result set true is encountered.
         *
         * This can be used to reuse the results of this texture stage as input to
         * more than one stage later in the pipeline.
         *
         * The last texture in the pipeline (the one with the highest sort value)
         * should not have this flag set.
         */
        """
        pass

    def setSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sort(const TextureStage self, int sort)
        
        /**
         * Changes the order in which the texture associated with this stage is
         * rendered relative to the other texture stages.  When geometry is rendered
         * with multiple textures, the textures are rendered in order from the lowest
         * sort number to the highest sort number.
         *
         * Also see set_priority(), which is used to select the most important
         * textures for rendering when some must be omitted because of hardware
         * limitations.
         */
        """
        pass

    def setTexcoordName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_texcoord_name(const TextureStage self, InternalName name)
        set_texcoord_name(const TextureStage self, str texcoord_name)
        
        /**
         * Indicate which set of UV's this texture stage will use.  Geometry may have
         * any number of associated UV sets, each of which must have a unique name.
         */
        
        /**
         * Indicate which set of UV's this texture stage will use.  Geometry may have
         * any number of associated UV sets, each of which must have a unique name.
         */
        """
        pass

    def setTexViewOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_tex_view_offset(const TextureStage self, int tex_view_offset)
        
        /**
         * Sets the tex_view_offset value.  This is used only when a special multiview
         * texture is bound to the TextureStage, and it selects the particular view of
         * the texture that is to be used.
         *
         * This value is added to the similar parameter on DisplayRegion to derive the
         * final texture view index that is selected for rendering.
         */
        """
        pass

    def set_alpha_scale(self, const_TextureStage_self, int_alpha_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_alpha_scale(const TextureStage self, int alpha_scale)
        
        /**
         * Sets an additional factor that will scale the alpha component after the
         * texture has been applied.  This is used only when the mode is CM_combine.
         *
         * The only legal values are 1, 2, or 4.
         */
        """
        pass

    def set_color(self, const_TextureStage_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const TextureStage self, const LVecBase4f color)
        
        /**
         * Set the color for this stage
         */
        """
        pass

    def set_combine_alpha(self, const_TextureStage_self, int_mode, int_source0, int_operand0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_combine_alpha(const TextureStage self, int mode, int source0, int operand0)
        set_combine_alpha(const TextureStage self, int mode, int source0, int operand0, int source1, int operand1)
        set_combine_alpha(const TextureStage self, int mode, int source0, int operand0, int source1, int operand1, int source2, int operand2)
        
        /**
         * Specifies any of the CombineMode values that represent a one-parameter
         * operation.  Specifically, this is CM_replace only.
         */
        
        /**
         * Specifies any of the CombineMode values that represent a two-parameter
         * operation.  Specifically, this is everything except for CM_replace and
         * CM_interpolate.
         */
        
        /**
         * Specifies any of the CombineMode values that represent a one-parameter
         * operation.  Specifically, this is CM_interpolate only.
         */
        """
        pass

    def set_combine_rgb(self, const_TextureStage_self, int_mode, int_source0, int_operand0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_combine_rgb(const TextureStage self, int mode, int source0, int operand0)
        set_combine_rgb(const TextureStage self, int mode, int source0, int operand0, int source1, int operand1)
        set_combine_rgb(const TextureStage self, int mode, int source0, int operand0, int source1, int operand1, int source2, int operand2)
        
        /**
         * Specifies any of the CombineMode values that represent a one-parameter
         * operation.  Specifically, this is CM_replace only.
         */
        
        /**
         * Specifies any of the CombineMode values that represent a two-parameter
         * operation.  Specifically, this is everything except for CM_replace and
         * CM_interpolate.
         */
        
        /**
         * Specifies any of the CombineMode values that represent a one-parameter
         * operation.  Specifically, this is CM_interpolate only.
         */
        """
        pass

    def set_mode(self, const_TextureStage_self, int_mode): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_mode(const TextureStage self, int mode)
        
        /**
         * Set the mode of this texture stage
         */
        """
        pass

    def set_name(self, const_TextureStage_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_name(const TextureStage self, str name)
        
        /**
         * Changes the name of this texture stage
         */
        """
        pass

    def set_priority(self, const_TextureStage_self, int_priority): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_priority(const TextureStage self, int priority)
        
        /**
         * Changes the relative importance of the texture associated with this stage
         * relative to the other texture stages that are applied simultaneously.
         *
         * This is unrelated to set_sort(), which controls the order in which multiple
         * textures are applied.  The priority number is used to decide which of the
         * requested textures are to be selected for rendering when more textures are
         * requested than the hardware will support.  The highest-priority n textures
         * are selected for rendering, and then rendered in order by their sort
         * factor.
         */
        """
        pass

    def set_rgb_scale(self, const_TextureStage_self, int_rgb_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_rgb_scale(const TextureStage self, int rgb_scale)
        
        /**
         * Sets an additional factor that will scale all three r, g, b components
         * after the texture has been applied.  This is used only when the mode is
         * CM_combine.
         *
         * The only legal values are 1, 2, or 4.
         */
        """
        pass

    def set_saved_result(self, const_TextureStage_self, bool_saved_result): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_saved_result(const TextureStage self, bool saved_result)
        
        /**
         * Sets the saved_result flag.  When this is true, the output of this stage
         * will be supplied as the "last_saved_result" source for any future stages,
         * until the next TextureStage with a saved_result set true is encountered.
         *
         * This can be used to reuse the results of this texture stage as input to
         * more than one stage later in the pipeline.
         *
         * The last texture in the pipeline (the one with the highest sort value)
         * should not have this flag set.
         */
        """
        pass

    def set_sort(self, const_TextureStage_self, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sort(const TextureStage self, int sort)
        
        /**
         * Changes the order in which the texture associated with this stage is
         * rendered relative to the other texture stages.  When geometry is rendered
         * with multiple textures, the textures are rendered in order from the lowest
         * sort number to the highest sort number.
         *
         * Also see set_priority(), which is used to select the most important
         * textures for rendering when some must be omitted because of hardware
         * limitations.
         */
        """
        pass

    def set_texcoord_name(self, const_TextureStage_self, InternalName_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_texcoord_name(const TextureStage self, InternalName name)
        set_texcoord_name(const TextureStage self, str texcoord_name)
        
        /**
         * Indicate which set of UV's this texture stage will use.  Geometry may have
         * any number of associated UV sets, each of which must have a unique name.
         */
        
        /**
         * Indicate which set of UV's this texture stage will use.  Geometry may have
         * any number of associated UV sets, each of which must have a unique name.
         */
        """
        pass

    def set_tex_view_offset(self, const_TextureStage_self, int_tex_view_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_tex_view_offset(const TextureStage self, int tex_view_offset)
        
        /**
         * Sets the tex_view_offset value.  This is used only when a special multiview
         * texture is bound to the TextureStage, and it selects the particular view of
         * the texture that is to be used.
         *
         * This value is added to the similar parameter on DisplayRegion to derive the
         * final texture view index that is selected for rendering.
         */
        """
        pass

    def usesColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uses_color(TextureStage self)
        
        /**
         * Returns true if the TextureStage makes use of whatever color is specified
         * in set_color(), false otherwise.
         */
        """
        pass

    def usesLastSavedResult(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uses_last_saved_result(TextureStage self)
        
        /**
         * Returns true if the TextureStage makes use of the CS_primary_color combine
         * source.
         */
        """
        pass

    def usesPrimaryColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        uses_primary_color(TextureStage self)
        
        /**
         * Returns true if the TextureStage makes use of the CS_primary_color combine
         * source.
         */
        """
        pass

    def uses_color(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uses_color(TextureStage self)
        
        /**
         * Returns true if the TextureStage makes use of whatever color is specified
         * in set_color(), false otherwise.
         */
        """
        pass

    def uses_last_saved_result(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uses_last_saved_result(TextureStage self)
        
        /**
         * Returns true if the TextureStage makes use of the CS_primary_color combine
         * source.
         */
        """
        pass

    def uses_primary_color(self, TextureStage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        uses_primary_color(TextureStage self)
        
        /**
         * Returns true if the TextureStage makes use of the CS_primary_color combine
         * source.
         */
        """
        pass

    def write(self, TextureStage_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(TextureStage self, ostream out)
        write(TextureStage self, ostream out, int indent_level)
        
        /**
         * Writes the details of this stage
         */
        
        /**
         * Writes the details of this stage
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    alpha_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    binormal_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rgb_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    saved_result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tangent_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texcoord_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_view_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CMAdd = 3
    CMAddSigned = 4
    CMDot3Rgb = 7
    CMDot3Rgba = 8
    CMInterpolate = 5
    CMModulate = 2
    CMReplace = 1
    CMSubtract = 6
    CMUndefined = 0
    CM_add = 3
    CM_add_signed = 4
    CM_dot3_rgb = 7
    CM_dot3_rgba = 8
    CM_interpolate = 5
    CM_modulate = 2
    CM_replace = 1
    CM_subtract = 6
    CM_undefined = 0
    COOneMinusSrcAlpha = 4
    COOneMinusSrcColor = 2
    COSrcAlpha = 3
    COSrcColor = 1
    COUndefined = 0
    CO_one_minus_src_alpha = 4
    CO_one_minus_src_color = 2
    CO_src_alpha = 3
    CO_src_color = 1
    CO_undefined = 0
    CSConstant = 2
    CSConstantColorScale = 5
    CSLastSavedResult = 6
    CSPrevious = 4
    CSPrimaryColor = 3
    CSTexture = 1
    CSUndefined = 0
    CS_constant = 2
    CS_constant_color_scale = 5
    CS_last_saved_result = 6
    CS_previous = 4
    CS_primary_color = 3
    CS_texture = 1
    CS_undefined = 0
    default = None # (!) real value is 'TextureStage default'
    DtoolClassDict = {
        'CMAdd': 3,
        'CMAddSigned': 4,
        'CMDot3Rgb': 7,
        'CMDot3Rgba': 8,
        'CMInterpolate': 5,
        'CMModulate': 2,
        'CMReplace': 1,
        'CMSubtract': 6,
        'CMUndefined': 0,
        'CM_add': 3,
        'CM_add_signed': 4,
        'CM_dot3_rgb': 7,
        'CM_dot3_rgba': 8,
        'CM_interpolate': 5,
        'CM_modulate': 2,
        'CM_replace': 1,
        'CM_subtract': 6,
        'CM_undefined': 0,
        'COOneMinusSrcAlpha': 4,
        'COOneMinusSrcColor': 2,
        'COSrcAlpha': 3,
        'COSrcColor': 1,
        'COUndefined': 0,
        'CO_one_minus_src_alpha': 4,
        'CO_one_minus_src_color': 2,
        'CO_src_alpha': 3,
        'CO_src_color': 1,
        'CO_undefined': 0,
        'CSConstant': 2,
        'CSConstantColorScale': 5,
        'CSLastSavedResult': 6,
        'CSPrevious': 4,
        'CSPrimaryColor': 3,
        'CSTexture': 1,
        'CSUndefined': 0,
        'CS_constant': 2,
        'CS_constant_color_scale': 5,
        'CS_last_saved_result': 6,
        'CS_previous': 4,
        'CS_primary_color': 3,
        'CS_texture': 1,
        'CS_undefined': 0,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'MAdd': 4,
        'MBlend': 2,
        'MBlendColorScale': 6,
        'MCombine': 5,
        'MDecal': 1,
        'MEmission': 16,
        'MGloss': 12,
        'MGlow': 11,
        'MHeight': 13,
        'MModulate': 0,
        'MModulateGloss': 8,
        'MModulateGlow': 7,
        'MNormal': 9,
        'MNormalGloss': 15,
        'MNormalHeight': 10,
        'MReplace': 3,
        'MSelector': 14,
        'M_add': 4,
        'M_blend': 2,
        'M_blend_color_scale': 6,
        'M_combine': 5,
        'M_decal': 1,
        'M_emission': 16,
        'M_gloss': 12,
        'M_glow': 11,
        'M_height': 13,
        'M_modulate': 0,
        'M_modulate_gloss': 8,
        'M_modulate_glow': 7,
        'M_normal': 9,
        'M_normal_gloss': 15,
        'M_normal_height': 10,
        'M_replace': 3,
        'M_selector': 14,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.TextureStage' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.TextureStage' objects>"
        '__doc__': '/**\n * Defines the properties of a named stage of the multitexture pipeline.  The\n * TextureAttrib will associated a number of these stages with Texture\n * objects, and the GSG will render geometry by sorting all of the currently\n * active TextureStages in order and then issuing the appropriate rendering\n * calls to activate them.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.TextureStage' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.TextureStage' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.TextureStage' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.TextureStage' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.TextureStage' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.TextureStage' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.TextureStage' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.TextureStage' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FCCA0>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.TextureStage' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.TextureStage' objects>"
        'alpha_scale': None, # (!) real value is "<attribute 'alpha_scale' of 'panda3d.core.TextureStage' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.TextureStage' objects>"
        'binormal_name': None, # (!) real value is "<attribute 'binormal_name' of 'panda3d.core.TextureStage' objects>"
        'color': None, # (!) real value is "<attribute 'color' of 'panda3d.core.TextureStage' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.TextureStage' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.TextureStage' objects>"
        'default': None, # (!) real value is "<attribute 'default' of 'panda3d.core.TextureStage'>"
        'getAlphaScale': None, # (!) real value is "<method 'getAlphaScale' of 'panda3d.core.TextureStage' objects>"
        'getBinormalName': None, # (!) real value is "<method 'getBinormalName' of 'panda3d.core.TextureStage' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FCCA0>)>'
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d.core.TextureStage' objects>"
        'getCombineAlphaMode': None, # (!) real value is "<method 'getCombineAlphaMode' of 'panda3d.core.TextureStage' objects>"
        'getCombineAlphaOperand0': None, # (!) real value is "<method 'getCombineAlphaOperand0' of 'panda3d.core.TextureStage' objects>"
        'getCombineAlphaOperand1': None, # (!) real value is "<method 'getCombineAlphaOperand1' of 'panda3d.core.TextureStage' objects>"
        'getCombineAlphaOperand2': None, # (!) real value is "<method 'getCombineAlphaOperand2' of 'panda3d.core.TextureStage' objects>"
        'getCombineAlphaSource0': None, # (!) real value is "<method 'getCombineAlphaSource0' of 'panda3d.core.TextureStage' objects>"
        'getCombineAlphaSource1': None, # (!) real value is "<method 'getCombineAlphaSource1' of 'panda3d.core.TextureStage' objects>"
        'getCombineAlphaSource2': None, # (!) real value is "<method 'getCombineAlphaSource2' of 'panda3d.core.TextureStage' objects>"
        'getCombineRgbMode': None, # (!) real value is "<method 'getCombineRgbMode' of 'panda3d.core.TextureStage' objects>"
        'getCombineRgbOperand0': None, # (!) real value is "<method 'getCombineRgbOperand0' of 'panda3d.core.TextureStage' objects>"
        'getCombineRgbOperand1': None, # (!) real value is "<method 'getCombineRgbOperand1' of 'panda3d.core.TextureStage' objects>"
        'getCombineRgbOperand2': None, # (!) real value is "<method 'getCombineRgbOperand2' of 'panda3d.core.TextureStage' objects>"
        'getCombineRgbSource0': None, # (!) real value is "<method 'getCombineRgbSource0' of 'panda3d.core.TextureStage' objects>"
        'getCombineRgbSource1': None, # (!) real value is "<method 'getCombineRgbSource1' of 'panda3d.core.TextureStage' objects>"
        'getCombineRgbSource2': None, # (!) real value is "<method 'getCombineRgbSource2' of 'panda3d.core.TextureStage' objects>"
        'getDefault': None, # (!) real value is '<staticmethod(<built-in method getDefault of type object at 0x00007FFCFE2FCCA0>)>'
        'getMode': None, # (!) real value is "<method 'getMode' of 'panda3d.core.TextureStage' objects>"
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.TextureStage' objects>"
        'getNumCombineAlphaOperands': None, # (!) real value is "<method 'getNumCombineAlphaOperands' of 'panda3d.core.TextureStage' objects>"
        'getNumCombineRgbOperands': None, # (!) real value is "<method 'getNumCombineRgbOperands' of 'panda3d.core.TextureStage' objects>"
        'getPriority': None, # (!) real value is "<method 'getPriority' of 'panda3d.core.TextureStage' objects>"
        'getRgbScale': None, # (!) real value is "<method 'getRgbScale' of 'panda3d.core.TextureStage' objects>"
        'getSavedResult': None, # (!) real value is "<method 'getSavedResult' of 'panda3d.core.TextureStage' objects>"
        'getSort': None, # (!) real value is "<method 'getSort' of 'panda3d.core.TextureStage' objects>"
        'getTangentName': None, # (!) real value is "<method 'getTangentName' of 'panda3d.core.TextureStage' objects>"
        'getTexViewOffset': None, # (!) real value is "<method 'getTexViewOffset' of 'panda3d.core.TextureStage' objects>"
        'getTexcoordName': None, # (!) real value is "<method 'getTexcoordName' of 'panda3d.core.TextureStage' objects>"
        'get_alpha_scale': None, # (!) real value is "<method 'get_alpha_scale' of 'panda3d.core.TextureStage' objects>"
        'get_binormal_name': None, # (!) real value is "<method 'get_binormal_name' of 'panda3d.core.TextureStage' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FCCA0>)>'
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d.core.TextureStage' objects>"
        'get_combine_alpha_mode': None, # (!) real value is "<method 'get_combine_alpha_mode' of 'panda3d.core.TextureStage' objects>"
        'get_combine_alpha_operand0': None, # (!) real value is "<method 'get_combine_alpha_operand0' of 'panda3d.core.TextureStage' objects>"
        'get_combine_alpha_operand1': None, # (!) real value is "<method 'get_combine_alpha_operand1' of 'panda3d.core.TextureStage' objects>"
        'get_combine_alpha_operand2': None, # (!) real value is "<method 'get_combine_alpha_operand2' of 'panda3d.core.TextureStage' objects>"
        'get_combine_alpha_source0': None, # (!) real value is "<method 'get_combine_alpha_source0' of 'panda3d.core.TextureStage' objects>"
        'get_combine_alpha_source1': None, # (!) real value is "<method 'get_combine_alpha_source1' of 'panda3d.core.TextureStage' objects>"
        'get_combine_alpha_source2': None, # (!) real value is "<method 'get_combine_alpha_source2' of 'panda3d.core.TextureStage' objects>"
        'get_combine_rgb_mode': None, # (!) real value is "<method 'get_combine_rgb_mode' of 'panda3d.core.TextureStage' objects>"
        'get_combine_rgb_operand0': None, # (!) real value is "<method 'get_combine_rgb_operand0' of 'panda3d.core.TextureStage' objects>"
        'get_combine_rgb_operand1': None, # (!) real value is "<method 'get_combine_rgb_operand1' of 'panda3d.core.TextureStage' objects>"
        'get_combine_rgb_operand2': None, # (!) real value is "<method 'get_combine_rgb_operand2' of 'panda3d.core.TextureStage' objects>"
        'get_combine_rgb_source0': None, # (!) real value is "<method 'get_combine_rgb_source0' of 'panda3d.core.TextureStage' objects>"
        'get_combine_rgb_source1': None, # (!) real value is "<method 'get_combine_rgb_source1' of 'panda3d.core.TextureStage' objects>"
        'get_combine_rgb_source2': None, # (!) real value is "<method 'get_combine_rgb_source2' of 'panda3d.core.TextureStage' objects>"
        'get_default': None, # (!) real value is '<staticmethod(<built-in method get_default of type object at 0x00007FFCFE2FCCA0>)>'
        'get_mode': None, # (!) real value is "<method 'get_mode' of 'panda3d.core.TextureStage' objects>"
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.TextureStage' objects>"
        'get_num_combine_alpha_operands': None, # (!) real value is "<method 'get_num_combine_alpha_operands' of 'panda3d.core.TextureStage' objects>"
        'get_num_combine_rgb_operands': None, # (!) real value is "<method 'get_num_combine_rgb_operands' of 'panda3d.core.TextureStage' objects>"
        'get_priority': None, # (!) real value is "<method 'get_priority' of 'panda3d.core.TextureStage' objects>"
        'get_rgb_scale': None, # (!) real value is "<method 'get_rgb_scale' of 'panda3d.core.TextureStage' objects>"
        'get_saved_result': None, # (!) real value is "<method 'get_saved_result' of 'panda3d.core.TextureStage' objects>"
        'get_sort': None, # (!) real value is "<method 'get_sort' of 'panda3d.core.TextureStage' objects>"
        'get_tangent_name': None, # (!) real value is "<method 'get_tangent_name' of 'panda3d.core.TextureStage' objects>"
        'get_tex_view_offset': None, # (!) real value is "<method 'get_tex_view_offset' of 'panda3d.core.TextureStage' objects>"
        'get_texcoord_name': None, # (!) real value is "<method 'get_texcoord_name' of 'panda3d.core.TextureStage' objects>"
        'involvesColorScale': None, # (!) real value is "<method 'involvesColorScale' of 'panda3d.core.TextureStage' objects>"
        'involves_color_scale': None, # (!) real value is "<method 'involves_color_scale' of 'panda3d.core.TextureStage' objects>"
        'isFixedFunction': None, # (!) real value is "<method 'isFixedFunction' of 'panda3d.core.TextureStage' objects>"
        'is_fixed_function': None, # (!) real value is "<method 'is_fixed_function' of 'panda3d.core.TextureStage' objects>"
        'mode': None, # (!) real value is "<attribute 'mode' of 'panda3d.core.TextureStage' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.TextureStage' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.TextureStage' objects>"
        'priority': None, # (!) real value is "<attribute 'priority' of 'panda3d.core.TextureStage' objects>"
        'rgb_scale': None, # (!) real value is "<attribute 'rgb_scale' of 'panda3d.core.TextureStage' objects>"
        'saved_result': None, # (!) real value is "<attribute 'saved_result' of 'panda3d.core.TextureStage' objects>"
        'setAlphaScale': None, # (!) real value is "<method 'setAlphaScale' of 'panda3d.core.TextureStage' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.core.TextureStage' objects>"
        'setCombineAlpha': None, # (!) real value is "<method 'setCombineAlpha' of 'panda3d.core.TextureStage' objects>"
        'setCombineRgb': None, # (!) real value is "<method 'setCombineRgb' of 'panda3d.core.TextureStage' objects>"
        'setMode': None, # (!) real value is "<method 'setMode' of 'panda3d.core.TextureStage' objects>"
        'setName': None, # (!) real value is "<method 'setName' of 'panda3d.core.TextureStage' objects>"
        'setPriority': None, # (!) real value is "<method 'setPriority' of 'panda3d.core.TextureStage' objects>"
        'setRgbScale': None, # (!) real value is "<method 'setRgbScale' of 'panda3d.core.TextureStage' objects>"
        'setSavedResult': None, # (!) real value is "<method 'setSavedResult' of 'panda3d.core.TextureStage' objects>"
        'setSort': None, # (!) real value is "<method 'setSort' of 'panda3d.core.TextureStage' objects>"
        'setTexViewOffset': None, # (!) real value is "<method 'setTexViewOffset' of 'panda3d.core.TextureStage' objects>"
        'setTexcoordName': None, # (!) real value is "<method 'setTexcoordName' of 'panda3d.core.TextureStage' objects>"
        'set_alpha_scale': None, # (!) real value is "<method 'set_alpha_scale' of 'panda3d.core.TextureStage' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.core.TextureStage' objects>"
        'set_combine_alpha': None, # (!) real value is "<method 'set_combine_alpha' of 'panda3d.core.TextureStage' objects>"
        'set_combine_rgb': None, # (!) real value is "<method 'set_combine_rgb' of 'panda3d.core.TextureStage' objects>"
        'set_mode': None, # (!) real value is "<method 'set_mode' of 'panda3d.core.TextureStage' objects>"
        'set_name': None, # (!) real value is "<method 'set_name' of 'panda3d.core.TextureStage' objects>"
        'set_priority': None, # (!) real value is "<method 'set_priority' of 'panda3d.core.TextureStage' objects>"
        'set_rgb_scale': None, # (!) real value is "<method 'set_rgb_scale' of 'panda3d.core.TextureStage' objects>"
        'set_saved_result': None, # (!) real value is "<method 'set_saved_result' of 'panda3d.core.TextureStage' objects>"
        'set_sort': None, # (!) real value is "<method 'set_sort' of 'panda3d.core.TextureStage' objects>"
        'set_tex_view_offset': None, # (!) real value is "<method 'set_tex_view_offset' of 'panda3d.core.TextureStage' objects>"
        'set_texcoord_name': None, # (!) real value is "<method 'set_texcoord_name' of 'panda3d.core.TextureStage' objects>"
        'sort': None, # (!) real value is "<attribute 'sort' of 'panda3d.core.TextureStage' objects>"
        'tangent_name': None, # (!) real value is "<attribute 'tangent_name' of 'panda3d.core.TextureStage' objects>"
        'tex_view_offset': None, # (!) real value is "<attribute 'tex_view_offset' of 'panda3d.core.TextureStage' objects>"
        'texcoord_name': None, # (!) real value is "<attribute 'texcoord_name' of 'panda3d.core.TextureStage' objects>"
        'usesColor': None, # (!) real value is "<method 'usesColor' of 'panda3d.core.TextureStage' objects>"
        'usesLastSavedResult': None, # (!) real value is "<method 'usesLastSavedResult' of 'panda3d.core.TextureStage' objects>"
        'usesPrimaryColor': None, # (!) real value is "<method 'usesPrimaryColor' of 'panda3d.core.TextureStage' objects>"
        'uses_color': None, # (!) real value is "<method 'uses_color' of 'panda3d.core.TextureStage' objects>"
        'uses_last_saved_result': None, # (!) real value is "<method 'uses_last_saved_result' of 'panda3d.core.TextureStage' objects>"
        'uses_primary_color': None, # (!) real value is "<method 'uses_primary_color' of 'panda3d.core.TextureStage' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.TextureStage' objects>"
    }
    MAdd = 4
    MBlend = 2
    MBlendColorScale = 6
    MCombine = 5
    MDecal = 1
    MEmission = 16
    MGloss = 12
    MGlow = 11
    MHeight = 13
    MModulate = 0
    MModulateGloss = 8
    MModulateGlow = 7
    MNormal = 9
    MNormalGloss = 15
    MNormalHeight = 10
    MReplace = 3
    MSelector = 14
    M_add = 4
    M_blend = 2
    M_blend_color_scale = 6
    M_combine = 5
    M_decal = 1
    M_emission = 16
    M_gloss = 12
    M_glow = 11
    M_height = 13
    M_modulate = 0
    M_modulate_gloss = 8
    M_modulate_glow = 7
    M_normal = 9
    M_normal_gloss = 15
    M_normal_height = 10
    M_replace = 3
    M_selector = 14


