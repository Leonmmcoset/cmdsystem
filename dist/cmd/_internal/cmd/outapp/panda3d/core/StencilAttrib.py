# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .RenderAttrib import RenderAttrib

class StencilAttrib(RenderAttrib):
    """
    /**
     * A StencilAttrib is a collection of all stencil render states.  The render
     * states in a StencilAttrib are read-only.  A StencilAttrib is created with
     * make or make_2_sided.  To determine if two sided stencil is supported, call
     * the function GraphicsStateGuardian:: get_supports_two_sided_stencil.
     */
    """
    def getClassSlot(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getRenderState(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_state(StencilAttrib self, int render_state_identifier)
        
        /**
         * Returns render state.
         */
        """
        pass

    def get_class_slot(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_slot()
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_render_state(self, StencilAttrib_self, int_render_state_identifier): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_state(StencilAttrib self, int render_state_identifier)
        
        /**
         * Returns render state.
         */
        """
        pass

    def make(self, bool_front_enable, int_front_comparison_function, int_stencil_fail_operation, int_stencil_pass_z_fail_operation, int_front_stencil_pass_z_pass_operation, int_reference, int_read_mask, int_write_mask): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make(bool front_enable, int front_comparison_function, int stencil_fail_operation, int stencil_pass_z_fail_operation, int front_stencil_pass_z_pass_operation, int reference, int read_mask, int write_mask)
        
        /**
         * Constructs a front face StencilAttrib.
         */
        """
        pass

    def make2Sided(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_2_sided(bool front_enable, bool back_enable, int front_comparison_function, int stencil_fail_operation, int stencil_pass_z_fail_operation, int front_stencil_pass_z_pass_operation, int reference, int read_mask, int write_mask, int back_comparison_function, int back_stencil_fail_operation, int back_stencil_pass_z_fail_operation, int back_stencil_pass_z_pass_operation)
        
        /**
         * Constructs a two-sided StencilAttrib.
         */
        """
        pass

    def make2SidedWithClear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_2_sided_with_clear(bool front_enable, bool back_enable, int front_comparison_function, int stencil_fail_operation, int stencil_pass_z_fail_operation, int front_stencil_pass_z_pass_operation, int reference, int read_mask, int write_mask, int back_comparison_function, int back_stencil_fail_operation, int back_stencil_pass_z_fail_operation, int back_stencil_pass_z_pass_operation, bool clear, int clear_value)
        
        /**
         * Constructs a two-sided StencilAttrib.
         */
        """
        pass

    def makeDefault(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def makeOff(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a StencilAttrib that has stenciling turned off.
         */
        """
        pass

    def makeWithClear(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_with_clear(bool front_enable, int front_comparison_function, int stencil_fail_operation, int stencil_pass_z_fail_operation, int front_stencil_pass_z_pass_operation, int reference, int read_mask, int write_mask, bool clear, int clear_value)
        
        /**
         * Constructs a front face StencilAttrib.
         */
        """
        pass

    def make_2_sided(self, bool_front_enable, bool_back_enable, int_front_comparison_function, int_stencil_fail_operation, int_stencil_pass_z_fail_operation, int_front_stencil_pass_z_pass_operation, int_reference, int_read_mask, int_write_mask, int_back_comparison_function, int_back_stencil_fail_operation, int_back_stencil_pass_z_fail_operation, int_back_stencil_pass_z_pass_operation): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_2_sided(bool front_enable, bool back_enable, int front_comparison_function, int stencil_fail_operation, int stencil_pass_z_fail_operation, int front_stencil_pass_z_pass_operation, int reference, int read_mask, int write_mask, int back_comparison_function, int back_stencil_fail_operation, int back_stencil_pass_z_fail_operation, int back_stencil_pass_z_pass_operation)
        
        /**
         * Constructs a two-sided StencilAttrib.
         */
        """
        pass

    def make_2_sided_with_clear(self, bool_front_enable, bool_back_enable, int_front_comparison_function, int_stencil_fail_operation, int_stencil_pass_z_fail_operation, int_front_stencil_pass_z_pass_operation, int_reference, int_read_mask, int_write_mask, int_back_comparison_function, int_back_stencil_fail_operation, int_back_stencil_pass_z_fail_operation, int_back_stencil_pass_z_pass_operation, bool_clear, int_clear_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_2_sided_with_clear(bool front_enable, bool back_enable, int front_comparison_function, int stencil_fail_operation, int stencil_pass_z_fail_operation, int front_stencil_pass_z_pass_operation, int reference, int read_mask, int write_mask, int back_comparison_function, int back_stencil_fail_operation, int back_stencil_pass_z_fail_operation, int back_stencil_pass_z_pass_operation, bool clear, int clear_value)
        
        /**
         * Constructs a two-sided StencilAttrib.
         */
        """
        pass

    def make_default(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_default()
        
        /**
         * Returns a RenderAttrib that corresponds to whatever the standard default
         * properties for render attributes of this type ought to be.
         */
        """
        pass

    def make_off(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_off()
        
        /**
         * Constructs a StencilAttrib that has stenciling turned off.
         */
        """
        pass

    def make_with_clear(self, bool_front_enable, int_front_comparison_function, int_stencil_fail_operation, int_stencil_pass_z_fail_operation, int_front_stencil_pass_z_pass_operation, int_reference, int_read_mask, int_write_mask, bool_clear, int_clear_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_with_clear(bool front_enable, int front_comparison_function, int stencil_fail_operation, int stencil_pass_z_fail_operation, int front_stencil_pass_z_pass_operation, int reference, int read_mask, int write_mask, bool clear, int clear_value)
        
        /**
         * Constructs a front face StencilAttrib.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    class_slot = 25
    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'SCFAlways': 8,
        'SCFEqual': 3,
        'SCFGreaterThan': 5,
        'SCFGreaterThanOrEqual': 7,
        'SCFLessThan': 2,
        'SCFLessThanOrEqual': 4,
        'SCFNever': 1,
        'SCFNotEqual': 6,
        'SCF_always': 8,
        'SCF_equal': 3,
        'SCF_greater_than': 5,
        'SCF_greater_than_or_equal': 7,
        'SCF_less_than': 2,
        'SCF_less_than_or_equal': 4,
        'SCF_never': 1,
        'SCF_not_equal': 6,
        'SODecrement': 4,
        'SODecrementSaturate': 7,
        'SOIncrement': 3,
        'SOIncrementSaturate': 6,
        'SOInvert': 5,
        'SOKeep': 0,
        'SOReplace': 2,
        'SOZero': 1,
        'SO_decrement': 4,
        'SO_decrement_saturate': 7,
        'SO_increment': 3,
        'SO_increment_saturate': 6,
        'SO_invert': 5,
        'SO_keep': 0,
        'SO_replace': 2,
        'SO_zero': 1,
        'SRSBackComparisonFunction': 7,
        'SRSBackStencilFailOperation': 8,
        'SRSBackStencilPassZFailOperation': 9,
        'SRSBackStencilPassZPassOperation': 10,
        'SRSClear': 11,
        'SRSClearValue': 12,
        'SRSFrontComparisonFunction': 0,
        'SRSFrontStencilFailOperation': 1,
        'SRSFrontStencilPassZFailOperation': 2,
        'SRSFrontStencilPassZPassOperation': 3,
        'SRSReadMask': 5,
        'SRSReference': 4,
        'SRSTotal': 13,
        'SRSWriteMask': 6,
        'SRS_back_comparison_function': 7,
        'SRS_back_stencil_fail_operation': 8,
        'SRS_back_stencil_pass_z_fail_operation': 9,
        'SRS_back_stencil_pass_z_pass_operation': 10,
        'SRS_clear': 11,
        'SRS_clear_value': 12,
        'SRS_front_comparison_function': 0,
        'SRS_front_stencil_fail_operation': 1,
        'SRS_front_stencil_pass_z_fail_operation': 2,
        'SRS_front_stencil_pass_z_pass_operation': 3,
        'SRS_read_mask': 5,
        'SRS_reference': 4,
        'SRS_total': 13,
        'SRS_write_mask': 6,
        '__doc__': '/**\n * A StencilAttrib is a collection of all stencil render states.  The render\n * states in a StencilAttrib are read-only.  A StencilAttrib is created with\n * make or make_2_sided.  To determine if two sided stencil is supported, call\n * the function GraphicsStateGuardian:: get_supports_two_sided_stencil.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.StencilAttrib' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE29B210>'
        'class_slot': None, # (!) real value is "<attribute 'class_slot' of 'panda3d.core.StencilAttrib'>"
        'getClassSlot': None, # (!) real value is '<staticmethod(<built-in method getClassSlot of type object at 0x00007FFCFE29B210>)>'
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE29B210>)>'
        'getRenderState': None, # (!) real value is "<method 'getRenderState' of 'panda3d.core.StencilAttrib' objects>"
        'get_class_slot': None, # (!) real value is '<staticmethod(<built-in method get_class_slot of type object at 0x00007FFCFE29B210>)>'
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE29B210>)>'
        'get_render_state': None, # (!) real value is "<method 'get_render_state' of 'panda3d.core.StencilAttrib' objects>"
        'make': None, # (!) real value is '<staticmethod(<built-in method make of type object at 0x00007FFCFE29B210>)>'
        'make2Sided': None, # (!) real value is '<staticmethod(<built-in method make2Sided of type object at 0x00007FFCFE29B210>)>'
        'make2SidedWithClear': None, # (!) real value is '<staticmethod(<built-in method make2SidedWithClear of type object at 0x00007FFCFE29B210>)>'
        'makeDefault': None, # (!) real value is '<staticmethod(<built-in method makeDefault of type object at 0x00007FFCFE29B210>)>'
        'makeOff': None, # (!) real value is '<staticmethod(<built-in method makeOff of type object at 0x00007FFCFE29B210>)>'
        'makeWithClear': None, # (!) real value is '<staticmethod(<built-in method makeWithClear of type object at 0x00007FFCFE29B210>)>'
        'make_2_sided': None, # (!) real value is '<staticmethod(<built-in method make_2_sided of type object at 0x00007FFCFE29B210>)>'
        'make_2_sided_with_clear': None, # (!) real value is '<staticmethod(<built-in method make_2_sided_with_clear of type object at 0x00007FFCFE29B210>)>'
        'make_default': None, # (!) real value is '<staticmethod(<built-in method make_default of type object at 0x00007FFCFE29B210>)>'
        'make_off': None, # (!) real value is '<staticmethod(<built-in method make_off of type object at 0x00007FFCFE29B210>)>'
        'make_with_clear': None, # (!) real value is '<staticmethod(<built-in method make_with_clear of type object at 0x00007FFCFE29B210>)>'
    }
    SCFAlways = 8
    SCFEqual = 3
    SCFGreaterThan = 5
    SCFGreaterThanOrEqual = 7
    SCFLessThan = 2
    SCFLessThanOrEqual = 4
    SCFNever = 1
    SCFNotEqual = 6
    SCF_always = 8
    SCF_equal = 3
    SCF_greater_than = 5
    SCF_greater_than_or_equal = 7
    SCF_less_than = 2
    SCF_less_than_or_equal = 4
    SCF_never = 1
    SCF_not_equal = 6
    SODecrement = 4
    SODecrementSaturate = 7
    SOIncrement = 3
    SOIncrementSaturate = 6
    SOInvert = 5
    SOKeep = 0
    SOReplace = 2
    SOZero = 1
    SO_decrement = 4
    SO_decrement_saturate = 7
    SO_increment = 3
    SO_increment_saturate = 6
    SO_invert = 5
    SO_keep = 0
    SO_replace = 2
    SO_zero = 1
    SRSBackComparisonFunction = 7
    SRSBackStencilFailOperation = 8
    SRSBackStencilPassZFailOperation = 9
    SRSBackStencilPassZPassOperation = 10
    SRSClear = 11
    SRSClearValue = 12
    SRSFrontComparisonFunction = 0
    SRSFrontStencilFailOperation = 1
    SRSFrontStencilPassZFailOperation = 2
    SRSFrontStencilPassZPassOperation = 3
    SRSReadMask = 5
    SRSReference = 4
    SRSTotal = 13
    SRSWriteMask = 6
    SRS_back_comparison_function = 7
    SRS_back_stencil_fail_operation = 8
    SRS_back_stencil_pass_z_fail_operation = 9
    SRS_back_stencil_pass_z_pass_operation = 10
    SRS_clear = 11
    SRS_clear_value = 12
    SRS_front_comparison_function = 0
    SRS_front_stencil_fail_operation = 1
    SRS_front_stencil_pass_z_fail_operation = 2
    SRS_front_stencil_pass_z_pass_operation = 3
    SRS_read_mask = 5
    SRS_reference = 4
    SRS_total = 13
    SRS_write_mask = 6


