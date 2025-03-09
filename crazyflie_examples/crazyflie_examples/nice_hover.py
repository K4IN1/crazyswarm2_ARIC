#!/usr/bin/env python

from crazyflie_py import Crazyswarm
from crazyflie_py.crazyflie import Crazyflie

import numpy as np
import signal

name1 = 'cf1'
name2 = 'cf2'
# name3 = 'cf3'
swarm = Crazyswarm()
timeHelper = swarm.timeHelper
allcfs = swarm.allcfs
# cf1:Crazyflie = swarm.allcfs.crazyfliesByName[name1]
cf2:Crazyflie = swarm.allcfs.crazyfliesByName[name2]

# cf3:Crazyflie = swarm.allcfs.crazyfliesByName[name3]
def keyInterHandler(Signal,Frame):
    loopSignal = 0
    position = {'x':0,'y':0,'z':0}
    allcfs.land(0.03,3.0)
    print('emergency stop')
    # for cf in allcfs.crazyflies:
    #     position['x']=cf.getParam('stateEstimate.x')
    #     position['y']=cf.getParam('stateEstimate.y')
    #     # position['z']=cf.getParam('stateEstimate.z')
    #     # cf.land(0.03,3.0)
    #     print(cf.prefix,"land to ",f"{position['x']},{position['y']},0.03")

def main():
    Z =0.3
    signal.signal(signal.SIGINT,keyInterHandler)
    allcfs.takeoff(targetHeight=Z, duration=5.0)
    timeHelper.sleep(6.0)

    # allcfs.goTo([0.0,0.0,0.3],yaw=0.,duration=2.0)
    # timeHelper.sleep(4.0)

    cf2.goTo([0.5,0.0,0.3],0.6,duration=5.0)
    timeHelper.sleep(6.0)
    # # cf1.goTo([-0.5,-0.5,0.5],0.,duration=3.0)
    # # # for cf in allcfs.crazyflies:
    # # # #     pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
    # # # #     cf.goTo(pos, 0, 0.5)
    # # timeHelper.sleep(4.0)
    cf2.goTo([0.0,0.0,0.3],0.,duration=5.0)
    timeHelper.sleep(6.0)

    # # print('press button to continue...')
    # # swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=2.0)
    timeHelper.sleep(2.0)


if __name__ == '__main__':
    main()
