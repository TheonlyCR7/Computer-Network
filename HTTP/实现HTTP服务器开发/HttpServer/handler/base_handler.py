
#  编码解码， 处理字节
#  码
class BaseRequestHandler:
    def __init__(self, server, request, client_address):
        self.server = server
        self.request = request
        self.client_address = client_address

    def handle(self):
        pass

# 继承类 BaseRequestHandler
class StreamRequestHandler(BaseRequestHandler):

    def __init__(self, server, request, client_address):
        BaseRequestHandler.__init__(self, server, request, client_address)

        self.rfile = self.request.makefile('rb')
        self.wfile = self.request.makefile('wb')
        self.wbuf = []

    # 编码： 将字符串转变为 字节码  再发送
    def encode(self, msg):
        # 如果 msg  不是字节码
        if not isinstance(msg, bytes):
            # 将 msg 编码为字节码
            msg = bytes(msg, encoding= 'utf-8')
        return msg

    # 解码：  将字节码 转变为 字符串
    def decode(self, msg):
        if isinstance(msg, bytes):
            msg = msg.decode()
        return msg

    # 读消息
    def read(self, length):
        msg = self.rfile.read(length)
        return self.decode(msg)

    # 读取一行消息
    def readlin(self, length = 65536):
        msg = self.rfile.readline(length).strip()
        return self.decode(msg)

    # 写消息
    def write_content(self, msg):
        msg = self.encode(msg)
        #  放入缓存
        self.wbuf.append(msg)

    def send(self):
        # 迭代
        for line in self.wbuf:
            self.wfile.write(line)
        self.wfile.flush()
        # 清空缓存区
        self.wbuf = []

    # 关闭服务
    def close(self):
        self.wfile.close()
        self.rfile.close()
