
import socket

# 实现网络服务器
class TCPServer:

    def __init__(self, server_address, handler_class):
        #类的属性
        self.serve_address = server_address
        self.HanderClass = handler_class
        # socket.AF_INFT 服务器之间网络通信     socket.SOCK_STREAM   流式socket , for TCP  处理字节流
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 关闭服务器
        self.is_shutdown = False

    #服务器的启动函数
    def serve_forever(self):
        self.socket.bind(self.serve_address)
        #  监听
        self.socket.listen(10)
        while not self.is_shutdown:

            # 1.接收请求
            request, client_address = self.get_request()
            try:
                # 2. 处理请求
                self.process_request(request, client_address)
            except Exception as e:
                print(e)
            finally:
                # 3. 关闭连接
                self.close_request(request)

    #接受请求
    def get_request(self):
        # 接受TCP连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
        return self.socket.accept()
        pass

    #处理请求
    def process_request(self, request, client_address):
        hadler = self.HanderClass(request, client_address)
        hadler.handle()

    #关闭请求
    def close_request(self, request):
        request.shutdown()
        request.close()

    #关闭服务器
    def shutdown(self):
        pass


