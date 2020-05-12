

from server.socket_server import TCPServer
from handler.base_handler import StreamRequestHandler

class TestBaseRequestHandler(StreamRequestHandler):

    # 具体处理的逻辑
    def handle(self):
        pass

# 测试  SockersERVER(TCPServer)
class SocketServerTest:

    def run_server(self):
        tcp_server = TCPServer(('127.0.0.1', 8888), TestBaseRequestHandler);
