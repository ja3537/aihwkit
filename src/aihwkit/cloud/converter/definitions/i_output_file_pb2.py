# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: i_output_file.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import i_common_pb2 as i__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='i_output_file.proto',
  package='aihwx.inferencing',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13i_output_file.proto\x12\x11\x61ihwx.inferencing\x1a\x0ei_common.proto\"}\n\x15InferenceResultsProto\x12\x13\n\x0bt_inference\x18\x01 \x02(\x02\x12\x14\n\x0c\x61vg_accuracy\x18\x02 \x02(\x02\x12\x14\n\x0cstd_accuracy\x18\x03 \x02(\x02\x12\x11\n\tavg_error\x18\x04 \x02(\x02\x12\x10\n\x08\x61vg_loss\x18\x05 \x02(\x02\"\x9d\x01\n\x12InferenceRunsProto\x12\x18\n\x10inference_repeat\x18\x01 \x02(\x03\x12\x12\n\nis_partial\x18\x02 \x02(\x08\x12\x14\n\x0ctime_elapsed\x18\x03 \x02(\x02\x12\x43\n\x11inference_results\x18\x04 \x03(\x0b\x32(.aihwx.inferencing.InferenceResultsProto\"\x7f\n\x11InferencingOutput\x12+\n\x07version\x18\x01 \x02(\x0b\x32\x1a.aihwx.inferencing.Version\x12=\n\x0einference_runs\x18\x02 \x02(\x0b\x32%.aihwx.inferencing.InferenceRunsProto'
  ,
  dependencies=[i__common__pb2.DESCRIPTOR,])




_INFERENCERESULTSPROTO = _descriptor.Descriptor(
  name='InferenceResultsProto',
  full_name='aihwx.inferencing.InferenceResultsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='t_inference', full_name='aihwx.inferencing.InferenceResultsProto.t_inference', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avg_accuracy', full_name='aihwx.inferencing.InferenceResultsProto.avg_accuracy', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='std_accuracy', full_name='aihwx.inferencing.InferenceResultsProto.std_accuracy', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avg_error', full_name='aihwx.inferencing.InferenceResultsProto.avg_error', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avg_loss', full_name='aihwx.inferencing.InferenceResultsProto.avg_loss', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=183,
)


_INFERENCERUNSPROTO = _descriptor.Descriptor(
  name='InferenceRunsProto',
  full_name='aihwx.inferencing.InferenceRunsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inference_repeat', full_name='aihwx.inferencing.InferenceRunsProto.inference_repeat', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_partial', full_name='aihwx.inferencing.InferenceRunsProto.is_partial', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_elapsed', full_name='aihwx.inferencing.InferenceRunsProto.time_elapsed', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inference_results', full_name='aihwx.inferencing.InferenceRunsProto.inference_results', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=343,
)


_INFERENCINGOUTPUT = _descriptor.Descriptor(
  name='InferencingOutput',
  full_name='aihwx.inferencing.InferencingOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='aihwx.inferencing.InferencingOutput.version', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inference_runs', full_name='aihwx.inferencing.InferencingOutput.inference_runs', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=472,
)

_INFERENCERUNSPROTO.fields_by_name['inference_results'].message_type = _INFERENCERESULTSPROTO
_INFERENCINGOUTPUT.fields_by_name['version'].message_type = i__common__pb2._VERSION
_INFERENCINGOUTPUT.fields_by_name['inference_runs'].message_type = _INFERENCERUNSPROTO
DESCRIPTOR.message_types_by_name['InferenceResultsProto'] = _INFERENCERESULTSPROTO
DESCRIPTOR.message_types_by_name['InferenceRunsProto'] = _INFERENCERUNSPROTO
DESCRIPTOR.message_types_by_name['InferencingOutput'] = _INFERENCINGOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InferenceResultsProto = _reflection.GeneratedProtocolMessageType('InferenceResultsProto', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCERESULTSPROTO,
  '__module__' : 'i_output_file_pb2'
  # @@protoc_insertion_point(class_scope:aihwx.inferencing.InferenceResultsProto)
  })
_sym_db.RegisterMessage(InferenceResultsProto)

InferenceRunsProto = _reflection.GeneratedProtocolMessageType('InferenceRunsProto', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCERUNSPROTO,
  '__module__' : 'i_output_file_pb2'
  # @@protoc_insertion_point(class_scope:aihwx.inferencing.InferenceRunsProto)
  })
_sym_db.RegisterMessage(InferenceRunsProto)

InferencingOutput = _reflection.GeneratedProtocolMessageType('InferencingOutput', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCINGOUTPUT,
  '__module__' : 'i_output_file_pb2'
  # @@protoc_insertion_point(class_scope:aihwx.inferencing.InferencingOutput)
  })
_sym_db.RegisterMessage(InferencingOutput)


# @@protoc_insertion_point(module_scope)
