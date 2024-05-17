# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class ButtonMap(TypedReferenceCount):
    """
    /**
     * This class represents a map containing all of the buttons of a (keyboard)
     * device, though it can also be used as a generic mapping between
     * ButtonHandles.  It maps an underlying 'raw' button to a 'virtual' button,
     * which may optionally be associated with an appropriate platform-specific
     * name for the button.
     */
    """
    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getMappedButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mapped_button(ButtonMap self, ButtonHandle raw)
        get_mapped_button(ButtonMap self, str raw_name)
        get_mapped_button(ButtonMap self, int i)
        
        /**
         * Returns the nth mapped button, meaning the button that the nth raw button
         * is mapped to.
         */
        
        /**
         * Returns the button that the given button is mapped to, or
         * ButtonHandle::none() if this map does not specify a mapped button for the
         * given raw button.
         */
        
        /**
         * Returns the button that the given button is mapped to, or
         * ButtonHandle::none() if this map does not specify a mapped button for the
         * given raw button.
         */
        """
        pass

    def getMappedButtonLabel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_mapped_button_label(ButtonMap self, ButtonHandle raw)
        get_mapped_button_label(ButtonMap self, str raw_name)
        get_mapped_button_label(ButtonMap self, int i)
        
        /**
         * Returns the label associated with the nth mapped button, meaning the button
         * that the nth raw button is mapped to.
         */
        
        /**
         * If the button map specifies a special name for the button (eg.  if the
         * operating system or keyboard device has a localized name describing the
         * key), returns it, or the empty string otherwise.
         *
         * Note that this is not the same as get_mapped_button().get_name(), which
         * returns the name of the Panda event associated with the button.
         */
        
        /**
         * If the button map specifies a special name for the button (eg.  if the
         * operating system or keyboard device has a localized name describing the
         * key), returns it, or the empty string otherwise.
         *
         * Note that this is not the same as get_mapped_button().get_name(), which
         * returns the name of the Panda event associated with the button.
         */
        """
        pass

    def getNumButtons(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_buttons(ButtonMap self)
        
        /**
         * Returns the number of buttons that this button mapping specifies.
         */
        """
        pass

    def getRawButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_raw_button(ButtonMap self, int i)
        
        /**
         * Returns the underlying raw button associated with the nth button.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_mapped_button(self, ButtonMap_self, ButtonHandle_raw): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mapped_button(ButtonMap self, ButtonHandle raw)
        get_mapped_button(ButtonMap self, str raw_name)
        get_mapped_button(ButtonMap self, int i)
        
        /**
         * Returns the nth mapped button, meaning the button that the nth raw button
         * is mapped to.
         */
        
        /**
         * Returns the button that the given button is mapped to, or
         * ButtonHandle::none() if this map does not specify a mapped button for the
         * given raw button.
         */
        
        /**
         * Returns the button that the given button is mapped to, or
         * ButtonHandle::none() if this map does not specify a mapped button for the
         * given raw button.
         */
        """
        pass

    def get_mapped_button_label(self, ButtonMap_self, ButtonHandle_raw): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_mapped_button_label(ButtonMap self, ButtonHandle raw)
        get_mapped_button_label(ButtonMap self, str raw_name)
        get_mapped_button_label(ButtonMap self, int i)
        
        /**
         * Returns the label associated with the nth mapped button, meaning the button
         * that the nth raw button is mapped to.
         */
        
        /**
         * If the button map specifies a special name for the button (eg.  if the
         * operating system or keyboard device has a localized name describing the
         * key), returns it, or the empty string otherwise.
         *
         * Note that this is not the same as get_mapped_button().get_name(), which
         * returns the name of the Panda event associated with the button.
         */
        
        /**
         * If the button map specifies a special name for the button (eg.  if the
         * operating system or keyboard device has a localized name describing the
         * key), returns it, or the empty string otherwise.
         *
         * Note that this is not the same as get_mapped_button().get_name(), which
         * returns the name of the Panda event associated with the button.
         */
        """
        pass

    def get_num_buttons(self, ButtonMap_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_buttons(ButtonMap self)
        
        /**
         * Returns the number of buttons that this button mapping specifies.
         */
        """
        pass

    def get_raw_button(self, ButtonMap_self, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_raw_button(ButtonMap self, int i)
        
        /**
         * Returns the underlying raw button associated with the nth button.
         */
        """
        pass

    def output(self, ButtonMap_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ButtonMap self, ostream out)
        
        /**
         *
         */
        """
        pass

    def write(self, ButtonMap_self, ostream_out, int_indent_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ButtonMap self, ostream out, int indent_level)
        
        /**
         *
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.ButtonMap' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.ButtonMap' objects>"
        '__doc__': "/**\n * This class represents a map containing all of the buttons of a (keyboard)\n * device, though it can also be used as a generic mapping between\n * ButtonHandles.  It maps an underlying 'raw' button to a 'virtual' button,\n * which may optionally be associated with an appropriate platform-specific\n * name for the button.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ButtonMap' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE370E90>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ButtonMap' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ButtonMap' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE370E90>)>'
        'getMappedButton': None, # (!) real value is "<method 'getMappedButton' of 'panda3d.core.ButtonMap' objects>"
        'getMappedButtonLabel': None, # (!) real value is "<method 'getMappedButtonLabel' of 'panda3d.core.ButtonMap' objects>"
        'getNumButtons': None, # (!) real value is "<method 'getNumButtons' of 'panda3d.core.ButtonMap' objects>"
        'getRawButton': None, # (!) real value is "<method 'getRawButton' of 'panda3d.core.ButtonMap' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE370E90>)>'
        'get_mapped_button': None, # (!) real value is "<method 'get_mapped_button' of 'panda3d.core.ButtonMap' objects>"
        'get_mapped_button_label': None, # (!) real value is "<method 'get_mapped_button_label' of 'panda3d.core.ButtonMap' objects>"
        'get_num_buttons': None, # (!) real value is "<method 'get_num_buttons' of 'panda3d.core.ButtonMap' objects>"
        'get_raw_button': None, # (!) real value is "<method 'get_raw_button' of 'panda3d.core.ButtonMap' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ButtonMap' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ButtonMap' objects>"
    }


