'''
Created on 03/12/2009

@author: allan
'''
from scipysim.actors import Channel, CompositeActor
from scipysim.actors.display import Plotter
from scipysim.actors.math import Summer
from scipysim.actors.math.trig import CTSinGenerator

import numpy

import logging
logging.basicConfig( level=logging.INFO )
logging.info( "Logger enabled" )

class SumSinPlot( CompositeActor ):
    """
    Summing two continous sinusoidal sources with different timesteps,
    and plotting.
    """
    def __init__( self ):
        '''Setup the simulation'''
        super( SumSinPlot, self ).__init__()
        connection1 = Channel( domain="CT" )
        connection2 = Channel( domain="CT" )
        connection3 = Channel()

        # 2 Hz, 90 degree phase
        src1 = CTSinGenerator( connection1, 2, 2.0, numpy.pi / 2, timestep = 0.001 )
        # 4 Hz, 45 degree phase, different timestep
        src2 = CTSinGenerator( connection2, 1, 3.5, numpy.pi / 4, timestep = 0.005 )

        summer = Summer( [connection1, connection2], connection3 )
        dst = Plotter( connection3, refresh_rate=50 )

        self.components = [src1, src2, summer, dst]

if __name__ == '__main__':
    SumSinPlot().run()
