# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import storage_pb2 as storage__pb2


class StorageBenchWrapperStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.Write = channel.unary_unary(
            "/storage_bench.StorageBenchWrapper/Write",
            request_serializer=storage__pb2.ObjectWrite.SerializeToString,
            response_deserializer=storage__pb2.EmptyResponse.FromString,
        )
        self.Read = channel.unary_unary(
            "/storage_bench.StorageBenchWrapper/Read",
            request_serializer=storage__pb2.ObjectRead.SerializeToString,
            response_deserializer=storage__pb2.EmptyResponse.FromString,
        )


class StorageBenchWrapperServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Write(self, request, context):
        """Performs an upload from a specific object.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Read(self, request, context):
        """Read a specific object.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_StorageBenchWrapperServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Write": grpc.unary_unary_rpc_method_handler(
            servicer.Write,
            request_deserializer=storage__pb2.ObjectWrite.FromString,
            response_serializer=storage__pb2.EmptyResponse.SerializeToString,
        ),
        "Read": grpc.unary_unary_rpc_method_handler(
            servicer.Read,
            request_deserializer=storage__pb2.ObjectRead.FromString,
            response_serializer=storage__pb2.EmptyResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "storage_bench.StorageBenchWrapper", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
