# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .TypedReferenceCount import TypedReferenceCount

class InputDevice(TypedReferenceCount):
    """
    /**
     * This is a structure representing a single input device.  Input devices may
     * have zero or more buttons, pointers, or axes associated with them, and
     * optionally a motion tracker.
     *
     * These devices are brought under a common interface because there is such a
     * large range of devices out there that may support any number of these types
     * of axes, we couldn't even begin to cover them with type-specific
     * subclasses.
     *
     * Use the various has_() and get_num_() methods to determine information about
     * the device capabilities. For instance, has_keyboard() will give an
     * indication that you can receive keystroke events from this device, and
     * get_num_buttons() will tell you that the device may send button events.
     *
     * There is the DeviceType enumeration, however, which will (if known) contain
     * identification of the general category of devices this fits in, such as
     * keyboard, mouse, gamepad, or flight stick.
     *
     * @since 1.10.0
     */
    """
    def disablePointerEvents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        disable_pointer_events(const InputDevice self)
        
        /**
         * Disables the generation of mouse-movement events.
         */
        """
        pass

    def disable_pointer_events(self, const_InputDevice_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        disable_pointer_events(const InputDevice self)
        
        /**
         * Disables the generation of mouse-movement events.
         */
        """
        pass

    def enablePointerEvents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        enable_pointer_events(const InputDevice self)
        
        /**
         * Enables the generation of mouse-movement events.
         */
        """
        pass

    def enable_pointer_events(self, const_InputDevice_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        enable_pointer_events(const InputDevice self)
        
        /**
         * Enables the generation of mouse-movement events.
         */
        """
        pass

    def findAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_axis(InputDevice self, Axis axis)
        
        /**
         * Returns the first AnalogAxis found with the given axis, or throw an assert
         * if the axis was not found in the list.
         */
        """
        pass

    def findButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        find_button(InputDevice self, ButtonHandle handle)
        
        /**
         * Returns the first ButtonState found with the given axis, or throw an assert
         * if the button handle was not found in the list.
         */
        """
        pass

    def find_axis(self, InputDevice_self, Axis_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_axis(InputDevice self, Axis axis)
        
        /**
         * Returns the first AnalogAxis found with the given axis, or throw an assert
         * if the axis was not found in the list.
         */
        """
        pass

    def find_button(self, InputDevice_self, ButtonHandle_handle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        find_button(InputDevice self, ButtonHandle handle)
        
        /**
         * Returns the first ButtonState found with the given axis, or throw an assert
         * if the button handle was not found in the list.
         */
        """
        pass

    def getButtonEvents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_button_events(const InputDevice self)
        
        /**
         * Returns the list of recently-generated ButtonEvents.
         * The list is also cleared.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getPointerEvents(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_pointer_events(const InputDevice self)
        
        /**
         * Returns a PointerEventList containing all the recent pointer events.
         * Clears the list.
         */
        """
        pass

    def get_button_events(self, const_InputDevice_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_button_events(const InputDevice self)
        
        /**
         * Returns the list of recently-generated ButtonEvents.
         * The list is also cleared.
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_pointer_events(self, const_InputDevice_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_pointer_events(const InputDevice self)
        
        /**
         * Returns a PointerEventList containing all the recent pointer events.
         * Clears the list.
         */
        """
        pass

    def hasButtonEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_button_event(InputDevice self)
        
        /**
         * Returns true if this device has a pending button event (a mouse button or
         * keyboard button down/up), false otherwise.  If this returns true, the
         * particular event may be extracted via get_button_event().
         */
        """
        pass

    def hasFeature(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_feature(InputDevice self, Feature feature)
        
        // Determine supported features
        
        /**
         * Returns true if the device supports the indicated feature.
         */
        """
        pass

    def hasPointerEvent(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_pointer_event(InputDevice self)
        
        /**
         * Returns true if this device has a pending pointer event (a mouse movement),
         * or false otherwise.  If this returns true, the particular event may be
         * extracted via get_pointer_event().
         */
        """
        pass

    def has_button_event(self, InputDevice_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_button_event(InputDevice self)
        
        /**
         * Returns true if this device has a pending button event (a mouse button or
         * keyboard button down/up), false otherwise.  If this returns true, the
         * particular event may be extracted via get_button_event().
         */
        """
        pass

    def has_feature(self, InputDevice_self, Feature_feature): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_feature(InputDevice self, Feature feature)
        
        // Determine supported features
        
        /**
         * Returns true if the device supports the indicated feature.
         */
        """
        pass

    def has_pointer_event(self, InputDevice_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_pointer_event(InputDevice self)
        
        /**
         * Returns true if this device has a pending pointer event (a mouse movement),
         * or false otherwise.  If this returns true, the particular event may be
         * extracted via get_pointer_event().
         */
        """
        pass

    def mapAxis(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        map_axis(const InputDevice self, int index, Axis axis)
        
        /**
         * Associates the indicated Axis with the axis of the indicated index
         * number.  Pass Axis::none to turn off any association.
         *
         * It is not necessary to call this if you simply want to query the state of
         * the various axes by index number.
         */
        """
        pass

    def mapButton(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        map_button(const InputDevice self, int index, ButtonHandle handle)
        
        // Associate buttons/axes with symbolic handles.
        
        /**
         * Associates the indicated ButtonHandle with the button of the indicated index
         * number.  When the given button index changes state, a corresponding
         * ButtonEvent will be generated with the given ButtonHandle.  Pass
         * ButtonHandle::none() to turn off any association.
         *
         * It is not necessary to call this if you simply want to query the state of
         * the various buttons by index number; this is only necessary in order to
         * generate ButtonEvents when the buttons change state.
         */
        """
        pass

    def map_axis(self, const_InputDevice_self, int_index, Axis_axis): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        map_axis(const InputDevice self, int index, Axis axis)
        
        /**
         * Associates the indicated Axis with the axis of the indicated index
         * number.  Pass Axis::none to turn off any association.
         *
         * It is not necessary to call this if you simply want to query the state of
         * the various axes by index number.
         */
        """
        pass

    def map_button(self, const_InputDevice_self, int_index, ButtonHandle_handle): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        map_button(const InputDevice self, int index, ButtonHandle handle)
        
        // Associate buttons/axes with symbolic handles.
        
        /**
         * Associates the indicated ButtonHandle with the button of the indicated index
         * number.  When the given button index changes state, a corresponding
         * ButtonEvent will be generated with the given ButtonHandle.  Pass
         * ButtonHandle::none() to turn off any association.
         *
         * It is not necessary to call this if you simply want to query the state of
         * the various buttons by index number; this is only necessary in order to
         * generate ButtonEvents when the buttons change state.
         */
        """
        pass

    def output(self, InputDevice_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(InputDevice self, ostream out)
        
        /**
         * Writes a one-line string describing the device.
         */
        """
        pass

    def poll(self, const_InputDevice_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        poll(const InputDevice self)
        
        /**
         * Polls the input device for new activity, to ensure it contains the latest
         * events.  This will only have any effect for some types of input devices;
         * others may be updated automatically, and this method will be a no-op.
         */
        """
        pass

    def setVibration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_vibration(const InputDevice self, double strong, double weak)
        
        // Enable rumble force-feedback effects
        
        /**
         * Sets the strength of the vibration effect, if supported.  The values are
         * clamped to 0-1 range. The first value axes the low-frequency rumble
         * motor, whereas the second axes the high-frequency motor, if present.
         */
        """
        pass

    def set_vibration(self, const_InputDevice_self, double_strong, double_weak): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_vibration(const InputDevice self, double strong, double weak)
        
        // Enable rumble force-feedback effects
        
        /**
         * Sets the strength of the vibration effect, if supported.  The values are
         * clamped to 0-1 range. The first value axes the low-frequency rumble
         * motor, whereas the second axes the high-frequency motor, if present.
         */
        """
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

    axes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    battery = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    buttons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Make device buttons and axes iterable"""

    connected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// This is false if we know that the device is not currently connected.
// May report false positives if we can't know this with certainty."""

    device_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// This contains an identification of the general type of device.  If
// this could not be determined, it is set to DC_unknown."""

    manufacturer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// The device's manufacturer, or the empty string if not known."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// The human-readable name of this input device."""

    product_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// USB product ID of the device, or 0 if not known."""

    serial_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// The device's serial number, or the empty string if not known."""

    tracker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// Getters for the various types of device data."""

    vendor_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """// USB vendor ID of the device, or 0 if not known."""

    _battery_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _pointer_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _tracker_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Axis = None # (!) real value is "<enum 'Axis'>"
    AxisState = None # (!) real value is "<class 'panda3d.core.AxisState'>"
    BatteryData = None # (!) real value is "<class 'panda3d.core.BatteryData'>"
    ButtonState = None # (!) real value is "<class 'panda3d.core.ButtonState'>"
    DeviceClass = None # (!) real value is "<enum 'DeviceClass'>"
    DtoolClassDict = {
        'Axis': None, # (!) real value is "<enum 'Axis'>"
        'AxisState': None, # (!) real value is "<class 'panda3d.core.AxisState'>"
        'BatteryData': None, # (!) real value is "<class 'panda3d.core.BatteryData'>"
        'ButtonState': None, # (!) real value is "<class 'panda3d.core.ButtonState'>"
        'DeviceClass': None, # (!) real value is "<enum 'DeviceClass'>"
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'Feature': None, # (!) real value is "<enum 'Feature'>"
        'SDown': 2,
        'SUnknown': 0,
        'SUp': 1,
        'S_down': 2,
        'S_unknown': 0,
        'S_up': 1,
        '__doc__': "/**\n * This is a structure representing a single input device.  Input devices may\n * have zero or more buttons, pointers, or axes associated with them, and\n * optionally a motion tracker.\n *\n * These devices are brought under a common interface because there is such a\n * large range of devices out there that may support any number of these types\n * of axes, we couldn't even begin to cover them with type-specific\n * subclasses.\n *\n * Use the various has_() and get_num_() methods to determine information about\n * the device capabilities. For instance, has_keyboard() will give an\n * indication that you can receive keystroke events from this device, and\n * get_num_buttons() will tell you that the device may send button events.\n *\n * There is the DeviceType enumeration, however, which will (if known) contain\n * identification of the general category of devices this fits in, such as\n * keyboard, mouse, gamepad, or flight stick.\n *\n * @since 1.10.0\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.InputDevice' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D6100>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.InputDevice' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.InputDevice' objects>"
        '_battery_data': None, # (!) real value is "<attribute '_battery_data' of 'panda3d.core.InputDevice' objects>"
        '_pointer_data': None, # (!) real value is "<attribute '_pointer_data' of 'panda3d.core.InputDevice' objects>"
        '_tracker_data': None, # (!) real value is "<attribute '_tracker_data' of 'panda3d.core.InputDevice' objects>"
        'axes': None, # (!) real value is "<attribute 'axes' of 'panda3d.core.InputDevice' objects>"
        'battery': None, # (!) real value is "<attribute 'battery' of 'panda3d.core.InputDevice' objects>"
        'buttons': None, # (!) real value is "<attribute 'buttons' of 'panda3d.core.InputDevice' objects>"
        'connected': None, # (!) real value is "<attribute 'connected' of 'panda3d.core.InputDevice' objects>"
        'device_class': None, # (!) real value is "<attribute 'device_class' of 'panda3d.core.InputDevice' objects>"
        'disablePointerEvents': None, # (!) real value is "<method 'disablePointerEvents' of 'panda3d.core.InputDevice' objects>"
        'disable_pointer_events': None, # (!) real value is "<method 'disable_pointer_events' of 'panda3d.core.InputDevice' objects>"
        'enablePointerEvents': None, # (!) real value is "<method 'enablePointerEvents' of 'panda3d.core.InputDevice' objects>"
        'enable_pointer_events': None, # (!) real value is "<method 'enable_pointer_events' of 'panda3d.core.InputDevice' objects>"
        'findAxis': None, # (!) real value is "<method 'findAxis' of 'panda3d.core.InputDevice' objects>"
        'findButton': None, # (!) real value is "<method 'findButton' of 'panda3d.core.InputDevice' objects>"
        'find_axis': None, # (!) real value is "<method 'find_axis' of 'panda3d.core.InputDevice' objects>"
        'find_button': None, # (!) real value is "<method 'find_button' of 'panda3d.core.InputDevice' objects>"
        'getButtonEvents': None, # (!) real value is "<method 'getButtonEvents' of 'panda3d.core.InputDevice' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2D6100>)>'
        'getPointerEvents': None, # (!) real value is "<method 'getPointerEvents' of 'panda3d.core.InputDevice' objects>"
        'get_button_events': None, # (!) real value is "<method 'get_button_events' of 'panda3d.core.InputDevice' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2D6100>)>'
        'get_pointer_events': None, # (!) real value is "<method 'get_pointer_events' of 'panda3d.core.InputDevice' objects>"
        'hasButtonEvent': None, # (!) real value is "<method 'hasButtonEvent' of 'panda3d.core.InputDevice' objects>"
        'hasFeature': None, # (!) real value is "<method 'hasFeature' of 'panda3d.core.InputDevice' objects>"
        'hasPointerEvent': None, # (!) real value is "<method 'hasPointerEvent' of 'panda3d.core.InputDevice' objects>"
        'has_button_event': None, # (!) real value is "<method 'has_button_event' of 'panda3d.core.InputDevice' objects>"
        'has_feature': None, # (!) real value is "<method 'has_feature' of 'panda3d.core.InputDevice' objects>"
        'has_pointer_event': None, # (!) real value is "<method 'has_pointer_event' of 'panda3d.core.InputDevice' objects>"
        'manufacturer': None, # (!) real value is "<attribute 'manufacturer' of 'panda3d.core.InputDevice' objects>"
        'mapAxis': None, # (!) real value is "<method 'mapAxis' of 'panda3d.core.InputDevice' objects>"
        'mapButton': None, # (!) real value is "<method 'mapButton' of 'panda3d.core.InputDevice' objects>"
        'map_axis': None, # (!) real value is "<method 'map_axis' of 'panda3d.core.InputDevice' objects>"
        'map_button': None, # (!) real value is "<method 'map_button' of 'panda3d.core.InputDevice' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.InputDevice' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.InputDevice' objects>"
        'poll': None, # (!) real value is "<method 'poll' of 'panda3d.core.InputDevice' objects>"
        'product_id': None, # (!) real value is "<attribute 'product_id' of 'panda3d.core.InputDevice' objects>"
        'serial_number': None, # (!) real value is "<attribute 'serial_number' of 'panda3d.core.InputDevice' objects>"
        'setVibration': None, # (!) real value is "<method 'setVibration' of 'panda3d.core.InputDevice' objects>"
        'set_vibration': None, # (!) real value is "<method 'set_vibration' of 'panda3d.core.InputDevice' objects>"
        'tracker': None, # (!) real value is "<attribute 'tracker' of 'panda3d.core.InputDevice' objects>"
        'vendor_id': None, # (!) real value is "<attribute 'vendor_id' of 'panda3d.core.InputDevice' objects>"
    }
    Feature = None # (!) real value is "<enum 'Feature'>"
    SDown = 2
    SUnknown = 0
    SUp = 1
    S_down = 2
    S_unknown = 0
    S_up = 1


