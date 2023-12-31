# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from soccer_msgs/line_output.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class line_output(genpy.Message):
  _md5sum = "345ed51685653b64ec0fd30346898686"
  _type = "soccer_msgs/line_output"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Point start_point
geometry_msgs/Point end_point
float32 probability
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['start_point','end_point','probability']
  _slot_types = ['geometry_msgs/Point','geometry_msgs/Point','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       start_point,end_point,probability

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(line_output, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.start_point is None:
        self.start_point = geometry_msgs.msg.Point()
      if self.end_point is None:
        self.end_point = geometry_msgs.msg.Point()
      if self.probability is None:
        self.probability = 0.
    else:
      self.start_point = geometry_msgs.msg.Point()
      self.end_point = geometry_msgs.msg.Point()
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
      buff.write(_get_struct_6df().pack(_x.start_point.x, _x.start_point.y, _x.start_point.z, _x.end_point.x, _x.end_point.y, _x.end_point.z, _x.probability))
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
      if self.start_point is None:
        self.start_point = geometry_msgs.msg.Point()
      if self.end_point is None:
        self.end_point = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 52
      (_x.start_point.x, _x.start_point.y, _x.start_point.z, _x.end_point.x, _x.end_point.y, _x.end_point.z, _x.probability,) = _get_struct_6df().unpack(str[start:end])
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
      buff.write(_get_struct_6df().pack(_x.start_point.x, _x.start_point.y, _x.start_point.z, _x.end_point.x, _x.end_point.y, _x.end_point.z, _x.probability))
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
      if self.start_point is None:
        self.start_point = geometry_msgs.msg.Point()
      if self.end_point is None:
        self.end_point = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 52
      (_x.start_point.x, _x.start_point.y, _x.start_point.z, _x.end_point.x, _x.end_point.y, _x.end_point.z, _x.probability,) = _get_struct_6df().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6df = None
def _get_struct_6df():
    global _struct_6df
    if _struct_6df is None:
        _struct_6df = struct.Struct("<6df")
    return _struct_6df
