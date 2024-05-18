# encoding: utf-8
# module fontTools.pens.momentsPen
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\fontTools\pens\momentsPen.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import fontTools.pens.basePen as __fontTools_pens_basePen


# Variables with simple values

COMPILED = True

# no functions
# classes

class BasePen(__fontTools_pens_basePen.DecomposingPen):
    """
    Base class for drawing pens. You must override _moveTo, _lineTo and
        _curveToOne. You may additionally override _closePath, _endPath,
        addComponent, addVarComponent, and/or _qCurveToOne. You should not
        override any other methods.
    """
    def closePath(self): # reliably restored by inspect
        # no doc
        pass

    def curveTo(self, *points): # reliably restored by inspect
        # no doc
        pass

    def endPath(self): # reliably restored by inspect
        # no doc
        pass

    def lineTo(self, pt): # reliably restored by inspect
        # no doc
        pass

    def moveTo(self, pt): # reliably restored by inspect
        # no doc
        pass

    def qCurveTo(self, *points): # reliably restored by inspect
        # no doc
        pass

    def _closePath(self): # reliably restored by inspect
        # no doc
        pass

    def _curveToOne(self, pt1, pt2, pt3): # reliably restored by inspect
        # no doc
        pass

    def _endPath(self): # reliably restored by inspect
        # no doc
        pass

    def _getCurrentPoint(self): # reliably restored by inspect
        """
        Return the current point. This is not part of the public
                interface, yet is useful for subclasses.
        """
        pass

    def _lineTo(self, pt): # reliably restored by inspect
        # no doc
        pass

    def _moveTo(self, pt): # reliably restored by inspect
        # no doc
        pass

    def _qCurveToOne(self, pt1, pt2): # reliably restored by inspect
        """
        This method implements the basic quadratic curve type. The
                default implementation delegates the work to the cubic curve
                function. Optionally override with a native implementation.
        """
        pass

    def __init__(self, glyphSet=None): # reliably restored by inspect
        # no doc
        pass


class MomentsPen(__fontTools_pens_basePen.BasePen):
    # no doc
    def _closePath(self): # real signature unknown; restored from __doc__
        """ MomentsPen._closePath(self) """
        pass

    def _curveToOne(self, p1, p2, p3): # real signature unknown; restored from __doc__
        """ MomentsPen._curveToOne(self, p1, p2, p3) """
        pass

    def _endPath(self): # real signature unknown; restored from __doc__
        """ MomentsPen._endPath(self) """
        pass

    def _lineTo(self, p1): # real signature unknown; restored from __doc__
        """ MomentsPen._lineTo(self, p1) """
        pass

    def _moveTo(self, p0): # real signature unknown; restored from __doc__
        """ MomentsPen._moveTo(self, p0) """
        pass

    def _qCurveToOne(self, p1, p2): # real signature unknown; restored from __doc__
        """ MomentsPen._qCurveToOne(self, p1, p2) """
        pass

    def __init__(self, glyphset=None): # real signature unknown; restored from __doc__
        """ MomentsPen.__init__(self, glyphset=None) """
        pass


class OpenContourError(__fontTools_pens_basePen.PenError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__all__ = [
    'MomentsPen',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020C2D9C6450>'

__spec__ = None # (!) real value is "ModuleSpec(name='fontTools.pens.momentsPen', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020C2D9C6450>, origin='C:\\\\Users\\\\leonm\\\\PycharmProjects\\\\leonsystem\\\\venv\\\\Lib\\\\site-packages\\\\fontTools\\\\pens\\\\momentsPen.cp311-win_amd64.pyd')"

__test__ = {}

