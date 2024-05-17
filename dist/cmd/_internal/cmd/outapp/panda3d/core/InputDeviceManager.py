# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class InputDeviceManager(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * This class keeps track of all the devices on a system, and sends out events
     * when a device has been hot-plugged.
     *
     * @since 1.10.0
     */
    """
    def addDevice(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        add_device(const InputDeviceManager self, InputDevice device)
        
        /**
         * Called when a new device has been discovered.  This may also be used to
         * register virtual devices.
         *
         * This causes a connect-device event to be thrown.
         */
        """
        pass

    def add_device(self, const_InputDeviceManager_self, InputDevice_device): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        add_device(const InputDeviceManager self, InputDevice device)
        
        /**
         * Called when a new device has been discovered.  This may also be used to
         * register virtual devices.
         *
         * This causes a connect-device event to be thrown.
         */
        """
        pass

    def getDevices(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_devices(InputDeviceManager self)
        get_devices(InputDeviceManager self, DeviceClass device_class)
        
        /**
         * Description: Returns all currently connected devices.
         */
        
        /**
         * Description: Returns all currently connected devices of the given device class.
         */
        """
        pass

    def getGlobalPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the singleton InputDeviceManager instance.
         */
        """
        pass

    def get_devices(self, InputDeviceManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_devices(InputDeviceManager self)
        get_devices(InputDeviceManager self, DeviceClass device_class)
        
        /**
         * Description: Returns all currently connected devices.
         */
        
        /**
         * Description: Returns all currently connected devices of the given device class.
         */
        """
        pass

    def get_global_ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_global_ptr()
        
        /**
         * Returns the singleton InputDeviceManager instance.
         */
        """
        pass

    def removeDevice(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        remove_device(const InputDeviceManager self, InputDevice device)
        
        /**
         * Called when a device has been removed, or when a device should otherwise no
         * longer be tracked.
         *
         * This causes a disconnect-device event to be thrown.
         */
        """
        pass

    def remove_device(self, const_InputDeviceManager_self, InputDevice_device): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        remove_device(const InputDeviceManager self, InputDevice device)
        
        /**
         * Called when a device has been removed, or when a device should otherwise no
         * longer be tracked.
         *
         * This causes a disconnect-device event to be thrown.
         */
        """
        pass

    def update(self, const_InputDeviceManager_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        update(const InputDeviceManager self)
        
        /**
         * Polls the system to see if there are any new devices.  In some
         * implementations this is a no-op.
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
        '__doc__': '/**\n * This class keeps track of all the devices on a system, and sends out events\n * when a device has been hot-plugged.\n *\n * @since 1.10.0\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.InputDeviceManager' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2D7150>'
        'addDevice': None, # (!) real value is "<method 'addDevice' of 'panda3d.core.InputDeviceManager' objects>"
        'add_device': None, # (!) real value is "<method 'add_device' of 'panda3d.core.InputDeviceManager' objects>"
        'getDevices': None, # (!) real value is "<method 'getDevices' of 'panda3d.core.InputDeviceManager' objects>"
        'getGlobalPtr': None, # (!) real value is '<staticmethod(<built-in method getGlobalPtr of type object at 0x00007FFCFE2D7150>)>'
        'get_devices': None, # (!) real value is "<method 'get_devices' of 'panda3d.core.InputDeviceManager' objects>"
        'get_global_ptr': None, # (!) real value is '<staticmethod(<built-in method get_global_ptr of type object at 0x00007FFCFE2D7150>)>'
        'removeDevice': None, # (!) real value is "<method 'removeDevice' of 'panda3d.core.InputDeviceManager' objects>"
        'remove_device': None, # (!) real value is "<method 'remove_device' of 'panda3d.core.InputDeviceManager' objects>"
        'update': None, # (!) real value is "<method 'update' of 'panda3d.core.InputDeviceManager' objects>"
    }


