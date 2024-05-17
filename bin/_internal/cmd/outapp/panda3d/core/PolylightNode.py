# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .PandaNode import PandaNode

class PolylightNode(PandaNode):
    """
    /**
     * A PolylightNode
     */
    """
    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(PolylightNode self, const PolylightNode other)
        
        /**
         * Returns a number less than zero if this PolylightNode sorts before the
         * other one, greater than zero if it sorts after, or zero if they are
         * equivalent.
         *
         * Two PolylightNodes are considered equivalent if they consist of exactly the
         * same properties Otherwise, they are different; different PolylightNodes
         * will be ranked in a consistent but undefined ordering; the ordering is
         * useful only for placing the PolylightNodes in a sorted container like an
         * STL set.
         */
        """
        pass

    def compare_to(self, PolylightNode_self, const_PolylightNode_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(PolylightNode self, const PolylightNode other)
        
        /**
         * Returns a number less than zero if this PolylightNode sorts before the
         * other one, greater than zero if it sorts after, or zero if they are
         * equivalent.
         *
         * Two PolylightNodes are considered equivalent if they consist of exactly the
         * same properties Otherwise, they are different; different PolylightNodes
         * will be ranked in a consistent but undefined ordering; the ordering is
         * useful only for placing the PolylightNodes in a sorted container like an
         * STL set.
         */
        """
        pass

    def disable(self, const_PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        disable(const PolylightNode self)
        
        /**
         * Disable this light
         */
        """
        pass

    def enable(self, const_PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enable(const PolylightNode self)
        
        /**
         * Enable this light
         */
        """
        pass

    def flickerOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flicker_off(const PolylightNode self)
        
        /**
         * Turn flickering off
         */
        """
        pass

    def flickerOn(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        flicker_on(const PolylightNode self)
        
        /**
         * Set flickering to true so at every loop this light's color is varied based
         * on flicker_type
         */
        """
        pass

    def flicker_off(self, const_PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flicker_off(const PolylightNode self)
        
        /**
         * Turn flickering off
         */
        """
        pass

    def flicker_on(self, const_PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        flicker_on(const PolylightNode self)
        
        /**
         * Set flickering to true so at every loop this light's color is varied based
         * on flicker_type
         */
        """
        pass

    def getA0(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_a0(PolylightNode self)
        
        /**
         * Get the quadratic attenuation factor a0 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def getA1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_a1(PolylightNode self)
        
        /**
         * Get the quadratic attenuation factor a1 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def getA2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_a2(PolylightNode self)
        
        /**
         * Get the quadratic attenuation factor a2 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def getAttenuation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_attenuation(PolylightNode self)
        
        /**
         * Get "linear" or "quadratic" attenuation type
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
        get_color(PolylightNode self)
        
        /**
         * Returns the light's color as LColor
         */
        """
        pass

    def getColorScenegraph(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_color_scenegraph(PolylightNode self)
        
        /**
         * This differs from get_color in that when applying the light color we need
         * to make sure that a color flattening external to the PolylightNode is not
         * ignored.
         */
        """
        pass

    def getFlickerType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_flicker_type(PolylightNode self)
        
        /**
         * Returns FRANDOM or FSIN
         */
        """
        pass

    def getFreq(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_freq(PolylightNode self)
        
        /**
         * Get frequency of sin flicker
         */
        """
        pass

    def getOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_offset(PolylightNode self)
        
        /**
         * Get the offset value for the random and sin flicker variations
         */
        """
        pass

    def getPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pos(PolylightNode self)
        
        /**
         * Returns position as a LPoint3
         */
        """
        pass

    def getRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_radius(PolylightNode self)
        
        /**
         * Get radius of the spherical light volume
         */
        """
        pass

    def getScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_scale(PolylightNode self)
        
        /**
         * Get the scale value for the random and sin flicker variations
         */
        """
        pass

    def getStepSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_step_size(PolylightNode self)
        
        /**
         * Get the step size for the sin function in flicker This is the increment
         * size for the value supplied to the sin function
         */
        """
        pass

    def get_a0(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_a0(PolylightNode self)
        
        /**
         * Get the quadratic attenuation factor a0 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def get_a1(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_a1(PolylightNode self)
        
        /**
         * Get the quadratic attenuation factor a1 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def get_a2(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_a2(PolylightNode self)
        
        /**
         * Get the quadratic attenuation factor a2 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def get_attenuation(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_attenuation(PolylightNode self)
        
        /**
         * Get "linear" or "quadratic" attenuation type
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_color(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color(PolylightNode self)
        
        /**
         * Returns the light's color as LColor
         */
        """
        pass

    def get_color_scenegraph(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_color_scenegraph(PolylightNode self)
        
        /**
         * This differs from get_color in that when applying the light color we need
         * to make sure that a color flattening external to the PolylightNode is not
         * ignored.
         */
        """
        pass

    def get_flicker_type(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_flicker_type(PolylightNode self)
        
        /**
         * Returns FRANDOM or FSIN
         */
        """
        pass

    def get_freq(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_freq(PolylightNode self)
        
        /**
         * Get frequency of sin flicker
         */
        """
        pass

    def get_offset(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_offset(PolylightNode self)
        
        /**
         * Get the offset value for the random and sin flicker variations
         */
        """
        pass

    def get_pos(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pos(PolylightNode self)
        
        /**
         * Returns position as a LPoint3
         */
        """
        pass

    def get_radius(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_radius(PolylightNode self)
        
        /**
         * Get radius of the spherical light volume
         */
        """
        pass

    def get_scale(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_scale(PolylightNode self)
        
        /**
         * Get the scale value for the random and sin flicker variations
         */
        """
        pass

    def get_step_size(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_step_size(PolylightNode self)
        
        /**
         * Get the step size for the sin function in flicker This is the increment
         * size for the value supplied to the sin function
         */
        """
        pass

    def isEnabled(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_enabled(PolylightNode self)
        
        /**
         * Is this light is enabled/disabled?
         */
        """
        pass

    def isFlickering(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_flickering(PolylightNode self)
        
        /**
         * Check is this light is flickering
         */
        """
        pass

    def is_enabled(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_enabled(PolylightNode self)
        
        /**
         * Is this light is enabled/disabled?
         */
        """
        pass

    def is_flickering(self, PolylightNode_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_flickering(PolylightNode self)
        
        /**
         * Check is this light is flickering
         */
        """
        pass

    def setA0(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_a0(const PolylightNode self, float a0)
        
        /**
         * Set the quadratic attenuation factor a0 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def setA1(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_a1(const PolylightNode self, float a1)
        
        /**
         * Set the quadratic attenuation factor a1 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def setA2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_a2(const PolylightNode self, float a2)
        
        /**
         * Set the quadratic attenuation factor a2 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def setAttenuation(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_attenuation(const PolylightNode self, int type)
        
        /**
         * Set ALINEAR or AQUADRATIC attenuation
         */
        """
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_color(const PolylightNode self, const LVecBase4f color)
        set_color(const PolylightNode self, float r, float g, float b)
        
        /**
         * Set the light's color...
         */
        
        /**
         * Set the light's color... 3 floats between 0 and 1
         */
        """
        pass

    def setFlickerType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_flicker_type(const PolylightNode self, int type)
        
        /**
         * Flicker type can be FRANDOM or FSIN At a later point there might be a
         * FCUSTOM Custom flicker will be a set of fix points recorded by animating
         * the light's intensity
         */
        """
        pass

    def setFreq(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_freq(const PolylightNode self, float f)
        
        /**
         * Set frequency of sin flicker
         */
        """
        pass

    def setOffset(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_offset(const PolylightNode self, float offset)
        
        /**
         * Set the offset value for the random and sin flicker variations... used to
         * tweak the flicker This value is added to the variation
         */
        """
        pass

    def setPos(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_pos(const PolylightNode self, const LPoint3f position)
        set_pos(const PolylightNode self, float x, float y, float z)
        
        /**
         * Set this light's position
         */
        
        /**
         * Set this light's position
         */
        """
        pass

    def setRadius(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_radius(const PolylightNode self, float r)
        
        /**
         * Set radius of the spherical light volume
         */
        """
        pass

    def setScale(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_scale(const PolylightNode self, float scale)
        
        /**
         * Set the scale value for the random and sin flicker variations... used to
         * tweak the flicker This value is multiplied with the variation
         */
        """
        pass

    def setStepSize(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_step_size(const PolylightNode self, float step)
        
        /**
         * Set the step size for the sin function in flicker This is the increment
         * size for the value supplied to the sin function
         */
        """
        pass

    def set_a0(self, const_PolylightNode_self, float_a0): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_a0(const PolylightNode self, float a0)
        
        /**
         * Set the quadratic attenuation factor a0 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def set_a1(self, const_PolylightNode_self, float_a1): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_a1(const PolylightNode self, float a1)
        
        /**
         * Set the quadratic attenuation factor a1 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def set_a2(self, const_PolylightNode_self, float_a2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_a2(const PolylightNode self, float a2)
        
        /**
         * Set the quadratic attenuation factor a2 fd = 1 / ( a0 + a1*distance +
         * a2*distance*distance)
         */
        """
        pass

    def set_attenuation(self, const_PolylightNode_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_attenuation(const PolylightNode self, int type)
        
        /**
         * Set ALINEAR or AQUADRATIC attenuation
         */
        """
        pass

    def set_color(self, const_PolylightNode_self, const_LVecBase4f_color): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_color(const PolylightNode self, const LVecBase4f color)
        set_color(const PolylightNode self, float r, float g, float b)
        
        /**
         * Set the light's color...
         */
        
        /**
         * Set the light's color... 3 floats between 0 and 1
         */
        """
        pass

    def set_flicker_type(self, const_PolylightNode_self, int_type): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_flicker_type(const PolylightNode self, int type)
        
        /**
         * Flicker type can be FRANDOM or FSIN At a later point there might be a
         * FCUSTOM Custom flicker will be a set of fix points recorded by animating
         * the light's intensity
         */
        """
        pass

    def set_freq(self, const_PolylightNode_self, float_f): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_freq(const PolylightNode self, float f)
        
        /**
         * Set frequency of sin flicker
         */
        """
        pass

    def set_offset(self, const_PolylightNode_self, float_offset): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_offset(const PolylightNode self, float offset)
        
        /**
         * Set the offset value for the random and sin flicker variations... used to
         * tweak the flicker This value is added to the variation
         */
        """
        pass

    def set_pos(self, const_PolylightNode_self, const_LPoint3f_position): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_pos(const PolylightNode self, const LPoint3f position)
        set_pos(const PolylightNode self, float x, float y, float z)
        
        /**
         * Set this light's position
         */
        
        /**
         * Set this light's position
         */
        """
        pass

    def set_radius(self, const_PolylightNode_self, float_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_radius(const PolylightNode self, float r)
        
        /**
         * Set radius of the spherical light volume
         */
        """
        pass

    def set_scale(self, const_PolylightNode_self, float_scale): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_scale(const PolylightNode self, float scale)
        
        /**
         * Set the scale value for the random and sin flicker variations... used to
         * tweak the flicker This value is multiplied with the variation
         */
        """
        pass

    def set_step_size(self, const_PolylightNode_self, float_step): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_step_size(const PolylightNode self, float step)
        
        /**
         * Set the step size for the sin function in flicker This is the increment
         * size for the value supplied to the sin function
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

    ALINEAR = 0
    AQUADRATIC = 1
    DtoolClassDict = {
        'ALINEAR': 0,
        'AQUADRATIC': 1,
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'FCUSTOM': 2,
        'FRANDOM': 0,
        'FSIN': 1,
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.PolylightNode' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.PolylightNode' objects>"
        '__doc__': '/**\n * A PolylightNode\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.core.PolylightNode' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.core.PolylightNode' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.core.PolylightNode' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.core.PolylightNode' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.PolylightNode' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.core.PolylightNode' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.core.PolylightNode' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.core.PolylightNode' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE299E20>'
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.core.PolylightNode' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.core.PolylightNode' objects>"
        'disable': None, # (!) real value is "<method 'disable' of 'panda3d.core.PolylightNode' objects>"
        'enable': None, # (!) real value is "<method 'enable' of 'panda3d.core.PolylightNode' objects>"
        'flickerOff': None, # (!) real value is "<method 'flickerOff' of 'panda3d.core.PolylightNode' objects>"
        'flickerOn': None, # (!) real value is "<method 'flickerOn' of 'panda3d.core.PolylightNode' objects>"
        'flicker_off': None, # (!) real value is "<method 'flicker_off' of 'panda3d.core.PolylightNode' objects>"
        'flicker_on': None, # (!) real value is "<method 'flicker_on' of 'panda3d.core.PolylightNode' objects>"
        'getA0': None, # (!) real value is "<method 'getA0' of 'panda3d.core.PolylightNode' objects>"
        'getA1': None, # (!) real value is "<method 'getA1' of 'panda3d.core.PolylightNode' objects>"
        'getA2': None, # (!) real value is "<method 'getA2' of 'panda3d.core.PolylightNode' objects>"
        'getAttenuation': None, # (!) real value is "<method 'getAttenuation' of 'panda3d.core.PolylightNode' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE299E20>)>'
        'getColor': None, # (!) real value is "<method 'getColor' of 'panda3d.core.PolylightNode' objects>"
        'getColorScenegraph': None, # (!) real value is "<method 'getColorScenegraph' of 'panda3d.core.PolylightNode' objects>"
        'getFlickerType': None, # (!) real value is "<method 'getFlickerType' of 'panda3d.core.PolylightNode' objects>"
        'getFreq': None, # (!) real value is "<method 'getFreq' of 'panda3d.core.PolylightNode' objects>"
        'getOffset': None, # (!) real value is "<method 'getOffset' of 'panda3d.core.PolylightNode' objects>"
        'getPos': None, # (!) real value is "<method 'getPos' of 'panda3d.core.PolylightNode' objects>"
        'getRadius': None, # (!) real value is "<method 'getRadius' of 'panda3d.core.PolylightNode' objects>"
        'getScale': None, # (!) real value is "<method 'getScale' of 'panda3d.core.PolylightNode' objects>"
        'getStepSize': None, # (!) real value is "<method 'getStepSize' of 'panda3d.core.PolylightNode' objects>"
        'get_a0': None, # (!) real value is "<method 'get_a0' of 'panda3d.core.PolylightNode' objects>"
        'get_a1': None, # (!) real value is "<method 'get_a1' of 'panda3d.core.PolylightNode' objects>"
        'get_a2': None, # (!) real value is "<method 'get_a2' of 'panda3d.core.PolylightNode' objects>"
        'get_attenuation': None, # (!) real value is "<method 'get_attenuation' of 'panda3d.core.PolylightNode' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE299E20>)>'
        'get_color': None, # (!) real value is "<method 'get_color' of 'panda3d.core.PolylightNode' objects>"
        'get_color_scenegraph': None, # (!) real value is "<method 'get_color_scenegraph' of 'panda3d.core.PolylightNode' objects>"
        'get_flicker_type': None, # (!) real value is "<method 'get_flicker_type' of 'panda3d.core.PolylightNode' objects>"
        'get_freq': None, # (!) real value is "<method 'get_freq' of 'panda3d.core.PolylightNode' objects>"
        'get_offset': None, # (!) real value is "<method 'get_offset' of 'panda3d.core.PolylightNode' objects>"
        'get_pos': None, # (!) real value is "<method 'get_pos' of 'panda3d.core.PolylightNode' objects>"
        'get_radius': None, # (!) real value is "<method 'get_radius' of 'panda3d.core.PolylightNode' objects>"
        'get_scale': None, # (!) real value is "<method 'get_scale' of 'panda3d.core.PolylightNode' objects>"
        'get_step_size': None, # (!) real value is "<method 'get_step_size' of 'panda3d.core.PolylightNode' objects>"
        'isEnabled': None, # (!) real value is "<method 'isEnabled' of 'panda3d.core.PolylightNode' objects>"
        'isFlickering': None, # (!) real value is "<method 'isFlickering' of 'panda3d.core.PolylightNode' objects>"
        'is_enabled': None, # (!) real value is "<method 'is_enabled' of 'panda3d.core.PolylightNode' objects>"
        'is_flickering': None, # (!) real value is "<method 'is_flickering' of 'panda3d.core.PolylightNode' objects>"
        'setA0': None, # (!) real value is "<method 'setA0' of 'panda3d.core.PolylightNode' objects>"
        'setA1': None, # (!) real value is "<method 'setA1' of 'panda3d.core.PolylightNode' objects>"
        'setA2': None, # (!) real value is "<method 'setA2' of 'panda3d.core.PolylightNode' objects>"
        'setAttenuation': None, # (!) real value is "<method 'setAttenuation' of 'panda3d.core.PolylightNode' objects>"
        'setColor': None, # (!) real value is "<method 'setColor' of 'panda3d.core.PolylightNode' objects>"
        'setFlickerType': None, # (!) real value is "<method 'setFlickerType' of 'panda3d.core.PolylightNode' objects>"
        'setFreq': None, # (!) real value is "<method 'setFreq' of 'panda3d.core.PolylightNode' objects>"
        'setOffset': None, # (!) real value is "<method 'setOffset' of 'panda3d.core.PolylightNode' objects>"
        'setPos': None, # (!) real value is "<method 'setPos' of 'panda3d.core.PolylightNode' objects>"
        'setRadius': None, # (!) real value is "<method 'setRadius' of 'panda3d.core.PolylightNode' objects>"
        'setScale': None, # (!) real value is "<method 'setScale' of 'panda3d.core.PolylightNode' objects>"
        'setStepSize': None, # (!) real value is "<method 'setStepSize' of 'panda3d.core.PolylightNode' objects>"
        'set_a0': None, # (!) real value is "<method 'set_a0' of 'panda3d.core.PolylightNode' objects>"
        'set_a1': None, # (!) real value is "<method 'set_a1' of 'panda3d.core.PolylightNode' objects>"
        'set_a2': None, # (!) real value is "<method 'set_a2' of 'panda3d.core.PolylightNode' objects>"
        'set_attenuation': None, # (!) real value is "<method 'set_attenuation' of 'panda3d.core.PolylightNode' objects>"
        'set_color': None, # (!) real value is "<method 'set_color' of 'panda3d.core.PolylightNode' objects>"
        'set_flicker_type': None, # (!) real value is "<method 'set_flicker_type' of 'panda3d.core.PolylightNode' objects>"
        'set_freq': None, # (!) real value is "<method 'set_freq' of 'panda3d.core.PolylightNode' objects>"
        'set_offset': None, # (!) real value is "<method 'set_offset' of 'panda3d.core.PolylightNode' objects>"
        'set_pos': None, # (!) real value is "<method 'set_pos' of 'panda3d.core.PolylightNode' objects>"
        'set_radius': None, # (!) real value is "<method 'set_radius' of 'panda3d.core.PolylightNode' objects>"
        'set_scale': None, # (!) real value is "<method 'set_scale' of 'panda3d.core.PolylightNode' objects>"
        'set_step_size': None, # (!) real value is "<method 'set_step_size' of 'panda3d.core.PolylightNode' objects>"
    }
    FCUSTOM = 2
    FRANDOM = 0
    FSIN = 1


