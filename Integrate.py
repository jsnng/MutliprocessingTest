from multiprocessing import Process, Manager, Event, freeze_support, Pipe, Pool
import time
import socket

from WSUSSL.Networking.ServerClass import Server
from WSUSSL.TeamControl.Skills import GoTowards as goto
from WSUSSL.TeamControl.teamcontrol import TeamControl
from WSUSSL.World.receiver import ssl_vision_receiver
from WSUSSL.World.receiver import grsim_coms
from WSUSSL.World.model import Model as wm


def multiprocess():
    # freeze_support()

    # controllers = Manager()
    #namespace = controllers.Namespace()

    # pipe = Pipe()
    world = wm()
    #receiver = ssl_vision_receiver(world)
    receiver = grsim_coms(world)
    receiver.listen_world()
    #server = Server(0)
    
    # update is the reciever updating the world values
    update = Process(target=receiver.listen_world)
    # coms is the server processes
    # coms = Process(target=Server(0))


    update.start()
    #coms.start()

   # update.join()
    #coms.join()

if __name__ == '__main__':

   multiprocess()