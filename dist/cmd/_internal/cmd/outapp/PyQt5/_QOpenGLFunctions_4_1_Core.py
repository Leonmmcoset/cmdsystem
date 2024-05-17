# encoding: utf-8
# module PyQt5._QOpenGLFunctions_4_1_Core
# from C:\Users\leonm\PycharmProjects\leonsystem\venv\Lib\site-packages\PyQt5\_QOpenGLFunctions_4_1_Core.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtGui as __PyQt5_QtGui


# no functions
# classes

class QOpenGLFunctions_4_1_Core(__PyQt5_QtGui.QAbstractOpenGLFunctions):
    """ QOpenGLFunctions_4_1_Core() """
    def glActiveShaderProgram(self, pipeline, program): # real signature unknown; restored from __doc__
        """ glActiveShaderProgram(self, pipeline: int, program: int) """
        pass

    def glActiveTexture(self, texture): # real signature unknown; restored from __doc__
        """ glActiveTexture(self, texture: int) """
        pass

    def glAttachShader(self, program, shader): # real signature unknown; restored from __doc__
        """ glAttachShader(self, program: int, shader: int) """
        pass

    def glBeginConditionalRender(self, id, mode): # real signature unknown; restored from __doc__
        """ glBeginConditionalRender(self, id: int, mode: int) """
        pass

    def glBeginQuery(self, target, id): # real signature unknown; restored from __doc__
        """ glBeginQuery(self, target: int, id: int) """
        pass

    def glBeginQueryIndexed(self, target, index, id): # real signature unknown; restored from __doc__
        """ glBeginQueryIndexed(self, target: int, index: int, id: int) """
        pass

    def glBeginTransformFeedback(self, primitiveMode): # real signature unknown; restored from __doc__
        """ glBeginTransformFeedback(self, primitiveMode: int) """
        pass

    def glBindAttribLocation(self, program, index, name, p_str=None): # real signature unknown; restored from __doc__
        """ glBindAttribLocation(self, program: int, index: int, name: Optional[str]) """
        pass

    def glBindBuffer(self, target, buffer): # real signature unknown; restored from __doc__
        """ glBindBuffer(self, target: int, buffer: int) """
        pass

    def glBindBufferBase(self, target, index, buffer): # real signature unknown; restored from __doc__
        """ glBindBufferBase(self, target: int, index: int, buffer: int) """
        pass

    def glBindFramebuffer(self, target, framebuffer): # real signature unknown; restored from __doc__
        """ glBindFramebuffer(self, target: int, framebuffer: int) """
        pass

    def glBindProgramPipeline(self, pipeline): # real signature unknown; restored from __doc__
        """ glBindProgramPipeline(self, pipeline: int) """
        pass

    def glBindRenderbuffer(self, target, renderbuffer): # real signature unknown; restored from __doc__
        """ glBindRenderbuffer(self, target: int, renderbuffer: int) """
        pass

    def glBindSampler(self, unit, sampler): # real signature unknown; restored from __doc__
        """ glBindSampler(self, unit: int, sampler: int) """
        pass

    def glBindTexture(self, target, texture): # real signature unknown; restored from __doc__
        """ glBindTexture(self, target: int, texture: int) """
        pass

    def glBindTransformFeedback(self, target, id): # real signature unknown; restored from __doc__
        """ glBindTransformFeedback(self, target: int, id: int) """
        pass

    def glBindVertexArray(self, array): # real signature unknown; restored from __doc__
        """ glBindVertexArray(self, array: int) """
        pass

    def glBlendColor(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ glBlendColor(self, red: float, green: float, blue: float, alpha: float) """
        pass

    def glBlendEquation(self, mode): # real signature unknown; restored from __doc__
        """ glBlendEquation(self, mode: int) """
        pass

    def glBlendEquationi(self, buf, mode): # real signature unknown; restored from __doc__
        """ glBlendEquationi(self, buf: int, mode: int) """
        pass

    def glBlendEquationSeparate(self, modeRGB, modeAlpha): # real signature unknown; restored from __doc__
        """ glBlendEquationSeparate(self, modeRGB: int, modeAlpha: int) """
        pass

    def glBlendEquationSeparatei(self, buf, modeRGB, modeAlpha): # real signature unknown; restored from __doc__
        """ glBlendEquationSeparatei(self, buf: int, modeRGB: int, modeAlpha: int) """
        pass

    def glBlendFunc(self, sfactor, dfactor): # real signature unknown; restored from __doc__
        """ glBlendFunc(self, sfactor: int, dfactor: int) """
        pass

    def glBlendFunci(self, buf, src, dst): # real signature unknown; restored from __doc__
        """ glBlendFunci(self, buf: int, src: int, dst: int) """
        pass

    def glBlendFuncSeparate(self, sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha): # real signature unknown; restored from __doc__
        """ glBlendFuncSeparate(self, sfactorRGB: int, dfactorRGB: int, sfactorAlpha: int, dfactorAlpha: int) """
        pass

    def glBlendFuncSeparatei(self, buf, srcRGB, dstRGB, srcAlpha, dstAlpha): # real signature unknown; restored from __doc__
        """ glBlendFuncSeparatei(self, buf: int, srcRGB: int, dstRGB: int, srcAlpha: int, dstAlpha: int) """
        pass

    def glBlitFramebuffer(self, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter): # real signature unknown; restored from __doc__
        """ glBlitFramebuffer(self, srcX0: int, srcY0: int, srcX1: int, srcY1: int, dstX0: int, dstY0: int, dstX1: int, dstY1: int, mask: int, filter: int) """
        pass

    def glBufferData(self, target, size, data, usage): # real signature unknown; restored from __doc__
        """ glBufferData(self, target: int, size: int, data: PYQT_OPENGL_ARRAY, usage: int) """
        pass

    def glBufferSubData(self, target, offset, size, data): # real signature unknown; restored from __doc__
        """ glBufferSubData(self, target: int, offset: int, size: int, data: PYQT_OPENGL_ARRAY) """
        pass

    def glCheckFramebufferStatus(self, target): # real signature unknown; restored from __doc__
        """ glCheckFramebufferStatus(self, target: int) -> int """
        return 0

    def glClampColor(self, target, clamp): # real signature unknown; restored from __doc__
        """ glClampColor(self, target: int, clamp: int) """
        pass

    def glClear(self, mask): # real signature unknown; restored from __doc__
        """ glClear(self, mask: int) """
        pass

    def glClearBufferfi(self, buffer, drawbuffer, depth, stencil): # real signature unknown; restored from __doc__
        """ glClearBufferfi(self, buffer: int, drawbuffer: int, depth: float, stencil: int) """
        pass

    def glClearColor(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ glClearColor(self, red: float, green: float, blue: float, alpha: float) """
        pass

    def glClearDepth(self, depth): # real signature unknown; restored from __doc__
        """ glClearDepth(self, depth: float) """
        pass

    def glClearDepthf(self, dd): # real signature unknown; restored from __doc__
        """ glClearDepthf(self, dd: float) """
        pass

    def glClearStencil(self, s): # real signature unknown; restored from __doc__
        """ glClearStencil(self, s: int) """
        pass

    def glColorMask(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ glColorMask(self, red: int, green: int, blue: int, alpha: int) """
        pass

    def glColorMaski(self, index, r, g, b, a): # real signature unknown; restored from __doc__
        """ glColorMaski(self, index: int, r: int, g: int, b: int, a: int) """
        pass

    def glColorP3ui(self, type, color): # real signature unknown; restored from __doc__
        """ glColorP3ui(self, type: int, color: int) """
        pass

    def glColorP4ui(self, type, color): # real signature unknown; restored from __doc__
        """ glColorP4ui(self, type: int, color: int) """
        pass

    def glCompileShader(self, shader): # real signature unknown; restored from __doc__
        """ glCompileShader(self, shader: int) """
        pass

    def glCompressedTexImage1D(self, target, level, internalformat, width, border, imageSize, data): # real signature unknown; restored from __doc__
        """ glCompressedTexImage1D(self, target: int, level: int, internalformat: int, width: int, border: int, imageSize: int, data: PYQT_OPENGL_ARRAY) """
        pass

    def glCompressedTexImage2D(self, target, level, internalformat, width, height, border, imageSize, data): # real signature unknown; restored from __doc__
        """ glCompressedTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, imageSize: int, data: PYQT_OPENGL_ARRAY) """
        pass

    def glCompressedTexImage3D(self, target, level, internalformat, width, height, depth, border, imageSize, data): # real signature unknown; restored from __doc__
        """ glCompressedTexImage3D(self, target: int, level: int, internalformat: int, width: int, height: int, depth: int, border: int, imageSize: int, data: PYQT_OPENGL_ARRAY) """
        pass

    def glCompressedTexSubImage1D(self, target, level, xoffset, width, format, imageSize, data): # real signature unknown; restored from __doc__
        """ glCompressedTexSubImage1D(self, target: int, level: int, xoffset: int, width: int, format: int, imageSize: int, data: PYQT_OPENGL_ARRAY) """
        pass

    def glCompressedTexSubImage2D(self, target, level, xoffset, yoffset, width, height, format, imageSize, data): # real signature unknown; restored from __doc__
        """ glCompressedTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, imageSize: int, data: PYQT_OPENGL_ARRAY) """
        pass

    def glCompressedTexSubImage3D(self, target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data): # real signature unknown; restored from __doc__
        """ glCompressedTexSubImage3D(self, target: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int, format: int, imageSize: int, data: PYQT_OPENGL_ARRAY) """
        pass

    def glCopyTexImage1D(self, target, level, internalformat, x, y, width, border): # real signature unknown; restored from __doc__
        """ glCopyTexImage1D(self, target: int, level: int, internalformat: int, x: int, y: int, width: int, border: int) """
        pass

    def glCopyTexImage2D(self, target, level, internalformat, x, y, width, height, border): # real signature unknown; restored from __doc__
        """ glCopyTexImage2D(self, target: int, level: int, internalformat: int, x: int, y: int, width: int, height: int, border: int) """
        pass

    def glCopyTexSubImage1D(self, target, level, xoffset, x, y, width): # real signature unknown; restored from __doc__
        """ glCopyTexSubImage1D(self, target: int, level: int, xoffset: int, x: int, y: int, width: int) """
        pass

    def glCopyTexSubImage2D(self, target, level, xoffset, yoffset, x, y, width, height): # real signature unknown; restored from __doc__
        """ glCopyTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, x: int, y: int, width: int, height: int) """
        pass

    def glCopyTexSubImage3D(self, target, level, xoffset, yoffset, zoffset, x, y, width, height): # real signature unknown; restored from __doc__
        """ glCopyTexSubImage3D(self, target: int, level: int, xoffset: int, yoffset: int, zoffset: int, x: int, y: int, width: int, height: int) """
        pass

    def glCreateProgram(self): # real signature unknown; restored from __doc__
        """ glCreateProgram(self) -> int """
        return 0

    def glCreateShader(self, type): # real signature unknown; restored from __doc__
        """ glCreateShader(self, type: int) -> int """
        return 0

    def glCullFace(self, mode): # real signature unknown; restored from __doc__
        """ glCullFace(self, mode: int) """
        pass

    def glDeleteBuffers(self, n, buffers): # real signature unknown; restored from __doc__
        """ glDeleteBuffers(self, n: int, buffers: PYQT_OPENGL_ARRAY) """
        pass

    def glDeleteProgram(self, program): # real signature unknown; restored from __doc__
        """ glDeleteProgram(self, program: int) """
        pass

    def glDeleteQueries(self, n, ids): # real signature unknown; restored from __doc__
        """ glDeleteQueries(self, n: int, ids: PYQT_OPENGL_ARRAY) """
        pass

    def glDeleteShader(self, shader): # real signature unknown; restored from __doc__
        """ glDeleteShader(self, shader: int) """
        pass

    def glDeleteTextures(self, n, textures): # real signature unknown; restored from __doc__
        """ glDeleteTextures(self, n: int, textures: PYQT_OPENGL_ARRAY) """
        pass

    def glDepthFunc(self, func): # real signature unknown; restored from __doc__
        """ glDepthFunc(self, func: int) """
        pass

    def glDepthMask(self, flag): # real signature unknown; restored from __doc__
        """ glDepthMask(self, flag: int) """
        pass

    def glDepthRange(self, nearVal, farVal): # real signature unknown; restored from __doc__
        """ glDepthRange(self, nearVal: float, farVal: float) """
        pass

    def glDepthRangef(self, n, f): # real signature unknown; restored from __doc__
        """ glDepthRangef(self, n: float, f: float) """
        pass

    def glDepthRangeIndexed(self, index, n, f): # real signature unknown; restored from __doc__
        """ glDepthRangeIndexed(self, index: int, n: float, f: float) """
        pass

    def glDetachShader(self, program, shader): # real signature unknown; restored from __doc__
        """ glDetachShader(self, program: int, shader: int) """
        pass

    def glDisable(self, cap): # real signature unknown; restored from __doc__
        """ glDisable(self, cap: int) """
        pass

    def glDisablei(self, target, index): # real signature unknown; restored from __doc__
        """ glDisablei(self, target: int, index: int) """
        pass

    def glDisableVertexAttribArray(self, index): # real signature unknown; restored from __doc__
        """ glDisableVertexAttribArray(self, index: int) """
        pass

    def glDrawArrays(self, mode, first, count): # real signature unknown; restored from __doc__
        """ glDrawArrays(self, mode: int, first: int, count: int) """
        pass

    def glDrawArraysInstanced(self, mode, first, count, instancecount): # real signature unknown; restored from __doc__
        """ glDrawArraysInstanced(self, mode: int, first: int, count: int, instancecount: int) """
        pass

    def glDrawBuffer(self, mode): # real signature unknown; restored from __doc__
        """ glDrawBuffer(self, mode: int) """
        pass

    def glDrawBuffers(self, n, bufs): # real signature unknown; restored from __doc__
        """ glDrawBuffers(self, n: int, bufs: PYQT_OPENGL_ARRAY) """
        pass

    def glDrawElements(self, mode, count, type, indices): # real signature unknown; restored from __doc__
        """ glDrawElements(self, mode: int, count: int, type: int, indices: PYQT_OPENGL_ARRAY) """
        pass

    def glDrawRangeElements(self, mode, start, end, count, type, indices): # real signature unknown; restored from __doc__
        """ glDrawRangeElements(self, mode: int, start: int, end: int, count: int, type: int, indices: PYQT_OPENGL_ARRAY) """
        pass

    def glDrawTransformFeedback(self, mode, id): # real signature unknown; restored from __doc__
        """ glDrawTransformFeedback(self, mode: int, id: int) """
        pass

    def glDrawTransformFeedbackStream(self, mode, id, stream): # real signature unknown; restored from __doc__
        """ glDrawTransformFeedbackStream(self, mode: int, id: int, stream: int) """
        pass

    def glEnable(self, cap): # real signature unknown; restored from __doc__
        """ glEnable(self, cap: int) """
        pass

    def glEnablei(self, target, index): # real signature unknown; restored from __doc__
        """ glEnablei(self, target: int, index: int) """
        pass

    def glEnableVertexAttribArray(self, index): # real signature unknown; restored from __doc__
        """ glEnableVertexAttribArray(self, index: int) """
        pass

    def glEndConditionalRender(self): # real signature unknown; restored from __doc__
        """ glEndConditionalRender(self) """
        pass

    def glEndQuery(self, target): # real signature unknown; restored from __doc__
        """ glEndQuery(self, target: int) """
        pass

    def glEndQueryIndexed(self, target, index): # real signature unknown; restored from __doc__
        """ glEndQueryIndexed(self, target: int, index: int) """
        pass

    def glEndTransformFeedback(self): # real signature unknown; restored from __doc__
        """ glEndTransformFeedback(self) """
        pass

    def glFinish(self): # real signature unknown; restored from __doc__
        """ glFinish(self) """
        pass

    def glFlush(self): # real signature unknown; restored from __doc__
        """ glFlush(self) """
        pass

    def glFramebufferRenderbuffer(self, target, attachment, renderbuffertarget, renderbuffer): # real signature unknown; restored from __doc__
        """ glFramebufferRenderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int) """
        pass

    def glFramebufferTexture(self, target, attachment, texture, level): # real signature unknown; restored from __doc__
        """ glFramebufferTexture(self, target: int, attachment: int, texture: int, level: int) """
        pass

    def glFramebufferTexture1D(self, target, attachment, textarget, texture, level): # real signature unknown; restored from __doc__
        """ glFramebufferTexture1D(self, target: int, attachment: int, textarget: int, texture: int, level: int) """
        pass

    def glFramebufferTexture2D(self, target, attachment, textarget, texture, level): # real signature unknown; restored from __doc__
        """ glFramebufferTexture2D(self, target: int, attachment: int, textarget: int, texture: int, level: int) """
        pass

    def glFramebufferTexture3D(self, target, attachment, textarget, texture, level, zoffset): # real signature unknown; restored from __doc__
        """ glFramebufferTexture3D(self, target: int, attachment: int, textarget: int, texture: int, level: int, zoffset: int) """
        pass

    def glFramebufferTextureLayer(self, target, attachment, texture, level, layer): # real signature unknown; restored from __doc__
        """ glFramebufferTextureLayer(self, target: int, attachment: int, texture: int, level: int, layer: int) """
        pass

    def glFrontFace(self, mode): # real signature unknown; restored from __doc__
        """ glFrontFace(self, mode: int) """
        pass

    def glGenBuffers(self, n): # real signature unknown; restored from __doc__
        """ glGenBuffers(self, n: int) -> Optional[Union[int, Tuple[int, ...]]] """
        pass

    def glGenerateMipmap(self, target): # real signature unknown; restored from __doc__
        """ glGenerateMipmap(self, target: int) """
        pass

    def glGenQueries(self, n): # real signature unknown; restored from __doc__
        """ glGenQueries(self, n: int) -> Optional[Union[int, Tuple[int, ...]]] """
        pass

    def glGenTextures(self, n): # real signature unknown; restored from __doc__
        """ glGenTextures(self, n: int) -> Optional[Union[int, Tuple[int, ...]]] """
        pass

    def glGetActiveAttrib(self, program, index): # real signature unknown; restored from __doc__
        """ glGetActiveAttrib(self, program: int, index: int) -> Tuple[str, int, int] """
        pass

    def glGetActiveUniform(self, program, index): # real signature unknown; restored from __doc__
        """ glGetActiveUniform(self, program: int, index: int) -> Tuple[str, int, int] """
        pass

    def glGetAttachedShaders(self, program): # real signature unknown; restored from __doc__
        """ glGetAttachedShaders(self, program: int) -> Tuple[int, ...] """
        pass

    def glGetAttribLocation(self, program, name, p_str=None): # real signature unknown; restored from __doc__
        """ glGetAttribLocation(self, program: int, name: Optional[str]) -> int """
        return 0

    def glGetBooleanv(self, pname): # real signature unknown; restored from __doc__
        """ glGetBooleanv(self, pname: int) -> Optional[Union[bool, Tuple[bool, ...]]] """
        pass

    def glGetBufferParameteriv(self, target, pname): # real signature unknown; restored from __doc__
        """ glGetBufferParameteriv(self, target: int, pname: int) -> Optional[int] """
        pass

    def glGetDoublev(self, pname): # real signature unknown; restored from __doc__
        """ glGetDoublev(self, pname: int) -> Optional[Union[float, Tuple[float, ...]]] """
        pass

    def glGetError(self): # real signature unknown; restored from __doc__
        """ glGetError(self) -> int """
        return 0

    def glGetFloatv(self, pname): # real signature unknown; restored from __doc__
        """ glGetFloatv(self, pname: int) -> Optional[Union[float, Tuple[float, ...]]] """
        pass

    def glGetIntegerv(self, pname): # real signature unknown; restored from __doc__
        """ glGetIntegerv(self, pname: int) -> Optional[Union[int, Tuple[int, ...]]] """
        pass

    def glGetProgramInfoLog(self, program): # real signature unknown; restored from __doc__
        """ glGetProgramInfoLog(self, program: int) -> bytes """
        return b""

    def glGetProgramiv(self, program, pname): # real signature unknown; restored from __doc__
        """ glGetProgramiv(self, program: int, pname: int) -> Optional[Union[int, Tuple[int, int, int]]] """
        pass

    def glGetQueryiv(self, target, pname): # real signature unknown; restored from __doc__
        """ glGetQueryiv(self, target: int, pname: int) -> Optional[int] """
        pass

    def glGetShaderInfoLog(self, shader): # real signature unknown; restored from __doc__
        """ glGetShaderInfoLog(self, shader: int) -> bytes """
        return b""

    def glGetShaderiv(self, shader, pname): # real signature unknown; restored from __doc__
        """ glGetShaderiv(self, shader: int, pname: int) -> Optional[int] """
        pass

    def glGetShaderSource(self, shader): # real signature unknown; restored from __doc__
        """ glGetShaderSource(self, shader: int) -> bytes """
        return b""

    def glGetString(self, name): # real signature unknown; restored from __doc__
        """ glGetString(self, name: int) -> Optional[str] """
        pass

    def glGetTexLevelParameterfv(self, target, level, pname): # real signature unknown; restored from __doc__
        """ glGetTexLevelParameterfv(self, target: int, level: int, pname: int) -> Optional[float] """
        pass

    def glGetTexLevelParameteriv(self, target, level, pname): # real signature unknown; restored from __doc__
        """ glGetTexLevelParameteriv(self, target: int, level: int, pname: int) -> Optional[int] """
        pass

    def glGetTexParameterfv(self, target, pname): # real signature unknown; restored from __doc__
        """ glGetTexParameterfv(self, target: int, pname: int) -> Optional[Union[float, Tuple[float, float, float, float]]] """
        pass

    def glGetTexParameteriv(self, target, pname): # real signature unknown; restored from __doc__
        """ glGetTexParameteriv(self, target: int, pname: int) -> Optional[Union[int, Tuple[int, int, int, int]]] """
        pass

    def glGetUniformLocation(self, program, name, p_str=None): # real signature unknown; restored from __doc__
        """ glGetUniformLocation(self, program: int, name: Optional[str]) -> int """
        return 0

    def glGetVertexAttribdv(self, index, pname): # real signature unknown; restored from __doc__
        """ glGetVertexAttribdv(self, index: int, pname: int) -> Optional[Union[float, Tuple[float, float, float, float]]] """
        pass

    def glGetVertexAttribfv(self, index, pname): # real signature unknown; restored from __doc__
        """ glGetVertexAttribfv(self, index: int, pname: int) -> Optional[Union[float, Tuple[float, float, float, float]]] """
        pass

    def glGetVertexAttribiv(self, index, pname): # real signature unknown; restored from __doc__
        """ glGetVertexAttribiv(self, index: int, pname: int) -> Optional[Union[int, Tuple[int, int, int, int]]] """
        pass

    def glHint(self, target, mode): # real signature unknown; restored from __doc__
        """ glHint(self, target: int, mode: int) """
        pass

    def glIndexub(self, c): # real signature unknown; restored from __doc__
        """ glIndexub(self, c: int) """
        pass

    def glIndexubv(self, c): # real signature unknown; restored from __doc__
        """ glIndexubv(self, c: PYQT_OPENGL_ARRAY) """
        pass

    def glIsBuffer(self, buffer): # real signature unknown; restored from __doc__
        """ glIsBuffer(self, buffer: int) -> int """
        return 0

    def glIsEnabled(self, cap): # real signature unknown; restored from __doc__
        """ glIsEnabled(self, cap: int) -> int """
        return 0

    def glIsEnabledi(self, target, index): # real signature unknown; restored from __doc__
        """ glIsEnabledi(self, target: int, index: int) -> int """
        return 0

    def glIsFramebuffer(self, framebuffer): # real signature unknown; restored from __doc__
        """ glIsFramebuffer(self, framebuffer: int) -> int """
        return 0

    def glIsProgram(self, program): # real signature unknown; restored from __doc__
        """ glIsProgram(self, program: int) -> int """
        return 0

    def glIsProgramPipeline(self, pipeline): # real signature unknown; restored from __doc__
        """ glIsProgramPipeline(self, pipeline: int) -> int """
        return 0

    def glIsQuery(self, id): # real signature unknown; restored from __doc__
        """ glIsQuery(self, id: int) -> int """
        return 0

    def glIsRenderbuffer(self, renderbuffer): # real signature unknown; restored from __doc__
        """ glIsRenderbuffer(self, renderbuffer: int) -> int """
        return 0

    def glIsSampler(self, sampler): # real signature unknown; restored from __doc__
        """ glIsSampler(self, sampler: int) -> int """
        return 0

    def glIsShader(self, shader): # real signature unknown; restored from __doc__
        """ glIsShader(self, shader: int) -> int """
        return 0

    def glIsTexture(self, texture): # real signature unknown; restored from __doc__
        """ glIsTexture(self, texture: int) -> int """
        return 0

    def glIsTransformFeedback(self, id): # real signature unknown; restored from __doc__
        """ glIsTransformFeedback(self, id: int) -> int """
        return 0

    def glIsVertexArray(self, array): # real signature unknown; restored from __doc__
        """ glIsVertexArray(self, array: int) -> int """
        return 0

    def glLineWidth(self, width): # real signature unknown; restored from __doc__
        """ glLineWidth(self, width: float) """
        pass

    def glLinkProgram(self, program): # real signature unknown; restored from __doc__
        """ glLinkProgram(self, program: int) """
        pass

    def glLogicOp(self, opcode): # real signature unknown; restored from __doc__
        """ glLogicOp(self, opcode: int) """
        pass

    def glMinSampleShading(self, value): # real signature unknown; restored from __doc__
        """ glMinSampleShading(self, value: float) """
        pass

    def glMultiTexCoordP1ui(self, texture, type, coords): # real signature unknown; restored from __doc__
        """ glMultiTexCoordP1ui(self, texture: int, type: int, coords: int) """
        pass

    def glMultiTexCoordP2ui(self, texture, type, coords): # real signature unknown; restored from __doc__
        """ glMultiTexCoordP2ui(self, texture: int, type: int, coords: int) """
        pass

    def glMultiTexCoordP3ui(self, texture, type, coords): # real signature unknown; restored from __doc__
        """ glMultiTexCoordP3ui(self, texture: int, type: int, coords: int) """
        pass

    def glMultiTexCoordP4ui(self, texture, type, coords): # real signature unknown; restored from __doc__
        """ glMultiTexCoordP4ui(self, texture: int, type: int, coords: int) """
        pass

    def glNormalP3ui(self, type, coords): # real signature unknown; restored from __doc__
        """ glNormalP3ui(self, type: int, coords: int) """
        pass

    def glPatchParameteri(self, pname, value): # real signature unknown; restored from __doc__
        """ glPatchParameteri(self, pname: int, value: int) """
        pass

    def glPauseTransformFeedback(self): # real signature unknown; restored from __doc__
        """ glPauseTransformFeedback(self) """
        pass

    def glPixelStoref(self, pname, param): # real signature unknown; restored from __doc__
        """ glPixelStoref(self, pname: int, param: float) """
        pass

    def glPixelStorei(self, pname, param): # real signature unknown; restored from __doc__
        """ glPixelStorei(self, pname: int, param: int) """
        pass

    def glPointParameterf(self, pname, param): # real signature unknown; restored from __doc__
        """ glPointParameterf(self, pname: int, param: float) """
        pass

    def glPointParameterfv(self, pname, params): # real signature unknown; restored from __doc__
        """ glPointParameterfv(self, pname: int, params: PYQT_OPENGL_ARRAY) """
        pass

    def glPointParameteri(self, pname, param): # real signature unknown; restored from __doc__
        """ glPointParameteri(self, pname: int, param: int) """
        pass

    def glPointParameteriv(self, pname, params): # real signature unknown; restored from __doc__
        """ glPointParameteriv(self, pname: int, params: PYQT_OPENGL_ARRAY) """
        pass

    def glPointSize(self, size): # real signature unknown; restored from __doc__
        """ glPointSize(self, size: float) """
        pass

    def glPolygonMode(self, face, mode): # real signature unknown; restored from __doc__
        """ glPolygonMode(self, face: int, mode: int) """
        pass

    def glPolygonOffset(self, factor, units): # real signature unknown; restored from __doc__
        """ glPolygonOffset(self, factor: float, units: float) """
        pass

    def glPrimitiveRestartIndex(self, index): # real signature unknown; restored from __doc__
        """ glPrimitiveRestartIndex(self, index: int) """
        pass

    def glProgramParameteri(self, program, pname, value): # real signature unknown; restored from __doc__
        """ glProgramParameteri(self, program: int, pname: int, value: int) """
        pass

    def glProgramUniform1d(self, program, location, v0): # real signature unknown; restored from __doc__
        """ glProgramUniform1d(self, program: int, location: int, v0: float) """
        pass

    def glProgramUniform1f(self, program, location, v0): # real signature unknown; restored from __doc__
        """ glProgramUniform1f(self, program: int, location: int, v0: float) """
        pass

    def glProgramUniform1i(self, program, location, v0): # real signature unknown; restored from __doc__
        """ glProgramUniform1i(self, program: int, location: int, v0: int) """
        pass

    def glProgramUniform1ui(self, program, location, v0): # real signature unknown; restored from __doc__
        """ glProgramUniform1ui(self, program: int, location: int, v0: int) """
        pass

    def glProgramUniform2d(self, program, location, v0, v1): # real signature unknown; restored from __doc__
        """ glProgramUniform2d(self, program: int, location: int, v0: float, v1: float) """
        pass

    def glProgramUniform2f(self, program, location, v0, v1): # real signature unknown; restored from __doc__
        """ glProgramUniform2f(self, program: int, location: int, v0: float, v1: float) """
        pass

    def glProgramUniform2i(self, program, location, v0, v1): # real signature unknown; restored from __doc__
        """ glProgramUniform2i(self, program: int, location: int, v0: int, v1: int) """
        pass

    def glProgramUniform2ui(self, program, location, v0, v1): # real signature unknown; restored from __doc__
        """ glProgramUniform2ui(self, program: int, location: int, v0: int, v1: int) """
        pass

    def glProgramUniform3d(self, program, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glProgramUniform3d(self, program: int, location: int, v0: float, v1: float, v2: float) """
        pass

    def glProgramUniform3f(self, program, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glProgramUniform3f(self, program: int, location: int, v0: float, v1: float, v2: float) """
        pass

    def glProgramUniform3i(self, program, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glProgramUniform3i(self, program: int, location: int, v0: int, v1: int, v2: int) """
        pass

    def glProgramUniform3ui(self, program, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glProgramUniform3ui(self, program: int, location: int, v0: int, v1: int, v2: int) """
        pass

    def glProgramUniform4d(self, program, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glProgramUniform4d(self, program: int, location: int, v0: float, v1: float, v2: float, v3: float) """
        pass

    def glProgramUniform4f(self, program, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glProgramUniform4f(self, program: int, location: int, v0: float, v1: float, v2: float, v3: float) """
        pass

    def glProgramUniform4i(self, program, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glProgramUniform4i(self, program: int, location: int, v0: int, v1: int, v2: int, v3: int) """
        pass

    def glProgramUniform4ui(self, program, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glProgramUniform4ui(self, program: int, location: int, v0: int, v1: int, v2: int, v3: int) """
        pass

    def glProvokingVertex(self, mode): # real signature unknown; restored from __doc__
        """ glProvokingVertex(self, mode: int) """
        pass

    def glQueryCounter(self, id, target): # real signature unknown; restored from __doc__
        """ glQueryCounter(self, id: int, target: int) """
        pass

    def glReadBuffer(self, mode): # real signature unknown; restored from __doc__
        """ glReadBuffer(self, mode: int) """
        pass

    def glReadPixels(self, x, y, width, height, format, type): # real signature unknown; restored from __doc__
        """ glReadPixels(self, x: int, y: int, width: int, height: int, format: int, type: int) -> Union[Tuple[float, ...], Tuple[int, ...]] """
        pass

    def glReleaseShaderCompiler(self): # real signature unknown; restored from __doc__
        """ glReleaseShaderCompiler(self) """
        pass

    def glRenderbufferStorage(self, target, internalformat, width, height): # real signature unknown; restored from __doc__
        """ glRenderbufferStorage(self, target: int, internalformat: int, width: int, height: int) """
        pass

    def glRenderbufferStorageMultisample(self, target, samples, internalformat, width, height): # real signature unknown; restored from __doc__
        """ glRenderbufferStorageMultisample(self, target: int, samples: int, internalformat: int, width: int, height: int) """
        pass

    def glResumeTransformFeedback(self): # real signature unknown; restored from __doc__
        """ glResumeTransformFeedback(self) """
        pass

    def glSampleCoverage(self, value, invert): # real signature unknown; restored from __doc__
        """ glSampleCoverage(self, value: float, invert: int) """
        pass

    def glSampleMaski(self, index, mask): # real signature unknown; restored from __doc__
        """ glSampleMaski(self, index: int, mask: int) """
        pass

    def glSamplerParameterf(self, sampler, pname, param): # real signature unknown; restored from __doc__
        """ glSamplerParameterf(self, sampler: int, pname: int, param: float) """
        pass

    def glSamplerParameteri(self, sampler, pname, param): # real signature unknown; restored from __doc__
        """ glSamplerParameteri(self, sampler: int, pname: int, param: int) """
        pass

    def glScissor(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ glScissor(self, x: int, y: int, width: int, height: int) """
        pass

    def glScissorIndexed(self, index, left, bottom, width, height): # real signature unknown; restored from __doc__
        """ glScissorIndexed(self, index: int, left: int, bottom: int, width: int, height: int) """
        pass

    def glSecondaryColorP3ui(self, type, color): # real signature unknown; restored from __doc__
        """ glSecondaryColorP3ui(self, type: int, color: int) """
        pass

    def glStencilFunc(self, func, ref, mask): # real signature unknown; restored from __doc__
        """ glStencilFunc(self, func: int, ref: int, mask: int) """
        pass

    def glStencilFuncSeparate(self, face, func, ref, mask): # real signature unknown; restored from __doc__
        """ glStencilFuncSeparate(self, face: int, func: int, ref: int, mask: int) """
        pass

    def glStencilMask(self, mask): # real signature unknown; restored from __doc__
        """ glStencilMask(self, mask: int) """
        pass

    def glStencilMaskSeparate(self, face, mask): # real signature unknown; restored from __doc__
        """ glStencilMaskSeparate(self, face: int, mask: int) """
        pass

    def glStencilOp(self, fail, zfail, zpass): # real signature unknown; restored from __doc__
        """ glStencilOp(self, fail: int, zfail: int, zpass: int) """
        pass

    def glStencilOpSeparate(self, face, sfail, dpfail, dppass): # real signature unknown; restored from __doc__
        """ glStencilOpSeparate(self, face: int, sfail: int, dpfail: int, dppass: int) """
        pass

    def glTexBuffer(self, target, internalformat, buffer): # real signature unknown; restored from __doc__
        """ glTexBuffer(self, target: int, internalformat: int, buffer: int) """
        pass

    def glTexCoordP1ui(self, type, coords): # real signature unknown; restored from __doc__
        """ glTexCoordP1ui(self, type: int, coords: int) """
        pass

    def glTexCoordP2ui(self, type, coords): # real signature unknown; restored from __doc__
        """ glTexCoordP2ui(self, type: int, coords: int) """
        pass

    def glTexCoordP3ui(self, type, coords): # real signature unknown; restored from __doc__
        """ glTexCoordP3ui(self, type: int, coords: int) """
        pass

    def glTexCoordP4ui(self, type, coords): # real signature unknown; restored from __doc__
        """ glTexCoordP4ui(self, type: int, coords: int) """
        pass

    def glTexImage1D(self, target, level, internalformat, width, border, format, type, pixels): # real signature unknown; restored from __doc__
        """ glTexImage1D(self, target: int, level: int, internalformat: int, width: int, border: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) """
        pass

    def glTexImage2D(self, target, level, internalformat, width, height, border, format, type, pixels): # real signature unknown; restored from __doc__
        """ glTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) """
        pass

    def glTexImage2DMultisample(self, target, samples, internalformat, width, height, fixedsamplelocations): # real signature unknown; restored from __doc__
        """ glTexImage2DMultisample(self, target: int, samples: int, internalformat: int, width: int, height: int, fixedsamplelocations: int) """
        pass

    def glTexImage3D(self, target, level, internalformat, width, height, depth, border, format, type, pixels): # real signature unknown; restored from __doc__
        """ glTexImage3D(self, target: int, level: int, internalformat: int, width: int, height: int, depth: int, border: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) """
        pass

    def glTexImage3DMultisample(self, target, samples, internalformat, width, height, depth, fixedsamplelocations): # real signature unknown; restored from __doc__
        """ glTexImage3DMultisample(self, target: int, samples: int, internalformat: int, width: int, height: int, depth: int, fixedsamplelocations: int) """
        pass

    def glTexParameterf(self, target, pname, param): # real signature unknown; restored from __doc__
        """ glTexParameterf(self, target: int, pname: int, param: float) """
        pass

    def glTexParameterfv(self, target, pname, params): # real signature unknown; restored from __doc__
        """ glTexParameterfv(self, target: int, pname: int, params: PYQT_OPENGL_ARRAY) """
        pass

    def glTexParameteri(self, target, pname, param): # real signature unknown; restored from __doc__
        """ glTexParameteri(self, target: int, pname: int, param: int) """
        pass

    def glTexParameteriv(self, target, pname, params): # real signature unknown; restored from __doc__
        """ glTexParameteriv(self, target: int, pname: int, params: PYQT_OPENGL_ARRAY) """
        pass

    def glTexSubImage1D(self, target, level, xoffset, width, format, type, pixels): # real signature unknown; restored from __doc__
        """ glTexSubImage1D(self, target: int, level: int, xoffset: int, width: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) """
        pass

    def glTexSubImage2D(self, target, level, xoffset, yoffset, width, height, format, type, pixels): # real signature unknown; restored from __doc__
        """ glTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) """
        pass

    def glTexSubImage3D(self, target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels): # real signature unknown; restored from __doc__
        """ glTexSubImage3D(self, target: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) """
        pass

    def glUniform1d(self, location, x): # real signature unknown; restored from __doc__
        """ glUniform1d(self, location: int, x: float) """
        pass

    def glUniform1f(self, location, v0): # real signature unknown; restored from __doc__
        """ glUniform1f(self, location: int, v0: float) """
        pass

    def glUniform1fv(self, location, count, value): # real signature unknown; restored from __doc__
        """ glUniform1fv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUniform1i(self, location, v0): # real signature unknown; restored from __doc__
        """ glUniform1i(self, location: int, v0: int) """
        pass

    def glUniform1iv(self, location, count, value): # real signature unknown; restored from __doc__
        """ glUniform1iv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUniform1ui(self, location, v0): # real signature unknown; restored from __doc__
        """ glUniform1ui(self, location: int, v0: int) """
        pass

    def glUniform2d(self, location, x, y): # real signature unknown; restored from __doc__
        """ glUniform2d(self, location: int, x: float, y: float) """
        pass

    def glUniform2f(self, location, v0, v1): # real signature unknown; restored from __doc__
        """ glUniform2f(self, location: int, v0: float, v1: float) """
        pass

    def glUniform2fv(self, location, count, value): # real signature unknown; restored from __doc__
        """ glUniform2fv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUniform2i(self, location, v0, v1): # real signature unknown; restored from __doc__
        """ glUniform2i(self, location: int, v0: int, v1: int) """
        pass

    def glUniform2iv(self, location, count, value): # real signature unknown; restored from __doc__
        """ glUniform2iv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUniform2ui(self, location, v0, v1): # real signature unknown; restored from __doc__
        """ glUniform2ui(self, location: int, v0: int, v1: int) """
        pass

    def glUniform3d(self, location, x, y, z): # real signature unknown; restored from __doc__
        """ glUniform3d(self, location: int, x: float, y: float, z: float) """
        pass

    def glUniform3f(self, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glUniform3f(self, location: int, v0: float, v1: float, v2: float) """
        pass

    def glUniform3fv(self, location, count, value): # real signature unknown; restored from __doc__
        """ glUniform3fv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUniform3i(self, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glUniform3i(self, location: int, v0: int, v1: int, v2: int) """
        pass

    def glUniform3iv(self, location, count, value): # real signature unknown; restored from __doc__
        """ glUniform3iv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUniform3ui(self, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glUniform3ui(self, location: int, v0: int, v1: int, v2: int) """
        pass

    def glUniform4d(self, location, x, y, z, w): # real signature unknown; restored from __doc__
        """ glUniform4d(self, location: int, x: float, y: float, z: float, w: float) """
        pass

    def glUniform4f(self, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glUniform4f(self, location: int, v0: float, v1: float, v2: float, v3: float) """
        pass

    def glUniform4fv(self, location, count, value): # real signature unknown; restored from __doc__
        """ glUniform4fv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUniform4i(self, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glUniform4i(self, location: int, v0: int, v1: int, v2: int, v3: int) """
        pass

    def glUniform4iv(self, location, count, value): # real signature unknown; restored from __doc__
        """ glUniform4iv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUniform4ui(self, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glUniform4ui(self, location: int, v0: int, v1: int, v2: int, v3: int) """
        pass

    def glUniformBlockBinding(self, program, uniformBlockIndex, uniformBlockBinding): # real signature unknown; restored from __doc__
        """ glUniformBlockBinding(self, program: int, uniformBlockIndex: int, uniformBlockBinding: int) """
        pass

    def glUniformMatrix2fv(self, location, count, transpose, value): # real signature unknown; restored from __doc__
        """ glUniformMatrix2fv(self, location: int, count: int, transpose: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUniformMatrix3fv(self, location, count, transpose, value): # real signature unknown; restored from __doc__
        """ glUniformMatrix3fv(self, location: int, count: int, transpose: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUniformMatrix4fv(self, location, count, transpose, value): # real signature unknown; restored from __doc__
        """ glUniformMatrix4fv(self, location: int, count: int, transpose: int, value: PYQT_OPENGL_ARRAY) """
        pass

    def glUnmapBuffer(self, target): # real signature unknown; restored from __doc__
        """ glUnmapBuffer(self, target: int) -> int """
        return 0

    def glUseProgram(self, program): # real signature unknown; restored from __doc__
        """ glUseProgram(self, program: int) """
        pass

    def glUseProgramStages(self, pipeline, stages, program): # real signature unknown; restored from __doc__
        """ glUseProgramStages(self, pipeline: int, stages: int, program: int) """
        pass

    def glValidateProgram(self, program): # real signature unknown; restored from __doc__
        """ glValidateProgram(self, program: int) """
        pass

    def glValidateProgramPipeline(self, pipeline): # real signature unknown; restored from __doc__
        """ glValidateProgramPipeline(self, pipeline: int) """
        pass

    def glVertexAttribDivisor(self, index, divisor): # real signature unknown; restored from __doc__
        """ glVertexAttribDivisor(self, index: int, divisor: int) """
        pass

    def glVertexAttribL1d(self, index, x): # real signature unknown; restored from __doc__
        """ glVertexAttribL1d(self, index: int, x: float) """
        pass

    def glVertexAttribL2d(self, index, x, y): # real signature unknown; restored from __doc__
        """ glVertexAttribL2d(self, index: int, x: float, y: float) """
        pass

    def glVertexAttribL3d(self, index, x, y, z): # real signature unknown; restored from __doc__
        """ glVertexAttribL3d(self, index: int, x: float, y: float, z: float) """
        pass

    def glVertexAttribL4d(self, index, x, y, z, w): # real signature unknown; restored from __doc__
        """ glVertexAttribL4d(self, index: int, x: float, y: float, z: float, w: float) """
        pass

    def glVertexAttribP1ui(self, index, type, normalized, value): # real signature unknown; restored from __doc__
        """ glVertexAttribP1ui(self, index: int, type: int, normalized: int, value: int) """
        pass

    def glVertexAttribP2ui(self, index, type, normalized, value): # real signature unknown; restored from __doc__
        """ glVertexAttribP2ui(self, index: int, type: int, normalized: int, value: int) """
        pass

    def glVertexAttribP3ui(self, index, type, normalized, value): # real signature unknown; restored from __doc__
        """ glVertexAttribP3ui(self, index: int, type: int, normalized: int, value: int) """
        pass

    def glVertexAttribP4ui(self, index, type, normalized, value): # real signature unknown; restored from __doc__
        """ glVertexAttribP4ui(self, index: int, type: int, normalized: int, value: int) """
        pass

    def glVertexAttribPointer(self, index, size, type, normalized, stride, pointer): # real signature unknown; restored from __doc__
        """ glVertexAttribPointer(self, index: int, size: int, type: int, normalized: int, stride: int, pointer: PYQT_OPENGL_BOUND_ARRAY) """
        pass

    def glVertexP2ui(self, type, value): # real signature unknown; restored from __doc__
        """ glVertexP2ui(self, type: int, value: int) """
        pass

    def glVertexP3ui(self, type, value): # real signature unknown; restored from __doc__
        """ glVertexP3ui(self, type: int, value: int) """
        pass

    def glVertexP4ui(self, type, value): # real signature unknown; restored from __doc__
        """ glVertexP4ui(self, type: int, value: int) """
        pass

    def glViewport(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ glViewport(self, x: int, y: int, width: int, height: int) """
        pass

    def glViewportIndexedf(self, index, x, y, w, h): # real signature unknown; restored from __doc__
        """ glViewportIndexedf(self, index: int, x: float, y: float, w: float, h: float) """
        pass

    def initializeOpenGLFunctions(self): # real signature unknown; restored from __doc__
        """ initializeOpenGLFunctions(self) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass


# variables with complex values



