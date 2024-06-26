#!/usr/bin/env python

from crazyflie_py import Crazyswarm


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    cf1 = swarm.allcfs.crazyfliesByName['cf1']
    cf3 = swarm.allcfs.crazyfliesByName['cf3']
    # set group mask to enable group 1 and 4 (one by one)
    
    cf1.setGroupMask(0b00000001)
    timeHelper.sleep(1)
    cf3.setGroupMask(0b00000010)
    timeHelper.sleep(1)

    print('Takeoff with a different mask (2) -> cf3(Green)should take off and land')
    allcfs.takeoff(targetHeight=0.5, duration=3.0, groupMask=2)
    timeHelper.sleep(3)
    allcfs.land(targetHeight=0.02, duration=3.0)
    timeHelper.sleep(3)

    print('Takeoff with correct mask (1) -> cf1(black) should take off and land')
    allcfs.takeoff(targetHeight=0.5, duration=3.0, groupMask=1)
    timeHelper.sleep(3)
    allcfs.land(targetHeight=0.02, duration=3.0)
    timeHelper.sleep(3)


if __name__ == '__main__':
    main()
