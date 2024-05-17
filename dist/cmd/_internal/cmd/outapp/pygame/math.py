# encoding: utf-8
# module pygame.math
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\pygame\math.cp311-win_amd64.pyd
# by generator 1.147
""" pygame module for vector classes """
# no imports

# functions

def clamp(value, min, max): # real signature unknown; restored from __doc__
    """
    clamp(value, min, max) -> float
    returns value clamped to min and max.
    """
    return 0.0

def disable_swizzling(*args, **kwargs): # real signature unknown
    """ Deprecated, will be removed in a future version. """
    pass

def enable_swizzling(*args, **kwargs): # real signature unknown
    """ Deprecated, will be removed in a future version """
    pass

def lerp(a, b, weight): # real signature unknown; restored from __doc__
    """
    lerp(a, b, weight) -> float
    interpolates between two values by a weight.
    """
    return 0.0

# classes

class Vector2(object):
    """
    Vector2() -> Vector2(0, 0)
    Vector2(int) -> Vector2
    Vector2(float) -> Vector2
    Vector2(Vector2) -> Vector2
    Vector2(x, y) -> Vector2
    Vector2((x, y)) -> Vector2
    a 2-Dimensional Vector
    """
    def angle_to(self, Vector2): # real signature unknown; restored from __doc__
        """
        angle_to(Vector2) -> float
        calculates the angle to a given vector in degrees.
        """
        return 0.0

    def as_polar(self): # real signature unknown; restored from __doc__
        """
        as_polar() -> (r, phi)
        returns a tuple with radial distance and azimuthal angle.
        """
        pass

    def clamp_magnitude(self, max_length): # real signature unknown; restored from __doc__
        """
        clamp_magnitude(max_length) -> Vector2
        clamp_magnitude(min_length, max_length) -> Vector2
        Returns a copy of a vector with the magnitude clamped between max_length and min_length.
        """
        return Vector2

    def clamp_magnitude_ip(self, max_length): # real signature unknown; restored from __doc__
        """
        clamp_magnitude_ip(max_length) -> None
        clamp_magnitude_ip(min_length, max_length) -> None
        Clamps the vector's magnitude between max_length and min_length
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """
        copy() -> Vector2
        Returns a copy of itself.
        """
        return Vector2

    def cross(self, Vector2): # real signature unknown; restored from __doc__
        """
        cross(Vector2) -> float
        calculates the cross- or vector-product
        """
        return 0.0

    def distance_squared_to(self, Vector2): # real signature unknown; restored from __doc__
        """
        distance_squared_to(Vector2) -> float
        calculates the squared Euclidean distance to a given vector.
        """
        return 0.0

    def distance_to(self, Vector2): # real signature unknown; restored from __doc__
        """
        distance_to(Vector2) -> float
        calculates the Euclidean distance to a given vector.
        """
        return 0.0

    def dot(self, Vector2): # real signature unknown; restored from __doc__
        """
        dot(Vector2) -> float
        calculates the dot- or scalar-product with the other vector
        """
        return 0.0

    def elementwise(self): # real signature unknown; restored from __doc__
        """
        elementwise() -> VectorElementwiseProxy
        The next operation will be performed elementwise.
        """
        return VectorElementwiseProxy

    def from_polar(self, (r, phi)): # real signature unknown; restored from __doc__
        """
        Vector2.from_polar((r, phi)) -> Vector2
        Vector2().from_polar((r, phi)) -> None
        Creates a Vector2(x, y) or sets x and y from a polar coordinates tuple.
        """
        return Vector2

    def is_normalized(self): # real signature unknown; restored from __doc__
        """
        is_normalized() -> Bool
        tests if the vector is normalized i.e. has length == 1.
        """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """
        length() -> float
        returns the Euclidean length of the vector.
        """
        return 0.0

    def length_squared(self): # real signature unknown; restored from __doc__
        """
        length_squared() -> float
        returns the squared Euclidean length of the vector.
        """
        return 0.0

    def lerp(self, Vector2, p_float): # real signature unknown; restored from __doc__
        """
        lerp(Vector2, float) -> Vector2
        returns a linear interpolation to the given vector.
        """
        return Vector2

    def magnitude(self): # real signature unknown; restored from __doc__
        """
        magnitude() -> float
        returns the Euclidean magnitude of the vector.
        """
        return 0.0

    def magnitude_squared(self): # real signature unknown; restored from __doc__
        """
        magnitude_squared() -> float
        returns the squared magnitude of the vector.
        """
        return 0.0

    def move_towards(self, Vector2, p_float): # real signature unknown; restored from __doc__
        """
        move_towards(Vector2, float) -> Vector2
        returns a vector moved toward the target by a given distance.
        """
        return Vector2

    def move_towards_ip(self, Vector2, p_float): # real signature unknown; restored from __doc__
        """
        move_towards_ip(Vector2, float) -> None
        moves the vector toward its target at a given distance.
        """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """
        normalize() -> Vector2
        returns a vector with the same direction but length 1.
        """
        return Vector2

    def normalize_ip(self): # real signature unknown; restored from __doc__
        """
        normalize_ip() -> None
        normalizes the vector in place so that its length is 1.
        """
        pass

    def project(self, Vector2): # real signature unknown; restored from __doc__
        """
        project(Vector2) -> Vector2
        projects a vector onto another.
        """
        return Vector2

    def reflect(self, Vector2): # real signature unknown; restored from __doc__
        """
        reflect(Vector2) -> Vector2
        returns a vector reflected of a given normal.
        """
        return Vector2

    def reflect_ip(self, Vector2): # real signature unknown; restored from __doc__
        """
        reflect_ip(Vector2) -> None
        reflect the vector of a given normal in place.
        """
        pass

    def rotate(self, angle): # real signature unknown; restored from __doc__
        """
        rotate(angle) -> Vector2
        rotates a vector by a given angle in degrees.
        """
        return Vector2

    def rotate_ip(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_ip(angle) -> None
        rotates the vector by a given angle in degrees in place.
        """
        pass

    def rotate_ip_rad(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_ip_rad(angle) -> None
        rotates the vector by a given angle in radians in place.
        """
        pass

    def rotate_rad(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_rad(angle) -> Vector2
        rotates a vector by a given angle in radians.
        """
        return Vector2

    def rotate_rad_ip(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_rad_ip(angle) -> None
        rotates the vector by a given angle in radians in place.
        """
        pass

    def scale_to_length(self, p_float): # real signature unknown; restored from __doc__
        """
        scale_to_length(float) -> None
        scales the vector to a given length.
        """
        pass

    def slerp(self, Vector2, p_float): # real signature unknown; restored from __doc__
        """
        slerp(Vector2, float) -> Vector2
        returns a spherical interpolation to the given vector.
        """
        return Vector2

    def update(self): # real signature unknown; restored from __doc__
        """
        update() -> None
        update(int) -> None
        update(float) -> None
        update(Vector2) -> None
        update(x, y) -> None
        update((x, y)) -> None
        Sets the coordinates of the vector.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __ifloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __itruediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/=value. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __safe_for_unpickling__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    epsilon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """small value used in comparisons"""

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class Vector3(object):
    """
    Vector3() -> Vector3(0, 0, 0)
    Vector3(int) -> Vector3
    Vector3(float) -> Vector3
    Vector3(Vector3) -> Vector3
    Vector3(x, y, z) -> Vector3
    Vector3((x, y, z)) -> Vector3
    a 3-Dimensional Vector
    """
    def angle_to(self, Vector3): # real signature unknown; restored from __doc__
        """
        angle_to(Vector3) -> float
        calculates the angle to a given vector in degrees.
        """
        return 0.0

    def as_spherical(self): # real signature unknown; restored from __doc__
        """
        as_spherical() -> (r, theta, phi)
        returns a tuple with radial distance, inclination and azimuthal angle.
        """
        pass

    def clamp_magnitude(self, max_length): # real signature unknown; restored from __doc__
        """
        clamp_magnitude(max_length) -> Vector3
        clamp_magnitude(min_length, max_length) -> Vector3
        Returns a copy of a vector with the magnitude clamped between max_length and min_length.
        """
        return Vector3

    def clamp_magnitude_ip(self, max_length): # real signature unknown; restored from __doc__
        """
        clamp_magnitude_ip(max_length) -> None
        clamp_magnitude_ip(min_length, max_length) -> None
        Clamps the vector's magnitude between max_length and min_length
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """
        copy() -> Vector3
        Returns a copy of itself.
        """
        return Vector3

    def cross(self, Vector3): # real signature unknown; restored from __doc__
        """
        cross(Vector3) -> Vector3
        calculates the cross- or vector-product
        """
        return Vector3

    def distance_squared_to(self, Vector3): # real signature unknown; restored from __doc__
        """
        distance_squared_to(Vector3) -> float
        calculates the squared Euclidean distance to a given vector.
        """
        return 0.0

    def distance_to(self, Vector3): # real signature unknown; restored from __doc__
        """
        distance_to(Vector3) -> float
        calculates the Euclidean distance to a given vector.
        """
        return 0.0

    def dot(self, Vector3): # real signature unknown; restored from __doc__
        """
        dot(Vector3) -> float
        calculates the dot- or scalar-product with the other vector
        """
        return 0.0

    def elementwise(self): # real signature unknown; restored from __doc__
        """
        elementwise() -> VectorElementwiseProxy
        The next operation will be performed elementwise.
        """
        return VectorElementwiseProxy

    def from_spherical(self, (r, theta, phi)): # real signature unknown; restored from __doc__
        """
        Vector3.from_spherical((r, theta, phi)) -> Vector3
        Vector3().from_spherical((r, theta, phi)) -> None
        Creates a Vector3(x, y, z) or sets x, y and z from a spherical coordinates 3-tuple.
        """
        return Vector3

    def is_normalized(self): # real signature unknown; restored from __doc__
        """
        is_normalized() -> Bool
        tests if the vector is normalized i.e. has length == 1.
        """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """
        length() -> float
        returns the Euclidean length of the vector.
        """
        return 0.0

    def length_squared(self): # real signature unknown; restored from __doc__
        """
        length_squared() -> float
        returns the squared Euclidean length of the vector.
        """
        return 0.0

    def lerp(self, Vector3, p_float): # real signature unknown; restored from __doc__
        """
        lerp(Vector3, float) -> Vector3
        returns a linear interpolation to the given vector.
        """
        return Vector3

    def magnitude(self): # real signature unknown; restored from __doc__
        """
        magnitude() -> float
        returns the Euclidean magnitude of the vector.
        """
        return 0.0

    def magnitude_squared(self): # real signature unknown; restored from __doc__
        """
        magnitude_squared() -> float
        returns the squared Euclidean magnitude of the vector.
        """
        return 0.0

    def move_towards(self, Vector3, p_float): # real signature unknown; restored from __doc__
        """
        move_towards(Vector3, float) -> Vector3
        returns a vector moved toward the target by a given distance.
        """
        return Vector3

    def move_towards_ip(self, Vector3, p_float): # real signature unknown; restored from __doc__
        """
        move_towards_ip(Vector3, float) -> None
        moves the vector toward its target at a given distance.
        """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """
        normalize() -> Vector3
        returns a vector with the same direction but length 1.
        """
        return Vector3

    def normalize_ip(self): # real signature unknown; restored from __doc__
        """
        normalize_ip() -> None
        normalizes the vector in place so that its length is 1.
        """
        pass

    def project(self, Vector3): # real signature unknown; restored from __doc__
        """
        project(Vector3) -> Vector3
        projects a vector onto another.
        """
        return Vector3

    def reflect(self, Vector3): # real signature unknown; restored from __doc__
        """
        reflect(Vector3) -> Vector3
        returns a vector reflected of a given normal.
        """
        return Vector3

    def reflect_ip(self, Vector3): # real signature unknown; restored from __doc__
        """
        reflect_ip(Vector3) -> None
        reflect the vector of a given normal in place.
        """
        pass

    def rotate(self, angle, Vector3): # real signature unknown; restored from __doc__
        """
        rotate(angle, Vector3) -> Vector3
        rotates a vector by a given angle in degrees.
        """
        return Vector3

    def rotate_ip(self, angle, Vector3): # real signature unknown; restored from __doc__
        """
        rotate_ip(angle, Vector3) -> None
        rotates the vector by a given angle in degrees in place.
        """
        pass

    def rotate_ip_rad(self, angle, Vector3): # real signature unknown; restored from __doc__
        """
        rotate_ip_rad(angle, Vector3) -> None
        rotates the vector by a given angle in radians in place.
        """
        pass

    def rotate_rad(self, angle, Vector3): # real signature unknown; restored from __doc__
        """
        rotate_rad(angle, Vector3) -> Vector3
        rotates a vector by a given angle in radians.
        """
        return Vector3

    def rotate_rad_ip(self, angle, Vector3): # real signature unknown; restored from __doc__
        """
        rotate_rad_ip(angle, Vector3) -> None
        rotates the vector by a given angle in radians in place.
        """
        pass

    def rotate_x(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_x(angle) -> Vector3
        rotates a vector around the x-axis by the angle in degrees.
        """
        return Vector3

    def rotate_x_ip(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_x_ip(angle) -> None
        rotates the vector around the x-axis by the angle in degrees in place.
        """
        pass

    def rotate_x_ip_rad(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_x_ip_rad(angle) -> None
        rotates the vector around the x-axis by the angle in radians in place.
        """
        pass

    def rotate_x_rad(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_x_rad(angle) -> Vector3
        rotates a vector around the x-axis by the angle in radians.
        """
        return Vector3

    def rotate_x_rad_ip(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_x_rad_ip(angle) -> None
        rotates the vector around the x-axis by the angle in radians in place.
        """
        pass

    def rotate_y(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_y(angle) -> Vector3
        rotates a vector around the y-axis by the angle in degrees.
        """
        return Vector3

    def rotate_y_ip(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_y_ip(angle) -> None
        rotates the vector around the y-axis by the angle in degrees in place.
        """
        pass

    def rotate_y_ip_rad(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_y_ip_rad(angle) -> None
        rotates the vector around the y-axis by the angle in radians in place.
        """
        pass

    def rotate_y_rad(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_y_rad(angle) -> Vector3
        rotates a vector around the y-axis by the angle in radians.
        """
        return Vector3

    def rotate_y_rad_ip(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_y_rad_ip(angle) -> None
        rotates the vector around the y-axis by the angle in radians in place.
        """
        pass

    def rotate_z(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_z(angle) -> Vector3
        rotates a vector around the z-axis by the angle in degrees.
        """
        return Vector3

    def rotate_z_ip(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_z_ip(angle) -> None
        rotates the vector around the z-axis by the angle in degrees in place.
        """
        pass

    def rotate_z_ip_rad(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_z_ip_rad(angle) -> None
        rotates the vector around the z-axis by the angle in radians in place.
        """
        pass

    def rotate_z_rad(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_z_rad(angle) -> Vector3
        rotates a vector around the z-axis by the angle in radians.
        """
        return Vector3

    def rotate_z_rad_ip(self, angle): # real signature unknown; restored from __doc__
        """
        rotate_z_rad_ip(angle) -> None
        rotates the vector around the z-axis by the angle in radians in place.
        """
        pass

    def scale_to_length(self, p_float): # real signature unknown; restored from __doc__
        """
        scale_to_length(float) -> None
        scales the vector to a given length.
        """
        pass

    def slerp(self, Vector3, p_float): # real signature unknown; restored from __doc__
        """
        slerp(Vector3, float) -> Vector3
        returns a spherical interpolation to the given vector.
        """
        return Vector3

    def update(self): # real signature unknown; restored from __doc__
        """
        update() -> None
        update(int) -> None
        update(float) -> None
        update(Vector3) -> None
        update(x, y, z) -> None
        update((x, y, z)) -> None
        Sets the coordinates of the vector.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __ifloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __itruediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/=value. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __safe_for_unpickling__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    epsilon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """small value used in comparisons"""

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class VectorElementwiseProxy(object):
    # no doc
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __hash__ = None


class VectorIterator(object):
    # no doc
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __length_hint__(self, *args, **kwargs): # real signature unknown
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass


# variables with complex values

_PYGAME_C_API = None # (!) real value is '<capsule object "pygame.math._PYGAME_C_API" at 0x000001F914F92010>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F914F98810>'

__spec__ = None # (!) real value is "ModuleSpec(name='pygame.math', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F914F98810>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\pygame\\\\math.cp311-win_amd64.pyd')"

