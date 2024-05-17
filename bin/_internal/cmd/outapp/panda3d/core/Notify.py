# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class Notify(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * An object that handles general error reporting to the user.  It contains a
     * pointer to an ostream, initially cerr, which can be reset at will to point
     * to different output devices, according to the needs of the application.
     * All output generated within Panda should vector through the Notify ostream.
     *
     * This also includes a collection of Categories and Severities, which may be
     * independently enabled or disabled, so that error messages may be squelched
     * or respected according to the wishes of the user.
     */
    """
    def clearAssertFailed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_assert_failed(const Notify self)
        
        /**
         * Resets the assert_failed flag that is set whenever an assertion test fails.
         * See has_assert_failed().
         */
        """
        pass

    def clearAssertHandler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        clear_assert_handler(const Notify self)
        
        /**
         * Removes the installed assert handler and restores default behavior of
         * nassertr() and nassertv().
         */
        """
        pass

    def clear_assert_failed(self, const_Notify_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_assert_failed(const Notify self)
        
        /**
         * Resets the assert_failed flag that is set whenever an assertion test fails.
         * See has_assert_failed().
         */
        """
        pass

    def clear_assert_handler(self, const_Notify_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear_assert_handler(const Notify self)
        
        /**
         * Removes the installed assert handler and restores default behavior of
         * nassertr() and nassertv().
         */
        """
        pass

    def getAssertErrorMessage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_assert_error_message(Notify self)
        
        /**
         * Returns the error message that corresponds to the assertion that most
         * recently failed.
         */
        """
        pass

    def getCategory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_category(const Notify self, str fullname)
        get_category(const Notify self, str basename, NotifyCategory parent_category)
        get_category(const Notify self, str basename, str parent_fullname)
        
        /**
         * Finds or creates a new Category given the basename of the category and its
         * parent in the category hierarchy.  The parent pointer may be NULL to
         * indicate this is a top-level Category.
         */
        
        /**
         * Finds or creates a new Category given the basename of the category and the
         * fullname of its parent.  This is another way to create a category when you
         * don't have a pointer to its parent handy, but you know the name of its
         * parent.  If the parent Category does not already exist, it will be created.
         */
        
        /**
         * Finds or creates a new Category given the fullname of the Category.  This
         * name should be a sequence of colon-separated names of parent Categories,
         * ending in the basename of this Category, e.g.  display:glxdisplay.  This is
         * a shorthand way to define a Category when a pointer to its parent is not
         * handy.
         */
        """
        pass

    def getOstreamPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_ostream_ptr(Notify self)
        
        /**
         * Returns the system-wide ostream for all Notify messages.
         */
        """
        pass

    def getTopCategory(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_top_category(const Notify self)
        
        /**
         * Returns the topmost Category in the hierarchy.  This may be used to
         * traverse the hierarchy of available Categories.
         */
        """
        pass

    def get_assert_error_message(self, Notify_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_assert_error_message(Notify self)
        
        /**
         * Returns the error message that corresponds to the assertion that most
         * recently failed.
         */
        """
        pass

    def get_category(self, const_Notify_self, str_fullname): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_category(const Notify self, str fullname)
        get_category(const Notify self, str basename, NotifyCategory parent_category)
        get_category(const Notify self, str basename, str parent_fullname)
        
        /**
         * Finds or creates a new Category given the basename of the category and its
         * parent in the category hierarchy.  The parent pointer may be NULL to
         * indicate this is a top-level Category.
         */
        
        /**
         * Finds or creates a new Category given the basename of the category and the
         * fullname of its parent.  This is another way to create a category when you
         * don't have a pointer to its parent handy, but you know the name of its
         * parent.  If the parent Category does not already exist, it will be created.
         */
        
        /**
         * Finds or creates a new Category given the fullname of the Category.  This
         * name should be a sequence of colon-separated names of parent Categories,
         * ending in the basename of this Category, e.g.  display:glxdisplay.  This is
         * a shorthand way to define a Category when a pointer to its parent is not
         * handy.
         */
        """
        pass

    def get_ostream_ptr(self, Notify_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_ostream_ptr(Notify self)
        
        /**
         * Returns the system-wide ostream for all Notify messages.
         */
        """
        pass

    def get_top_category(self, const_Notify_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_top_category(const Notify self)
        
        /**
         * Returns the topmost Category in the hierarchy.  This may be used to
         * traverse the hierarchy of available Categories.
         */
        """
        pass

    def hasAssertFailed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_assert_failed(Notify self)
        
        /**
         * Returns true if an assertion test has failed (and not been ignored) since
         * the last call to clear_assert_failed().
         *
         * When an assertion test fails, the assert handler may decide either to
         * abort, return, or ignore the assertion.  Naturally, if it decides to abort,
         * this flag is irrelevant.  If it chooses to ignore the assertion, the flag
         * is not set.  However, if the assert handler chooses to return out of the
         * function (the normal case), it will also set this flag to indicate that an
         * assertion failure has occurred.
         *
         * This will also be the behavior in the absence of a user-defined assert
         * handler.
         */
        """
        pass

    def hasAssertHandler(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        has_assert_handler(Notify self)
        
        /**
         * Returns true if a user assert handler has been installed, false otherwise.
         */
        """
        pass

    def has_assert_failed(self, Notify_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_assert_failed(Notify self)
        
        /**
         * Returns true if an assertion test has failed (and not been ignored) since
         * the last call to clear_assert_failed().
         *
         * When an assertion test fails, the assert handler may decide either to
         * abort, return, or ignore the assertion.  Naturally, if it decides to abort,
         * this flag is irrelevant.  If it chooses to ignore the assertion, the flag
         * is not set.  However, if the assert handler chooses to return out of the
         * function (the normal case), it will also set this flag to indicate that an
         * assertion failure has occurred.
         *
         * This will also be the behavior in the absence of a user-defined assert
         * handler.
         */
        """
        pass

    def has_assert_handler(self, Notify_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        has_assert_handler(Notify self)
        
        /**
         * Returns true if a user assert handler has been installed, false otherwise.
         */
        """
        pass

    def null(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        null()
        
        /**
         * A convenient way to get an ostream that doesn't do anything.  Returned by
         * Category::out() when a particular Category and/or Severity is disabled.
         */
        """
        pass

    def out(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        out()
        
        /**
         * A convenient way to get the ostream that should be written to for a Notify-
         * type message.  Also see Category::out() for a message that is specific to a
         * particular Category.
         */
        """
        pass

    def ptr(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        ptr()
        
        /**
         * Returns the pointer to the global Notify object.  There is only one of
         * these in the world.
         */
        """
        pass

    def setOstreamPtr(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_ostream_ptr(const Notify self, object ostream_ptr, bool delete_later)
        
        /**
         * Changes the ostream that all subsequent Notify messages will be written to.
         * If the previous ostream was set with delete_later = true, this will delete
         * the previous ostream.  If ostream_ptr is NULL, this resets the default to
         * cerr.
         */
        """
        pass

    def set_ostream_ptr(self, const_Notify_self, object_ostream_ptr, bool_delete_later): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_ostream_ptr(const Notify self, object ostream_ptr, bool delete_later)
        
        /**
         * Changes the ostream that all subsequent Notify messages will be written to.
         * If the previous ostream was set with delete_later = true, this will delete
         * the previous ostream.  If ostream_ptr is NULL, this resets the default to
         * cerr.
         */
        """
        pass

    def writeString(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        write_string(str str)
        
        /**
         * A convenient way for scripting languages, which may know nothing about
         * ostreams, to write to Notify.  This writes a single string, followed by an
         * implicit newline, to the Notify output stream.
         */
        """
        pass

    def write_string(self, str_str): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write_string(str str)
        
        /**
         * A convenient way for scripting languages, which may know nothing about
         * ostreams, to write to Notify.  This writes a single string, followed by an
         * implicit newline, to the Notify output stream.
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
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.core.Notify' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.core.Notify' objects>"
        '__doc__': '/**\n * An object that handles general error reporting to the user.  It contains a\n * pointer to an ostream, initially cerr, which can be reset at will to point\n * to different output devices, according to the needs of the application.\n * All output generated within Panda should vector through the Notify ostream.\n *\n * This also includes a collection of Categories and Severities, which may be\n * independently enabled or disabled, so that error messages may be squelched\n * or respected according to the wishes of the user.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.Notify' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE2627F0>'
        'clearAssertFailed': None, # (!) real value is "<method 'clearAssertFailed' of 'panda3d.core.Notify' objects>"
        'clearAssertHandler': None, # (!) real value is "<method 'clearAssertHandler' of 'panda3d.core.Notify' objects>"
        'clear_assert_failed': None, # (!) real value is "<method 'clear_assert_failed' of 'panda3d.core.Notify' objects>"
        'clear_assert_handler': None, # (!) real value is "<method 'clear_assert_handler' of 'panda3d.core.Notify' objects>"
        'getAssertErrorMessage': None, # (!) real value is "<method 'getAssertErrorMessage' of 'panda3d.core.Notify' objects>"
        'getCategory': None, # (!) real value is "<method 'getCategory' of 'panda3d.core.Notify' objects>"
        'getOstreamPtr': None, # (!) real value is "<method 'getOstreamPtr' of 'panda3d.core.Notify' objects>"
        'getTopCategory': None, # (!) real value is "<method 'getTopCategory' of 'panda3d.core.Notify' objects>"
        'get_assert_error_message': None, # (!) real value is "<method 'get_assert_error_message' of 'panda3d.core.Notify' objects>"
        'get_category': None, # (!) real value is "<method 'get_category' of 'panda3d.core.Notify' objects>"
        'get_ostream_ptr': None, # (!) real value is "<method 'get_ostream_ptr' of 'panda3d.core.Notify' objects>"
        'get_top_category': None, # (!) real value is "<method 'get_top_category' of 'panda3d.core.Notify' objects>"
        'hasAssertFailed': None, # (!) real value is "<method 'hasAssertFailed' of 'panda3d.core.Notify' objects>"
        'hasAssertHandler': None, # (!) real value is "<method 'hasAssertHandler' of 'panda3d.core.Notify' objects>"
        'has_assert_failed': None, # (!) real value is "<method 'has_assert_failed' of 'panda3d.core.Notify' objects>"
        'has_assert_handler': None, # (!) real value is "<method 'has_assert_handler' of 'panda3d.core.Notify' objects>"
        'null': None, # (!) real value is '<staticmethod(<built-in method null of type object at 0x00007FFCFE2627F0>)>'
        'out': None, # (!) real value is '<staticmethod(<built-in method out of type object at 0x00007FFCFE2627F0>)>'
        'ptr': None, # (!) real value is '<staticmethod(<built-in method ptr of type object at 0x00007FFCFE2627F0>)>'
        'setOstreamPtr': None, # (!) real value is "<method 'setOstreamPtr' of 'panda3d.core.Notify' objects>"
        'set_ostream_ptr': None, # (!) real value is "<method 'set_ostream_ptr' of 'panda3d.core.Notify' objects>"
        'writeString': None, # (!) real value is '<staticmethod(<built-in method writeString of type object at 0x00007FFCFE2627F0>)>'
        'write_string': None, # (!) real value is '<staticmethod(<built-in method write_string of type object at 0x00007FFCFE2627F0>)>'
    }


