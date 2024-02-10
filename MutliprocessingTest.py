from multiprocessing import Process, Manager, Event, freeze_support, Pipe, Pool
import time
import socket

def foo(namespace, event):
    i = 0
    # make a counter that sets a shared namespace variable x to the counter
    while True:
        i += 1
        namespace.x = i
        # set an event when the counter increments
        event.set()
        time.sleep(1)


class bar:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 50514
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def test(self, x):
        # send x into a socket on localhost
        x = bytes(str(x).encode('utf-8'))
        self.sock.sendto(x, (self.host, self.port))

    def listen(self, namespace, event):
        while True:
            # check if the event is set
            if event.is_set():
                # send via socket to UDP.py
                self.test(namespace.x)
                event.clear()

if __name__ == '__main__':

    freeze_support()

    controllers = Manager()
    namespace = controllers.Namespace()

    event = Event()

    test = bar()

    # func is a counter subprocess
    func = Process(target=foo, args=(namespace, event))
    # gunc is a socket sender
    gunc = Process(target=test.listen, args=(namespace, event))

    func.start()
    gunc.start()

    func.join()
    gunc.join()