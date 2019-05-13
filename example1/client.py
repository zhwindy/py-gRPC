#! /usr/bin/env python
# encoding=utf-8
import grpc
import hello_pb2
import hello_pb2_grpc


def main():
    channel = grpc.insecure_channel('localhost:8989')

    client = hello_pb2_grpc.sayHelloStub(channel)

    print(10*"*", client.Main(hello_pb2.oneRequest(say='hai')).res)


if __name__ == "__main__":
    main()
