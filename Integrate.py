from multiprocessing import Process, Manager, Event, freeze_support, Pipe, Pool
import time
import socket

from serverClass import Server
from goTo import GoTowards as goto
from reciver import proto2_ssl_vision_py_receiver as ssl_reciever
from worldModel import Model as wm


def multiprocess():
    freeze_support()

    controllers = Manager()
    namespace = controllers.Namespace()

    event = Event()
    world = wm()
    #server = Server()
    reciever = ssl_reciever()
    reciever.set_world_model(world)
    reciever.receive()

    # update is the reciever updating the world values
    update = Process(target=reciever.listen())
    # coms is the server processes
    #coms = Process(target=Server(),args=(1))


    update.start()
    #gunc.start()
    #coms.start()

    update.join()
    #gunc.join()
    #coms.join()

if __name__ == '__main__':

   multiprocess()