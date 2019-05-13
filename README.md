### 安装grpc
python
```
pip install grpcio
```
依赖
```
pip install protobuf
```
工具
```
pip install grpcio-tools
```

### 用gRPC框架实现简易RPC服务

整个过程分为5步:
1. 编写协议文件``hello.proto`
2. 用grpc-tools将协议文件编译成`hello_pb2.py`和`hello_pb2_grpc.py`两个文件
3. 使用文件`hello_pb2_grpc.py`的服务器Stub类,实现服务器端的逻辑
4. 使用文件`hello_pb2_grpc.py`的客户端Stub类,实现客户端代码
5. 分别运行服务器端和客户端,观察结果是否与预期结果一致

#### grpc-tools编译命令
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto
```
* --python_out 指定生成hello_pb2.py文件的路径
* --grpc_python_out 指定生成hello_pb2_grpc.py文件的路径
* -I 指定协议文件`hello.proto`的路径

#### 编译生成的两个py文件
1. `xxx_pb2.py`文件提供了序列化和反序列化的方法
2. `xxx_pb2_grpc.py`文件提供了服务器Stub类和客户端Stub类


#### 两个方法
1. 序列化方法：`SerializeToString()`
2. 反序列化方法：`ParseFromString(msg: bytes)`

#### 错误处理
报错:
```
Traceback (most recent call last):
  File "server.py", line 7, in <module>
    import hello_pb2
  File "/Users/zpf/work/py-gRPC/example1/hello_pb2.py", line 23, in <module>
    serialized_pb=_b('\n\x0bhello.proto\x12\x05hello\"\x19\n\noneRequest\x12\x0b\n\x03say\x18\x01 \x01(\t\"\x1a\n\x0boneResponse\x12\x0b\n\x03res\x18\x01 \x01(\t2;\n\x08sayHello\x12/\n\x04Main\x12\x11.hel
lo.oneRequest\x1a\x12.hello.oneResponse\"\x00\x62\x06proto3')
TypeError: __init__() got an unexpected keyword argument 'serialized_options'
```
原因:
```
终端上的 protoc 版本 与python库内的protobuf版本不一样
```
解决办法:
```
pip install -U protobuf
```