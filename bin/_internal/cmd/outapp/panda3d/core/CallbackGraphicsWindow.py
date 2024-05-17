# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


from .GraphicsWindow import GraphicsWindow

class CallbackGraphicsWindow(GraphicsWindow):
    """
    /**
     * This special window object doesn't represent a window in its own right, but
     * instead hooks into some third-party API for creating and rendering to
     * windows via callbacks.  This can be used to allow Panda to render into an
     * already-created OpenGL context, for instance.
     */
    """
    def clearEventsCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_events_callback(const CallbackGraphicsWindow self)
        
        /**
         * Removes the callback set by an earlier call to set_events_callback().
         */
        """
        pass

    def clearPropertiesCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_properties_callback(const CallbackGraphicsWindow self)
        
        /**
         * Removes the callback set by an earlier call to set_properties_callback().
         */
        """
        pass

    def clearRenderCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_render_callback(const CallbackGraphicsWindow self)
        
        /**
         * Removes the callback set by an earlier call to set_render_callback().
         */
        """
        pass

    def clear_events_callback(self, const_CallbackGraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_events_callback(const CallbackGraphicsWindow self)
        
        /**
         * Removes the callback set by an earlier call to set_events_callback().
         */
        """
        pass

    def clear_properties_callback(self, const_CallbackGraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_properties_callback(const CallbackGraphicsWindow self)
        
        /**
         * Removes the callback set by an earlier call to set_properties_callback().
         */
        """
        pass

    def clear_render_callback(self, const_CallbackGraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_render_callback(const CallbackGraphicsWindow self)
        
        /**
         * Removes the callback set by an earlier call to set_render_callback().
         */
        """
        pass

    def createInputDevice(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        create_input_device(const CallbackGraphicsWindow self, str name)
        
        /**
         * Adds a new input device (mouse) to the window with the indicated name.
         * Returns the index of the new device.
         */
        """
        pass

    def create_input_device(self, const_CallbackGraphicsWindow_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        create_input_device(const CallbackGraphicsWindow self, str name)
        
        /**
         * Adds a new input device (mouse) to the window with the indicated name.
         * Returns the index of the new device.
         */
        """
        pass

    def getClassType(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def getEventsCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_events_callback(CallbackGraphicsWindow self)
        
        /**
         * Returns the CallbackObject set by set_events_callback().
         */
        """
        pass

    def getPropertiesCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_properties_callback(CallbackGraphicsWindow self)
        
        /**
         * Returns the CallbackObject set by set_properties_callback().
         */
        """
        pass

    def getRenderCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_render_callback(CallbackGraphicsWindow self)
        
        /**
         * Returns the CallbackObject set by set_render_callback().
         */
        """
        pass

    def get_class_type(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_type()
        """
        pass

    def get_events_callback(self, CallbackGraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_events_callback(CallbackGraphicsWindow self)
        
        /**
         * Returns the CallbackObject set by set_events_callback().
         */
        """
        pass

    def get_properties_callback(self, CallbackGraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_properties_callback(CallbackGraphicsWindow self)
        
        /**
         * Returns the CallbackObject set by set_properties_callback().
         */
        """
        pass

    def get_render_callback(self, CallbackGraphicsWindow_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_render_callback(CallbackGraphicsWindow self)
        
        /**
         * Returns the CallbackObject set by set_render_callback().
         */
        """
        pass

    def setEventsCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_events_callback(const CallbackGraphicsWindow self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when this window is polled
         * for window events, including mouse and keyboard events, as well as window
         * resize events and other system-generated events.
         *
         * This callback will receive a CallbackGraphicsWindow::EventsCallbackData.
         *
         * This callback should process any system-generated events, and call
         * data->upcall() to process requested property change requests made via
         * request_properties().
         */
        """
        pass

    def setPropertiesCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_properties_callback(const CallbackGraphicsWindow self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when this window receives a
         * property change request from user code (e.g.  via request_properties).
         *
         * This callback will receive a
         * CallbackGraphicsWindow::PropertiesCallbackData, which provides a
         * get_properties() method that returns a modifiable reference to a
         * WindowsProperties object.  This object will contain only those properties
         * requested by user code.  The callback should handle any of the requests it
         * finds, including and especially set_open(), and remove them from the object
         * when it has handled them.  Any unhandled properties should be left
         * unchanged in the properties object.
         */
        """
        pass

    def setRenderCallback(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_render_callback(const CallbackGraphicsWindow self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when this window is invoked
         * (in the draw thread) to render its contents, and/or flip the graphics
         * buffers.
         *
         * This callback will actually serve several different functions.  It
         * receivces a RenderCallbackData, and you can query data->get_callback_type()
         * to return the actual function of each particular callback.
         */
        """
        pass

    def set_events_callback(self, const_CallbackGraphicsWindow_self, CallbackObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_events_callback(const CallbackGraphicsWindow self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when this window is polled
         * for window events, including mouse and keyboard events, as well as window
         * resize events and other system-generated events.
         *
         * This callback will receive a CallbackGraphicsWindow::EventsCallbackData.
         *
         * This callback should process any system-generated events, and call
         * data->upcall() to process requested property change requests made via
         * request_properties().
         */
        """
        pass

    def set_properties_callback(self, const_CallbackGraphicsWindow_self, CallbackObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_properties_callback(const CallbackGraphicsWindow self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when this window receives a
         * property change request from user code (e.g.  via request_properties).
         *
         * This callback will receive a
         * CallbackGraphicsWindow::PropertiesCallbackData, which provides a
         * get_properties() method that returns a modifiable reference to a
         * WindowsProperties object.  This object will contain only those properties
         * requested by user code.  The callback should handle any of the requests it
         * finds, including and especially set_open(), and remove them from the object
         * when it has handled them.  Any unhandled properties should be left
         * unchanged in the properties object.
         */
        """
        pass

    def set_render_callback(self, const_CallbackGraphicsWindow_self, CallbackObject_object): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_render_callback(const CallbackGraphicsWindow self, CallbackObject object)
        
        /**
         * Sets the CallbackObject that will be notified when this window is invoked
         * (in the draw thread) to render its contents, and/or flip the graphics
         * buffers.
         *
         * This callback will actually serve several different functions.  It
         * receivces a RenderCallbackData, and you can query data->get_callback_type()
         * to return the actual function of each particular callback.
         */
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        'EventsCallbackData': None, # (!) real value is "<class 'panda3d.core.EventsCallbackData'>"
        'PropertiesCallbackData': None, # (!) real value is "<class 'panda3d.core.PropertiesCallbackData'>"
        'RCTBeginFlip': 2,
        'RCTBeginFrame': 0,
        'RCTEndFlip': 3,
        'RCTEndFrame': 1,
        'RCT_begin_flip': 2,
        'RCT_begin_frame': 0,
        'RCT_end_flip': 3,
        'RCT_end_frame': 1,
        'RenderCallbackData': None, # (!) real value is "<class 'panda3d.core.RenderCallbackData'>"
        'WindowCallbackData': None, # (!) real value is "<class 'panda3d.core.WindowCallbackData'>"
        '__doc__': "/**\n * This special window object doesn't represent a window in its own right, but\n * instead hooks into some third-party API for creating and rendering to\n * windows via callbacks.  This can be used to allow Panda to render into an\n * already-created OpenGL context, for instance.\n */",
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2DE920>'
        'clearEventsCallback': None, # (!) real value is "<method 'clearEventsCallback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'clearPropertiesCallback': None, # (!) real value is "<method 'clearPropertiesCallback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'clearRenderCallback': None, # (!) real value is "<method 'clearRenderCallback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'clear_events_callback': None, # (!) real value is "<method 'clear_events_callback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'clear_properties_callback': None, # (!) real value is "<method 'clear_properties_callback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'clear_render_callback': None, # (!) real value is "<method 'clear_render_callback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'createInputDevice': None, # (!) real value is "<method 'createInputDevice' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'create_input_device': None, # (!) real value is "<method 'create_input_device' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'getClassType': None, # (!) real value is '<staticmethod(<built-in method getClassType of type object at 0x00007FFCFE2DE920>)>'
        'getEventsCallback': None, # (!) real value is "<method 'getEventsCallback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'getPropertiesCallback': None, # (!) real value is "<method 'getPropertiesCallback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'getRenderCallback': None, # (!) real value is "<method 'getRenderCallback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'get_class_type': None, # (!) real value is '<staticmethod(<built-in method get_class_type of type object at 0x00007FFCFE2DE920>)>'
        'get_events_callback': None, # (!) real value is "<method 'get_events_callback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'get_properties_callback': None, # (!) real value is "<method 'get_properties_callback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'get_render_callback': None, # (!) real value is "<method 'get_render_callback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'setEventsCallback': None, # (!) real value is "<method 'setEventsCallback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'setPropertiesCallback': None, # (!) real value is "<method 'setPropertiesCallback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'setRenderCallback': None, # (!) real value is "<method 'setRenderCallback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'set_events_callback': None, # (!) real value is "<method 'set_events_callback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'set_properties_callback': None, # (!) real value is "<method 'set_properties_callback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
        'set_render_callback': None, # (!) real value is "<method 'set_render_callback' of 'panda3d.core.CallbackGraphicsWindow' objects>"
    }
    EventsCallbackData = None # (!) real value is "<class 'panda3d.core.EventsCallbackData'>"
    PropertiesCallbackData = None # (!) real value is "<class 'panda3d.core.PropertiesCallbackData'>"
    RCTBeginFlip = 2
    RCTBeginFrame = 0
    RCTEndFlip = 3
    RCTEndFrame = 1
    RCT_begin_flip = 2
    RCT_begin_frame = 0
    RCT_end_flip = 3
    RCT_end_frame = 1
    RenderCallbackData = None # (!) real value is "<class 'panda3d.core.RenderCallbackData'>"
    WindowCallbackData = None # (!) real value is "<class 'panda3d.core.WindowCallbackData'>"


