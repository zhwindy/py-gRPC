#! /usr/bin/env python
# encoding=utf-8

import grpc
import time
from concurrent import futures
import hello_pb2
import hello_pb2_grpc


class sayHelloServicer(hello_pb2_grpc.sayHelloServicer):
    def Main(self, request, context):
        text = "Hello World!"
        return hello_pb2.oneResponse(res=text)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=15))
    servicer = sayHelloServicer()

    hello_pb2_grpc.add_sayHelloServicer_to_server(servicer, server)

    server.add_insecure_port('127.0.0.1:8989')
    server.start()

    try:
        time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    main()
