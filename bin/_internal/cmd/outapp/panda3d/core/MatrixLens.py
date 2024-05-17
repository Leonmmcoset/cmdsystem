# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .Lens import Lens

class MatrixLens(Lens):
    """
    /**
     * A completely generic linear lens.  This is provided for the benefit of low-
     * level code that wants to specify a perspective or orthographic frustum via
     * an explicit projection matrix, but not mess around with fov's or focal
     * lengths or any of that nonsense.
     */
    """
    def clearLeftEyeMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_left_eye_mat(const MatrixLens self)
        
        /**
         * Removes the custom projection matrix set for the left eye, and uses the
         * center matrix (set by set_user_mat) instead.
         */
        """
        pass

    def clearRightEyeMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_right_eye_mat(const MatrixLens self)
        
        /**
         * Removes the custom projection matrix set for the right eye, and uses the
         * center matrix (set by set_user_mat) instead.
         */
        """
        pass

    def clear_left_eye_mat(self, const_MatrixLens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_left_eye_mat(const MatrixLens self)
        
        /**
         * Removes the custom projection matrix set for the left eye, and uses the
         * center matrix (set by set_user_mat) instead.
         */
        """
        pass

    def clear_right_eye_mat(self, const_MatrixLens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_right_eye_mat(const MatrixLens self)
        
        /**
         * Removes the custom projection matrix set for the right eye, and uses the
         * center matrix (set by set_user_mat) instead.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getLeftEyeMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_left_eye_mat(MatrixLens self)
        
        /**
         * Returns the custom projection matrix for the left eye, if any, or the
         * center matrix if there is no custom matrix set for the left eye.
         */
        """
        pass

    def getRightEyeMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_right_eye_mat(MatrixLens self)
        
        /**
         * Returns the custom projection matrix for the right eye, if any, or the
         * center matrix if there is no custom matrix set for the right eye.
         */
        """
        pass

    def getUserMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_user_mat(MatrixLens self)
        
        /**
         * Returns the explicit projection matrix as set by the user.  This does not
         * include transforms on the lens or film (e.g.  a film offset or view hpr).
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_left_eye_mat(self, MatrixLens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_left_eye_mat(MatrixLens self)
        
        /**
         * Returns the custom projection matrix for the left eye, if any, or the
         * center matrix if there is no custom matrix set for the left eye.
         */
        """
        pass

    def get_right_eye_mat(self, MatrixLens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_right_eye_mat(MatrixLens self)
        
        /**
         * Returns the custom projection matrix for the right eye, if any, or the
         * center matrix if there is no custom matrix set for the right eye.
         */
        """
        pass

    def get_user_mat(self, MatrixLens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_user_mat(MatrixLens self)
        
        /**
         * Returns the explicit projection matrix as set by the user.  This does not
         * include transforms on the lens or film (e.g.  a film offset or view hpr).
         */
        """
        pass

    def hasLeftEyeMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_left_eye_mat(MatrixLens self)
        
        /**
         * Returns true if the camera has a custom projection matrix set for the left
         * eye, or false if the center matrix (set by set_user_mat) will be used for
         * the left eye.
         */
        """
        pass

    def hasRightEyeMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_right_eye_mat(MatrixLens self)
        
        /**
         * Returns true if the camera has a custom projection matrix set for the right
         * eye, or false if the center matrix (set by set_user_mat) will be used for
         * the right eye.
         */
        """
        pass

    def has_left_eye_mat(self, MatrixLens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_left_eye_mat(MatrixLens self)
        
        /**
         * Returns true if the camera has a custom projection matrix set for the left
         * eye, or false if the center matrix (set by set_user_mat) will be used for
         * the left eye.
         */
        """
        pass

    def has_right_eye_mat(self, MatrixLens_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_right_eye_mat(MatrixLens self)
        
        /**
         * Returns true if the camera has a custom projection matrix set for the right
         * eye, or false if the center matrix (set by set_user_mat) will be used for
         * the right eye.
         */
        """
        pass

    def setLeftEyeMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_left_eye_mat(const MatrixLens self, const LMatrix4f user_mat)
        
        /**
         * Sets a custom projection matrix for the left eye.  This is only used if the
         * lens is attached to a stereo camera, in which case the left eye matrix will
         * be used to draw the scene in the left eye (but the center matrix--the
         * user_mat--will still be used to cull the scene).
         *
         * This matrix should not be too different from the center matrix (set by
         * set_user_mat()) or culling errors may become obvious.
         */
        """
        pass

    def setRightEyeMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_right_eye_mat(const MatrixLens self, const LMatrix4f user_mat)
        
        /**
         * Sets a custom projection matrix for the right eye.  This is only used if
         * the lens is attached to a stereo camera, in which case the right eye matrix
         * will be used to draw the scene in the right eye (but the center matrix--the
         * user_mat--will still be used to cull the scene).
         *
         * This matrix should not be too different from the center matrix (set by
         * set_user_mat()) or culling errors may become obvious.
         */
        """
        pass

    def setUserMat(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_user_mat(const MatrixLens self, const LMatrix4f user_mat)
        
        /**
         * Explicitly specifies the projection matrix.  This matrix should convert X
         * and Y to the range [-film_size/2, film_size/2], where (-fs/2,-fs/2) is the
         * lower left corner of the screen and (fs/2, fs/2) is the upper right.  Z
         * should go to the range [-1, 1], where -1 is the near plane and 1 is the far
         * plane.  Note that this is a left-handed Y-up coordinate system.
         *
         * The default film_size for a MatrixLens is 2, so the default range is [-1,
         * 1] for both X and Y.  This is consistent with the GL conventions for
         * projection matrices.
         */
        """
        pass

    def set_left_eye_mat(self, const_MatrixLens_self, const_LMatrix4f_user_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_left_eye_mat(const MatrixLens self, const LMatrix4f user_mat)
        
        /**
         * Sets a custom projection matrix for the left eye.  This is only used if the
         * lens is attached to a stereo camera, in which case the left eye matrix will
         * be used to draw the scene in the left eye (but the center matrix--the
         * user_mat--will still be used to cull the scene).
         *
         * This matrix should not be too different from the center matrix (set by
         * set_user_mat()) or culling errors may become obvious.
         */
        """
        pass

    def set_right_eye_mat(self, const_MatrixLens_self, const_LMatrix4f_user_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_right_eye_mat(const MatrixLens self, const LMatrix4f user_mat)
        
        /**
         * Sets a custom projection matrix for the right eye.  This is only used if
         * the lens is attached to a stereo camera, in which case the right eye matrix
         * will be used to draw the scene in the right eye (but the center matrix--the
         * user_mat--will still be used to cull the scene).
         *
         * This matrix should not be too different from the center matrix (set by
         * set_user_mat()) or culling errors may become obvious.
         */
        """
        pass

    def set_user_mat(self, const_MatrixLens_self, const_LMatrix4f_user_mat): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_user_mat(const MatrixLens self, const LMatrix4f user_mat)
        
        /**
         * Explicitly specifies the projection matrix.  This matrix should convert X
         * and Y to the range [-film_size/2, film_size/2], where (-fs/2,-fs/2) is the
         * lower left corner of the screen and (fs/2, fs/2) is the upper right.  Z
         * should go to the range [-1, 1], where -1 is the near plane and 1 is the far
         * plane.  Note that this is a left-handed Y-up coordinate system.
         *
         * The default film_size for a MatrixLens is 2, so the default range is [-1,
         * 1] for both X and Y.  This is consistent with the GL conventions for
         * projection matrices.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    user_mat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': "/**\n * A completely generic linear lens.  This is provided for the benefit of low-\n * level code that wants to specify a perspective or orthographic frustum via\n * an explicit projection matrix, but not mess around with fov's or focal\n * lengths or any of that nonsense.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MatrixLens' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2FFBC0>'
        'clearLeftEyeMat': None, # (!) real value is "<method 'clearLeftEyeMat' of 'panda3d.core.MatrixLens' objects>"
        'clearRightEyeMat': None, # (!) real value is "<method 'clearRightEyeMat' of 'panda3d.core.MatrixLens' objects>"
        'clear_left_eye_mat': None, # (!) real value is "<method 'clear_left_eye_mat' of 'panda3d.core.MatrixLens' objects>"
        'clear_right_eye_mat': None, # (!) real value is "<method 'clear_right_eye_mat' of 'panda3d.core.MatrixLens' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2FFBC0>)>'
        'getLeftEyeMat': None, # (!) real value is "<method 'getLeftEyeMat' of 'panda3d.core.MatrixLens' objects>"
        'getRightEyeMat': None, # (!) real value is "<method 'getRightEyeMat' of 'panda3d.core.MatrixLens' objects>"
        'getUserMat': None, # (!) real value is "<method 'getUserMat' of 'panda3d.core.MatrixLens' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2FFBC0>)>'
        'get_left_eye_mat': None, # (!) real value is "<method 'get_left_eye_mat' of 'panda3d.core.MatrixLens' objects>"
        'get_right_eye_mat': None, # (!) real value is "<method 'get_right_eye_mat' of 'panda3d.core.MatrixLens' objects>"
        'get_user_mat': None, # (!) real value is "<method 'get_user_mat' of 'panda3d.core.MatrixLens' objects>"
        'hasLeftEyeMat': None, # (!) real value is "<method 'hasLeftEyeMat' of 'panda3d.core.MatrixLens' objects>"
        'hasRightEyeMat': None, # (!) real value is "<method 'hasRightEyeMat' of 'panda3d.core.MatrixLens' objects>"
        'has_left_eye_mat': None, # (!) real value is "<method 'has_left_eye_mat' of 'panda3d.core.MatrixLens' objects>"
        'has_right_eye_mat': None, # (!) real value is "<method 'has_right_eye_mat' of 'panda3d.core.MatrixLens' objects>"
        'setLeftEyeMat': None, # (!) real value is "<method 'setLeftEyeMat' of 'panda3d.core.MatrixLens' objects>"
        'setRightEyeMat': None, # (!) real value is "<method 'setRightEyeMat' of 'panda3d.core.MatrixLens' objects>"
        'setUserMat': None, # (!) real value is "<method 'setUserMat' of 'panda3d.core.MatrixLens' objects>"
        'set_left_eye_mat': None, # (!) real value is "<method 'set_left_eye_mat' of 'panda3d.core.MatrixLens' objects>"
        'set_right_eye_mat': None, # (!) real value is "<method 'set_right_eye_mat' of 'panda3d.core.MatrixLens' objects>"
        'set_user_mat': None, # (!) real value is "<method 'set_user_mat' of 'panda3d.core.MatrixLens' objects>"
        'user_mat': None, # (!) real value is "<attribute 'user_mat' of 'panda3d.core.MatrixLens' objects>"
    }


