# encoding: utf-8
# module panda3d.ode
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\ode.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class OdeJoint(__panda3d_core.TypedObject):
    """
    /**
     *
     */
    """
    def attach(self, const_OdeJoint_self, object_body1, object_body2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach(const OdeJoint self, object body1, object body2)
        """
        pass

    def attachBodies(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_bodies(const OdeJoint self, const OdeBody body1, const OdeBody body2)
        
        /**
         * Attaches two OdeBody objects to this joint.  Order is important.  Consider
         * using the OdeJoint::attach extension function if you're using the Python
         * interface.
         */
        """
        pass

    def attachBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        attach_body(const OdeJoint self, const OdeBody body, int index)
        
        /**
         * Attaches a single OdeBody to this joint at the specified index (0 or 1).
         * The other index will be set to the environment (null). Consider using the
         * OdeJoint::attach extension function if you're using the Python interface.
         */
        """
        pass

    def attach_bodies(self, const_OdeJoint_self, const_OdeBody_body1, const_OdeBody_body2): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_bodies(const OdeJoint self, const OdeBody body1, const OdeBody body2)
        
        /**
         * Attaches two OdeBody objects to this joint.  Order is important.  Consider
         * using the OdeJoint::attach extension function if you're using the Python
         * interface.
         */
        """
        pass

    def attach_body(self, const_OdeJoint_self, const_OdeBody_body, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        attach_body(const OdeJoint self, const OdeBody body, int index)
        
        /**
         * Attaches a single OdeBody to this joint at the specified index (0 or 1).
         * The other index will be set to the environment (null). Consider using the
         * OdeJoint::attach extension function if you're using the Python interface.
         */
        """
        pass

    def compareTo(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        compare_to(OdeJoint self, const OdeJoint other)
        """
        pass

    def compare_to(self, OdeJoint_self, const_OdeJoint_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        compare_to(OdeJoint self, const OdeJoint other)
        """
        pass

    def convert(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert(OdeJoint self)
        """
        pass

    def convertToAMotor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_a_motor(OdeJoint self)
        """
        pass

    def convertToBall(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_ball(OdeJoint self)
        """
        pass

    def convertToContact(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_contact(OdeJoint self)
        """
        pass

    def convertToFixed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_fixed(OdeJoint self)
        """
        pass

    def convertToHinge(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_hinge(OdeJoint self)
        """
        pass

    def convertToHinge2(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_hinge2(OdeJoint self)
        """
        pass

    def convertToLMotor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_l_motor(OdeJoint self)
        """
        pass

    def convertToNull(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_null(OdeJoint self)
        """
        pass

    def convertToPlane2d(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_plane2d(OdeJoint self)
        """
        pass

    def convertToSlider(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_slider(OdeJoint self)
        """
        pass

    def convertToUniversal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        convert_to_universal(OdeJoint self)
        """
        pass

    def convert_to_a_motor(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_a_motor(OdeJoint self)
        """
        pass

    def convert_to_ball(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_ball(OdeJoint self)
        """
        pass

    def convert_to_contact(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_contact(OdeJoint self)
        """
        pass

    def convert_to_fixed(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_fixed(OdeJoint self)
        """
        pass

    def convert_to_hinge(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_hinge(OdeJoint self)
        """
        pass

    def convert_to_hinge2(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_hinge2(OdeJoint self)
        """
        pass

    def convert_to_l_motor(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_l_motor(OdeJoint self)
        """
        pass

    def convert_to_null(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_null(OdeJoint self)
        """
        pass

    def convert_to_plane2d(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_plane2d(OdeJoint self)
        """
        pass

    def convert_to_slider(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_slider(OdeJoint self)
        """
        pass

    def convert_to_universal(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        convert_to_universal(OdeJoint self)
        """
        pass

    def destroy(self, const_OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        destroy(const OdeJoint self)
        """
        pass

    def detach(self, const_OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        detach(const OdeJoint self)
        """
        pass

    def getBody(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_body(OdeJoint self, int index)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getFeedback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_feedback(const OdeJoint self)
        """
        pass

    def getId(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_id(OdeJoint self)
        
        /**
         * Returns the underlying dJointID.
         */
        """
        pass

    def getJointType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_joint_type(OdeJoint self)
        
        /* INLINE void *get_data(); */
        """
        pass

    def get_body(self, OdeJoint_self, int_index): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_body(OdeJoint self, int index)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_feedback(self, const_OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_feedback(const OdeJoint self)
        """
        pass

    def get_id(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_id(OdeJoint self)
        
        /**
         * Returns the underlying dJointID.
         */
        """
        pass

    def get_joint_type(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_joint_type(OdeJoint self)
        
        /* INLINE void *get_data(); */
        """
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_empty(OdeJoint self)
        
        /**
         * Returns true if the ID is 0, meaning the OdeJoint does not point to a valid
         * joint.  It is an error to call a method on an empty joint.  Note that an
         * empty OdeJoint also evaluates to False.
         */
        """
        pass

    def is_empty(self, OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_empty(OdeJoint self)
        
        /**
         * Returns true if the ID is 0, meaning the OdeJoint does not point to a valid
         * joint.  It is an error to call a method on an empty joint.  Note that an
         * empty OdeJoint also evaluates to False.
         */
        """
        pass

    def setFeedback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_feedback(const OdeJoint self)
        set_feedback(const OdeJoint self, OdeJointFeedback param0)
        set_feedback(const OdeJoint self, bool flag)
        """
        pass

    def set_feedback(self, const_OdeJoint_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_feedback(const OdeJoint self)
        set_feedback(const OdeJoint self, OdeJointFeedback param0)
        set_feedback(const OdeJoint self, bool flag)
        """
        pass

    def write(self, OdeJoint_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(OdeJoint self, ostream out, int indent)
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'JTAMotor': 9,
        'JTBall': 1,
        'JTContact': 4,
        'JTFixed': 7,
        'JTHinge': 2,
        'JTHinge2': 6,
        'JTLMotor': 10,
        'JTNone': 0,
        'JTNull': 8,
        'JTPlane2d': 11,
        'JTSlider': 3,
        'JTUniversal': 5,
        'JT_a_motor': 9,
        'JT_ball': 1,
        'JT_contact': 4,
        'JT_fixed': 7,
        'JT_hinge': 2,
        'JT_hinge2': 6,
        'JT_l_motor': 10,
        'JT_none': 0,
        'JT_null': 8,
        'JT_plane2d': 11,
        'JT_slider': 3,
        'JT_universal': 5,
        '__bool__': None, # (!) real value is "<slot wrapper '__bool__' of 'panda3d.ode.OdeJoint' objects>"
        '__doc__': '/**\n *\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.ode.OdeJoint' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.ode.OdeJoint' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.ode.OdeJoint' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.ode.OdeJoint' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ode.OdeJoint' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.ode.OdeJoint' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.ode.OdeJoint' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.ode.OdeJoint' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEB1C0>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.ode.OdeJoint' objects>"
        'attach': None, # (!) real value is "<method 'attach' of 'panda3d.ode.OdeJoint' objects>"
        'attachBodies': None, # (!) real value is "<method 'attachBodies' of 'panda3d.ode.OdeJoint' objects>"
        'attachBody': None, # (!) real value is "<method 'attachBody' of 'panda3d.ode.OdeJoint' objects>"
        'attach_bodies': None, # (!) real value is "<method 'attach_bodies' of 'panda3d.ode.OdeJoint' objects>"
        'attach_body': None, # (!) real value is "<method 'attach_body' of 'panda3d.ode.OdeJoint' objects>"
        'compareTo': None, # (!) real value is "<method 'compareTo' of 'panda3d.ode.OdeJoint' objects>"
        'compare_to': None, # (!) real value is "<method 'compare_to' of 'panda3d.ode.OdeJoint' objects>"
        'convert': None, # (!) real value is "<method 'convert' of 'panda3d.ode.OdeJoint' objects>"
        'convertToAMotor': None, # (!) real value is "<method 'convertToAMotor' of 'panda3d.ode.OdeJoint' objects>"
        'convertToBall': None, # (!) real value is "<method 'convertToBall' of 'panda3d.ode.OdeJoint' objects>"
        'convertToContact': None, # (!) real value is "<method 'convertToContact' of 'panda3d.ode.OdeJoint' objects>"
        'convertToFixed': None, # (!) real value is "<method 'convertToFixed' of 'panda3d.ode.OdeJoint' objects>"
        'convertToHinge': None, # (!) real value is "<method 'convertToHinge' of 'panda3d.ode.OdeJoint' objects>"
        'convertToHinge2': None, # (!) real value is "<method 'convertToHinge2' of 'panda3d.ode.OdeJoint' objects>"
        'convertToLMotor': None, # (!) real value is "<method 'convertToLMotor' of 'panda3d.ode.OdeJoint' objects>"
        'convertToNull': None, # (!) real value is "<method 'convertToNull' of 'panda3d.ode.OdeJoint' objects>"
        'convertToPlane2d': None, # (!) real value is "<method 'convertToPlane2d' of 'panda3d.ode.OdeJoint' objects>"
        'convertToSlider': None, # (!) real value is "<method 'convertToSlider' of 'panda3d.ode.OdeJoint' objects>"
        'convertToUniversal': None, # (!) real value is "<method 'convertToUniversal' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_a_motor': None, # (!) real value is "<method 'convert_to_a_motor' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_ball': None, # (!) real value is "<method 'convert_to_ball' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_contact': None, # (!) real value is "<method 'convert_to_contact' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_fixed': None, # (!) real value is "<method 'convert_to_fixed' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_hinge': None, # (!) real value is "<method 'convert_to_hinge' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_hinge2': None, # (!) real value is "<method 'convert_to_hinge2' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_l_motor': None, # (!) real value is "<method 'convert_to_l_motor' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_null': None, # (!) real value is "<method 'convert_to_null' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_plane2d': None, # (!) real value is "<method 'convert_to_plane2d' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_slider': None, # (!) real value is "<method 'convert_to_slider' of 'panda3d.ode.OdeJoint' objects>"
        'convert_to_universal': None, # (!) real value is "<method 'convert_to_universal' of 'panda3d.ode.OdeJoint' objects>"
        'destroy': None, # (!) real value is "<method 'destroy' of 'panda3d.ode.OdeJoint' objects>"
        'detach': None, # (!) real value is "<method 'detach' of 'panda3d.ode.OdeJoint' objects>"
        'getBody': None, # (!) real value is "<method 'getBody' of 'panda3d.ode.OdeJoint' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEB1C0>)>'
        'getFeedback': None, # (!) real value is "<method 'getFeedback' of 'panda3d.ode.OdeJoint' objects>"
        'getId': None, # (!) real value is "<method 'getId' of 'panda3d.ode.OdeJoint' objects>"
        'getJointType': None, # (!) real value is "<method 'getJointType' of 'panda3d.ode.OdeJoint' objects>"
        'get_body': None, # (!) real value is "<method 'get_body' of 'panda3d.ode.OdeJoint' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEB1C0>)>'
        'get_feedback': None, # (!) real value is "<method 'get_feedback' of 'panda3d.ode.OdeJoint' objects>"
        'get_id': None, # (!) real value is "<method 'get_id' of 'panda3d.ode.OdeJoint' objects>"
        'get_joint_type': None, # (!) real value is "<method 'get_joint_type' of 'panda3d.ode.OdeJoint' objects>"
        'isEmpty': None, # (!) real value is "<method 'isEmpty' of 'panda3d.ode.OdeJoint' objects>"
        'is_empty': None, # (!) real value is "<method 'is_empty' of 'panda3d.ode.OdeJoint' objects>"
        'setFeedback': None, # (!) real value is "<method 'setFeedback' of 'panda3d.ode.OdeJoint' objects>"
        'set_feedback': None, # (!) real value is "<method 'set_feedback' of 'panda3d.ode.OdeJoint' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.ode.OdeJoint' objects>"
    }
    JTAMotor = 9
    JTBall = 1
    JTContact = 4
    JTFixed = 7
    JTHinge = 2
    JTHinge2 = 6
    JTLMotor = 10
    JTNone = 0
    JTNull = 8
    JTPlane2d = 11
    JTSlider = 3
    JTUniversal = 5
    JT_a_motor = 9
    JT_ball = 1
    JT_contact = 4
    JT_fixed = 7
    JT_hinge = 2
    JT_hinge2 = 6
    JT_l_motor = 10
    JT_none = 0
    JT_null = 8
    JT_plane2d = 11
    JT_slider = 3
    JT_universal = 5


