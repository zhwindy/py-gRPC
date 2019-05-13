#!/usr/bin/env python
# encoding=utf-8
import grpc
import data_pb2
import data_pb2_grpc


def run():
    channel = grpc.insecure_channel("127.0.0.1:8989")
    client = data_pb2_grpc.FormatDataStub(channel)

    for i in range(10):
        response = client.doFormat(data_pb2.Data(test="hello world"))
        print("Result:", response.test)


if __name__ == "__main__":
    run()
