# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import hello_pb2 as hello__pb2


class sayHelloStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Main = channel.unary_unary(
        '/hello.sayHello/Main',
        request_serializer=hello__pb2.oneRequest.SerializeToString,
        response_deserializer=hello__pb2.oneResponse.FromString,
        )


class sayHelloServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Main(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_sayHelloServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Main': grpc.unary_unary_rpc_method_handler(
          servicer.Main,
          request_deserializer=hello__pb2.oneRequest.FromString,
          response_serializer=hello__pb2.oneResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hello.sayHello', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))