# encoding: utf-8
# module panda3d.ode
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\ode.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class OdeWorld(__panda3d_core.TypedObject):
    """
    /**
     *
     */
    """
    def addBodyDampening(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_body_dampening(const OdeWorld self, OdeBody body, int surface)
        
        // void assign_surface_body(OdeBody& body, int surface);
        """
        pass

    def add_body_dampening(self, const_OdeWorld_self, OdeBody_body, int_surface): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_body_dampening(const OdeWorld self, OdeBody body, int surface)
        
        // void assign_surface_body(OdeBody& body, int surface);
        """
        pass

    def applyDampening(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        apply_dampening(const OdeWorld self, float dt, OdeBody body)
        """
        pass

    def apply_dampening(self, const_OdeWorld_self, float_dt, OdeBody_body): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        apply_dampening(const OdeWorld self, float dt, OdeBody body)
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(OdeWorld self, const OdeWorld other)
        """
        pass

    def compare_to(self, OdeWorld_self, const_OdeWorld_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(OdeWorld self, const OdeWorld other)
        """
        pass

    def destroy(self, const_OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        destroy(const OdeWorld self)
        """
        pass

    def getAutoDisableAngularThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_disable_angular_threshold(OdeWorld self)
        """
        pass

    def getAutoDisableFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_disable_flag(OdeWorld self)
        """
        pass

    def getAutoDisableLinearThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_disable_linear_threshold(OdeWorld self)
        """
        pass

    def getAutoDisableSteps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_disable_steps(OdeWorld self)
        """
        pass

    def getAutoDisableTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_auto_disable_time(OdeWorld self)
        """
        pass

    def getCfm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_cfm(OdeWorld self)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getContactMaxCorrectingVel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contact_max_correcting_vel(OdeWorld self)
        """
        pass

    def getContactSurfaceLayer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_contact_surface_layer(OdeWorld self)
        """
        pass

    def getErp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_erp(OdeWorld self)
        """
        pass

    def getGravity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_gravity(OdeWorld self)
        """
        pass

    def getId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_id(OdeWorld self)
        
        /**
         * Returns the underlying dWorldID.
         */
        """
        pass

    def getQuickStepNumIterations(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_quick_step_num_iterations(OdeWorld self)
        """
        pass

    def getQuickStepW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_quick_step_w(OdeWorld self)
        """
        pass

    def get_auto_disable_angular_threshold(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_disable_angular_threshold(OdeWorld self)
        """
        pass

    def get_auto_disable_flag(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_disable_flag(OdeWorld self)
        """
        pass

    def get_auto_disable_linear_threshold(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_disable_linear_threshold(OdeWorld self)
        """
        pass

    def get_auto_disable_steps(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_disable_steps(OdeWorld self)
        """
        pass

    def get_auto_disable_time(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_auto_disable_time(OdeWorld self)
        """
        pass

    def get_cfm(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_cfm(OdeWorld self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_contact_max_correcting_vel(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contact_max_correcting_vel(OdeWorld self)
        """
        pass

    def get_contact_surface_layer(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_contact_surface_layer(OdeWorld self)
        """
        pass

    def get_erp(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_erp(OdeWorld self)
        """
        pass

    def get_gravity(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_gravity(OdeWorld self)
        """
        pass

    def get_id(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_id(OdeWorld self)
        
        /**
         * Returns the underlying dWorldID.
         */
        """
        pass

    def get_quick_step_num_iterations(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_quick_step_num_iterations(OdeWorld self)
        """
        pass

    def get_quick_step_w(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_quick_step_w(OdeWorld self)
        """
        pass

    def impulseToForce(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        impulse_to_force(const OdeWorld self, float stepsize, const LVecBase3f impulse)
        impulse_to_force(const OdeWorld self, float stepsize, float ix, float iy, float iz)
        """
        pass

    def impulse_to_force(self, const_OdeWorld_self, float_stepsize, const_LVecBase3f_impulse): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        impulse_to_force(const OdeWorld self, float stepsize, const LVecBase3f impulse)
        impulse_to_force(const OdeWorld self, float stepsize, float ix, float iy, float iz)
        """
        pass

    def initSurfaceTable(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        init_surface_table(const OdeWorld self, int num_surfaces)
        """
        pass

    def init_surface_table(self, const_OdeWorld_self, int_num_surfaces): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        init_surface_table(const OdeWorld self, int num_surfaces)
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(OdeWorld self)
        
        /**
         * Returns true if the ID is 0, meaning the OdeWorld does not point to a valid
         * world.  It is an error to call a method on an empty world.  Note that an
         * empty OdeWorld also evaluates to False.
         */
        """
        pass

    def is_empty(self, OdeWorld_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(OdeWorld self)
        
        /**
         * Returns true if the ID is 0, meaning the OdeWorld does not point to a valid
         * world.  It is an error to call a method on an empty world.  Note that an
         * empty OdeWorld also evaluates to False.
         */
        """
        pass

    def quickStep(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        quick_step(const OdeWorld self, float stepsize)
        """
        pass

    def quick_step(self, const_OdeWorld_self, float_stepsize): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        quick_step(const OdeWorld self, float stepsize)
        """
        pass

    def setAutoDisableAngularThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_disable_angular_threshold(const OdeWorld self, float angular_threshold)
        """
        pass

    def setAutoDisableFlag(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_disable_flag(const OdeWorld self, int do_auto_disable)
        """
        pass

    def setAutoDisableLinearThreshold(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_disable_linear_threshold(const OdeWorld self, float linear_threshold)
        """
        pass

    def setAutoDisableSteps(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_disable_steps(const OdeWorld self, int steps)
        """
        pass

    def setAutoDisableTime(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_auto_disable_time(const OdeWorld self, float time)
        """
        pass

    def setCfm(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cfm(const OdeWorld self, float cfm)
        """
        pass

    def setContactMaxCorrectingVel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_contact_max_correcting_vel(const OdeWorld self, float vel)
        """
        pass

    def setContactSurfaceLayer(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_contact_surface_layer(const OdeWorld self, float depth)
        """
        pass

    def setErp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_erp(const OdeWorld self, float erp)
        """
        pass

    def setGravity(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_gravity(const OdeWorld self, const LVecBase3f vec)
        set_gravity(const OdeWorld self, float x, float y, float z)
        """
        pass

    def setQuickStepNumIterations(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_quick_step_num_iterations(const OdeWorld self, int num)
        """
        pass

    def setQuickStepW(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_quick_step_w(const OdeWorld self, float over_relaxation)
        """
        pass

    def setSurfaceEntry(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_surface_entry(const OdeWorld self, int pos1, int pos2, float mu, float bounce, float bounce_vel, float soft_erp, float soft_cfm, float slip, float dampen)
        """
        pass

    def set_auto_disable_angular_threshold(self, const_OdeWorld_self, float_angular_threshold): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_disable_angular_threshold(const OdeWorld self, float angular_threshold)
        """
        pass

    def set_auto_disable_flag(self, const_OdeWorld_self, int_do_auto_disable): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_disable_flag(const OdeWorld self, int do_auto_disable)
        """
        pass

    def set_auto_disable_linear_threshold(self, const_OdeWorld_self, float_linear_threshold): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_disable_linear_threshold(const OdeWorld self, float linear_threshold)
        """
        pass

    def set_auto_disable_steps(self, const_OdeWorld_self, int_steps): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_disable_steps(const OdeWorld self, int steps)
        """
        pass

    def set_auto_disable_time(self, const_OdeWorld_self, float_time): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_auto_disable_time(const OdeWorld self, float time)
        """
        pass

    def set_cfm(self, const_OdeWorld_self, float_cfm): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cfm(const OdeWorld self, float cfm)
        """
        pass

    def set_contact_max_correcting_vel(self, const_OdeWorld_self, float_vel): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_contact_max_correcting_vel(const OdeWorld self, float vel)
        """
        pass

    def set_contact_surface_layer(self, const_OdeWorld_self, float_depth): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_contact_surface_layer(const OdeWorld self, float depth)
        """
        pass

    def set_erp(self, const_OdeWorld_self, float_erp): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_erp(const OdeWorld self, float erp)
        """
        pass

    def set_gravity(self, const_OdeWorld_self, const_LVecBase3f_vec): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_gravity(const OdeWorld self, const LVecBase3f vec)
        set_gravity(const OdeWorld self, float x, float y, float z)
        """
        pass

    def set_quick_step_num_iterations(self, const_OdeWorld_self, int_num): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_quick_step_num_iterations(const OdeWorld self, int num)
        """
        pass

    def set_quick_step_w(self, const_OdeWorld_self, float_over_relaxation): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_quick_step_w(const OdeWorld self, float over_relaxation)
        """
        pass

    def set_surface_entry(self, const_OdeWorld_self, int_pos1, int_pos2, float_mu, float_bounce, float_bounce_vel, float_soft_erp, float_soft_cfm, float_slip, float_dampen): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_surface_entry(const OdeWorld self, int pos1, int pos2, float mu, float bounce, float bounce_vel, float soft_erp, float soft_cfm, float slip, float dampen)
        """
        pass

    def step(self, const_OdeWorld_self, float_stepsize): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        step(const OdeWorld self, float stepsize)
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.ode.OdeWorld' objects>"
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.ode.OdeWorld' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.ode.OdeWorld' objects>"
        '__doc__': '/**\n *\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.ode.OdeWorld' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.ode.OdeWorld' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.ode.OdeWorld' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.ode.OdeWorld' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ode.OdeWorld' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.ode.OdeWorld' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.ode.OdeWorld' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.ode.OdeWorld' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEAC50>'
        'addBodyDampening': None, # (!) real value is "<method 'addBodyDampening' of 'panda3d.ode.OdeWorld' objects>"
        'add_body_dampening': None, # (!) real value is "<method 'add_body_dampening' of 'panda3d.ode.OdeWorld' objects>"
        'applyDampening': None, # (!) real value is "<method 'applyDampening' of 'panda3d.ode.OdeWorld' objects>"
        'apply_dampening': None, # (!) real value is "<method 'apply_dampening' of 'panda3d.ode.OdeWorld' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.ode.OdeWorld' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.ode.OdeWorld' objects>"
        'destroy': None, # (!) real value is "<method 'destroy' of 'panda3d.ode.OdeWorld' objects>"
        'getAutoDisableAngularThreshold': None, # (!) real value is "<method 'getAutoDisableAngularThreshold' of 'panda3d.ode.OdeWorld' objects>"
        'getAutoDisableFlag': None, # (!) real value is "<method 'getAutoDisableFlag' of 'panda3d.ode.OdeWorld' objects>"
        'getAutoDisableLinearThreshold': None, # (!) real value is "<method 'getAutoDisableLinearThreshold' of 'panda3d.ode.OdeWorld' objects>"
        'getAutoDisableSteps': None, # (!) real value is "<method 'getAutoDisableSteps' of 'panda3d.ode.OdeWorld' objects>"
        'getAutoDisableTime': None, # (!) real value is "<method 'getAutoDisableTime' of 'panda3d.ode.OdeWorld' objects>"
        'getCfm': None, # (!) real value is "<method 'getCfm' of 'panda3d.ode.OdeWorld' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEAC50>)>'
        'getContactMaxCorrectingVel': None, # (!) real value is "<method 'getContactMaxCorrectingVel' of 'panda3d.ode.OdeWorld' objects>"
        'getContactSurfaceLayer': None, # (!) real value is "<method 'getContactSurfaceLayer' of 'panda3d.ode.OdeWorld' objects>"
        'getErp': None, # (!) real value is "<method 'getErp' of 'panda3d.ode.OdeWorld' objects>"
        'getGravity': None, # (!) real value is "<method 'getGravity' of 'panda3d.ode.OdeWorld' objects>"
        'getId': None, # (!) real value is "<method 'getId' of 'panda3d.ode.OdeWorld' objects>"
        'getQuickStepNumIterations': None, # (!) real value is "<method 'getQuickStepNumIterations' of 'panda3d.ode.OdeWorld' objects>"
        'getQuickStepW': None, # (!) real value is "<method 'getQuickStepW' of 'panda3d.ode.OdeWorld' objects>"
        'get_auto_disable_angular_threshold': None, # (!) real value is "<method 'get_auto_disable_angular_threshold' of 'panda3d.ode.OdeWorld' objects>"
        'get_auto_disable_flag': None, # (!) real value is "<method 'get_auto_disable_flag' of 'panda3d.ode.OdeWorld' objects>"
        'get_auto_disable_linear_threshold': None, # (!) real value is "<method 'get_auto_disable_linear_threshold' of 'panda3d.ode.OdeWorld' objects>"
        'get_auto_disable_steps': None, # (!) real value is "<method 'get_auto_disable_steps' of 'panda3d.ode.OdeWorld' objects>"
        'get_auto_disable_time': None, # (!) real value is "<method 'get_auto_disable_time' of 'panda3d.ode.OdeWorld' objects>"
        'get_cfm': None, # (!) real value is "<method 'get_cfm' of 'panda3d.ode.OdeWorld' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEAC50>)>'
        'get_contact_max_correcting_vel': None, # (!) real value is "<method 'get_contact_max_correcting_vel' of 'panda3d.ode.OdeWorld' objects>"
        'get_contact_surface_layer': None, # (!) real value is "<method 'get_contact_surface_layer' of 'panda3d.ode.OdeWorld' objects>"
        'get_erp': None, # (!) real value is "<method 'get_erp' of 'panda3d.ode.OdeWorld' objects>"
        'get_gravity': None, # (!) real value is "<method 'get_gravity' of 'panda3d.ode.OdeWorld' objects>"
        'get_id': None, # (!) real value is "<method 'get_id' of 'panda3d.ode.OdeWorld' objects>"
        'get_quick_step_num_iterations': None, # (!) real value is "<method 'get_quick_step_num_iterations' of 'panda3d.ode.OdeWorld' objects>"
        'get_quick_step_w': None, # (!) real value is "<method 'get_quick_step_w' of 'panda3d.ode.OdeWorld' objects>"
        'impulseToForce': None, # (!) real value is "<method 'impulseToForce' of 'panda3d.ode.OdeWorld' objects>"
        'impulse_to_force': None, # (!) real value is "<method 'impulse_to_force' of 'panda3d.ode.OdeWorld' objects>"
        'initSurfaceTable': None, # (!) real value is "<method 'initSurfaceTable' of 'panda3d.ode.OdeWorld' objects>"
        'init_surface_table': None, # (!) real value is "<method 'init_surface_table' of 'panda3d.ode.OdeWorld' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.ode.OdeWorld' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.ode.OdeWorld' objects>"
        'quickStep': None, # (!) real value is "<method 'quickStep' of 'panda3d.ode.OdeWorld' objects>"
        'quick_step': None, # (!) real value is "<method 'quick_step' of 'panda3d.ode.OdeWorld' objects>"
        'setAutoDisableAngularThreshold': None, # (!) real value is "<method 'setAutoDisableAngularThreshold' of 'panda3d.ode.OdeWorld' objects>"
        'setAutoDisableFlag': None, # (!) real value is "<method 'setAutoDisableFlag' of 'panda3d.ode.OdeWorld' objects>"
        'setAutoDisableLinearThreshold': None, # (!) real value is "<method 'setAutoDisableLinearThreshold' of 'panda3d.ode.OdeWorld' objects>"
        'setAutoDisableSteps': None, # (!) real value is "<method 'setAutoDisableSteps' of 'panda3d.ode.OdeWorld' objects>"
        'setAutoDisableTime': None, # (!) real value is "<method 'setAutoDisableTime' of 'panda3d.ode.OdeWorld' objects>"
        'setCfm': None, # (!) real value is "<method 'setCfm' of 'panda3d.ode.OdeWorld' objects>"
        'setContactMaxCorrectingVel': None, # (!) real value is "<method 'setContactMaxCorrectingVel' of 'panda3d.ode.OdeWorld' objects>"
        'setContactSurfaceLayer': None, # (!) real value is "<method 'setContactSurfaceLayer' of 'panda3d.ode.OdeWorld' objects>"
        'setErp': None, # (!) real value is "<method 'setErp' of 'panda3d.ode.OdeWorld' objects>"
        'setGravity': None, # (!) real value is "<method 'setGravity' of 'panda3d.ode.OdeWorld' objects>"
        'setQuickStepNumIterations': None, # (!) real value is "<method 'setQuickStepNumIterations' of 'panda3d.ode.OdeWorld' objects>"
        'setQuickStepW': None, # (!) real value is "<method 'setQuickStepW' of 'panda3d.ode.OdeWorld' objects>"
        'setSurfaceEntry': None, # (!) real value is "<method 'setSurfaceEntry' of 'panda3d.ode.OdeWorld' objects>"
        'set_auto_disable_angular_threshold': None, # (!) real value is "<method 'set_auto_disable_angular_threshold' of 'panda3d.ode.OdeWorld' objects>"
        'set_auto_disable_flag': None, # (!) real value is "<method 'set_auto_disable_flag' of 'panda3d.ode.OdeWorld' objects>"
        'set_auto_disable_linear_threshold': None, # (!) real value is "<method 'set_auto_disable_linear_threshold' of 'panda3d.ode.OdeWorld' objects>"
        'set_auto_disable_steps': None, # (!) real value is "<method 'set_auto_disable_steps' of 'panda3d.ode.OdeWorld' objects>"
        'set_auto_disable_time': None, # (!) real value is "<method 'set_auto_disable_time' of 'panda3d.ode.OdeWorld' objects>"
        'set_cfm': None, # (!) real value is "<method 'set_cfm' of 'panda3d.ode.OdeWorld' objects>"
        'set_contact_max_correcting_vel': None, # (!) real value is "<method 'set_contact_max_correcting_vel' of 'panda3d.ode.OdeWorld' objects>"
        'set_contact_surface_layer': None, # (!) real value is "<method 'set_contact_surface_layer' of 'panda3d.ode.OdeWorld' objects>"
        'set_erp': None, # (!) real value is "<method 'set_erp' of 'panda3d.ode.OdeWorld' objects>"
        'set_gravity': None, # (!) real value is "<method 'set_gravity' of 'panda3d.ode.OdeWorld' objects>"
        'set_quick_step_num_iterations': None, # (!) real value is "<method 'set_quick_step_num_iterations' of 'panda3d.ode.OdeWorld' objects>"
        'set_quick_step_w': None, # (!) real value is "<method 'set_quick_step_w' of 'panda3d.ode.OdeWorld' objects>"
        'set_surface_entry': None, # (!) real value is "<method 'set_surface_entry' of 'panda3d.ode.OdeWorld' objects>"
        'step': None, # (!) real value is "<method 'step' of 'panda3d.ode.OdeWorld' objects>"
    }


