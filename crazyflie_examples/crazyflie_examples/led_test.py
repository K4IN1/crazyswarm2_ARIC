# script to test led.bitmask

from crazyflie_py import Crazyswarm
from crazyflie_py.crazyflie import Crazyflie

name1 = 'cf1'
name3 = 'cf3'

def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper

    cf1:Crazyflie = swarm.allcfs.crazyfliesByName[name1]
    cf3:Crazyflie = swarm.allcfs.crazyfliesByName[name3]

    cf1.setParam('led.bitmask',128)
    timeHelper.sleep(3)
    cf3.setParam('led.bitmask',128)
    timeHelper.sleep(3)
    
    cf1.setParam('led.bitmask',191)
    timeHelper.sleep(3)
    cf3.setParam('led.bitmask',191)
    timeHelper.sleep(3)

    cf1.setParam('led.bitmask',0)
    timeHelper.sleep(3)
    cf3.setParam('led.bitmask',0)
    timeHelper.sleep(3)

if __name__ == '__main__':
    main()
