# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from soccer_msgs/localization_output.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import geometry_msgs.msg

class localization_output(genpy.Message):
  _md5sum = "a0a17b80e5cd0e7f3ccaa26b9d99c3b4"
  _type = "soccer_msgs/localization_output"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Point position
bool dilemmaActive
uint8 DILEMMA_UNKNOWN=0
uint8 DILEMMA_BENCHSIDE=1
uint8 DILEMMA_FARSIDE=2
uint8 DILEMMA_CENTER=3
uint8 DILEMMA_GOAL=4
uint8 lastDilemmaState
time lastResolvedDilemma
float32 probability
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  # Pseudo-constants
  DILEMMA_UNKNOWN = 0
  DILEMMA_BENCHSIDE = 1
  DILEMMA_FARSIDE = 2
  DILEMMA_CENTER = 3
  DILEMMA_GOAL = 4

  __slots__ = ['position','dilemmaActive','lastDilemmaState','lastResolvedDilemma','probability']
  _slot_types = ['geometry_msgs/Point','bool','uint8','time','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       position,dilemmaActive,lastDilemmaState,lastResolvedDilemma,probability

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(localization_output, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.dilemmaActive is None:
        self.dilemmaActive = False
      if self.lastDilemmaState is None:
        self.lastDilemmaState = 0
      if self.lastResolvedDilemma is None:
        self.lastResolvedDilemma = genpy.Time()
      if self.probability is None:
        self.probability = 0.
    else:
      self.position = geometry_msgs.msg.Point()
      self.dilemmaActive = False
      self.lastDilemmaState = 0
      self.lastResolvedDilemma = genpy.Time()
      self.probability = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3d2B2If().pack(_x.position.x, _x.position.y, _x.position.z, _x.dilemmaActive, _x.lastDilemmaState, _x.lastResolvedDilemma.secs, _x.lastResolvedDilemma.nsecs, _x.probability))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.lastResolvedDilemma is None:
        self.lastResolvedDilemma = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 38
      (_x.position.x, _x.position.y, _x.position.z, _x.dilemmaActive, _x.lastDilemmaState, _x.lastResolvedDilemma.secs, _x.lastResolvedDilemma.nsecs, _x.probability,) = _get_struct_3d2B2If().unpack(str[start:end])
      self.dilemmaActive = bool(self.dilemmaActive)
      self.lastResolvedDilemma.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3d2B2If().pack(_x.position.x, _x.position.y, _x.position.z, _x.dilemmaActive, _x.lastDilemmaState, _x.lastResolvedDilemma.secs, _x.lastResolvedDilemma.nsecs, _x.probability))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.lastResolvedDilemma is None:
        self.lastResolvedDilemma = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 38
      (_x.position.x, _x.position.y, _x.position.z, _x.dilemmaActive, _x.lastDilemmaState, _x.lastResolvedDilemma.secs, _x.lastResolvedDilemma.nsecs, _x.probability,) = _get_struct_3d2B2If().unpack(str[start:end])
      self.dilemmaActive = bool(self.dilemmaActive)
      self.lastResolvedDilemma.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d2B2If = None
def _get_struct_3d2B2If():
    global _struct_3d2B2If
    if _struct_3d2B2If is None:
        _struct_3d2B2If = struct.Struct("<3d2B2If")
    return _struct_3d2B2If
