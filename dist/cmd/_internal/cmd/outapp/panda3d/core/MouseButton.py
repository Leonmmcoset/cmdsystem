# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class MouseButton(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class is just used as a convenient namespace for grouping all of these
     * handy functions that return buttons which map to standard mouse buttons.
     */
    """
    def button(self, int_button_number): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        button(int button_number)
        
        /**
         * Returns the ButtonHandle associated with the particular numbered mouse
         * button (zero-based), if there is one, or ButtonHandle::none() if there is
         * not.
         */
        """
        pass

    def five(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        five()
        
        /**
         * Returns the ButtonHandle associated with the fifth mouse button.
         */
        """
        pass

    def four(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        four()
        
        /**
         * Returns the ButtonHandle associated with the fourth mouse button.
         */
        """
        pass

    def isMouseButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_mouse_button(ButtonHandle button)
        
        /**
         * Returns true if the indicated ButtonHandle is a mouse button, false if it
         * is some other kind of button.
         */
        """
        pass

    def is_mouse_button(self, ButtonHandle_button): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_mouse_button(ButtonHandle button)
        
        /**
         * Returns true if the indicated ButtonHandle is a mouse button, false if it
         * is some other kind of button.
         */
        """
        pass

    def one(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        one()
        
        /**
         * Returns the ButtonHandle associated with the first mouse button.
         */
        """
        pass

    def three(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        three()
        
        /**
         * Returns the ButtonHandle associated with the third mouse button.
         */
        """
        pass

    def two(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        two()
        
        /**
         * Returns the ButtonHandle associated with the second mouse button.
         */
        """
        pass

    def wheelDown(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wheel_down()
        
        /**
         * Returns the ButtonHandle generated when the mouse wheel is rolled one notch
         * downwards.
         */
        """
        pass

    def wheelLeft(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wheel_left()
        
        /**
         * Returns the ButtonHandle generated when the mouse is scrolled to the left.
         * Usually, you'll only find the horizontal scroll on laptops.
         */
        """
        pass

    def wheelRight(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wheel_right()
        
        /**
         * Returns the ButtonHandle generated when the mouse is scrolled to the right.
         * Usually, you'll only find the horizontal scroll on laptops.
         */
        """
        pass

    def wheelUp(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        wheel_up()
        
        /**
         * Returns the ButtonHandle generated when the mouse wheel is rolled one notch
         * upwards.
         */
        """
        pass

    def wheel_down(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wheel_down()
        
        /**
         * Returns the ButtonHandle generated when the mouse wheel is rolled one notch
         * downwards.
         */
        """
        pass

    def wheel_left(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wheel_left()
        
        /**
         * Returns the ButtonHandle generated when the mouse is scrolled to the left.
         * Usually, you'll only find the horizontal scroll on laptops.
         */
        """
        pass

    def wheel_right(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wheel_right()
        
        /**
         * Returns the ButtonHandle generated when the mouse is scrolled to the right.
         * Usually, you'll only find the horizontal scroll on laptops.
         */
        """
        pass

    def wheel_up(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        wheel_up()
        
        /**
         * Returns the ButtonHandle generated when the mouse wheel is rolled one notch
         * upwards.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.MouseButton' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.MouseButton' objects>"
        '__doc__': '/**\n * This class is just used as a convenient namespace for grouping all of these\n * handy functions that return buttons which map to standard mouse buttons.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.MouseButton' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE372B90>'
        'button': None, # (!) real value is '<staticmethod(<built-in method button of type object at 0x00007FFCFE372B90>)>'
        'five': None, # (!) real value is '<staticmethod(<built-in method five of type object at 0x00007FFCFE372B90>)>'
        'four': None, # (!) real value is '<staticmethod(<built-in method four of type object at 0x00007FFCFE372B90>)>'
        'isMouseButton': None, # (!) real value is '<staticmethod(<built-in method isMouseButton of type object at 0x00007FFCFE372B90>)>'
        'is_mouse_button': None, # (!) real value is '<staticmethod(<built-in method is_mouse_button of type object at 0x00007FFCFE372B90>)>'
        'one': None, # (!) real value is '<staticmethod(<built-in method one of type object at 0x00007FFCFE372B90>)>'
        'three': None, # (!) real value is '<staticmethod(<built-in method three of type object at 0x00007FFCFE372B90>)>'
        'two': None, # (!) real value is '<staticmethod(<built-in method two of type object at 0x00007FFCFE372B90>)>'
        'wheelDown': None, # (!) real value is '<staticmethod(<built-in method wheelDown of type object at 0x00007FFCFE372B90>)>'
        'wheelLeft': None, # (!) real value is '<staticmethod(<built-in method wheelLeft of type object at 0x00007FFCFE372B90>)>'
        'wheelRight': None, # (!) real value is '<staticmethod(<built-in method wheelRight of type object at 0x00007FFCFE372B90>)>'
        'wheelUp': None, # (!) real value is '<staticmethod(<built-in method wheelUp of type object at 0x00007FFCFE372B90>)>'
        'wheel_down': None, # (!) real value is '<staticmethod(<built-in method wheel_down of type object at 0x00007FFCFE372B90>)>'
        'wheel_left': None, # (!) real value is '<staticmethod(<built-in method wheel_left of type object at 0x00007FFCFE372B90>)>'
        'wheel_right': None, # (!) real value is '<staticmethod(<built-in method wheel_right of type object at 0x00007FFCFE372B90>)>'
        'wheel_up': None, # (!) real value is '<staticmethod(<built-in method wheel_up of type object at 0x00007FFCFE372B90>)>'
    }


