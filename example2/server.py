#!/usr/bin/env python
# encoding=utf-8
import grpc
import time
from concurrent import futures
import data_pb2
import data_pb2_grpc


class doFormat(data_pb2_grpc.FormatDataServicer):
    def doFormat(self, request, context):
        text = request.test
        return data_pb2.Data(test=text.upper())


def run_server():
    """
    启动RPC服务
    """
    address = '127.0.0.1:8989'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    servicer = doFormat()
    data_pb2_grpc.add_FormatDataServicer_to_server(servicer, server)
    server.add_insecure_port(address)
    print(f"RPC SERVER Start {address}")
    server.start()

    try:
        time.sleep(500)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    run_server()
