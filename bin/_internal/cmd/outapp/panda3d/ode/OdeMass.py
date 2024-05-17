# encoding: utf-8
# module panda3d.ode
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\ode.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class OdeMass(__panda3d_core.TypedReferenceCount):
    """
    /**
     *
     */
    """
    def add(self, const_OdeMass_self, OdeMass_other): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add(const OdeMass self, OdeMass other)
        """
        pass

    def adjust(self, const_OdeMass_self, float_newmass): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        adjust(const OdeMass self, float newmass)
        """
        pass

    def check(self, const_OdeMass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        check(const OdeMass self)
        """
        pass

    def getCenter(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_center(OdeMass self)
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getInertialTensor(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_inertial_tensor(OdeMass self)
        """
        pass

    def getMagnitude(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_magnitude(OdeMass self)
        """
        pass

    def get_center(self, OdeMass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_center(OdeMass self)
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_inertial_tensor(self, OdeMass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_inertial_tensor(OdeMass self)
        """
        pass

    def get_magnitude(self, OdeMass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_magnitude(OdeMass self)
        """
        pass

    def rotate(self, const_OdeMass_self, const_LMatrix3f_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        rotate(const OdeMass self, const LMatrix3f r)
        """
        pass

    def setBox(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_box(const OdeMass self, float density, const LVecBase3f size)
        set_box(const OdeMass self, float density, float lx, float ly, float lz)
        """
        pass

    def setBoxTotal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_box_total(const OdeMass self, float total_mass, const LVecBase3f size)
        set_box_total(const OdeMass self, float total_mass, float lx, float ly, float lz)
        """
        pass

    def setCapsule(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_capsule(const OdeMass self, float density, int direction, float radius, float length)
        """
        pass

    def setCapsuleTotal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_capsule_total(const OdeMass self, float total_mass, int direction, float radius, float length)
        """
        pass

    def setCylinder(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cylinder(const OdeMass self, float density, int direction, float radius, float length)
        """
        pass

    def setCylinderTotal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_cylinder_total(const OdeMass self, float total_mass, int direction, float radius, float length)
        """
        pass

    def setParameters(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_parameters(const OdeMass self, float themass, const LVecBase3f center, const LMatrix3f r)
        set_parameters(const OdeMass self, float themass, float cgx, float cgy, float cgz, float I11, float I22, float I33, float I12, float I13, float I23)
        """
        pass

    def setSphere(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sphere(const OdeMass self, float density, float radius)
        """
        pass

    def setSphereTotal(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sphere_total(const OdeMass self, float total_mass, float radius)
        """
        pass

    def setZero(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_zero(const OdeMass self)
        """
        pass

    def set_box(self, const_OdeMass_self, float_density, const_LVecBase3f_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_box(const OdeMass self, float density, const LVecBase3f size)
        set_box(const OdeMass self, float density, float lx, float ly, float lz)
        """
        pass

    def set_box_total(self, const_OdeMass_self, float_total_mass, const_LVecBase3f_size): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_box_total(const OdeMass self, float total_mass, const LVecBase3f size)
        set_box_total(const OdeMass self, float total_mass, float lx, float ly, float lz)
        """
        pass

    def set_capsule(self, const_OdeMass_self, float_density, int_direction, float_radius, float_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_capsule(const OdeMass self, float density, int direction, float radius, float length)
        """
        pass

    def set_capsule_total(self, const_OdeMass_self, float_total_mass, int_direction, float_radius, float_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_capsule_total(const OdeMass self, float total_mass, int direction, float radius, float length)
        """
        pass

    def set_cylinder(self, const_OdeMass_self, float_density, int_direction, float_radius, float_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cylinder(const OdeMass self, float density, int direction, float radius, float length)
        """
        pass

    def set_cylinder_total(self, const_OdeMass_self, float_total_mass, int_direction, float_radius, float_length): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_cylinder_total(const OdeMass self, float total_mass, int direction, float radius, float length)
        """
        pass

    def set_parameters(self, const_OdeMass_self, float_themass, const_LVecBase3f_center, const_LMatrix3f_r): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_parameters(const OdeMass self, float themass, const LVecBase3f center, const LMatrix3f r)
        set_parameters(const OdeMass self, float themass, float cgx, float cgy, float cgz, float I11, float I22, float I33, float I12, float I13, float I23)
        """
        pass

    def set_sphere(self, const_OdeMass_self, float_density, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sphere(const OdeMass self, float density, float radius)
        """
        pass

    def set_sphere_total(self, const_OdeMass_self, float_total_mass, float_radius): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sphere_total(const OdeMass self, float total_mass, float radius)
        """
        pass

    def set_zero(self, const_OdeMass_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_zero(const OdeMass self)
        """
        pass

    def translate(self, const_OdeMass_self, const_LVecBase3f_pos): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        translate(const OdeMass self, const LVecBase3f pos)
        translate(const OdeMass self, float x, float y, float z)
        """
        pass

    def write(self, OdeMass_self, ostream_out, int_indent): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(OdeMass self, ostream out, int indent)
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.ode.OdeMass' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.ode.OdeMass' objects>"
        '__doc__': '/**\n *\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.ode.OdeMass' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC9DEB730>'
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.ode.OdeMass' objects>"
        'add': None, # (!) real value is "<method 'add' of 'panda3d.ode.OdeMass' objects>"
        'adjust': None, # (!) real value is "<method 'adjust' of 'panda3d.ode.OdeMass' objects>"
        'check': None, # (!) real value is "<method 'check' of 'panda3d.ode.OdeMass' objects>"
        'getCenter': None, # (!) real value is "<method 'getCenter' of 'panda3d.ode.OdeMass' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFDC9DEB730>)>'
        'getInertialTensor': None, # (!) real value is "<method 'getInertialTensor' of 'panda3d.ode.OdeMass' objects>"
        'getMagnitude': None, # (!) real value is "<method 'getMagnitude' of 'panda3d.ode.OdeMass' objects>"
        'get_center': None, # (!) real value is "<method 'get_center' of 'panda3d.ode.OdeMass' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFDC9DEB730>)>'
        'get_inertial_tensor': None, # (!) real value is "<method 'get_inertial_tensor' of 'panda3d.ode.OdeMass' objects>"
        'get_magnitude': None, # (!) real value is "<method 'get_magnitude' of 'panda3d.ode.OdeMass' objects>"
        'rotate': None, # (!) real value is "<method 'rotate' of 'panda3d.ode.OdeMass' objects>"
        'setBox': None, # (!) real value is "<method 'setBox' of 'panda3d.ode.OdeMass' objects>"
        'setBoxTotal': None, # (!) real value is "<method 'setBoxTotal' of 'panda3d.ode.OdeMass' objects>"
        'setCapsule': None, # (!) real value is "<method 'setCapsule' of 'panda3d.ode.OdeMass' objects>"
        'setCapsuleTotal': None, # (!) real value is "<method 'setCapsuleTotal' of 'panda3d.ode.OdeMass' objects>"
        'setCylinder': None, # (!) real value is "<method 'setCylinder' of 'panda3d.ode.OdeMass' objects>"
        'setCylinderTotal': None, # (!) real value is "<method 'setCylinderTotal' of 'panda3d.ode.OdeMass' objects>"
        'setParameters': None, # (!) real value is "<method 'setParameters' of 'panda3d.ode.OdeMass' objects>"
        'setSphere': None, # (!) real value is "<method 'setSphere' of 'panda3d.ode.OdeMass' objects>"
        'setSphereTotal': None, # (!) real value is "<method 'setSphereTotal' of 'panda3d.ode.OdeMass' objects>"
        'setZero': None, # (!) real value is "<method 'setZero' of 'panda3d.ode.OdeMass' objects>"
        'set_box': None, # (!) real value is "<method 'set_box' of 'panda3d.ode.OdeMass' objects>"
        'set_box_total': None, # (!) real value is "<method 'set_box_total' of 'panda3d.ode.OdeMass' objects>"
        'set_capsule': None, # (!) real value is "<method 'set_capsule' of 'panda3d.ode.OdeMass' objects>"
        'set_capsule_total': None, # (!) real value is "<method 'set_capsule_total' of 'panda3d.ode.OdeMass' objects>"
        'set_cylinder': None, # (!) real value is "<method 'set_cylinder' of 'panda3d.ode.OdeMass' objects>"
        'set_cylinder_total': None, # (!) real value is "<method 'set_cylinder_total' of 'panda3d.ode.OdeMass' objects>"
        'set_parameters': None, # (!) real value is "<method 'set_parameters' of 'panda3d.ode.OdeMass' objects>"
        'set_sphere': None, # (!) real value is "<method 'set_sphere' of 'panda3d.ode.OdeMass' objects>"
        'set_sphere_total': None, # (!) real value is "<method 'set_sphere_total' of 'panda3d.ode.OdeMass' objects>"
        'set_zero': None, # (!) real value is "<method 'set_zero' of 'panda3d.ode.OdeMass' objects>"
        'translate': None, # (!) real value is "<method 'translate' of 'panda3d.ode.OdeMass' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.ode.OdeMass' objects>"
    }


