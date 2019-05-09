# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='hello',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bhello.proto\x12\x05hello\"\x19\n\noneRequest\x12\x0b\n\x03say\x18\x01 \x01(\t\"\x1a\n\x0boneResponse\x12\x0b\n\x03res\x18\x01 \x01(\t2;\n\x08sayHello\x12/\n\x04Main\x12\x11.hello.oneRequest\x1a\x12.hello.oneResponse\"\x00\x62\x06proto3')
)




_ONEREQUEST = _descriptor.Descriptor(
  name='oneRequest',
  full_name='hello.oneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='say', full_name='hello.oneRequest.say', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=47,
)


_ONERESPONSE = _descriptor.Descriptor(
  name='oneResponse',
  full_name='hello.oneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='hello.oneResponse.res', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=75,
)

DESCRIPTOR.message_types_by_name['oneRequest'] = _ONEREQUEST
DESCRIPTOR.message_types_by_name['oneResponse'] = _ONERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

oneRequest = _reflection.GeneratedProtocolMessageType('oneRequest', (_message.Message,), dict(
  DESCRIPTOR = _ONEREQUEST,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:hello.oneRequest)
  ))
_sym_db.RegisterMessage(oneRequest)

oneResponse = _reflection.GeneratedProtocolMessageType('oneResponse', (_message.Message,), dict(
  DESCRIPTOR = _ONERESPONSE,
  __module__ = 'hello_pb2'
  # @@protoc_insertion_point(class_scope:hello.oneResponse)
  ))
_sym_db.RegisterMessage(oneResponse)



_SAYHELLO = _descriptor.ServiceDescriptor(
  name='sayHello',
  full_name='hello.sayHello',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=77,
  serialized_end=136,
  methods=[
  _descriptor.MethodDescriptor(
    name='Main',
    full_name='hello.sayHello.Main',
    index=0,
    containing_service=None,
    input_type=_ONEREQUEST,
    output_type=_ONERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SAYHELLO)

DESCRIPTOR.services_by_name['sayHello'] = _SAYHELLO

# @@protoc_insertion_point(module_scope)