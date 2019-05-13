#!/usr/bin/env python
# encoding=utf-8
import grpc
import data_pb2
import data_pb2_grpc

ADDRESS = "127.0.0.1:8989"


def run_client():
    channel = grpc.insecure_channel(ADDRESS)
    client = data_pb2_grpc.FormatDataStub(channel)

    for _ in range(10):
        response = client.doFormat(data_pb2.Data(test="hello world"))
        print("Result:", response.test)


if __name__ == "__main__":
    run_client()
