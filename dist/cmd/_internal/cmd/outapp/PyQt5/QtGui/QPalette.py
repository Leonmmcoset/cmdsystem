# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPalette(__sip.simplewrapper):
    """
    QPalette()
    QPalette(button: Union[QColor, Qt.GlobalColor])
    QPalette(button: Qt.GlobalColor)
    QPalette(button: Union[QColor, Qt.GlobalColor], background: Union[QColor, Qt.GlobalColor])
    QPalette(foreground: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], button: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], light: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], dark: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], mid: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], text: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], bright_text: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], base: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], background: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient])
    QPalette(palette: QPalette)
    QPalette(variant: Any)
    """
    def alternateBase(self): # real signature unknown; restored from __doc__
        """ alternateBase(self) -> QBrush """
        return QBrush

    def base(self): # real signature unknown; restored from __doc__
        """ base(self) -> QBrush """
        return QBrush

    def brightText(self): # real signature unknown; restored from __doc__
        """ brightText(self) -> QBrush """
        return QBrush

    def brush(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        brush(self, cg: QPalette.ColorGroup, cr: QPalette.ColorRole) -> QBrush
        brush(self, cr: QPalette.ColorRole) -> QBrush
        """
        return QBrush

    def button(self): # real signature unknown; restored from __doc__
        """ button(self) -> QBrush """
        return QBrush

    def buttonText(self): # real signature unknown; restored from __doc__
        """ buttonText(self) -> QBrush """
        return QBrush

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def color(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        color(self, cg: QPalette.ColorGroup, cr: QPalette.ColorRole) -> QColor
        color(self, cr: QPalette.ColorRole) -> QColor
        """
        return QColor

    def currentColorGroup(self): # real signature unknown; restored from __doc__
        """ currentColorGroup(self) -> QPalette.ColorGroup """
        pass

    def dark(self): # real signature unknown; restored from __doc__
        """ dark(self) -> QBrush """
        return QBrush

    def highlight(self): # real signature unknown; restored from __doc__
        """ highlight(self) -> QBrush """
        return QBrush

    def highlightedText(self): # real signature unknown; restored from __doc__
        """ highlightedText(self) -> QBrush """
        return QBrush

    def isBrushSet(self, cg, cr): # real signature unknown; restored from __doc__
        """ isBrushSet(self, cg: QPalette.ColorGroup, cr: QPalette.ColorRole) -> bool """
        return False

    def isCopyOf(self, p): # real signature unknown; restored from __doc__
        """ isCopyOf(self, p: QPalette) -> bool """
        return False

    def isEqual(self, cr1, cr2): # real signature unknown; restored from __doc__
        """ isEqual(self, cr1: QPalette.ColorGroup, cr2: QPalette.ColorGroup) -> bool """
        return False

    def light(self): # real signature unknown; restored from __doc__
        """ light(self) -> QBrush """
        return QBrush

    def link(self): # real signature unknown; restored from __doc__
        """ link(self) -> QBrush """
        return QBrush

    def linkVisited(self): # real signature unknown; restored from __doc__
        """ linkVisited(self) -> QBrush """
        return QBrush

    def mid(self): # real signature unknown; restored from __doc__
        """ mid(self) -> QBrush """
        return QBrush

    def midlight(self): # real signature unknown; restored from __doc__
        """ midlight(self) -> QBrush """
        return QBrush

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ placeholderText(self) -> QBrush """
        return QBrush

    def resolve(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resolve(self, a0: QPalette) -> QPalette
        resolve(self) -> int
        resolve(self, mask: int)
        """
        return QPalette or 0

    def setBrush(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setBrush(self, cg: QPalette.ColorGroup, cr: QPalette.ColorRole, brush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient])
        setBrush(self, acr: QPalette.ColorRole, abrush: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient])
        """
        pass

    def setColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setColor(self, acg: QPalette.ColorGroup, acr: QPalette.ColorRole, acolor: Union[QColor, Qt.GlobalColor])
        setColor(self, acr: QPalette.ColorRole, acolor: Union[QColor, Qt.GlobalColor])
        """
        pass

    def setColorGroup(self, cr, foreground, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setColorGroup(self, cr: QPalette.ColorGroup, foreground: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], button: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], light: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], dark: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], mid: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], text: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], bright_text: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], base: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient], background: Union[QBrush, Union[QColor, Qt.GlobalColor], QGradient]) """
        pass

    def setCurrentColorGroup(self, cg): # real signature unknown; restored from __doc__
        """ setCurrentColorGroup(self, cg: QPalette.ColorGroup) """
        pass

    def shadow(self): # real signature unknown; restored from __doc__
        """ shadow(self) -> QBrush """
        return QBrush

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QPalette) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> QBrush """
        return QBrush

    def toolTipBase(self): # real signature unknown; restored from __doc__
        """ toolTipBase(self) -> QBrush """
        return QBrush

    def toolTipText(self): # real signature unknown; restored from __doc__
        """ toolTipText(self) -> QBrush """
        return QBrush

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> QBrush """
        return QBrush

    def windowText(self): # real signature unknown; restored from __doc__
        """ windowText(self) -> QBrush """
        return QBrush

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Active = 0
    All = 5
    AlternateBase = 16
    Background = 10
    Base = 9
    BrightText = 7
    Button = 1
    ButtonText = 8
    Current = 4
    Dark = 4
    Disabled = 1
    Foreground = 0
    Highlight = 12
    HighlightedText = 13
    Inactive = 2
    Light = 2
    Link = 14
    LinkVisited = 15
    Mid = 5
    Midlight = 3
    NColorGroups = 3
    NColorRoles = 21
    Normal = 0
    NoRole = 17
    PlaceholderText = 20
    Shadow = 11
    Text = 6
    ToolTipBase = 18
    ToolTipText = 19
    Window = 10
    WindowText = 0
    __hash__ = None


