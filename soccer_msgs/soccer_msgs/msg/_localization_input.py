# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from soccer_msgs/localization_input.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class localization_input(genpy.Message):
  _md5sum = "55ad187482d73ebd80c17129190be487"
  _type = "soccer_msgs/localization_input"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Point position
bool setOrientation
bool setPosition
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['position','setOrientation','setPosition']
  _slot_types = ['geometry_msgs/Point','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       position,setOrientation,setPosition

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(localization_input, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.position is None:
        self.position = geometry_msgs.msg.Point()
      if self.setOrientation is None:
        self.setOrientation = False
      if self.setPosition is None:
        self.setPosition = False
    else:
      self.position = geometry_msgs.msg.Point()
      self.setOrientation = False
      self.setPosition = False

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
      buff.write(_get_struct_3d2B().pack(_x.position.x, _x.position.y, _x.position.z, _x.setOrientation, _x.setPosition))
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
      end = 0
      _x = self
      start = end
      end += 26
      (_x.position.x, _x.position.y, _x.position.z, _x.setOrientation, _x.setPosition,) = _get_struct_3d2B().unpack(str[start:end])
      self.setOrientation = bool(self.setOrientation)
      self.setPosition = bool(self.setPosition)
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
      buff.write(_get_struct_3d2B().pack(_x.position.x, _x.position.y, _x.position.z, _x.setOrientation, _x.setPosition))
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
      end = 0
      _x = self
      start = end
      end += 26
      (_x.position.x, _x.position.y, _x.position.z, _x.setOrientation, _x.setPosition,) = _get_struct_3d2B().unpack(str[start:end])
      self.setOrientation = bool(self.setOrientation)
      self.setPosition = bool(self.setPosition)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d2B = None
def _get_struct_3d2B():
    global _struct_3d2B
    if _struct_3d2B is None:
        _struct_3d2B = struct.Struct("<3d2B")
    return _struct_3d2B