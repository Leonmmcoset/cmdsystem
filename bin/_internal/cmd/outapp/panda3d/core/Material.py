# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedWritableReferenceCount import TypedWritableReferenceCount

from .Namable import Namable

class Material(TypedWritableReferenceCount, Namable):
    """
    /**
     * Defines the way an object appears in the presence of lighting.  A material
     * is only necessary if lighting is to be enabled; otherwise, the material
     * isn't used.
     *
     * There are two workflows that are supported: the "classic" workflow of
     * providing separate ambient, diffuse and specular colors, and the
     * "metalness" workflow, in which a base color is specified along with a
     * "metallic" value that indicates whether the material is a metal or a
     * dielectric.
     *
     * The size of the specular highlight can be specified by either specifying
     * the specular exponent (shininess) or by specifying a roughness value that
     * in perceptually linear in the range of 0-1.
     */
    """
    def assign(self, const_Material_self, const_Material_copy): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        assign(const Material self, const Material copy)
        """
        pass

    def clearAmbient(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_ambient(const Material self)
        
        /**
         * Removes the explicit ambient color from the material.
         */
        """
        pass

    def clearBaseColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_base_color(const Material self)
        
        /**
         * Removes the explicit base_color color from the material.
         */
        """
        pass

    def clearDiffuse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_diffuse(const Material self)
        
        /**
         * Removes the explicit diffuse color from the material.
         */
        """
        pass

    def clearEmission(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_emission(const Material self)
        
        /**
         * Removes the explicit emission color from the material.
         */
        """
        pass

    def clearMetallic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_metallic(const Material self)
        
        /**
         * Removes the explicit metallic setting from the material.
         */
        """
        pass

    def clearSpecular(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_specular(const Material self)
        
        /**
         * Removes the explicit specular color from the material.
         */
        """
        pass

    def clear_ambient(self, const_Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_ambient(const Material self)
        
        /**
         * Removes the explicit ambient color from the material.
         */
        """
        pass

    def clear_base_color(self, const_Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_base_color(const Material self)
        
        /**
         * Removes the explicit base_color color from the material.
         */
        """
        pass

    def clear_diffuse(self, const_Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_diffuse(const Material self)
        
        /**
         * Removes the explicit diffuse color from the material.
         */
        """
        pass

    def clear_emission(self, const_Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_emission(const Material self)
        
        /**
         * Removes the explicit emission color from the material.
         */
        """
        pass

    def clear_metallic(self, const_Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_metallic(const Material self)
        
        /**
         * Removes the explicit metallic setting from the material.
         */
        """
        pass

    def clear_specular(self, const_Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_specular(const Material self)
        
        /**
         * Removes the explicit specular color from the material.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(Material self, const Material other)
        
        /**
         * Returns a number less than zero if this material sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         * The sorting order is arbitrary and largely meaningless, except to
         * differentiate different materials.
         */
        """
        pass

    def compare_to(self, Material_self, const_Material_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(Material self, const Material other)
        
        /**
         * Returns a number less than zero if this material sorts before the other
         * one, greater than zero if it sorts after, or zero if they are equivalent.
         * The sorting order is arbitrary and largely meaningless, except to
         * differentiate different materials.
         */
        """
        pass

    def getAmbient(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ambient(Material self)
        
        /**
         * Returns the ambient color setting, if it has been set.  Returns (0,0,0,0)
         * if the ambient color has not been set.
         */
        """
        pass

    def getBaseColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_base_color(Material self)
        
        /**
         * Returns the base_color color setting, if it has been set.  If neither the
         * base color nor the metallic have been set, this returns the diffuse color.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default()
        
        /**
         * Returns the default material.
         */
        """
        pass

    def getDiffuse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_diffuse(Material self)
        
        /**
         * Returns the diffuse color setting, if it has been set.  Returns (1,1,1,1)
         * if the diffuse color has not been set.
         */
        """
        pass

    def getEmission(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_emission(Material self)
        
        /**
         * Returns the emission color setting, if it has been set.  Returns (0,0,0,0)
         * if the emission color has not been set.
         */
        """
        pass

    def getLocal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_local(Material self)
        
        /**
         * Returns the local viewer flag.  Set set_local().
         */
        """
        pass

    def getMetallic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_metallic(Material self)
        
        /**
         * Returns the metallic setting, if it has been set.  Returns 0 if it has not
         * been set.
         */
        """
        pass

    def getRefractiveIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_refractive_index(Material self)
        
        /**
         * Returns the index of refraction, or 1 if none has been set for this
         * material.
         */
        """
        pass

    def getRoughness(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_roughness(Material self)
        
        /**
         * Returns the roughness previously specified by set_roughness.  If none was
         * previously set, this value is computed from the shininess value.
         */
        """
        pass

    def getShininess(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_shininess(Material self)
        
        /**
         * Returns the shininess exponent of the material.
         */
        """
        pass

    def getSpecular(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_specular(Material self)
        
        /**
         * Returns the specular color setting, if it has been set.  Returns (0,0,0,0)
         * if the specular color has not been set.
         */
        """
        pass

    def getTwoside(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_twoside(Material self)
        
        /**
         * Returns the state of the two-sided lighting flag.  See set_twoside().
         */
        """
        pass

    def get_ambient(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ambient(Material self)
        
        /**
         * Returns the ambient color setting, if it has been set.  Returns (0,0,0,0)
         * if the ambient color has not been set.
         */
        """
        pass

    def get_base_color(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_base_color(Material self)
        
        /**
         * Returns the base_color color setting, if it has been set.  If neither the
         * base color nor the metallic have been set, this returns the diffuse color.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default()
        
        /**
         * Returns the default material.
         */
        """
        pass

    def get_diffuse(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_diffuse(Material self)
        
        /**
         * Returns the diffuse color setting, if it has been set.  Returns (1,1,1,1)
         * if the diffuse color has not been set.
         */
        """
        pass

    def get_emission(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_emission(Material self)
        
        /**
         * Returns the emission color setting, if it has been set.  Returns (0,0,0,0)
         * if the emission color has not been set.
         */
        """
        pass

    def get_local(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_local(Material self)
        
        /**
         * Returns the local viewer flag.  Set set_local().
         */
        """
        pass

    def get_metallic(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_metallic(Material self)
        
        /**
         * Returns the metallic setting, if it has been set.  Returns 0 if it has not
         * been set.
         */
        """
        pass

    def get_refractive_index(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_refractive_index(Material self)
        
        /**
         * Returns the index of refraction, or 1 if none has been set for this
         * material.
         */
        """
        pass

    def get_roughness(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_roughness(Material self)
        
        /**
         * Returns the roughness previously specified by set_roughness.  If none was
         * previously set, this value is computed from the shininess value.
         */
        """
        pass

    def get_shininess(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_shininess(Material self)
        
        /**
         * Returns the shininess exponent of the material.
         */
        """
        pass

    def get_specular(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_specular(Material self)
        
        /**
         * Returns the specular color setting, if it has been set.  Returns (0,0,0,0)
         * if the specular color has not been set.
         */
        """
        pass

    def get_twoside(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_twoside(Material self)
        
        /**
         * Returns the state of the two-sided lighting flag.  See set_twoside().
         */
        """
        pass

    def hasAmbient(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_ambient(Material self)
        
        /**
         * Returns true if the ambient color has been explicitly set for this
         * material, false otherwise.
         */
        """
        pass

    def hasBaseColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_base_color(Material self)
        
        /**
         * Returns true if the base color has been explicitly set for this material,
         * false otherwise.
         */
        """
        pass

    def hasDiffuse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_diffuse(Material self)
        
        /**
         * Returns true if the diffuse color has been explicitly set for this
         * material, false otherwise.
         */
        """
        pass

    def hasEmission(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_emission(Material self)
        
        /**
         * Returns true if the emission color has been explicitly set for this
         * material, false otherwise.
         */
        """
        pass

    def hasMetallic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_metallic(Material self)
        
        /**
         * Returns true if the metallic has been explicitly set for this material,
         * false otherwise.
         */
        """
        pass

    def hasRefractiveIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_refractive_index(Material self)
        
        /**
         * Returns true if a refractive index has explicitly been specified for this
         * material.
         */
        """
        pass

    def hasRoughness(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_roughness(Material self)
        
        /**
         * Returns true if the roughness has been explicitly set for this material,
         * false otherwise.
         */
        """
        pass

    def hasSpecular(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_specular(Material self)
        
        /**
         * Returns true if the specular color has been explicitly set for this
         * material, false otherwise.
         */
        """
        pass

    def has_ambient(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_ambient(Material self)
        
        /**
         * Returns true if the ambient color has been explicitly set for this
         * material, false otherwise.
         */
        """
        pass

    def has_base_color(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_base_color(Material self)
        
        /**
         * Returns true if the base color has been explicitly set for this material,
         * false otherwise.
         */
        """
        pass

    def has_diffuse(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_diffuse(Material self)
        
        /**
         * Returns true if the diffuse color has been explicitly set for this
         * material, false otherwise.
         */
        """
        pass

    def has_emission(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_emission(Material self)
        
        /**
         * Returns true if the emission color has been explicitly set for this
         * material, false otherwise.
         */
        """
        pass

    def has_metallic(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_metallic(Material self)
        
        /**
         * Returns true if the metallic has been explicitly set for this material,
         * false otherwise.
         */
        """
        pass

    def has_refractive_index(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_refractive_index(Material self)
        
        /**
         * Returns true if a refractive index has explicitly been specified for this
         * material.
         */
        """
        pass

    def has_roughness(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_roughness(Material self)
        
        /**
         * Returns true if the roughness has been explicitly set for this material,
         * false otherwise.
         */
        """
        pass

    def has_specular(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_specular(Material self)
        
        /**
         * Returns true if the specular color has been explicitly set for this
         * material, false otherwise.
         */
        """
        pass

    def isAttribLocked(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_attrib_locked(Material self)
        
        /**
         * @deprecated This no longer has any meaning in 1.10.
         */
        """
        pass

    def is_attrib_locked(self, Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_attrib_locked(Material self)
        
        /**
         * @deprecated This no longer has any meaning in 1.10.
         */
        """
        pass

    def output(self, Material_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(Material self, ostream out)
        
        /**
         *
         */
        """
        pass

    def setAmbient(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ambient(const Material self, const LVecBase4f color)
        
        /**
         * Specifies the ambient color setting of the material.  This will be the
         * multiplied by any ambient lights in effect on the material to set its base
         * color.
         *
         * This is the color of the object as it appears in the absence of direct
         * light.
         *
         * If this is not set, the object color will be used.
         */
        """
        pass

    def setAttribLock(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_attrib_lock(const Material self)
        
        /**
         * @deprecated This no longer has any meaning in 1.10.
         */
        """
        pass

    def setBaseColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_base_color(const Material self, const LVecBase4f color)
        
        /**
         * Specifies the base color of the material.  In conjunction with
         * set_metallic, this is an alternate way to specify the color of a material.
         * For dielectrics, this will determine the value of the diffuse color, and
         * for metals, this will determine the value of the specular color.
         *
         * Setting this will clear an explicit specular, diffuse or ambient color
         * assignment.
         *
         * If this is not set, the object color will be used.
         */
        """
        pass

    def setDiffuse(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_diffuse(const Material self, const LVecBase4f color)
        
        /**
         * Specifies the diffuse color setting of the material.  This will be
         * multiplied by any lights in effect on the material to get the color in the
         * parts of the object illuminated by the lights.
         *
         * This is the primary color of an object; the color of the object as it
         * appears in direct light, in the absence of highlights.
         *
         * If this is not set, the object color will be used.
         */
        """
        pass

    def setEmission(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_emission(const Material self, const LVecBase4f color)
        
        /**
         * Specifies the emission color setting of the material.  This is the color of
         * the object as it appears in the absence of any light whatsover, including
         * ambient light.  It is as if the object is glowing by this color (although
         * of course it will not illuminate neighboring objects).
         *
         * If this is not set, the object will not glow by its own light and will only
         * appear visible in the presence of one or more lights.
         */
        """
        pass

    def setLocal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_local(const Material self, bool local)
        
        /**
         * Sets the local viewer flag.  Set this true to enable camera-relative
         * specular highlights, or false to use orthogonal specular highlights.  The
         * default value is true.  Applications that use orthogonal projection should
         * specify false.
         */
        """
        pass

    def setMetallic(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_metallic(const Material self, float metallic)
        
        /**
         * Sets the metallic setting of the material, which is is used for physically-
         * based rendering models.  This is usually 0 for dielectric materials and 1
         * for metals.  It really does not make sense to set this to a value other
         * than 0 or 1, but it is nonetheless a float for compatibility with tools
         * that allow setting this to values other than 0 or 1.
         */
        """
        pass

    def setRefractiveIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_refractive_index(const Material self, float refractive_index)
        
        /**
         * Sets the index of refraction of the material, which is used to determine
         * the specular color in absence of an explicit specular color assignment.
         * This is usually 1.5 for dielectric materials.  It is not very useful for
         * metals, since they cannot be described as easily with a single number.
         *
         * Should be 1 or higher.  The default is 1.
         */
        """
        pass

    def setRoughness(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_roughness(const Material self, float roughness)
        
        /**
         * Sets the roughness exponent of the material, where 0 is completely shiny
         * (infinite shininess), and 1 is a completely dull object (0 shininess).
         * This is a different, more perceptually intuitive way of controlling the
         * size of the specular spot, and more commonly used in physically-based
         * rendering.
         *
         * Setting a roughness recalculates the shininess value.
         */
        """
        pass

    def setShininess(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_shininess(const Material self, float shininess)
        
        /**
         * Sets the shininess exponent of the material.  This controls the size of the
         * specular highlight spot.  In general, larger number produce a smaller
         * specular highlight, which makes the object appear shinier.  Smaller numbers
         * produce a larger highlight, which makes the object appear less shiny.
         *
         * This is usually in the range 0..128.
         *
         * Setting a shininess value removes any previous roughness assignment.
         */
        """
        pass

    def setSpecular(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_specular(const Material self, const LVecBase4f color)
        
        /**
         * Specifies the specular color setting of the material.  This will be
         * multiplied by any lights in effect on the material to compute the color of
         * specular highlights on the object.
         *
         * This is the highlight color of an object: the color of small highlight
         * reflections.
         *
         * If this is not set, the specular color is taken from the index of
         * refraction, which is 1 by default (meaning no specular reflections are
         * generated).
         */
        """
        pass

    def setTwoside(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_twoside(const Material self, bool twoside)
        
        /**
         * Set this true to enable two-sided lighting.  When two-sided lighting is on,
         * both sides of a polygon will be lit by this material.  The default is for
         * two-sided lighting to be off, in which case only the front surface is lit.
         */
        """
        pass

    def set_ambient(self, const_Material_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ambient(const Material self, const LVecBase4f color)
        
        /**
         * Specifies the ambient color setting of the material.  This will be the
         * multiplied by any ambient lights in effect on the material to set its base
         * color.
         *
         * This is the color of the object as it appears in the absence of direct
         * light.
         *
         * If this is not set, the object color will be used.
         */
        """
        pass

    def set_attrib_lock(self, const_Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_attrib_lock(const Material self)
        
        /**
         * @deprecated This no longer has any meaning in 1.10.
         */
        """
        pass

    def set_base_color(self, const_Material_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_base_color(const Material self, const LVecBase4f color)
        
        /**
         * Specifies the base color of the material.  In conjunction with
         * set_metallic, this is an alternate way to specify the color of a material.
         * For dielectrics, this will determine the value of the diffuse color, and
         * for metals, this will determine the value of the specular color.
         *
         * Setting this will clear an explicit specular, diffuse or ambient color
         * assignment.
         *
         * If this is not set, the object color will be used.
         */
        """
        pass

    def set_diffuse(self, const_Material_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_diffuse(const Material self, const LVecBase4f color)
        
        /**
         * Specifies the diffuse color setting of the material.  This will be
         * multiplied by any lights in effect on the material to get the color in the
         * parts of the object illuminated by the lights.
         *
         * This is the primary color of an object; the color of the object as it
         * appears in direct light, in the absence of highlights.
         *
         * If this is not set, the object color will be used.
         */
        """
        pass

    def set_emission(self, const_Material_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_emission(const Material self, const LVecBase4f color)
        
        /**
         * Specifies the emission color setting of the material.  This is the color of
         * the object as it appears in the absence of any light whatsover, including
         * ambient light.  It is as if the object is glowing by this color (although
         * of course it will not illuminate neighboring objects).
         *
         * If this is not set, the object will not glow by its own light and will only
         * appear visible in the presence of one or more lights.
         */
        """
        pass

    def set_local(self, const_Material_self, bool_local): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_local(const Material self, bool local)
        
        /**
         * Sets the local viewer flag.  Set this true to enable camera-relative
         * specular highlights, or false to use orthogonal specular highlights.  The
         * default value is true.  Applications that use orthogonal projection should
         * specify false.
         */
        """
        pass

    def set_metallic(self, const_Material_self, float_metallic): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_metallic(const Material self, float metallic)
        
        /**
         * Sets the metallic setting of the material, which is is used for physically-
         * based rendering models.  This is usually 0 for dielectric materials and 1
         * for metals.  It really does not make sense to set this to a value other
         * than 0 or 1, but it is nonetheless a float for compatibility with tools
         * that allow setting this to values other than 0 or 1.
         */
        """
        pass

    def set_refractive_index(self, const_Material_self, float_refractive_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_refractive_index(const Material self, float refractive_index)
        
        /**
         * Sets the index of refraction of the material, which is used to determine
         * the specular color in absence of an explicit specular color assignment.
         * This is usually 1.5 for dielectric materials.  It is not very useful for
         * metals, since they cannot be described as easily with a single number.
         *
         * Should be 1 or higher.  The default is 1.
         */
        """
        pass

    def set_roughness(self, const_Material_self, float_roughness): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_roughness(const Material self, float roughness)
        
        /**
         * Sets the roughness exponent of the material, where 0 is completely shiny
         * (infinite shininess), and 1 is a completely dull object (0 shininess).
         * This is a different, more perceptually intuitive way of controlling the
         * size of the specular spot, and more commonly used in physically-based
         * rendering.
         *
         * Setting a roughness recalculates the shininess value.
         */
        """
        pass

    def set_shininess(self, const_Material_self, float_shininess): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_shininess(const Material self, float shininess)
        
        /**
         * Sets the shininess exponent of the material.  This controls the size of the
         * specular highlight spot.  In general, larger number produce a smaller
         * specular highlight, which makes the object appear shinier.  Smaller numbers
         * produce a larger highlight, which makes the object appear less shiny.
         *
         * This is usually in the range 0..128.
         *
         * Setting a shininess value removes any previous roughness assignment.
         */
        """
        pass

    def set_specular(self, const_Material_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_specular(const Material self, const LVecBase4f color)
        
        /**
         * Specifies the specular color setting of the material.  This will be
         * multiplied by any lights in effect on the material to compute the color of
         * specular highlights on the object.
         *
         * This is the highlight color of an object: the color of small highlight
         * reflections.
         *
         * If this is not set, the specular color is taken from the index of
         * refraction, which is 1 by default (meaning no specular reflections are
         * generated).
         */
        """
        pass

    def set_twoside(self, const_Material_self, bool_twoside): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_twoside(const Material self, bool twoside)
        
        /**
         * Set this true to enable two-sided lighting.  When two-sided lighting is on,
         * both sides of a polygon will be lit by this material.  The default is for
         * two-sided lighting to be off, in which case only the front surface is lit.
         */
        """
        pass

    def upcastToNamable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_Namable(const Material self)
        
        upcast from Material to Namable
        """
        pass

    def upcastToTypedWritableReferenceCount(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const Material self)
        
        upcast from Material to TypedWritableReferenceCount
        """
        pass

    def upcast_to_Namable(self, const_Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_Namable(const Material self)
        
        upcast from Material to Namable
        """
        pass

    def upcast_to_TypedWritableReferenceCount(self, const_Material_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        upcast_to_TypedWritableReferenceCount(const Material self)
        
        upcast from Material to TypedWritableReferenceCount
        """
        pass

    def write(self, Material_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(Material self, ostream out, int indent)
        
        /**
         *
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

    ambient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    base_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    emission = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    local = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metallic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refractive_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    roughness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shininess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    specular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    twoside = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Material' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Material' objects>"
        '__doc__': '/**\n * Defines the way an object appears in the presence of lighting.  A material\n * is only necessary if lighting is to be enabled; otherwise, the material\n * isn\'t used.\n *\n * There are two workflows that are supported: the "classic" workflow of\n * providing separate ambient, diffuse and specular colors, and the\n * "metalness" workflow, in which a base color is specified along with a\n * "metallic" value that indicates whether the material is a metal or a\n * dielectric.\n *\n * The size of the specular highlight can be specified by either specifying\n * the specular exponent (shininess) or by specifying a roughness value that\n * in perceptually linear in the range of 0-1.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.Material' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.Material' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.Material' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.Material' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Material' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.Material' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.Material' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.Material' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FF820>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.Material' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.Material' objects>"
        'ambient': None, # (!) real value is "<attribute 'ambient' of 'panda3d.core.Material' objects>"
        'assign': None, # (!) real value is "<method 'assign' of 'panda3d.core.Material' objects>"
        'base_color': None, # (!) real value is "<attribute 'base_color' of 'panda3d.core.Material' objects>"
        'clearAmbient': None, # (!) real value is "<method 'clearAmbient' of 'panda3d.core.Material' objects>"
        'clearBaseColor': None, # (!) real value is "<method 'clearBaseColor' of 'panda3d.core.Material' objects>"
        'clearDiffuse': None, # (!) real value is "<method 'clearDiffuse' of 'panda3d.core.Material' objects>"
        'clearEmission': None, # (!) real value is "<method 'clearEmission' of 'panda3d.core.Material' objects>"
        'clearMetallic': None, # (!) real value is "<method 'clearMetallic' of 'panda3d.core.Material' objects>"
        'clearSpecular': None, # (!) real value is "<method 'clearSpecular' of 'panda3d.core.Material' objects>"
        'clear_ambient': None, # (!) real value is "<method 'clear_ambient' of 'panda3d.core.Material' objects>"
        'clear_base_color': None, # (!) real value is "<method 'clear_base_color' of 'panda3d.core.Material' objects>"
        'clear_diffuse': None, # (!) real value is "<method 'clear_diffuse' of 'panda3d.core.Material' objects>"
        'clear_emission': None, # (!) real value is "<method 'clear_emission' of 'panda3d.core.Material' objects>"
        'clear_metallic': None, # (!) real value is "<method 'clear_metallic' of 'panda3d.core.Material' objects>"
        'clear_specular': None, # (!) real value is "<method 'clear_specular' of 'panda3d.core.Material' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.Material' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.Material' objects>"
        'diffuse': None, # (!) real value is "<attribute 'diffuse' of 'panda3d.core.Material' objects>"
        'emission': None, # (!) real value is "<attribute 'emission' of 'panda3d.core.Material' objects>"
        'getAmbient': None, # (!) real value is "<method 'getAmbient' of 'panda3d.core.Material' objects>"
        'getBaseColor': None, # (!) real value is "<method 'getBaseColor' of 'panda3d.core.Material' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FF820>)>'
        'getDefault': None, # (!) real value is '<staticmethod(<built-in method getDefault of type object at 0x00007FFCFE2FF820>)>'
        'getDiffuse': None, # (!) real value is "<method 'getDiffuse' of 'panda3d.core.Material' objects>"
        'getEmission': None, # (!) real value is "<method 'getEmission' of 'panda3d.core.Material' objects>"
        'getLocal': None, # (!) real value is "<method 'getLocal' of 'panda3d.core.Material' objects>"
        'getMetallic': None, # (!) real value is "<method 'getMetallic' of 'panda3d.core.Material' objects>"
        'getRefractiveIndex': None, # (!) real value is "<method 'getRefractiveIndex' of 'panda3d.core.Material' objects>"
        'getRoughness': None, # (!) real value is "<method 'getRoughness' of 'panda3d.core.Material' objects>"
        'getShininess': None, # (!) real value is "<method 'getShininess' of 'panda3d.core.Material' objects>"
        'getSpecular': None, # (!) real value is "<method 'getSpecular' of 'panda3d.core.Material' objects>"
        'getTwoside': None, # (!) real value is "<method 'getTwoside' of 'panda3d.core.Material' objects>"
        'get_ambient': None, # (!) real value is "<method 'get_ambient' of 'panda3d.core.Material' objects>"
        'get_base_color': None, # (!) real value is "<method 'get_base_color' of 'panda3d.core.Material' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FF820>)>'
        'get_default': None, # (!) real value is '<staticmethod(<built-in method get_default of type object at 0x00007FFCFE2FF820>)>'
        'get_diffuse': None, # (!) real value is "<method 'get_diffuse' of 'panda3d.core.Material' objects>"
        'get_emission': None, # (!) real value is "<method 'get_emission' of 'panda3d.core.Material' objects>"
        'get_local': None, # (!) real value is "<method 'get_local' of 'panda3d.core.Material' objects>"
        'get_metallic': None, # (!) real value is "<method 'get_metallic' of 'panda3d.core.Material' objects>"
        'get_refractive_index': None, # (!) real value is "<method 'get_refractive_index' of 'panda3d.core.Material' objects>"
        'get_roughness': None, # (!) real value is "<method 'get_roughness' of 'panda3d.core.Material' objects>"
        'get_shininess': None, # (!) real value is "<method 'get_shininess' of 'panda3d.core.Material' objects>"
        'get_specular': None, # (!) real value is "<method 'get_specular' of 'panda3d.core.Material' objects>"
        'get_twoside': None, # (!) real value is "<method 'get_twoside' of 'panda3d.core.Material' objects>"
        'hasAmbient': None, # (!) real value is "<method 'hasAmbient' of 'panda3d.core.Material' objects>"
        'hasBaseColor': None, # (!) real value is "<method 'hasBaseColor' of 'panda3d.core.Material' objects>"
        'hasDiffuse': None, # (!) real value is "<method 'hasDiffuse' of 'panda3d.core.Material' objects>"
        'hasEmission': None, # (!) real value is "<method 'hasEmission' of 'panda3d.core.Material' objects>"
        'hasMetallic': None, # (!) real value is "<method 'hasMetallic' of 'panda3d.core.Material' objects>"
        'hasRefractiveIndex': None, # (!) real value is "<method 'hasRefractiveIndex' of 'panda3d.core.Material' objects>"
        'hasRoughness': None, # (!) real value is "<method 'hasRoughness' of 'panda3d.core.Material' objects>"
        'hasSpecular': None, # (!) real value is "<method 'hasSpecular' of 'panda3d.core.Material' objects>"
        'has_ambient': None, # (!) real value is "<method 'has_ambient' of 'panda3d.core.Material' objects>"
        'has_base_color': None, # (!) real value is "<method 'has_base_color' of 'panda3d.core.Material' objects>"
        'has_diffuse': None, # (!) real value is "<method 'has_diffuse' of 'panda3d.core.Material' objects>"
        'has_emission': None, # (!) real value is "<method 'has_emission' of 'panda3d.core.Material' objects>"
        'has_metallic': None, # (!) real value is "<method 'has_metallic' of 'panda3d.core.Material' objects>"
        'has_refractive_index': None, # (!) real value is "<method 'has_refractive_index' of 'panda3d.core.Material' objects>"
        'has_roughness': None, # (!) real value is "<method 'has_roughness' of 'panda3d.core.Material' objects>"
        'has_specular': None, # (!) real value is "<method 'has_specular' of 'panda3d.core.Material' objects>"
        'isAttribLocked': None, # (!) real value is "<method 'isAttribLocked' of 'panda3d.core.Material' objects>"
        'is_attrib_locked': None, # (!) real value is "<method 'is_attrib_locked' of 'panda3d.core.Material' objects>"
        'local': None, # (!) real value is "<attribute 'local' of 'panda3d.core.Material' objects>"
        'metallic': None, # (!) real value is "<attribute 'metallic' of 'panda3d.core.Material' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.Material' objects>"
        'refractive_index': None, # (!) real value is "<attribute 'refractive_index' of 'panda3d.core.Material' objects>"
        'roughness': None, # (!) real value is "<attribute 'roughness' of 'panda3d.core.Material' objects>"
        'setAmbient': None, # (!) real value is "<method 'setAmbient' of 'panda3d.core.Material' objects>"
        'setAttribLock': None, # (!) real value is "<method 'setAttribLock' of 'panda3d.core.Material' objects>"
        'setBaseColor': None, # (!) real value is "<method 'setBaseColor' of 'panda3d.core.Material' objects>"
        'setDiffuse': None, # (!) real value is "<method 'setDiffuse' of 'panda3d.core.Material' objects>"
        'setEmission': None, # (!) real value is "<method 'setEmission' of 'panda3d.core.Material' objects>"
        'setLocal': None, # (!) real value is "<method 'setLocal' of 'panda3d.core.Material' objects>"
        'setMetallic': None, # (!) real value is "<method 'setMetallic' of 'panda3d.core.Material' objects>"
        'setRefractiveIndex': None, # (!) real value is "<method 'setRefractiveIndex' of 'panda3d.core.Material' objects>"
        'setRoughness': None, # (!) real value is "<method 'setRoughness' of 'panda3d.core.Material' objects>"
        'setShininess': None, # (!) real value is "<method 'setShininess' of 'panda3d.core.Material' objects>"
        'setSpecular': None, # (!) real value is "<method 'setSpecular' of 'panda3d.core.Material' objects>"
        'setTwoside': None, # (!) real value is "<method 'setTwoside' of 'panda3d.core.Material' objects>"
        'set_ambient': None, # (!) real value is "<method 'set_ambient' of 'panda3d.core.Material' objects>"
        'set_attrib_lock': None, # (!) real value is "<method 'set_attrib_lock' of 'panda3d.core.Material' objects>"
        'set_base_color': None, # (!) real value is "<method 'set_base_color' of 'panda3d.core.Material' objects>"
        'set_diffuse': None, # (!) real value is "<method 'set_diffuse' of 'panda3d.core.Material' objects>"
        'set_emission': None, # (!) real value is "<method 'set_emission' of 'panda3d.core.Material' objects>"
        'set_local': None, # (!) real value is "<method 'set_local' of 'panda3d.core.Material' objects>"
        'set_metallic': None, # (!) real value is "<method 'set_metallic' of 'panda3d.core.Material' objects>"
        'set_refractive_index': None, # (!) real value is "<method 'set_refractive_index' of 'panda3d.core.Material' objects>"
        'set_roughness': None, # (!) real value is "<method 'set_roughness' of 'panda3d.core.Material' objects>"
        'set_shininess': None, # (!) real value is "<method 'set_shininess' of 'panda3d.core.Material' objects>"
        'set_specular': None, # (!) real value is "<method 'set_specular' of 'panda3d.core.Material' objects>"
        'set_twoside': None, # (!) real value is "<method 'set_twoside' of 'panda3d.core.Material' objects>"
        'shininess': None, # (!) real value is "<attribute 'shininess' of 'panda3d.core.Material' objects>"
        'specular': None, # (!) real value is "<attribute 'specular' of 'panda3d.core.Material' objects>"
        'twoside': None, # (!) real value is "<attribute 'twoside' of 'panda3d.core.Material' objects>"
        'upcastToNamable': None, # (!) real value is "<method 'upcastToNamable' of 'panda3d.core.Material' objects>"
        'upcastToTypedWritableReferenceCount': None, # (!) real value is "<method 'upcastToTypedWritableReferenceCount' of 'panda3d.core.Material' objects>"
        'upcast_to_Namable': None, # (!) real value is "<method 'upcast_to_Namable' of 'panda3d.core.Material' objects>"
        'upcast_to_TypedWritableReferenceCount': None, # (!) real value is "<method 'upcast_to_TypedWritableReferenceCount' of 'panda3d.core.Material' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.Material' objects>"
    }


