from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError

class BaseServer(TCPServer):
    def handle_stream(self, stream, address):
        self._stream = stream
        self._address = address
        print(address)
        self.read_request()

    def read_request(self):
        self._stream.read_until('\n', self.handle_request)

    def handle_request(self,data):
        requestBody = data[:-1]
        print(requestBody)

if __name__ == '__main__':
    server = BaseServer()
    #server.bind(8081,"192.168.0.2")
    server.bind(8081)

    server.start(1)
    IOLoop.current().start()
