"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from crazyflie_py import Crazyswarm


TAKEOFF_DURATION = 2.0
HOVER_DURATION = 5.0


def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf1 = swarm.allcfs.crazyfliesByName['cf1']
    cf3 = swarm.allcfs.crazyfliesByName['cf3']

    cf1.setParam('led.bitmask',255)
    cf1.takeoff(targetHeight=1.0, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)
    cf1.goTo([1.0,1.0,1.0],0,3)
    timeHelper.sleep(HOVER_DURATION)
    cf1.land(targetHeight=0.04, duration=2.5)
    timeHelper.sleep(TAKEOFF_DURATION)
    cf1.setParam('led.bitmask',0)
    
    cf3.setParam('led.bitmask',255)
    cf3.takeoff(targetHeight=1.0, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)
    cf3.goTo([1.0,1.0,1.0],0,3)
    timeHelper.sleep(HOVER_DURATION)
    cf3.land(targetHeight=0.04, duration=2.5)
    timeHelper.sleep(TAKEOFF_DURATION)
    cf3.setParam('led.bitmask',0)

if __name__ == '__main__':
    main()
