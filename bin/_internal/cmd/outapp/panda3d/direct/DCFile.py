# encoding: utf-8
# module panda3d.direct
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\panda3d\direct.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import dtoolconfig as __dtoolconfig
import panda3d.core as __panda3d_core


class DCFile(__dtoolconfig.DTOOL_SUPER_BASE):
    """
    /**
     * Represents the complete list of Distributed Class descriptions as read from
     * a .dc file.
     */
    """
    def allObjectsValid(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        all_objects_valid(DCFile self)
        
        /**
         * Returns true if all of the classes read from the DC file were defined and
         * valid, or false if any of them were undefined ("bogus classes").  If this
         * is true, we might have read a partial file.
         */
        """
        pass

    def all_objects_valid(self, DCFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        all_objects_valid(DCFile self)
        
        /**
         * Returns true if all of the classes read from the DC file were defined and
         * valid, or false if any of them were undefined ("bogus classes").  If this
         * is true, we might have read a partial file.
         */
        """
        pass

    def clear(self, const_DCFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        clear(const DCFile self)
        
        /**
         * Removes all of the classes defined within the DCFile and prepares it for
         * reading a new file.
         */
        """
        pass

    def getClass(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class(DCFile self, int n)
        
        /**
         * Returns the nth class read from the .dc file(s).
         */
        """
        pass

    def getClassByName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_class_by_name(DCFile self, str name)
        
        /**
         * Returns the class that has the indicated name, or NULL if there is no such
         * class.
         */
        """
        pass

    def getFieldByIndex(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_field_by_index(DCFile self, int index_number)
        
        /**
         * Returns a pointer to the one DCField that has the indicated index number,
         * of all the DCFields across all classes in the file.
         *
         * This method is only valid if dc-multiple-inheritance is set true in the
         * Config.prc file.  Without this setting, different DCFields may share the
         * same index number, so this global lookup is not possible.
         */
        """
        pass

    def getHash(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_hash(DCFile self)
        
        /**
         * Returns a 32-bit hash index associated with this file.  This number is
         * guaranteed to be consistent if the contents of the file have not changed,
         * and it is very likely to be different if the contents of the file do
         * change.
         */
        """
        pass

    def getImportModule(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_import_module(DCFile self, int n)
        
        /**
         * Returns the module named by the nth import line read from the .dc file(s).
         */
        """
        pass

    def getImportSymbol(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_import_symbol(DCFile self, int n, int i)
        
        /**
         * Returns the ith symbol named by the nth import line read from the .dc
         * file(s).
         */
        """
        pass

    def getKeyword(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keyword(DCFile self, int n)
        
        /**
         * Returns the nth keyword read from the .dc file(s).
         */
        """
        pass

    def getKeywordByName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_keyword_by_name(DCFile self, str name)
        
        /**
         * Returns the keyword that has the indicated name, or NULL if there is no
         * such keyword name.
         */
        """
        pass

    def getNumClasses(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_classes(DCFile self)
        
        /**
         * Returns the number of classes read from the .dc file(s).
         */
        """
        pass

    def getNumImportModules(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_import_modules(DCFile self)
        
        /**
         * Returns the number of import lines read from the .dc file(s).
         */
        """
        pass

    def getNumImportSymbols(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_import_symbols(DCFile self, int n)
        
        /**
         * Returns the number of symbols explicitly imported by the nth import line.
         * If this is 0, the line is "import modulename"; if it is more than 0, the
         * line is "from modulename import symbol, symbol ... ".
         */
        """
        pass

    def getNumKeywords(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_keywords(DCFile self)
        
        /**
         * Returns the number of keywords read from the .dc file(s).
         */
        """
        pass

    def getNumTypedefs(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_num_typedefs(DCFile self)
        
        /**
         * Returns the number of typedefs read from the .dc file(s).
         */
        """
        pass

    def getSwitchByName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_switch_by_name(DCFile self, str name)
        
        /**
         * Returns the switch that has the indicated name, or NULL if there is no such
         * switch.
         */
        """
        pass

    def getTypedef(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_typedef(DCFile self, int n)
        
        /**
         * Returns the nth typedef read from the .dc file(s).
         */
        """
        pass

    def getTypedefByName(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        get_typedef_by_name(DCFile self, str name)
        
        /**
         * Returns the typedef that has the indicated name, or NULL if there is no
         * such typedef name.
         */
        """
        pass

    def get_class(self, DCFile_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class(DCFile self, int n)
        
        /**
         * Returns the nth class read from the .dc file(s).
         */
        """
        pass

    def get_class_by_name(self, DCFile_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_class_by_name(DCFile self, str name)
        
        /**
         * Returns the class that has the indicated name, or NULL if there is no such
         * class.
         */
        """
        pass

    def get_field_by_index(self, DCFile_self, int_index_number): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_field_by_index(DCFile self, int index_number)
        
        /**
         * Returns a pointer to the one DCField that has the indicated index number,
         * of all the DCFields across all classes in the file.
         *
         * This method is only valid if dc-multiple-inheritance is set true in the
         * Config.prc file.  Without this setting, different DCFields may share the
         * same index number, so this global lookup is not possible.
         */
        """
        pass

    def get_hash(self, DCFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_hash(DCFile self)
        
        /**
         * Returns a 32-bit hash index associated with this file.  This number is
         * guaranteed to be consistent if the contents of the file have not changed,
         * and it is very likely to be different if the contents of the file do
         * change.
         */
        """
        pass

    def get_import_module(self, DCFile_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_import_module(DCFile self, int n)
        
        /**
         * Returns the module named by the nth import line read from the .dc file(s).
         */
        """
        pass

    def get_import_symbol(self, DCFile_self, int_n, int_i): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_import_symbol(DCFile self, int n, int i)
        
        /**
         * Returns the ith symbol named by the nth import line read from the .dc
         * file(s).
         */
        """
        pass

    def get_keyword(self, DCFile_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keyword(DCFile self, int n)
        
        /**
         * Returns the nth keyword read from the .dc file(s).
         */
        """
        pass

    def get_keyword_by_name(self, DCFile_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_keyword_by_name(DCFile self, str name)
        
        /**
         * Returns the keyword that has the indicated name, or NULL if there is no
         * such keyword name.
         */
        """
        pass

    def get_num_classes(self, DCFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_classes(DCFile self)
        
        /**
         * Returns the number of classes read from the .dc file(s).
         */
        """
        pass

    def get_num_import_modules(self, DCFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_import_modules(DCFile self)
        
        /**
         * Returns the number of import lines read from the .dc file(s).
         */
        """
        pass

    def get_num_import_symbols(self, DCFile_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_import_symbols(DCFile self, int n)
        
        /**
         * Returns the number of symbols explicitly imported by the nth import line.
         * If this is 0, the line is "import modulename"; if it is more than 0, the
         * line is "from modulename import symbol, symbol ... ".
         */
        """
        pass

    def get_num_keywords(self, DCFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_keywords(DCFile self)
        
        /**
         * Returns the number of keywords read from the .dc file(s).
         */
        """
        pass

    def get_num_typedefs(self, DCFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_num_typedefs(DCFile self)
        
        /**
         * Returns the number of typedefs read from the .dc file(s).
         */
        """
        pass

    def get_switch_by_name(self, DCFile_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_switch_by_name(DCFile self, str name)
        
        /**
         * Returns the switch that has the indicated name, or NULL if there is no such
         * switch.
         */
        """
        pass

    def get_typedef(self, DCFile_self, int_n): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_typedef(DCFile self, int n)
        
        /**
         * Returns the nth typedef read from the .dc file(s).
         */
        """
        pass

    def get_typedef_by_name(self, DCFile_self, str_name): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        get_typedef_by_name(DCFile self, str name)
        
        /**
         * Returns the typedef that has the indicated name, or NULL if there is no
         * such typedef name.
         */
        """
        pass

    def read(self, const_DCFile_self, istream_in, str_filename): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read(const DCFile self, istream in, str filename)
        
        /**
         * Opens and reads the indicated .dc file by name.  The distributed classes
         * defined in the file will be appended to the set of distributed classes
         * already recorded, if any.
         *
         * Returns true if the file is successfully read, false if there was an error
         * (in which case the file might have been partially read).
         */
        
        /**
         * Parses the already-opened input stream for distributed class descriptions.
         * The filename parameter is optional and is only used when reporting errors.
         *
         * The distributed classes defined in the file will be appended to the set of
         * distributed classes already recorded, if any.
         *
         * Returns true if the file is successfully read, false if there was an error
         * (in which case the file might have been partially read).
         */
        """
        pass

    def readAll(self, *args, **kwargs): # real signature unknown
        """
        C++ Interface:
        read_all(const DCFile self)
        
        /**
         * This special method reads all of the .dc files named by the "dc-file"
         * config.prc variable, and loads them into the DCFile namespace.
         */
        """
        pass

    def read_all(self, const_DCFile_self): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        read_all(const DCFile self)
        
        /**
         * This special method reads all of the .dc files named by the "dc-file"
         * config.prc variable, and loads them into the DCFile namespace.
         */
        """
        pass

    def write(self, DCFile_self, Filename_filename, bool_brief): # real signature unknown; restored from __doc__
        """
        C++ Interface:
        write(DCFile self, Filename filename, bool brief)
        write(DCFile self, ostream out, bool brief)
        
        /**
         * Opens the indicated filename for output and writes a parseable description
         * of all the known distributed classes to the file.
         *
         * Returns true if the description is successfully written, false otherwise.
         */
        
        /**
         * Writes a parseable description of all the known distributed classes to the
         * stream.
         *
         * Returns true if the description is successfully written, false otherwise.
         */
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    DtoolClassDict = {
        'DtoolClassDict': '<value is a self-reference, replaced by this string>',
        '__copy__': None, # (!) real value is "<method '__copy__' of 'panda3d.direct.DCFile' objects>"
        '__deepcopy__': None, # (!) real value is "<method '__deepcopy__' of 'panda3d.direct.DCFile' objects>"
        '__doc__': '/**\n * Represents the complete list of Distributed Class descriptions as read from\n * a .dc file.\n */',
        '__eq__': None, # (!) real value is "<slot wrapper '__eq__' of 'panda3d.direct.DCFile' objects>"
        '__ge__': None, # (!) real value is "<slot wrapper '__ge__' of 'panda3d.direct.DCFile' objects>"
        '__gt__': None, # (!) real value is "<slot wrapper '__gt__' of 'panda3d.direct.DCFile' objects>"
        '__hash__': None, # (!) real value is "<slot wrapper '__hash__' of 'panda3d.direct.DCFile' objects>"
        '__init__': None, # (!) real value is "<slot wrapper '__init__' of 'panda3d.direct.DCFile' objects>"
        '__le__': None, # (!) real value is "<slot wrapper '__le__' of 'panda3d.direct.DCFile' objects>"
        '__lt__': None, # (!) real value is "<slot wrapper '__lt__' of 'panda3d.direct.DCFile' objects>"
        '__ne__': None, # (!) real value is "<slot wrapper '__ne__' of 'panda3d.direct.DCFile' objects>"
        '__new__': None, # (!) real value is '<built-in method __new__ of type object at 0x00007FFDC68DEB70>'
        'allObjectsValid': None, # (!) real value is "<method 'allObjectsValid' of 'panda3d.direct.DCFile' objects>"
        'all_objects_valid': None, # (!) real value is "<method 'all_objects_valid' of 'panda3d.direct.DCFile' objects>"
        'clear': None, # (!) real value is "<method 'clear' of 'panda3d.direct.DCFile' objects>"
        'getClass': None, # (!) real value is "<method 'getClass' of 'panda3d.direct.DCFile' objects>"
        'getClassByName': None, # (!) real value is "<method 'getClassByName' of 'panda3d.direct.DCFile' objects>"
        'getFieldByIndex': None, # (!) real value is "<method 'getFieldByIndex' of 'panda3d.direct.DCFile' objects>"
        'getHash': None, # (!) real value is "<method 'getHash' of 'panda3d.direct.DCFile' objects>"
        'getImportModule': None, # (!) real value is "<method 'getImportModule' of 'panda3d.direct.DCFile' objects>"
        'getImportSymbol': None, # (!) real value is "<method 'getImportSymbol' of 'panda3d.direct.DCFile' objects>"
        'getKeyword': None, # (!) real value is "<method 'getKeyword' of 'panda3d.direct.DCFile' objects>"
        'getKeywordByName': None, # (!) real value is "<method 'getKeywordByName' of 'panda3d.direct.DCFile' objects>"
        'getNumClasses': None, # (!) real value is "<method 'getNumClasses' of 'panda3d.direct.DCFile' objects>"
        'getNumImportModules': None, # (!) real value is "<method 'getNumImportModules' of 'panda3d.direct.DCFile' objects>"
        'getNumImportSymbols': None, # (!) real value is "<method 'getNumImportSymbols' of 'panda3d.direct.DCFile' objects>"
        'getNumKeywords': None, # (!) real value is "<method 'getNumKeywords' of 'panda3d.direct.DCFile' objects>"
        'getNumTypedefs': None, # (!) real value is "<method 'getNumTypedefs' of 'panda3d.direct.DCFile' objects>"
        'getSwitchByName': None, # (!) real value is "<method 'getSwitchByName' of 'panda3d.direct.DCFile' objects>"
        'getTypedef': None, # (!) real value is "<method 'getTypedef' of 'panda3d.direct.DCFile' objects>"
        'getTypedefByName': None, # (!) real value is "<method 'getTypedefByName' of 'panda3d.direct.DCFile' objects>"
        'get_class': None, # (!) real value is "<method 'get_class' of 'panda3d.direct.DCFile' objects>"
        'get_class_by_name': None, # (!) real value is "<method 'get_class_by_name' of 'panda3d.direct.DCFile' objects>"
        'get_field_by_index': None, # (!) real value is "<method 'get_field_by_index' of 'panda3d.direct.DCFile' objects>"
        'get_hash': None, # (!) real value is "<method 'get_hash' of 'panda3d.direct.DCFile' objects>"
        'get_import_module': None, # (!) real value is "<method 'get_import_module' of 'panda3d.direct.DCFile' objects>"
        'get_import_symbol': None, # (!) real value is "<method 'get_import_symbol' of 'panda3d.direct.DCFile' objects>"
        'get_keyword': None, # (!) real value is "<method 'get_keyword' of 'panda3d.direct.DCFile' objects>"
        'get_keyword_by_name': None, # (!) real value is "<method 'get_keyword_by_name' of 'panda3d.direct.DCFile' objects>"
        'get_num_classes': None, # (!) real value is "<method 'get_num_classes' of 'panda3d.direct.DCFile' objects>"
        'get_num_import_modules': None, # (!) real value is "<method 'get_num_import_modules' of 'panda3d.direct.DCFile' objects>"
        'get_num_import_symbols': None, # (!) real value is "<method 'get_num_import_symbols' of 'panda3d.direct.DCFile' objects>"
        'get_num_keywords': None, # (!) real value is "<method 'get_num_keywords' of 'panda3d.direct.DCFile' objects>"
        'get_num_typedefs': None, # (!) real value is "<method 'get_num_typedefs' of 'panda3d.direct.DCFile' objects>"
        'get_switch_by_name': None, # (!) real value is "<method 'get_switch_by_name' of 'panda3d.direct.DCFile' objects>"
        'get_typedef': None, # (!) real value is "<method 'get_typedef' of 'panda3d.direct.DCFile' objects>"
        'get_typedef_by_name': None, # (!) real value is "<method 'get_typedef_by_name' of 'panda3d.direct.DCFile' objects>"
        'read': None, # (!) real value is "<method 'read' of 'panda3d.direct.DCFile' objects>"
        'readAll': None, # (!) real value is "<method 'readAll' of 'panda3d.direct.DCFile' objects>"
        'read_all': None, # (!) real value is "<method 'read_all' of 'panda3d.direct.DCFile' objects>"
        'write': None, # (!) real value is "<method 'write' of 'panda3d.direct.DCFile' objects>"
    }


