'''
Created on 03/12/2009

@author: allan
'''
import Queue as queue

from actors.plotter import Plotter

from actors.ctsin import CTSin
from actors.summer import Summer
import matplotlib.pyplot as plt
import numpy

import logging
logging.basicConfig(level=logging.INFO)
logging.info("Logger enabled")


def run_sum_sin_plot():
    connection1 = queue.Queue(0)
    connection2 = queue.Queue(0)
    connection3 = queue.Queue(0)

    src1 = CTSin(connection1, 2, 2.0, numpy.pi/2) # 2 Hz, 90 degree phase
    src2 = CTSin(connection2, 1, 3.5, numpy.pi/4) # 4 Hz, 45 degree phase

    summer = Summer([connection1, connection2], connection3)
    dst = Plotter(connection3)

    components = [src1, src2, summer, dst]

    logging.info("Starting simulation")
    for component in components:
        component.start()
    logging.debug("Finished starting actors")


    plt.show()   # The program will stay "running" while this plot is open

    for component in components:
        component.join()

    logging.debug("Finished running actor")

if __name__ == '__main__':
    run_sum_sin_plot()
