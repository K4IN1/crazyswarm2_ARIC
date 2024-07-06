from crazyflie_py import Crazyswarm
from crazyflie_py.crazyflie import Crazyflie

name1 = 'cf1'
name3 = 'cf3'

TAKEOFF_DURATION = 2.0
HOVER_DURATION = 5.0
TARGET_HEIGHT = 0.5

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper

    cf1:Crazyflie = swarm.allcfs.crazyfliesByName[name1]
    cf3:Crazyflie = swarm.allcfs.crazyfliesByName[name3]

    cf1.setGroupMask(0b00000001)
    timeHelper.sleep(0.5)
    cf3.setGroupMask(0b00000010)
    timeHelper.sleep(0.5)

    cf1.takeoff(TARGET_HEIGHT,TAKEOFF_DURATION,groupMask=0b00000001)
    timeHelper.sleep(3)
    cf3.takeoff(TARGET_HEIGHT,TAKEOFF_DURATION,groupMask=0b00000010)
    timeHelper.sleep(3)
    
    cf1.land(0.04,2.5,groupMask=0b00000001)
    timeHelper.sleep(3)
    cf3.land(0.04,2.5,groupMask=0b00000001)
    timeHelper.sleep(3)

    swarm.allcfs.land(0.04,2.5,0)
    timeHelper.sleep(3)

if __name__ == '__main__':
    main()