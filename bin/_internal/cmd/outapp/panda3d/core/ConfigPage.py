# encoding: utf-8
# module panda3d.core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\core.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import enum as __enum


class ConfigPage(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * A page of ConfigDeclarations that may be loaded or unloaded.  Typically
     * this represents a single .prc file that is read from disk at runtime, but
     * it may also represent a list of declarations built up by application code
     * and explicitly loaded.
     */
    """
    def clear(self, const_ConfigPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const ConfigPage self)
        
        /**
         * Removes all of the declarations from the page.
         */
        """
        pass

    def deleteDeclaration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        delete_declaration(const ConfigPage self, ConfigDeclaration decl)
        
        /**
         * Removes the indicated declaration from the page and deletes it.  Returns
         * true if the declaration is successfully removed, false if it was not on the
         * page.
         */
        """
        pass

    def delete_declaration(self, const_ConfigPage_self, ConfigDeclaration_decl): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        delete_declaration(const ConfigPage self, ConfigDeclaration decl)
        
        /**
         * Removes the indicated declaration from the page and deletes it.  Returns
         * true if the declaration is successfully removed, false if it was not on the
         * page.
         */
        """
        pass

    def getDeclaration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_declaration(ConfigPage self, int n)
        
        /**
         * Returns the nth declaration on the page.
         */
        """
        pass

    def getDefaultPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_default_page()
        
        /**
         * Returns a pointer to the global "default page".  This is the ConfigPage
         * that lists all variables' original default values.
         */
        """
        pass

    def getLocalPage(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_local_page()
        
        /**
         * Returns a pointer to the global "local page".  This is the ConfigPage that
         * lists the locally-assigned values for any variables in the world that have
         * such a local assignment.
         */
        """
        pass

    def getName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_name(ConfigPage self)
        
        /**
         * Returns the name of the page.  If the page was loaded from a .prc file,
         * this is usually the filename.
         */
        """
        pass

    def getNumDeclarations(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_declarations(ConfigPage self)
        
        /**
         * Returns the number of declarations on the page.
         */
        """
        pass

    def getPageSeq(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_page_seq(ConfigPage self)
        
        /**
         * Returns the sequence number of the page.
         *
         * Sequence numbers for a particular class (implicit vs.  explicit) of pages
         * are assigned as each page is loaded; each page is given a higher sequence
         * number than all the pages loaded before it.
         *
         * The implicit_load pages, which are discovered in the file system
         * automatically, have a different set of sequence numbers than the explicit
         * pages.
         */
        """
        pass

    def getSignature(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_signature(ConfigPage self)
        
        /**
         * Returns the raw binary signature that was found in the prc file, if any.
         * This method is probably not terribly useful for most applications.
         */
        """
        pass

    def getSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_sort(ConfigPage self)
        
        /**
         * Returns the explicit sort order of this particular ConfigPage.  See
         * set_sort().
         */
        """
        pass

    def getStringValue(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_string_value(ConfigPage self, int n)
        
        /**
         * Returns the value assigned by the nth declaration on the page.
         */
        """
        pass

    def getTrustLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_trust_level(ConfigPage self)
        
        /**
         * Returns the trust level associated with this page.  An untrusted page is
         * trust level 0; if the page was loaded from a signed .prc file, its trust
         * level is the index number of the certificate that signed it.  Generally, a
         * higher trust level value represents a greater level of trust.
         */
        """
        pass

    def getVariableName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_variable_name(ConfigPage self, int n)
        
        /**
         * Returns the variable named by the nth declaration on the page.
         */
        """
        pass

    def get_declaration(self, ConfigPage_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_declaration(ConfigPage self, int n)
        
        /**
         * Returns the nth declaration on the page.
         */
        """
        pass

    def get_default_page(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_default_page()
        
        /**
         * Returns a pointer to the global "default page".  This is the ConfigPage
         * that lists all variables' original default values.
         */
        """
        pass

    def get_local_page(self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_local_page()
        
        /**
         * Returns a pointer to the global "local page".  This is the ConfigPage that
         * lists the locally-assigned values for any variables in the world that have
         * such a local assignment.
         */
        """
        pass

    def get_name(self, ConfigPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_name(ConfigPage self)
        
        /**
         * Returns the name of the page.  If the page was loaded from a .prc file,
         * this is usually the filename.
         */
        """
        pass

    def get_num_declarations(self, ConfigPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_declarations(ConfigPage self)
        
        /**
         * Returns the number of declarations on the page.
         */
        """
        pass

    def get_page_seq(self, ConfigPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_page_seq(ConfigPage self)
        
        /**
         * Returns the sequence number of the page.
         *
         * Sequence numbers for a particular class (implicit vs.  explicit) of pages
         * are assigned as each page is loaded; each page is given a higher sequence
         * number than all the pages loaded before it.
         *
         * The implicit_load pages, which are discovered in the file system
         * automatically, have a different set of sequence numbers than the explicit
         * pages.
         */
        """
        pass

    def get_signature(self, ConfigPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_signature(ConfigPage self)
        
        /**
         * Returns the raw binary signature that was found in the prc file, if any.
         * This method is probably not terribly useful for most applications.
         */
        """
        pass

    def get_sort(self, ConfigPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_sort(ConfigPage self)
        
        /**
         * Returns the explicit sort order of this particular ConfigPage.  See
         * set_sort().
         */
        """
        pass

    def get_string_value(self, ConfigPage_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_string_value(ConfigPage self, int n)
        
        /**
         * Returns the value assigned by the nth declaration on the page.
         */
        """
        pass

    def get_trust_level(self, ConfigPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_trust_level(ConfigPage self)
        
        /**
         * Returns the trust level associated with this page.  An untrusted page is
         * trust level 0; if the page was loaded from a signed .prc file, its trust
         * level is the index number of the certificate that signed it.  Generally, a
         * higher trust level value represents a greater level of trust.
         */
        """
        pass

    def get_variable_name(self, ConfigPage_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_variable_name(ConfigPage self, int n)
        
        /**
         * Returns the variable named by the nth declaration on the page.
         */
        """
        pass

    def isImplicit(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_implicit(ConfigPage self)
        
        /**
         * Returns true if the page was loaded by implicitly searching the config path
         * on startup, or false if it was explicitly loaded by dynamic code after
         * initial startup.
         */
        """
        pass

    def isSpecial(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_special(ConfigPage self)
        
        /**
         * Returns true if this is the special "default" or "local" page, or false if
         * it is an ordinary page, e.g.  an implicit page loaded from a prc file at
         * startup, or an explicit page created by
         * ConfigPageManager::make_explicit_page().
         */
        """
        pass

    def isVariableUsed(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        is_variable_used(ConfigPage self, int n)
        
        /**
         * Returns true if the nth active variable on the page has been used by code,
         * false otherwise.
         */
        """
        pass

    def is_implicit(self, ConfigPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_implicit(ConfigPage self)
        
        /**
         * Returns true if the page was loaded by implicitly searching the config path
         * on startup, or false if it was explicitly loaded by dynamic code after
         * initial startup.
         */
        """
        pass

    def is_special(self, ConfigPage_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_special(ConfigPage self)
        
        /**
         * Returns true if this is the special "default" or "local" page, or false if
         * it is an ordinary page, e.g.  an implicit page loaded from a prc file at
         * startup, or an explicit page created by
         * ConfigPageManager::make_explicit_page().
         */
        """
        pass

    def is_variable_used(self, ConfigPage_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        is_variable_used(ConfigPage self, int n)
        
        /**
         * Returns true if the nth active variable on the page has been used by code,
         * false otherwise.
         */
        """
        pass

    def makeDeclaration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        make_declaration(const ConfigPage self, ConfigVariableCore variable, str value)
        make_declaration(const ConfigPage self, str variable, str value)
        
        /**
         * Adds the indicated variable/value pair as a new declaration on the page.
         */
        
        /**
         * Adds the indicated variable/value pair as a new declaration on the page.
         */
        """
        pass

    def make_declaration(self, const_ConfigPage_self, ConfigVariableCore_variable, str_value): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        make_declaration(const ConfigPage self, ConfigVariableCore variable, str value)
        make_declaration(const ConfigPage self, str variable, str value)
        
        /**
         * Adds the indicated variable/value pair as a new declaration on the page.
         */
        
        /**
         * Adds the indicated variable/value pair as a new declaration on the page.
         */
        """
        pass

    def modifyDeclaration(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        modify_declaration(const ConfigPage self, int n)
        
        /**
         * Returns a modifiable pointer to the nth declaration on the page.  Any
         * modifications will appear in the output, if the page is written out with
         * ConfigPage::write().
         */
        """
        pass

    def modify_declaration(self, const_ConfigPage_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        modify_declaration(const ConfigPage self, int n)
        
        /**
         * Returns a modifiable pointer to the nth declaration on the page.  Any
         * modifications will appear in the output, if the page is written out with
         * ConfigPage::write().
         */
        """
        pass

    def output(self, ConfigPage_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output(ConfigPage self, ostream out)
        
        /**
         *
         */
        """
        pass

    def outputBriefSignature(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        output_brief_signature(ConfigPage self, ostream out)
        
        /**
         * Outputs the first few hex digits of the signature.
         */
        """
        pass

    def output_brief_signature(self, ConfigPage_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        output_brief_signature(ConfigPage self, ostream out)
        
        /**
         * Outputs the first few hex digits of the signature.
         */
        """
        pass

    def readEncryptedPrc(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_encrypted_prc(const ConfigPage self, istream in, str password)
        
        /**
         * Automatically decrypts and reads the stream, given the indicated password.
         * Note that if the password is incorrect, the result may be garbage.
         */
        """
        pass

    def readPrc(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_prc(const ConfigPage self, istream in)
        
        /**
         * Reads the contents of a complete prc file, as returned by the indicated
         * istream, into the current page file.  Returns true on success, or false on
         * some I/O error.
         *
         * This is a low-level interface.  Normally you do not need to call it
         * directly.  See the global functions load_prc_file() and unload_prc_file(),
         * defined in panda/src/putil, for a higher-level interface.
         */
        """
        pass

    def read_encrypted_prc(self, const_ConfigPage_self, istream_in, str_password): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_encrypted_prc(const ConfigPage self, istream in, str password)
        
        /**
         * Automatically decrypts and reads the stream, given the indicated password.
         * Note that if the password is incorrect, the result may be garbage.
         */
        """
        pass

    def read_prc(self, const_ConfigPage_self, istream_in): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_prc(const ConfigPage self, istream in)
        
        /**
         * Reads the contents of a complete prc file, as returned by the indicated
         * istream, into the current page file.  Returns true on success, or false on
         * some I/O error.
         *
         * This is a low-level interface.  Normally you do not need to call it
         * directly.  See the global functions load_prc_file() and unload_prc_file(),
         * defined in panda/src/putil, for a higher-level interface.
         */
        """
        pass

    def setSort(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_sort(const ConfigPage self, int sort)
        
        /**
         * Changes the explicit sort order of this particular ConfigPage.  Lower-
         * numbered pages supercede higher-numbered pages.  Initially, all explicitly-
         * loaded pages have sort value 0, and implicitly-loaded pages (found on disk)
         * have sort value 10; you may set an individual page higher or lower to
         * influence its priority relative to other pages.
         */
        """
        pass

    def setTrustLevel(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        set_trust_level(const ConfigPage self, int trust_level)
        
        /**
         * Explicitly sets the trust level on this particular page.  Note that any
         * subsequent changes to the page, or to any variable declarations on it, will
         * reset the trust level to zero.
         */
        """
        pass

    def set_sort(self, const_ConfigPage_self, int_sort): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_sort(const ConfigPage self, int sort)
        
        /**
         * Changes the explicit sort order of this particular ConfigPage.  Lower-
         * numbered pages supercede higher-numbered pages.  Initially, all explicitly-
         * loaded pages have sort value 0, and implicitly-loaded pages (found on disk)
         * have sort value 10; you may set an individual page higher or lower to
         * influence its priority relative to other pages.
         */
        """
        pass

    def set_trust_level(self, const_ConfigPage_self, int_trust_level): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        set_trust_level(const ConfigPage self, int trust_level)
        
        /**
         * Explicitly sets the trust level on this particular page.  Note that any
         * subsequent changes to the page, or to any variable declarations on it, will
         * reset the trust level to zero.
         */
        """
        pass

    def write(self, ConfigPage_self, ostream_out): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(ConfigPage self, ostream out)
        
        /**
         *
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

    declarations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    implicit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_seq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    special = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trust_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__doc__': '/**\n * A page of ConfigDeclarations that may be loaded or unloaded.  Typically\n * this represents a single .prc file that is read from disk at runtime, but\n * it may also represent a list of declarations built up by application code\n * and explicitly loaded.\n */',
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.core.ConfigPage' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFCFE262280>'
        '__repr__': None, # (!) real value is "<slot wrapper '__repr__' of 'panda3d.core.ConfigPage' objects>"
        '__str__': None, # (!) real value is "<slot wrapper '__str__' of 'panda3d.core.ConfigPage' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.core.ConfigPage' objects>"
        'declarations': None, # (!) real value is "<attribute 'declarations' of 'panda3d.core.ConfigPage' objects>"
        'deleteDeclaration': None, # (!) real value is "<method 'deleteDeclaration' of 'panda3d.core.ConfigPage' objects>"
        'delete_declaration': None, # (!) real value is "<method 'delete_declaration' of 'panda3d.core.ConfigPage' objects>"
        'getDeclaration': None, # (!) real value is "<method 'getDeclaration' of 'panda3d.core.ConfigPage' objects>"
        'getDefaultPage': None, # (!) real value is '<staticmethod(<built-in method getDefaultPage of type object at 0x00007FFCFE262280>)>'
        'getLocalPage': None, # (!) real value is '<staticmethod(<built-in method getLocalPage of type object at 0x00007FFCFE262280>)>'
        'getName': None, # (!) real value is "<method 'getName' of 'panda3d.core.ConfigPage' objects>"
        'getNumDeclarations': None, # (!) real value is "<method 'getNumDeclarations' of 'panda3d.core.ConfigPage' objects>"
        'getPageSeq': None, # (!) real value is "<method 'getPageSeq' of 'panda3d.core.ConfigPage' objects>"
        'getSignature': None, # (!) real value is "<method 'getSignature' of 'panda3d.core.ConfigPage' objects>"
        'getSort': None, # (!) real value is "<method 'getSort' of 'panda3d.core.ConfigPage' objects>"
        'getStringValue': None, # (!) real value is "<method 'getStringValue' of 'panda3d.core.ConfigPage' objects>"
        'getTrustLevel': None, # (!) real value is "<method 'getTrustLevel' of 'panda3d.core.ConfigPage' objects>"
        'getVariableName': None, # (!) real value is "<method 'getVariableName' of 'panda3d.core.ConfigPage' objects>"
        'get_declaration': None, # (!) real value is "<method 'get_declaration' of 'panda3d.core.ConfigPage' objects>"
        'get_default_page': None, # (!) real value is '<staticmethod(<built-in method get_default_page of type object at 0x00007FFCFE262280>)>'
        'get_local_page': None, # (!) real value is '<staticmethod(<built-in method get_local_page of type object at 0x00007FFCFE262280>)>'
        'get_name': None, # (!) real value is "<method 'get_name' of 'panda3d.core.ConfigPage' objects>"
        'get_num_declarations': None, # (!) real value is "<method 'get_num_declarations' of 'panda3d.core.ConfigPage' objects>"
        'get_page_seq': None, # (!) real value is "<method 'get_page_seq' of 'panda3d.core.ConfigPage' objects>"
        'get_signature': None, # (!) real value is "<method 'get_signature' of 'panda3d.core.ConfigPage' objects>"
        'get_sort': None, # (!) real value is "<method 'get_sort' of 'panda3d.core.ConfigPage' objects>"
        'get_string_value': None, # (!) real value is "<method 'get_string_value' of 'panda3d.core.ConfigPage' objects>"
        'get_trust_level': None, # (!) real value is "<method 'get_trust_level' of 'panda3d.core.ConfigPage' objects>"
        'get_variable_name': None, # (!) real value is "<method 'get_variable_name' of 'panda3d.core.ConfigPage' objects>"
        'implicit': None, # (!) real value is "<attribute 'implicit' of 'panda3d.core.ConfigPage' objects>"
        'isImplicit': None, # (!) real value is "<method 'isImplicit' of 'panda3d.core.ConfigPage' objects>"
        'isSpecial': None, # (!) real value is "<method 'isSpecial' of 'panda3d.core.ConfigPage' objects>"
        'isVariableUsed': None, # (!) real value is "<method 'isVariableUsed' of 'panda3d.core.ConfigPage' objects>"
        'is_implicit': None, # (!) real value is "<method 'is_implicit' of 'panda3d.core.ConfigPage' objects>"
        'is_special': None, # (!) real value is "<method 'is_special' of 'panda3d.core.ConfigPage' objects>"
        'is_variable_used': None, # (!) real value is "<method 'is_variable_used' of 'panda3d.core.ConfigPage' objects>"
        'makeDeclaration': None, # (!) real value is "<method 'makeDeclaration' of 'panda3d.core.ConfigPage' objects>"
        'make_declaration': None, # (!) real value is "<method 'make_declaration' of 'panda3d.core.ConfigPage' objects>"
        'modifyDeclaration': None, # (!) real value is "<method 'modifyDeclaration' of 'panda3d.core.ConfigPage' objects>"
        'modify_declaration': None, # (!) real value is "<method 'modify_declaration' of 'panda3d.core.ConfigPage' objects>"
        'name': None, # (!) real value is "<attribute 'name' of 'panda3d.core.ConfigPage' objects>"
        'output': None, # (!) real value is "<method 'output' of 'panda3d.core.ConfigPage' objects>"
        'outputBriefSignature': None, # (!) real value is "<method 'outputBriefSignature' of 'panda3d.core.ConfigPage' objects>"
        'output_brief_signature': None, # (!) real value is "<method 'output_brief_signature' of 'panda3d.core.ConfigPage' objects>"
        'page_seq': None, # (!) real value is "<attribute 'page_seq' of 'panda3d.core.ConfigPage' objects>"
        'readEncryptedPrc': None, # (!) real value is "<method 'readEncryptedPrc' of 'panda3d.core.ConfigPage' objects>"
        'readPrc': None, # (!) real value is "<method 'readPrc' of 'panda3d.core.ConfigPage' objects>"
        'read_encrypted_prc': None, # (!) real value is "<method 'read_encrypted_prc' of 'panda3d.core.ConfigPage' objects>"
        'read_prc': None, # (!) real value is "<method 'read_prc' of 'panda3d.core.ConfigPage' objects>"
        'setSort': None, # (!) real value is "<method 'setSort' of 'panda3d.core.ConfigPage' objects>"
        'setTrustLevel': None, # (!) real value is "<method 'setTrustLevel' of 'panda3d.core.ConfigPage' objects>"
        'set_sort': None, # (!) real value is "<method 'set_sort' of 'panda3d.core.ConfigPage' objects>"
        'set_trust_level': None, # (!) real value is "<method 'set_trust_level' of 'panda3d.core.ConfigPage' objects>"
        'signature': None, # (!) real value is "<attribute 'signature' of 'panda3d.core.ConfigPage' objects>"
        'sort': None, # (!) real value is "<attribute 'sort' of 'panda3d.core.ConfigPage' objects>"
        'special': None, # (!) real value is "<attribute 'special' of 'panda3d.core.ConfigPage' objects>"
        'trust_level': None, # (!) real value is "<attribute 'trust_level' of 'panda3d.core.ConfigPage' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.core.ConfigPage' objects>"
    }


