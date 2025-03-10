#!/usr/bin/env python

from crazyflie_py import Crazyswarm
import numpy as np


def main():
    
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    
    allcfs.land(targetHeight=0.02, duration=2.0)
    timeHelper.sleep(1.0)


if __name__ == '__main__':
    main()
