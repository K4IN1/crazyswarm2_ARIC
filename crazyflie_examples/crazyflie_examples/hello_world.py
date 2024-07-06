"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from crazyflie_py import Crazyswarm
from crazyflie_py.crazyflie import Crazyflie

name1 = 'cf1'
name3 = 'cf3'

TAKEOFF_DURATION = 2.0
HOVER_DURATION = 5.0


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf1:Crazyflie = swarm.allcfs.crazyfliesByName[name1]
    cf3:Crazyflie = swarm.allcfs.crazyfliesByName[name3]

    cf1.setGroupMask(0b00000001)
    timeHelper.sleep(0.5)
    cf3.setGroupMask(0b00000010)
    timeHelper.sleep(0.5)

    cf1.setParam('led.bitmask',255)
    timeHelper.sleep(3)
    cf3.setParam('led.bitmask',255)
    timeHelper.sleep(3)

    cf1.setParam('led.bitmask',191)
    timeHelper.sleep(3)
    cf3.setParam('led.bitmask',191)
    timeHelper.sleep(3)

    cf1.setParam('led.bitmask',0)
    timeHelper.sleep(3)
    cf3.setParam('led.bitmask',0)
    timeHelper.sleep(3)

    cf1.takeoff(targetHeight=0.5, duration=TAKEOFF_DURATION,groupMask=0b00000001)
    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)
    # cf1.goTo([1.0,1.0,1.0],0,3)
    # timeHelper.sleep(HOVER_DURATION)
    cf1.land(targetHeight=0.04, duration=2.5,groupMask=0b00000001)
    timeHelper.sleep(3)
    # cf1.setParam('led.bitmask',0)
    
    cf3.takeoff(targetHeight=0.5, duration=TAKEOFF_DURATION,groupMask=0b00000010)
    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)
    # cf3.goTo([-1.0,-1.0,1.0],0,3)
    # timeHelper.sleep(HOVER_DURATION)
    cf3.land(targetHeight=0.04, duration=2.5,groupMask=0b00000010)
    timeHelper.sleep(3)
    # cf3.setParam('led.bitmask',0)

if __name__ == '__main__':
    main()
